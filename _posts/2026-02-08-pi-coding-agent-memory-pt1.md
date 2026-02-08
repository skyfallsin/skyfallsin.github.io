---
layout: post
title: "Ramping Up Eng Velocity with the Pi Coding Agent: Memory, Pt1"
date: 2026-02-08
published: false
---

I work across two repos, a Swift macOS app and a Python backend, with ~15 microservices. Every new [pi](https://github.com/badlogic/pi-mono) session costs 5-10 minutes re-explaining what I was doing, which tickets are in flight, what conventions matter. The `AGENTS.md` handles static stuff. Working state vanishes.

I described what I wanted to pi: three tiers of memory, all plain Markdown, no embeddings, no vector search. It built the whole thing as a pi extension in one session.

## What it created

A single TypeScript extension at `~/.pi/agent/extensions/memory.ts` (~460 lines) and a file layout under `~/.pi/agent/memory/`:

```
MEMORY.md              — curated long-term (decisions, preferences, durable facts)
SCRATCHPAD.md          — checklist of things to fix later
CATCHUP.md             — auto-generated "where we left off" summary
daily/YYYY-MM-DD.md   — append-only daily log
```

## Context injection

The extension hooks `before_agent_start` to append all memory into the system prompt each turn. It loads MEMORY.md, SCRATCHPAD.md, today's daily log, and yesterday's. Two days is enough for continuity without blowing the context window.

```typescript
pi.on("before_agent_start", async (event, _ctx) => {
    const memoryContext = buildMemoryContext();
    if (!memoryContext) return;
    return {
        systemPrompt: event.systemPrompt + memoryInstructions + memoryContext,
    };
});
```

`buildMemoryContext()` just concatenates the four files with section headers. Nothing clever.

## Tools

Three tools registered: `memory_write`, `memory_read`, `scratchpad`.

Every write gets an HTML comment with timestamp and short session ID for provenance:

```typescript
const stamped = `<!-- ${ts} [${sid}] -->\n${content}`;
```

`memory_write` returns existing file content in the tool result so the model can see what's already there and skip duplicates. The scratchpad uses `- [ ]` / `- [x]` checklist format with substring matching — `done("sprite")` checks off the first open item containing "sprite".

```typescript
// parseScratchpad pulls items from the checklist format
const match = lines[i].match(/^- \[([ xX])\] (.+)$/);
```

## Dashboard widget

On `session_start`, a widget renders the catchup summary and open scratchpad items. Clears itself on `agent_start` so it doesn't eat screen space once work begins.

```typescript
ctx.ui.setWidget("memory-dashboard", (_tui, _theme) => {
    return new Markdown(sections.join("\n\n---\n\n"), 1, 0, mdTheme);
});
```

## Background job

I asked pi to set up a launchd job that runs every 2 hours to clear done scratchpad items and generate a catchup summary. It created a plist at `~/Library/LaunchAgents/com.pi.scratchpad-review.plist` that runs pi headlessly:

```bash
pi -p "Review the scratchpad. Clear any done items.
Then read today's daily log and the scratchpad.
Write a bullet-point 'where we left off' summary
(max 5 bullets, each under 80 chars) to
~/.pi/agent/memory/CATCHUP.md ..."
```

The output is what I see when I open a new session:

```markdown
- SEC tickets JO-1555/1558 done; JO-1567 (sh -c hardening) open
- Sprite memory tools deployed but untested end-to-end
- JO-1568 (sprite memory) queued behind DB rewrite
- Lance as single source of truth for sprite history is in
- Uncommitted: server.ts, prompt.py, provisioning, ansible
```

No re-explaining needed.

## What's next

Part 2 will cover what happens when memory files grow — compaction, raw text vs. summaries, and whether this holds up or needs something smarter.
