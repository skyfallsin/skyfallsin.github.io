---
layout: post
title: Analyzing 4,784 AI Agent Skills
date: 2026-02-03
---

As part of jo's upcoming launch, I collected **4,784 AI agent skills from 5 registries** for [skill-search](https://github.com/jo-inc/skill-search) and scored them for quality. **[Browse all skills →](/data/skills-db/)**

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
| Claude Code | `~/.claude/skills/` | `.claude/skills/` |
| Codex | `~/.codex/skills/` | `.codex/skills/` |
| OpenClaw | `~/.openclaw/skills/` | `.openclaw/skills/` |

Or invoke directly with `/skill-name`. The agent follows the instructions using its existing tools.

## Self-Improvement Loop

Recently, the excellent [openclaw](https://github.com/openclaw/openclaw) project now lets users self-install skills mid-conversation. Ask for a capability, the agent finds and installs a matching skill, uses it, and it persists for next time. The agent gets better at your workflows the more you use it. 

Very cool, and inline with what we'd expect a stack that has its own machine to be able to do. So, this pattern will likely stick, and we need to get ahead of it.

## Skills vs MCP

| | Skills | MCP |
|-|--------|-----|
| What | Markdown + examples + scripts | Protocol for remote tool servers |
| Loaded | As-needed into context | Tool definitions at startup |
| Executes via | Agent's existing tools (bash, file ops) | Dedicated MCP tool calls |
| Token cost | Pay when used | Pay upfront |

Skills are *instructions*. MCP is *tooling*. [Anthropic's framing](https://claude.com/blog/skills): "Think of Skills as custom onboarding materials that let you package expertise."

## The Registries

| Registry | Type | Skills | Avg Score | Range |
|----------|------|--------|-----------|-------|
| [openai-experimental](https://github.com/openai/codex/tree/main/codex-cli/.codex/skills/.experimental) | official | 5 | 83.0 | 72-92 |
| [openai](https://github.com/openai/codex/tree/main/codex-cli/.codex/skills) | official | 31 | 81.2 | 48-94 |
| [anthropic](https://github.com/anthropics/courses/tree/master/prompt_engineering_interactive_tutorial/Anthropic%201P/07_Skills) | official | 16 | 78.6 | 55-95 |
| [clawdhub](https://github.com/openclaw/skills) | community | 3,764 | 78.0 | 20-95 |
| [skillssh](https://skills.sh) | community | 968 | 77.7 | 28-95 |

<canvas id="registryChart" width="600" height="300" data-chart="
new Chart(document.getElementById('registryChart'), {
  type: 'bar',
  data: {
    labels: ['openai-exp', 'openai', 'anthropic', 'clawdhub', 'skillssh'],
    datasets: [{
      label: 'Avg Quality Score',
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

Closer than I expected. Everyone lands around 78-83.

## Quality Distribution

<canvas id="qualityDistChart" width="600" height="300" data-chart="
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

31% score 90+. 56% score 80+. Most appear usable, atleast from these stats.

## Quality Signals

| Signal | Impact |
|--------|--------|
| Structured workflow | +15 |
| Code examples | +12 |
| Bundled scripts | +10 |
| Clear triggers | +8 |
| No content | -20 |
| Placeholder text | -15 |
| Very short (<500 chars) | -10 |

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

~10% of skills include npm/pip install commands. Many bundle scripts right in the repo. MCP doesn't protect you. Skills route around it by telling the agent to use bash.

[1Password found infostealing malware in skill registries](https://1password.com/blog/from-magic-to-malware-how-openclaws-agent-skills-become-an-attack-surface). Their line:

> "Markdown isn't content in an agent ecosystem. Markdown is an installer."

This wasn't as much of a problem before, but with agents that can run on a persistent filesystem that also compound, the attack surface area just spiked dramatically.

### No verification

No provenance. No signed releases, no stable identity. "openai/pdf" and "random-github-user/pdf" coexist.

## So Why Use Skills?

Because they do work. The ecosystem is messy but the primitives are right. A folder with instructions that the agent loads when needed. No server to run, no protocol to implement, no dependencies to manage. Just markdown.

The best skills encode expertise that would take you hours to write out each time. Systematic debugging. Code review checklists. Framework-specific patterns. You pay tokens only when you need them.

Treat it like early npm or pip. Read what you install. Prefer skills from known sources. Don't run random bash scripts. The norms will catch up.

## Browse

- [Interactive table →](/data/skills-db/)
- [skills.db](/data/skills-db/skills.db) (SQLite, 2.1MB)
- [skills.json](/data/skills-db/skills.json)

```bash
curl -LO https://skyfallsin.github.io/data/skills-db/skills.db
sqlite3 skills.db "SELECT name, quality_score FROM skills ORDER BY quality_score DESC LIMIT 10"
```

---

[skill-search](https://github.com/jo-inc/skill-search) is the scraper and scorer behind this. Planning to add quality scoring to the CLI so you can filter before installing. PRs welcome.
