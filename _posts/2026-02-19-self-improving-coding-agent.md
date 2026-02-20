---
layout: post
title: "My Coding Agent Watches Me Get Frustrated, Then Fixes Itself"
date: 2026-02-19
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

I say "bro" a lot when my coding agent does the wrong thing. I say "no" and "not that" and "I literally just said." I repeat myself. I undo its work. I sigh audibly even though it can't hear me.

All of that frustration is data. [Pi](https://pi.dev/) stores every session as structured JSONL on disk. Every message, every tool call, every correction. What if the agent could read all of that, figure out what it keeps getting wrong, and fix its own rules?

**[pi-reflect](https://github.com/jo-inc/pi-reflect)** does exactly that. It reviews recent conversations, finds the friction, and edits the behavioral rules file so the same mistakes don't happen again. Schedule it daily. Wake up to a better agent.

---

## How it works

Point it at the markdown file that controls how your agent behaves. `AGENTS.md`, `CLAUDE.md`, whatever you use. It reads session transcripts from the past N days, sends them to an LLM along with the current rules, and asks one question: where did the user have to correct this agent?

It's looking for the moments you lost patience. "No, not that." "I already told you." "Just do it, stop asking." It proposes surgical edits, either strengthening a rule you already have or adding a new one. Safety checks make sure edits match exactly, aren't ambiguous, and don't blow away the file. Then it auto-commits to git.

```
/reflect ./AGENTS.md
```

One LLM call per run. ~$0.05-0.15 with Sonnet.

---

## The rules I'd never have written

After a week of daily runs, my AGENTS.md has rules that are weirdly specific. The kind of specific you only get from watching someone get annoyed over and over.

"When the user says 'continue' or repeats instructions, that means you're stalling. Act immediately."

"NEVER use `git add .`. Always add files explicitly by name."

"When asked to write a tweet, write ONE version. Don't give 3 options."

I didn't sit down and write these. The agent proposed them after watching me lose my patience across dozens of sessions. The file grew from 180 to 325 lines over 7 runs. Every edit auto-commits, so `git log AGENTS.md` reads like a record of the agent learning not to piss me off.

---

## It works on any markdown file

The engine doesn't care what it's editing. It sees a file and evidence, then proposes edits to close the gap. The `prompt` field controls what gap to look for: behavioral correctness, factual completeness, identity convergence. Same engine, different targets.

I run it on three files:

- **AGENTS.md** — daily behavioral corrections from [pi](https://pi.dev/) sessions
- **SOUL.md** — weekly personality sharpening from [Jo](https://askjo.ai) conversations, pulled via a shell command that queries the production database
- **TOOLS.md** — CLI gotchas and command patterns

Each target has its own data sources. Transcripts can come from pi session files, shell commands, HTTP endpoints, or local files with glob patterns.

The SOUL.md case is the interesting one. Jo is a consumer AI assistant with a personality, a tone, things it should and shouldn't say. Reflect reviews a week of real user conversations and sharpens the identity file from generic to specific. The personality converges toward something that fits actual interaction patterns, not what we imagined at design time.

---

## The frustration is measurably declining

`/reflect-stats` tracks correction rate (corrections per session) over time. Here's mine:

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

0.45 down to 0.07. The agent stopped doing the things that annoyed me. The spike on Feb 14-15 is real. I started an extensive Rust project unlike anything I'd built before, and the agent hit a wall of new mistakes it hadn't been corrected on yet. The rules file absorbed them.

It also tracks which rules aren't sticking:

```
Recurring (not sticking):
  Read Before Acting     ×9 (6 strengthen, 3 add)
  Scope & Precision      ×5 (2 strengthen, 3 add)
  Execute first          ×3 (2 strengthen, 1 add)
  Anti-Over-Engineering  ×2 (0 strengthen, 2 add)

Resolved (edited once, not repeated): 6 rules
```

"Read Before Acting" strengthened 6 times. The agent keeps theorizing instead of reading the code. The wording still isn't forceful enough. The resolved rules stuck on the first try.

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
