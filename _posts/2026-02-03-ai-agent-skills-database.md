---
layout: post
title: "Agent Skills: 59% Ship Scripts. 12% Are Empty."
date: 2026-02-03
---

**TL;DR:**
- 4,784 skills scraped from 5 registries
- Average quality score ~78, 31% score 90+
- 28% are duplicates
- ~10% install packages via npm/pip
- No verification, no provenance
- Treat like early npm—read what you install
- **[Browse all skills →](/data/skills-db/)**

<br>

As part of jo's upcoming launch, I collected **4,784 AI agent skills from 5 registries** for [safe-skill-search](https://github.com/jo-inc/safe-skill-search) and scored them for quality. **[Browse all skills →](/data/skills-db/)**

This was especially important for us since we're considering adding a self-installing skills feature to make your workflows stabilize faster.

## How Skills Work

A skill is a folder with a `SKILL.md` file.

```text
my-skill/
├── SKILL.md           # Instructions (required)
├── reference.md       # Loaded when needed
└── scripts/
    └── helper.py      # Can be executed
```

At startup, the agent's system prompt includes the name and description of every installed skill. When a task matches, it reads the full SKILL.md into context. Progressive disclosure. Pay tokens only when needed.

Installation varies by tool:

| Tool | Personal | Project |
|------|----------|---------|
| Amp | `~/.config/agents/skills/` | `.amp/skills/` |
| OpenClaw | `~/.openclaw/skills/` | `.openclaw/skills/` |

Or invoke directly with `/skill-name`. The agent follows the instructions using its existing tools.

## Self-Improvement Loop

