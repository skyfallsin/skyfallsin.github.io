---
layout: post
title: "camoufox-browser: why AI agents need C++ anti-detection"
date: 2026-02-03
published: false
---

We learned this the dumb way: web scraping in 2026 isn't "fetch HTML." Modern browsing—especially at sites that matter—has turned into a negotiation with a paranoid machine. And if you show up looking even slightly off, that machine wins in under 200ms.

---

## Why JavaScript patching stopped working

We were building agents that needed to browse, not just hit APIs. Playwright worked fine on friendly sites. Then we aimed it at Google, Amazon, anything behind Cloudflare—and we didn't get rate-limited. We got *judged*.

Detection systems weren't just looking at `User-Agent`. They were measuring WebGL renderer strings, AudioContext sample rates, `navigator.hardwareConcurrency`, screen geometry, WebRTC IP leaks, battery API quirks, speech synthesis voices, and hundreds of other tells.

We did what everyone does: installed stealth plugins, patched `navigator.webdriver`, told ourselves it was "just a couple flags." It worked briefly. Then the patch itself became the fingerprint.

The lesson: **anything you can change in JavaScript, they can inspect in JavaScript.** If the page can see your override, detection systems can reason about it.

---

## Why C++ is the right layer

When JavaScript calls `navigator.hardwareConcurrency`, it's backed by a C++ implementation in Firefox. Override it in JS, and pages can detect the override—property descriptors look wrong, prototypes don't match, functions aren't native. But change the C++ return path, and JavaScript sees the spoofed value as if it's real. No wrapper, no shim, no tell.

That's what **[Camoufox](https://camoufox.com)** does. From the README:

> In Camoufox, data is intercepted at the C++ implementation level, making the changes undetectable through JavaScript inspection.

So we built **[camoufox-browser](https://github.com/jo-inc/camoufox-browser)**: a headless browser server for AI agents, powered by Camoufox. Engine-level changes—the kind commercial anti-detect browsers sell for $100+/month—packaged for agent workflows.

---

## What gets intercepted

The patches follow a simple pattern: check config, return spoofed value if set, otherwise fall through to normal implementation. From [`fingerprint-injection.patch`](https://github.com/daijro/camoufox/blob/main/patches/fingerprint-injection.patch):

```cpp
double nsGlobalWindowInner::GetInnerWidth(ErrorResult& aError) {
  if (auto value = MaskConfig::GetDouble("window.innerWidth"))
    return value.value();
  FORWARD_TO_OUTER_OR_THROW(GetInnerWidthOuter, (aError), aError, 0);
}
```

This pattern covers window geometry, navigator fields, screen details, WebGL parameters (GPU fingerprints via [`webgl-spoofing.patch`](https://github.com/daijro/camoufox/blob/main/patches/webgl-spoofing.patch)), WebRTC IP masking ([`webrtc-ip-spoofing.patch`](https://github.com/daijro/camoufox/blob/main/patches/webrtc-ip-spoofing.patch)), audio fingerprints, geolocation with auto-approval, battery API, and speech synthesis voices.

Camoufox also includes Bézier curve-based mouse trajectories in [`MouseTrajectories.hpp`](https://github.com/daijro/camoufox/blob/main/additions/camoucfg/MouseTrajectories.hpp)—because detection systems increasingly grade *how* you interact, not just what you send.

**All of this is intercepted in C++ before JavaScript ever sees it.**

---

## Why we wrapped it as a server

Agents don't want raw HTML. A Google results page is ~500KB of markup; the accessibility tree is ~5KB. That matters when your client is a model with a token budget.

So camoufox-browser provides:
- **Accessibility snapshots** instead of HTML
- **Element refs** (`e1`, `e2`, `e3`) instead of brittle selectors  
- **Macros** for common sites (`@google_search`, `@youtube_search`, `@amazon_search`)

```bash
# Create tab, get snapshot, click by ref
curl -X POST http://localhost:9377/tabs \
  -d '{"userId": "agent1", "sessionKey": "task1", "url": "https://google.com"}'

curl "http://localhost:9377/tabs/TAB_ID/snapshot?userId=agent1"

curl -X POST http://localhost:9377/tabs/TAB_ID/click \
  -d '{"userId": "agent1", "ref": "e3"}'
```

---

## Installing as an OpenClaw plugin

```bash
openclaw plugins install @askjo/camoufox-browser
```

Exposes tools: `camoufox_create_tab`, `camoufox_snapshot`, `camoufox_click`, `camoufox_type`, `camoufox_navigate`, `camoufox_scroll`, `camoufox_screenshot`.

OpenClaw supports multiple browser backends via profiles—use Camoufox where bouncers are strict, simpler stacks where they aren't:

```json
{
  "browser": {
    "profiles": {
      "camoufox": { "cdpUrl": "http://127.0.0.1:9377" },
      "browserless": { "cdpUrl": "https://browserless.io?token=KEY" }
    },
    "defaultProfile": "camoufox"
  }
}
```

---

## Proxies still matter

C++ spoofing handles browser identity, not IP identity. Most anti-bot systems correlate both: same fingerprint from 100 IPs looks weird; 100 fingerprints from one IP also looks weird.

The rule: **rotate fingerprints with IPs, keep them stable within a session.** Camoufox configures fingerprints per-session via environment variables, which maps well to isolated agent sessions. Residential proxies behave better than datacenter—the internet knows what datacenter ranges look like.

---

## Getting started

```bash
git clone https://github.com/jo-inc/camoufox-browser
cd camoufox-browser && npm install && npm start
curl http://localhost:9377/health
```

We didn't build this because we love browsers. We built it because our agents kept getting stopped at the door. At some point, you either keep arguing with JavaScript, or you change the thing JavaScript is talking to.
