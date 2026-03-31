---
layout: post
title: "Running 4B models on Apple's Neural Engine"
date: 2026-03-30
published: true
description: "Qwen3.5-4B hits 11.66 tok/s single-stream on ANE with int8 quantization, and four concurrent streams reach 28.62 tok/s aggregate — all on the Neural Engine, GPU and CPU idle."
---

**TL;DR:**
- 4B and 9B models on ANE, bypassing CoreML entirely
- 11.66 tok/s single-stream, 28.62 tok/s with four concurrent streams — GPU and CPU idle
- Same 16-core ANE on every M1 through M5, regardless of SKU
- Bottleneck is dispatch overhead, not compute or bandwidth
- Code: [ane.cpp](https://github.com/skyfallsin/ane.cpp) + [field guide](https://github.com/skyfallsin/apple-neural-engine-field-guide)

---

GPUs are great for local inference if the goal is raw tokens per second on one chat, but they're a poor fit if what you actually want is many small inference streams running quietly in the background for hours — on an M3 Max, sustained GPU inference pulls 40–60W from the GPU cluster alone[^1], and that adds up fast on battery.

[Jo](https://askjo.ai) is a personal AI that runs on a hybrid stack — important things never leave your Mac, and sensitive external tasks are handled on your own cloud machine. The local macOS side handles on-device context: browser history clustering, note indexing, local tool dispatch. Today those workloads either wake the GPU or wait for the cloud, both of which have tradeoffs in power draw and latency respectively.

What we really want is an autonomous ambient layer on your machine, things organizing by themselves and context building up quietly. Getting that to work without draining the battery means finding hardware that can carry parallel inference at low power — and if something can do that, the local side of Jo becomes a thing that runs continuously instead of intermittently. That's the target.

## The Neural Engine

Every Apple Silicon chip since M1 has a 16-core Neural Engine[^2] — same core count on the base Air as on the Max, same MIL programs through the same `_ANEInMemoryModel` interface, for five years running. An M1 Air and an M4 Max both have identical ANE blocks. That kind of consistency across SKUs is unusual for Apple, and it means we can target the ANE and know what to expect regardless of what machine a user has.

Apple exposes the ANE through CoreML[^3], but CoreML doesn't give you direct control over dispatch scheduling or IOSurface tensor layout — both of which matter for autoregressive transformer decode. ane.cpp bypasses CoreML and talks to the ANE directly through Apple's private `AppleNeuralEngine.framework`[^4].

| Generation | ANE cores | TOPS | Base BW | Process |
|---|---:|---:|---:|---|
| M1 (2020) | 16 | 11 | 68 GB/s | 5 nm |
| M2 (2022) | 16 | 15.8 | 100 GB/s | 5 nm |
| M3 (2023) | 16 | 18 | 100 GB/s | 3 nm |
| M4 (2024) | 16 | 38 | 120 GB/s | 3 nm |
| M5 (2025) | 16 | — | 154 GB/s | 3 nm |

TOPS have doubled from M3 to M4, but we're nowhere near saturating even the M1's 11 TOPS — our bottleneck is dispatch overhead, not raw compute. That makes the TOPS progression less interesting than the fact that the dispatch architecture hasn't changed. Base-tier memory bandwidth has also grown substantially, and the effect on ANE work is [less straightforward](#more-on-the-hardware).

## What we built

[ane.cpp](https://github.com/skyfallsin/ane.cpp) runs Qwen3.5 end-to-end on the Neural Engine, building on [maderix](https://github.com/maderix/ANE)[^4]'s reverse-engineering of Apple's private ANE framework and [johnmai-dev](https://github.com/johnmai-dev/ANE-LM)[^5]'s first working LLM runtime on ANE. Current M3 Max numbers (warmed 5-run medians, 500 generated tokens, Qwen thinking defaults[^7]):

| Model | Mode | Prompt | Generate |
|---|---|---:|---:|
| Qwen3.5-4B[^7] | fp16 | 18.93 tok/s | 9.21 tok/s |
| Qwen3.5-4B[^7] | int8 | 30.08 tok/s | 11.66 tok/s |
| Qwen3.5-9B | fp16 | 6.49 tok/s | 4.27 tok/s |
| Qwen3.5-9B | int8 | 7.39 tok/s | 7.01 tok/s |

### Concurrency

Single-stream generation isn't fast. But single-stream speed isn't really the point — what's more interesting is concurrency. During token generation most of the ANE's capacity goes unused, which means we can run multiple streams at once.

The tables below are from warmed serve-mode runs with Qwen's thinking defaults (`--enable-thinking`, `top_p=0.95`, `top_k=20`, `presence_penalty=1.5`, `repeat_penalty=1.0`, `temp=1.0`), 8 requests at 100 generated tokens each, 3 repeats per concurrency level, `--sessions 4`.

Aggregate generation throughput across all active streams:

<div style="max-width: 520px; margin: 1.5em auto;">
<canvas id="concurrencyChart" height="280" data-chart="
new Chart(document.getElementById('concurrencyChart'), {
  type: 'line',
  data: {
    labels: ['1 stream', '2 streams', '4 streams'],
    datasets: [{
      label: '4B int8',
      data: [10.53, 15.95, 28.62],
      borderColor: '#0066cc',
      backgroundColor: 'rgba(0, 102, 204, 0.08)',
      borderWidth: 2.5,
      pointRadius: 5,
      pointBackgroundColor: '#0066cc',
      tension: 0.2,
      fill: true
    }, {
      label: '4B fp16',
      data: [8.62, 12.59, 20.75],
      borderColor: '#66a3d2',
      borderWidth: 2,
      pointRadius: 4,
      pointBackgroundColor: '#66a3d2',
      tension: 0.2
    }, {
      label: '9B int8',
      data: [5.76, 5.81, 6.57],
      borderColor: '#6c757d',
      borderWidth: 2,
      pointRadius: 4,
      pointBackgroundColor: '#6c757d',
      tension: 0.2
    }, {
      label: '9B fp16',
      data: [3.62, 4.44, 4.89],
      borderColor: '#adb5bd',
      borderWidth: 2,
      pointRadius: 4,
      pointBackgroundColor: '#adb5bd',
      tension: 0.2
    }]
  },
  options: {
    responsive: true,
    plugins: {
      legend: { position: 'top' },
      tooltip: {
        callbacks: {
          label: function(ctx) {
            return ctx.dataset.label + ': ' + ctx.raw + ' tok/s';
          }
        }
      }
    },
    scales: {
      y: {
        beginAtZero: true,
        title: { display: true, text: 'Aggregate tok/s' },
        max: 32
      }
    }
  }
});
"></canvas>
</div>

Per-stream average at each concurrency level:

| Model | Mode | 1 stream | 2 streams | 4 streams |
|---|---|---:|---:|---:|
| Qwen3.5-4B | fp16 | 9.91 | 7.97 | 6.67 |
| Qwen3.5-4B | int8 | 12.19 | 9.61 | 9.25 |
| Qwen3.5-9B | fp16 | 4.31 | 2.77 | 1.71 |
| Qwen3.5-9B | int8 | 7.38 | 3.80 | 2.09 |

Four concurrent inference streams, locally, one process, on the neural engine, with the GPU and CPU staying free for everything else. If you just look at tokens-per-joule, the neural engine looks roughly comparable to GPU/CPU work in our measurements so far. But combine that with slower token generation and it means you can run this in parallel with multiple jobs for a much longer time.

We haven't really had the opportunity before to run many little agent streams locally, continuously, without turning the machine into a space heater. There have been some reports that M4s and M5s can more aggressively speed things up using runtime paths[^12] we don't currently have access to on M3, but we haven't verified that yet.

## How the runtime works

ane.cpp compiles each weight matrix into an ANE convolution kernel[^8] with weights baked in at compile time, and for each generated token the runtime bounces back and forth between ANE and CPU — ANE handles the big matrix multiplications, CPU handles the sequential stuff like attention and normalization that ANE can't do well in fp16[^9].

<div style="max-width: 480px; margin: 2em auto; font-family: 'JetBrains Mono', monospace; font-size: 12px; line-height: 1.6;">
<div style="padding: 6px 12px; background: var(--bg-alt); border: 1px solid var(--border); border-radius: 4px; margin-bottom: 4px; text-align: center; color: var(--text-muted);">
  Embedding lookup (CPU)
</div>
<div style="text-align: center; color: var(--text-muted); opacity: 0.5; line-height: 1;">↓</div>
<div style="border: 2px solid var(--accent); border-radius: 6px; padding: 10px 12px; margin-bottom: 4px;">
  <div style="text-align: center; color: var(--text-muted); font-size: 11px; margin-bottom: 6px;">× 32 layers</div>
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 4px;">
    <div style="padding: 4px 8px; background: var(--bg-alt); border: 1px solid var(--border); border-radius: 3px; color: var(--text-muted);">RMSNorm (CPU)</div>
    <div style="padding: 4px 8px; background: var(--accent); color: #fff; border-radius: 3px;"><b>Fused QKV</b> (ANE)</div>
    <div style="padding: 4px 8px; background: var(--bg-alt); border: 1px solid var(--border); border-radius: 3px; color: var(--text-muted);">RoPE + Attn (CPU)</div>
    <div style="padding: 4px 8px; background: var(--accent); color: #fff; border-radius: 3px;"><b>O proj + res</b> (ANE)</div>
    <div style="padding: 4px 8px; background: var(--bg-alt); border: 1px solid var(--border); border-radius: 3px; color: var(--text-muted);">RMSNorm (CPU)</div>
    <div style="padding: 4px 8px; background: var(--accent); color: #fff; border-radius: 3px;"><b>FFN + res</b> (ANE)</div>
  </div>
</div>
<div style="text-align: center; color: var(--text-muted); opacity: 0.5; line-height: 1;">↓</div>
<div style="padding: 6px 12px; background: var(--bg-alt); border: 1px solid var(--border); border-radius: 4px; margin-bottom: 4px; text-align: center; color: var(--text-muted);">
  Final norm (CPU)
</div>
<div style="text-align: center; color: var(--text-muted); opacity: 0.5; line-height: 1;">↓</div>
<div style="padding: 6px 12px; background: var(--accent); color: #fff; border-radius: 4px; text-align: center;">
  <b>LM head</b> (ANE, chunked)
</div>
</div>

The key operations are the fused kernels — `oproj_add` combines the output projection with a residual add in a single ANE dispatch[^10], and `ffn_resadd` does the same for the SwiGLU FFN block[^10]. This matters because decode on this hardware is dispatch-bound, with a rough fit of `latency ≈ 119µs + bytes / 78 GB/s`[^9] and about 113 dispatches per generated token where the fixed overhead dominates. Cutting even a few dispatches per layer adds up quickly across 32 layers.

Each weight matrix compiles into a MIL convolution program[^8] that gets loaded onto the ANE via Apple's private `AppleNeuralEngine.framework`[^4], and a persistent compile cache means the first-run compilation cost only needs to be paid once per kernel variant.

### Prefill

For prefill (processing the prompt), we pack multiple tokens into the W-lane dimension of the ANE's IOSurface tensors[^11]. The ANE requires a minimum spatial width of 32, so for single-token decode most of that width is wasted. During prefill we can batch 4 tokens at once across those lanes, which gets us roughly 2x the throughput compared to generation.

## More on the hardware

The ANE uses memory differently than a GPU. Weights don't stream from DRAM during inference — they're baked into ANE kernels at compile time. So the classic GPU bottleneck (bandwidth-bound weight loading) doesn't apply here. What does flow through memory is activation data: every time the runtime bounces between ANE and CPU — roughly 113 times per generated token — it writes results to an IOSurface and reads them back through DMA. Our measurements give an effective per-dispatch transfer rate of about 78 GB/s, with the bulk of each dispatch's latency (~119µs) coming from fixed overhead rather than the transfer itself.

For single-stream decode, that means bandwidth barely registers. Activation tensors are small at 4B scale (a few KB per dispatch), and the fixed dispatch overhead dominates so thoroughly that the M3 Pro's bandwidth regression — 154 vs the M2 Pro's 205 GB/s, after Apple trimmed the memory bus from 256-bit to 192-bit — produced no measurable change in ANE throughput. Single-stream decode is dispatch-bound, and no amount of extra bandwidth changes that.

But the workload we actually care about isn't single-stream. Four concurrent sessions generating tokens simultaneously means four times the activation traffic sharing the same memory bus. During W-lane batched prefill, each dispatch carries 4× the data. And if future runtime improvements chip away at that 119µs dispatch overhead — which is the single biggest thing standing between ANE inference and meaningfully higher throughput — the bandwidth term becomes the next ceiling. At that point, the difference between a base-tier M1 at 68 GB/s and a base-tier M5 at 154 GB/s starts determining how many concurrent streams can run before they contend with each other.

All our concurrency measurements are on M3 Max, which has 307+ GB/s of headroom. Whether a base-chip M1 or M5 would show different scaling is an open question — but it's the right question, because the workload we're building toward (multiple always-on agent streams on a MacBook Air) is exactly the scenario where base-tier bandwidth would be the constraint.

## What's next

The immediate priority is getting this into Jo — wiring ane.cpp as the backend for local indexing, background summarization, and the other ambient workloads that currently wake the GPU or round-trip to the cloud. That's the whole reason we went down this rabbit hole, and the concurrency numbers are good enough to start building on.

Beyond that, the things we're most interested in:

**Newer chips.** All of our measurements are on M3 Max, and several dead ends — runtime-weight convolutions, `_ANEClient` direct evaluation, multi-procedure MIL chaining — have external reports suggesting they may work on M4 or M5. The M4 doubled ANE TOPS from 18 to 38, and the M5 introduced per-GPU-core Neural Accelerators and a higher-bandwidth memory path. We don't know yet whether those translate into meaningfully faster dispatch or just more headroom we can't saturate, but finding out is near the top of the list.

**Smaller models.** A 1–2B dense model that's good enough for classification, routing, and summarization would be substantially faster on ANE — fewer layers means fewer dispatches per token, which is exactly where our bottleneck is. We currently support Qwen3.5 at 4B and 9B; adding smaller variants or other architectures is straightforward.

**Rigorous energy measurement.** The energy story is central to the thesis but we haven't published proper numbers yet. We have `powermetrics`-based tooling in the repo (`scripts/energy_benchmark.sh`) that measures per-subsystem power draw during inference, and the preliminary picture is encouraging. We just need to run it systematically across workloads and concurrency levels and publish the results.

**More model architectures.** ane.cpp currently only runs Qwen-family models. The compilation and dispatch infrastructure is generic enough that adding other dense transformer architectures (Llama, Gemma, Phi) should be mostly a matter of wiring up the layer configs and any architecture-specific attention patterns.

The optimizations that survived are the boring ones — fused kernels[^10], W-lane batching[^11], chunked FFN, and int8 weight quantization via `constexpr_blockwise_shift_scale` — and plenty of ideas didn't: ANE decode attention, speculative decode / self-draft, ANE RMSNorm fusion mega-kernels, cross-layer norm fusion, 3-runtime-input kernels, packed-slice workarounds, INT4, and runtime-weight convolutions all failed on M3 Max. The companion [field guide](https://github.com/skyfallsin/apple-neural-engine-field-guide)[^13] records each dead end alongside wins in a [karpathy/autoresearch](https://github.com/karpathy/autoresearch)-style loop: write a focused test, measure it, keep or discard, repeat.

## Repos

- [ane.cpp](https://github.com/skyfallsin/ane.cpp)
- [apple-neural-engine-field-guide](https://github.com/skyfallsin/apple-neural-engine-field-guide)

Both repos are MIT-licensed. We'd love contributions, especially from anyone with M4 or M5 hardware.

## Acknowledgments

This work wouldn't exist without [maderix](https://github.com/maderix/ANE), who reverse-engineered Apple's private ANE framework and made direct hardware access possible, and [johnmai-dev](https://github.com/johnmai-dev/ANE-LM), who built the first working LLM runtime on top of it. ane.cpp is a fork of johnmai-dev's project. Thanks also to [thebasedcapital](https://github.com/thebasedcapital/ane-infer) for exploring `_ANEClient` direct evaluation and multi-procedure MIL paths, and to the [Qwen team](https://huggingface.co/Qwen) for the excellent open-weight models we run on this hardware.

---

[^1]: Measured with [llama.cpp](https://github.com/ggml-org/llama.cpp) at full GPU utilization on M3 Max.

[^2]: Apple's Neural Engine is a fixed-function matrix accelerator present in every Apple Silicon chip since M1. Apple publishes TOPS and memory bandwidth specs per generation — see the specs table above. Within a generation, every SKU (base, Pro, Max) shares the same 16-core ANE block; only the Ultra variants (Mac Studio and Mac Pro) double it to 32 cores. Base-chip bandwidth has grown from 68 GB/s (M1, LPDDR4X) to 154 GB/s (M5, LPDDR5X-9600), while Max variants range from 410 to 614 GB/s. Unlike GPU configurations which vary dramatically by price tier, the ANE is one of the most consistent pieces of silicon in the lineup. Source data from Apple's [product spec sheets](https://support.apple.com/en-us/111902) and [Wikipedia's Apple Silicon articles](https://en.wikipedia.org/wiki/Apple_M4).

[^3]: [CoreML](https://developer.apple.com/documentation/coreml) is Apple's public ML framework. It can target the ANE, but the compiler makes opaque decisions about what runs where, the supported operation set is constrained, and there's no direct control over dispatch scheduling or IOSurface layout — all of which matter for autoregressive transformer decode.

[^4]: [maderix/ANE](https://github.com/maderix/ANE) — reverse-engineered Apple's private `AppleNeuralEngine.framework` to enable direct ANE access via `_ANEInMemoryModel`, `_ANERequest`, and `_ANEIOSurfaceObject` ObjC runtime classes, bypassing CoreML entirely. This is the foundation that makes everything else here possible.

[^5]: [johnmai-dev/ANE-LM](https://github.com/johnmai-dev/ANE-LM) — built the first working LLM inference runtime on top of maderix's ANE bridge, including safetensors loading, tokenizer support, chat templates, and a full Qwen3 forward pass on ANE. ane.cpp is a fork of this project.

[^6]: [Qwen3.5](https://huggingface.co/Qwen/Qwen3.5-4B) is a dense transformer model from Alibaba's Qwen team, using a hybrid architecture that mixes full attention with DeltaNet linear attention layers. We support the [4B](https://huggingface.co/Qwen/Qwen3.5-4B) and [9B](https://huggingface.co/Qwen/Qwen3.5-9B) parameter variants.

[^7]: Qwen3.5-4B uses a [hybrid DeltaNet + full attention architecture](https://qwenlm.github.io/blog/qwen3.5/) where most layers use linear attention with convolutional state, and every Nth layer uses standard full attention with KV cache. This means the per-layer ANE kernel structure varies — linear attention layers use a different projection pattern than full attention layers.

[^8]: ANE convolution kernels are compiled from [MIL (Model Intermediate Language)](https://apple.github.io/coremltools/docs-guides/source/model-intermediate-language.html) programs. Each weight matrix becomes a `conv` op with weights baked into the program binary. The ANE compiler turns these into hardware instructions loaded via `compileWithQoS:options:error:` and `loadWithQoS:options:error:` on `_ANEInMemoryModel`.

[^9]: fp16 RMSNorm on ANE showed an error floor of roughly 0.01 that was too large for fused norm+FFN mega-kernels we wanted to build — this is documented in detail in the [field guide test results](https://github.com/skyfallsin/apple-neural-engine-field-guide/blob/main/tests/README.md). The dispatch scaling fit comes from the same measurement suite.

[^10]: `oproj_add` fuses the output projection convolution with a residual add in one ANE dispatch: `x_updated = x_residual + conv(O_proj, attn_out)`. `ffn_resadd` fuses the full SwiGLU FFN (gate + up + silu + down projections) with a residual add: `output = x_residual + down(silu(gate(x)) * up(x))`. Each saves one ANE dispatch per layer, which at ~119µs fixed cost per dispatch adds up quickly across 32 layers.

[^11]: The ANE requires IOSurface tensors with a minimum spatial width (W dimension) of 32. For single-token decode, 31 of those lanes are unused. W-lane batching packs multiple independent tokens or requests into those lanes — during prefill we batch 4 prompt tokens across the W dimension, and during concurrent serving we batch decode steps from multiple active sessions. This is the primary mechanism behind the concurrency throughput scaling.

[^12]: [thebasedcapital/ane-infer](https://github.com/thebasedcapital/ane-infer) explored `_ANEClient` direct evaluation via `doEvaluateDirectWithModel:options:request:qos:error:` which bypasses the ANE daemon, and also investigated multi-procedure MIL models and chaining APIs (`prepareChainingWithModel:`). Their headline speeds come from Metal GPU decode on M5 hardware, not from a superior ANE path, but the direct eval and multi-procedure discoveries are real and may matter on newer chips.

[^13]: The [apple-neural-engine-field-guide](https://github.com/skyfallsin/apple-neural-engine-field-guide) contains 40+ focused test programs documenting what works and what doesn't on ANE, including failed attempts at speculative decode, runtime-weight convolutions, ANE-only attention, and various fusion strategies. It follows a [karpathy/autoresearch](https://github.com/karpathy/autoresearch)-style loop of write → measure → keep or discard.
