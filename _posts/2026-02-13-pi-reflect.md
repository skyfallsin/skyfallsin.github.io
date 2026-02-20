---
layout: post
title: "*.md is all you need"
date: 2026-02-13
published: true
image: /images/posts/pi-reflect.png
thumb: /images/logos/pi-reflect.png
thumb_dark: /images/logos/pi-reflect-dark.png
force: light
---

<p align="center" style="margin: 4em 0;">
  <img src="/images/posts/pi-reflect.png" alt="pi-reflect" width="550" class="theme-img-light" />
  <img src="/images/posts/pi-reflect-dark.png" alt="pi-reflect" width="550" class="theme-img-dark" />
</p>

My obsession with [pi](https://pi.dev/) continues. Session files in pi are stored on disk as structured JSONL. Every user message, every assistant response, every tool call. That's uncommon in the coding agent ecosystem, and it means you can build a self-improving agent for yourself with just markdown files.

[pi-mem](/2026/02/11/pi-mem.html) gave me persistent memory. **[pi-reflect](https://github.com/jo-inc/pi-reflect)** closes the loop: it reviews recent conversations, finds where the agent screwed up, and edits the behavioral rules file so it doesn't happen again. Schedule it daily. Wake up to a better agent.

---

## How it works

Point it at a markdown file that controls how the agent behaves. `AGENTS.md`, `CLAUDE.md`, whatever. It reads session transcripts from the past N days, sends them to an LLM with the current rules, and asks: where did the user have to redirect this agent?

The LLM looks for real friction: user saying "no", "not that", "bro", "wtf". User repeating themselves. User undoing the agent's work. It proposes surgical edits, either strengthening an existing rule or adding a new one. Edits are applied with safety checks (exact text match, ambiguity detection, size sanity), then auto-committed to git.

```
/reflect ./AGENTS.md
```

One LLM call per run. ~$0.05–0.15 with Sonnet.

---

## What the edits look like

After a week of daily runs, my AGENTS.md has rules I never would have written myself. Not because they're surprising, but because they're the kind of specific that only comes from friction.

"When the user says 'continue' or repeats instructions, that means you're stalling. Act immediately."

"NEVER use `git add .`. Always add files explicitly by name."

"When asked to write a tweet, write ONE version. Don't give 3 options."

These came from the agent watching me get frustrated across dozens of sessions. The file grew from 180 to 325 lines over 7 runs. Every edit auto-commits, so `git log AGENTS.md` reads like a changelog of behavioral convergence.

---

## Beyond AGENTS.md

The engine doesn't know what it's editing. It sees a markdown file and evidence, then proposes edits to close the gap. The `prompt` field controls what gap to look for: behavioral correctness, factual completeness, identity convergence. Same engine, different targets.

I run it on three files:

- **AGENTS.md** — daily behavioral corrections from [pi](https://pi.dev/) sessions
- **SOUL.md** — weekly personality sharpening from [Jo](https://askjo.ai) conversations, pulled via a shell command that queries the production database
- **TOOLS.md** — CLI gotchas and command patterns

Each target has its own data sources. Transcripts can come from pi session files, shell commands, HTTP endpoints, or local files with glob patterns. All support `{lookbackDays}` interpolation and per-source byte caps.

The SOUL.md case is the interesting one. Jo is a consumer AI assistant with a personality, a tone, things it should and shouldn't say. Reflect reviews a week of real user conversations and sharpens the identity file from generic to specific. The personality converges toward something that fits the actual interaction patterns, not what we imagined at design time.

---

## Does it work

`/reflect-stats` tracks correction rate (corrections per session) over time. Here's mine for AGENTS.md over the last two weeks:

```
2026-02-05  0.45  ████        (9/20 sessions)
2026-02-06  0.30  ███         (18/61 sessions)
2026-02-07  0.24  ██          (15/62 sessions)
2026-02-08  0.24  ██          (15/62 sessions)
2026-02-09  0.24  ██          (15/62 sessions)
2026-02-10  0.25  ██          (15/61 sessions)
2026-02-11  0.10  █           (6/62 sessions)
2026-02-12  0.07  █           (5/67 sessions)
2026-02-13  0.10  █           (3/29 sessions)
2026-02-14  0.52  █████       (24/46 sessions)
2026-02-15  1.07  ███████████ (47/44 sessions)
2026-02-16  0.67  ███████     (28/42 sessions)
```

The drop from 0.45 to 0.07 is the agent absorbing my patterns. The spike on Feb 14-15 is real. I started an extensive Rust project unlike anything I'd built before, generating novel correction patterns the rules hadn't seen. The file grew from 180 to 325 lines.

It also tracks rule recidivism, which sections keep getting re-edited:

```
Recurring (not sticking):
  Read Before Acting     ×9 (6 strengthen, 3 add)
  Scope & Precision      ×5 (2 strengthen, 3 add)
  Execute first          ×3 (2 strengthen, 1 add)
  Anti-Over-Engineering  ×2 (0 strengthen, 2 add)

Resolved (edited once, not repeated): 6 rules
```

"Read Before Acting" getting strengthened 6 times tells me the wording still isn't forceful enough. The resolved rules stuck on the first try.

---

## Installation

```bash
pi install git:github.com/jo-inc/pi-reflect
```

```bash
/reflect ./AGENTS.md        # run once
/reflect                    # use saved target
/reflect-stats              # see if it's working
```

Schedule daily: `pi -p --no-session "/reflect"`

There's an [agent-readable setup guide](https://github.com/jo-inc/pi-reflect/blob/main/SETUP.md). Ask your pi to set it up for you.

---

## What's next

[Jo](https://askjo.ai) already runs pi-mem and pi-reflect for every user. Each person gets their own memory files and their own reflection loop, sharpening Jo's behavior and personality per-user from real conversations. It's early but it works.

The pattern isn't specific to coding agents. Any app that stores user interactions and has a configuration surface (a prompt, a preferences file, a rules engine) could run the same loop. Review what happened, find the friction, edit the config. Self-improving apps without a training pipeline. Just structured logs and a markdown file.

The repo is at [github.com/jo-inc/pi-reflect](https://github.com/jo-inc/pi-reflect). MIT licensed. ~900 lines of TypeScript, 137 tests.