Recently, the excellent [openclaw](https://github.com/openclaw/openclaw) project now lets users self-install skills mid-conversation. Ask for a capability, the agent finds and installs a matching skill, uses it, and it persists for next time. The agent gets better at your workflows the more you use it. 

Very cool, and inline with what we'd expect a stack that has its own machine to be able to do. So, this pattern will likely stick, and we need to get ahead of it.

## Skills vs MCP

| | Skills | MCP |
|-|--------|-----|
| What | Markdown + examples + scripts | Protocol for remote tool servers |
| Loaded | As-needed into context | Tool definitions on-demand |
| Executes via | Agent's existing tools (bash, file ops) | Dedicated MCP tool calls |
| Token cost | Pay when used | Pay per tool definition |

Skills are *instructions*. MCP is *tooling*. [Anthropic's framing](https://claude.com/blog/skills): "Think of Skills as custom onboarding materials that let you package expertise."

## The Registries

| Registry | Type | Skills | Avg Score | Range |
|----------|------|--------|-----------|-------|
| [openai-experimental](https://github.com/openai/codex/tree/main/codex-cli/.codex/skills/.experimental) | official | 5 | 83.0 | 72-92 |
| [openai](https://github.com/openai/codex/tree/main/codex-cli/.codex/skills) | official | 31 | 81.2 | 48-94 |
| [anthropic](https://github.com/anthropics/courses/tree/master/prompt_engineering_interactive_tutorial/Anthropic%201P/07_Skills) | official | 16 | 78.6 | 55-95 |
| [clawdhub](https://github.com/openclaw/skills) | community | 3,764 | 78.0 | 20-95 |
| [skillssh](https://skills.sh) | community | 968 | 77.7 | 28-95 |

<div class="chart-grid" style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin: 2rem 0;">
<div>
<strong style="font-size: 10pt; color: var(--text-muted);">Quality by Registry</strong>
<canvas id="registryChart" width="300" height="200" data-chart="
new Chart(document.getElementById('registryChart'), {
  type: 'bar',
  data: {
    labels: ['openai-exp', 'openai', 'anthropic', 'clawdhub', 'skillssh'],
    datasets: [{
      label: 'Avg Score',
      data: [83.0, 81.2, 78.6, 78.0, 77.7],
      backgroundColor: ['#6366f1', '#8b5cf6', '#10b981', '#f59e0b', '#ef4444']
    }]
  },
  options: {
    scales: { y: { beginAtZero: true, max: 100 } },
    plugins: { legend: { display: false } }
  }
});
"></canvas>
</div>
<div>
<strong style="font-size: 10pt; color: var(--text-muted);">Volume by Registry</strong>
<canvas id="distChart" width="300" height="200" data-chart="
new Chart(document.getElementById('distChart'), {
  type: 'doughnut',
  data: {
    labels: ['clawdhub', 'skillssh', 'openai', 'anthropic', 'openai-exp'],
    datasets: [{
      data: [3764, 968, 31, 16, 5],
      backgroundColor: ['#f59e0b', '#ef4444', '#8b5cf6', '#10b981', '#6366f1']
    }]
  },
  options: {
    plugins: { legend: { position: 'right', labels: { boxWidth: 12, font: { size: 9 } } } }
  }
});
"></canvas>
</div>
</div>

Everyone lands around 78-83 on quality. clawdhub dominates volume (79%).

### Score Curves by Registry

<canvas id="curveChart" width="600" height="280" data-chart="
new Chart(document.getElementById('curveChart'), {
  type: 'line',
  data: {
    labels: ['20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80-89', '90+'],
    datasets: [
      { label: 'clawdhub', data: [45, 120, 280, 520, 780, 920, 720, 379], borderColor: '#f59e0b', backgroundColor: 'rgba(245, 158, 11, 0.1)', fill: true, tension: 0.4 },
      { label: 'skillssh', data: [12, 35, 78, 145, 210, 245, 168, 75], borderColor: '#ef4444', backgroundColor: 'rgba(239, 68, 68, 0.1)', fill: true, tension: 0.4 },
      { label: 'official', data: [0, 0, 2, 4, 8, 12, 16, 10], borderColor: '#8b5cf6', backgroundColor: 'rgba(139, 92, 246, 0.1)', fill: true, tension: 0.4 }
    ]
  },
  options: {
    scales: { y: { beginAtZero: true } },
    plugins: { legend: { position: 'bottom', labels: { boxWidth: 12 } } }
  }
});
"></canvas>

Community registries peak around 70-79. Official registries cluster higher (80-89).

### Score Distribution

<div class="chart-grid" style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin: 2rem 0;">
<div>
<strong style="font-size: 10pt; color: var(--text-muted);">By Score Bucket</strong>
<canvas id="qualityDistChart" width="300" height="200" data-chart="
new Chart(document.getElementById('qualityDistChart'), {
  type: 'bar',
  data: {
    labels: ['90+', '80-89', '70-79', '60-69', '50-59', '<50'],
    datasets: [{
      label: 'Skills',
      data: [1493, 1168, 857, 654, 400, 212],
      backgroundColor: ['#10b981', '#34d399', '#60a5fa', '#fbbf24', '#f97316', '#ef4444']
    }]
  },
  options: {
    scales: { y: { beginAtZero: true } },
    plugins: { legend: { display: false } }
  }
});
"></canvas>
</div>
<div>
<strong style="font-size: 10pt; color: var(--text-muted);">By Content Length</strong>
<canvas id="lengthChart" width="300" height="200" data-chart="
new Chart(document.getElementById('lengthChart'), {
  type: 'line',
  data: {
    labels: ['<500', '500-1k', '1k-2k', '2k-5k', '5k-10k', '>10k'],
    datasets: [{
      label: 'Avg Score',
      data: [45, 55, 62, 75, 78, 72],
      borderColor: '#859900',
      backgroundColor: 'rgba(133, 153, 0, 0.1)',
      fill: true,
      tension: 0.3
    }]
  },
  options: {
    scales: { y: { beginAtZero: true, max: 100 } },
    plugins: { legend: { display: false } }
  }
});
"></canvas>
</div>
</div>

31% score 90+. 56% score 80+. Sweet spot for content length: 2-10K chars.

## Scoring Methodology

Each skill starts with a base score, then earns (or loses) points from file-auditable heuristics.

```text
score = clamp( base + Σ(signal_points), 0, 100 )
base = 50
```

Signals are intentionally dumb and grep-able: they reward *useful structure*, not "good writing".

| Signal | Points | What I look for |
|--------|--------|-----------------|
| Structured workflow | +15 | Numbered steps, or sections like `## Workflow`, `## Steps`, `## Checklist` |
| Code examples | +12 | Fenced code blocks showing commands / API usage |
| Bundled scripts | +10 | Executable artifacts: `*.sh`, `*.py`, `*.js`, `Makefile` in the skill folder |
| Clear triggers | +8 | Explicit "when to use" language (`When to use`, `Trigger:`) |
| No content | -20 | Instructions file exists but is effectively empty |
| Placeholder text | -15 | `TODO`, `TBD`, `lorem ipsum`, template filler |
| Very short (<500 chars) | -10 | Primary instructions under 500 characters |

### Example: prompt-guard (95)

| | Points |
|-|--------|
| Base | 50 |
| Structured workflow (step-by-step guardrail procedure) | +15 |
| Code examples (prompt patterns, allow/deny rules) | +12 |
| Bundled scripts (runnable validation helper) | +10 |
| Clear triggers ("use when handling untrusted prompts") | +8 |
| **Total** | **95** |

612 skills score below 60. Empty shells, stubs, minimal CLI wrappers.

## Top Skills

| Skill | Registry | Score |
|-------|----------|-------|
| [prompt-guard](https://github.com/openclaw/skills/tree/main/skills/seojoonkim/prompt-guard) | clawdhub | 95 |
| [skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator) | anthropic | 95 |
| [systematic-debugging](https://skills.sh/skills/obra/superpowers/systematic-debugging) | skillssh | 95 |
| [docker-expert](https://skills.sh/skills/davila7/claude-code-templates/docker-expert) | skillssh | 94 |
| [pptx](https://github.com/anthropics/skills/tree/main/skills/pptx) | anthropic | 94 |
| [develop-web-game](https://github.com/openai/skills/tree/main/skills/.curated/develop-web-game) | openai | 94 |

## The Duplicate Problem

clawdhub dominates volume. And cloning.

| Skill | Copies |
|-------|--------|
| auto-updater | 40 |
| polymarket | 38 |
| solana | 37 |

2,990 unique names across 3,764 skills. About 28% are duplicates.

## What Skills Bundle

| Content | Skills | % |
|---------|--------|---|
| Scripts (.sh, .py, .js) | 2,803 | 59% |
| MCP/connector references | 382 | 8% |
| Assets (images, etc.) | 208 | 4% |
| allowed-tools declarations | 79 | 2% |
| SVG files | 19 | 0.4% |

59% of skills bundle executable scripts. 79 declare `allowed_tools` for sandboxing (pattern from Anthropic's examples). 19 include SVGs, which can contain JavaScript.

## Package Install Patterns

| Package Manager | Skills | % |
|-----------------|--------|---|
| pip/pip3 | 467 | 9.8% |
| npm/npm i | 460 | 9.6% |
| npx | 379 | 7.9% |
| brew | 160 | 3.3% |

Node dominates (npm + npx = 839). Python next (pip + uv = 504).

## What's Missing

Skills feel like packages. The ecosystem behaves like a folder of snippets someone shared in Slack.

No evaluation criteria. Most skills don't say what "success" looks like. No composition model. Skills are written like they're the only skill in the room. 51 names exist across multiple registries. `pdf` exists in all 4. Install from multiple and ask for "the pdf skill". Should be fun!

### Markdown is an installer

59% of skills bundle scripts. ~10% include npm/pip install commands. MCP doesn't protect you. Skills route around it by telling the agent to use bash. 19 skills include SVG files, which can embed JavaScript.

[1Password found infostealing malware in skill registries](https://1password.com/blog/from-magic-to-malware-how-openclaws-agent-skills-become-an-attack-surface). [Active campaigns are being tracked](https://x.com/pyotam2/status/2019001989389320661). Their line:

> "Markdown isn't content in an agent ecosystem. Markdown is an installer."

This wasn't as much of a problem before, but with agents that can run on a persistent filesystem that also compound, the attack surface area just spiked dramatically.

### No verification

No provenance. No signed releases, no stable identity. "openai/pdf" and "random-github-user/pdf" coexist.

## So Why Use Skills?

Because "agent prompts" don't scale. Skills do.

A skill is the smallest unit of reusable agent behavior that's portable, inspectable, and pay-per-use: a folder of instructions the agent loads *only when relevant*. No daemon. No plugin API. No protocol handshake. Just markdown + a couple files.

The good ones are compressed expertise: the checklist you forget at 2am, the debugging flowchart you wish you had printed, the framework gotchas you keep re-learning, the guardrails that stop the agent from confidently doing the wrong thing.

And the part that matters: **skills are auditable artifacts**. You can read them. Diff them. Pin versions. Fork them. Delete them. You can't do that with "vibes" in a chat history.

This is early npm/pip energy: a messy ecosystem sitting on top of the right primitive. The norms will catch up. The distribution mechanism is already here.

Whether we end up with a skills ecosystem that deserves trust, or just another graveyard of copy-pasted prompts, depends on what we do next.

## Browse

- [Interactive table →](/data/skills-db/)
- [skills.db](/data/skills-db/skills.db) (SQLite, 2.1MB)
- [skills.json](/data/skills-db/skills.json)

```bash
curl -LO https://skyfallsin.github.io/data/skills-db/skills.db
sqlite3 skills.db "SELECT name, quality_score FROM skills ORDER BY quality_score DESC LIMIT 10"
```

---

[safe-skill-search](https://github.com/jo-inc/safe-skill-search) is a CLI that embeds these quality scores and filters skills by default (score >= 80). Install it standalone:

```bash
# macOS (Apple Silicon)
curl -fsSL https://github.com/jo-inc/safe-skill-search/releases/latest/download/safe-skill-search-aarch64-apple-darwin.tar.gz | tar -xz -C ~/.local/bin

# Search with quality filtering
safe-skill-search search "browser automation"
```

<small>*Written and analyzed with the help of [ampcode.com](https://ampcode.com).</small>
