---
layout: post
title: analyzing 4,784 ai agent skills
date: 2026-02-03
---

I built a database of AI agent skills from 5 registries and scored them for quality.

## the registries

- [**anthropic**](https://github.com/anthropics/courses/tree/master/prompt_engineering_interactive_tutorial/Anthropic%201P/07_Skills) — official Anthropic skills
- [**openai**](https://github.com/openai/codex/tree/main/codex-cli/.codex/skills) — official OpenAI Codex skills
- [**openai-experimental**](https://github.com/openai/codex/tree/main/codex-cli/.codex/skills/.experimental) — experimental Codex skills
- [**clawdhub**](https://github.com/openclaw/skills) — community registry (largest)
- [**skillssh**](https://skills.sh) — community registry with web UI

## the data

| Registry | Skills | Avg Score | Range |
|----------|--------|-----------|-------|
| [openai-experimental](https://github.com/openai/codex/tree/main/codex-cli/.codex/skills/.experimental) | 5 | 83.0 | 72-92 |
| [openai](https://github.com/openai/codex/tree/main/codex-cli/.codex/skills) | 31 | 81.2 | 48-94 |
| [anthropic](https://github.com/anthropics/courses/tree/master/prompt_engineering_interactive_tutorial/Anthropic%201P/07_Skills) | 16 | 78.6 | 55-95 |
| [clawdhub](https://github.com/openclaw/skills) | 3,764 | 62.5 | 25-95 |
| [skillssh](https://skills.sh) | 968 | 59.7 | 30-95 |

<canvas id="registryChart" width="600" height="300" data-chart="
new Chart(document.getElementById('registryChart'), {
  type: 'bar',
  data: {
    labels: ['openai-exp', 'openai', 'anthropic', 'clawdhub', 'skillssh'],
    datasets: [{
      label: 'Avg Quality Score',
      data: [83.0, 81.2, 78.6, 62.5, 59.7],
      backgroundColor: ['#268bd2', '#2aa198', '#859900', '#b58900', '#cb4b16']
    }]
  },
  options: {
    scales: { y: { beginAtZero: true, max: 100 } },
    plugins: { legend: { display: false } }
  }
});
"></canvas>

Official registries score higher. Community registries have more variance.

## what makes a skill good

After reading hundreds of skills, patterns emerged:

| Signal | Impact | Example |
|--------|--------|---------|
| Structured workflow | +15 | phases, decision trees, numbered steps |
| Code examples | +12 | fenced blocks with real usage |
| Bundled scripts | +10 | `.py`, `.sh` files in `scripts/` |
| Clear triggers | +8 | "use when X", "invoke if Y" |
| Error handling | +5 | troubleshooting, fallbacks |
| Best practices | +5 | anti-patterns, "don't do X" |
| Placeholder content | -15 | TODO, TBD, `<placeholder>` |
| Very short (<500 chars) | -10 | insufficient guidance |
| Vague claims | -8 | "world-class" without code |

## top skills

| Skill | Registry | Score | Why |
|-------|----------|-------|-----|
| [prompt-guard](https://github.com/openclaw/skills/tree/main/skills/seojoonkim/prompt-guard) | clawdhub | 95 | 349 attack patterns, Python scripts |
| [skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator) | anthropic | 95 | meta-skill, progressive disclosure |
| [systematic-debugging](https://skills.sh/skills/obra/superpowers/systematic-debugging) | skillssh | 95 | iron law methodology, 4 phases |
| [docker-expert](https://skills.sh/skills/davila7/claude-code-templates/docker-expert) | skillssh | 94 | detection commands, security sections |
| [pptx](https://github.com/anthropics/skills/tree/main/skills/pptx) | anthropic | 94 | decision tree, JSON schemas |
| [develop-web-game](https://github.com/openai/skills/tree/main/skills/.curated/develop-web-game) | openai | 94 | playwright harness, test checklist |
| [docx](https://github.com/anthropics/skills/tree/main/skills/docx) | anthropic | 93 | redlining workflow, pandoc integration |
| [security-ownership-map](https://github.com/openai/skills/tree/main/skills/.curated/security-ownership-map) | openai | 93 | bundled scripts, neo4j import |
| [imagegen](https://github.com/openai/skills/tree/main/skills/.curated/imagegen) | openai | 92 | CLI modes, prompting guidance |
| [doc-coauthoring](https://github.com/anthropics/skills/tree/main/skills/doc-coauthoring) | anthropic | 92 | 3-stage workflow, exit conditions |

## distribution

<canvas id="distChart" width="600" height="300" data-chart="
new Chart(document.getElementById('distChart'), {
  type: 'doughnut',
  data: {
    labels: ['clawdhub (3764)', 'skillssh (968)', 'openai (31)', 'anthropic (16)', 'openai-exp (5)'],
    datasets: [{
      data: [3764, 968, 31, 16, 5],
      backgroundColor: ['#b58900', '#cb4b16', '#268bd2', '#859900', '#2aa198']
    }]
  },
  options: {
    plugins: { legend: { position: 'right' } }
  }
});
"></canvas>

clawdhub dominates by volume. But it has a duplicate problem.

## the duplicate problem

Same skill forked 15+ times:

| Skill | Copies |
|-------|--------|
| yahoo-finance | 15 |
| agent-browser | 8 |
| humanizer | 6 |
| remind-me | 5 |

Most are unchanged forks. The registry is ~79% duplicates.

## quality by content length

<canvas id="lengthChart" width="600" height="250" data-chart="
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
    scales: { y: { beginAtZero: true, max: 100 } }
  }
});
"></canvas>

Sweet spot is 2-10K characters. Beyond that, diminishing returns.

## what's missing

| Gap | Problem |
|-----|---------|
| Evaluation criteria | how do you know the skill worked? |
| Version constraints | which model versions support this? |
| Conflict detection | two skills want same trigger? |
| Composition | how do skills chain together? |

The ecosystem is young.

## browse

**[→ Interactive table with all 4,784 skills](/data/skills-db/)** — sortable, filterable, fast.

## download

```bash
curl -LO https://skyfallsin.github.io/data/skills-db/skills.db
sqlite3 skills.db "SELECT name, quality_score FROM skills ORDER BY quality_score DESC LIMIT 10"
```

---

## appendix: the database

### schema

```sql
CREATE TABLE skills (
    id INTEGER PRIMARY KEY,
    slug TEXT,
    name TEXT,
    registry TEXT,
    description TEXT,
    skill_md TEXT,
    github_url TEXT,
    stars INTEGER,
    trusted INTEGER,
    quality_score INTEGER,
    quality_rationale TEXT
);
```

### example queries

```sql
-- high quality with bundled scripts
SELECT name, registry, quality_score 
FROM skills 
WHERE quality_rationale LIKE '%scripts%' 
  AND quality_score > 80;

-- search by topic
SELECT name, registry, quality_score
FROM skills
WHERE skill_md LIKE '%playwright%'
ORDER BY quality_score DESC;
```

### scoring function

```python
import re

def score_skill(content: str) -> int:
    score = 50  # base
    
    # positive signals
    if re.search(r'workflow|steps|phases', content, re.I):
        score += 15
    score += min(len(re.findall(r'```\w+', content)) * 4, 12)
    if re.search(r'scripts?/|\.py\b|\.sh\b', content):
        score += 10
    if re.search(r'when to use|trigger|invoke', content, re.I):
        score += 8
    
    # negative signals
    if re.search(r'TODO|TBD|placeholder', content, re.I):
        score -= 15
    if len(content) < 500:
        score -= 10
    
    return max(20, min(98, score))
```

### scraping skills.sh

skills.sh doesn't have a content API, so I scraped the pages:

```python
import aiohttp
from bs4 import BeautifulSoup

async def fetch_skill_content(session, skill):
    url = f"https://skills.sh/skills/{skill['slug']}"
    async with session.get(url) as resp:
        html = await resp.text()
        soup = BeautifulSoup(html, 'html.parser')
        
        content_div = soup.find('div', class_='skill-content')
        if content_div:
            return content_div.get_text()
    return None
```

### files

All data available at [/data/skills-db/](/data/skills-db/):

| File | Size | Description |
|------|------|-------------|
| skills.db | 37MB | SQLite database |
| skills.json | 1MB | JSON export for table |
| apply_quality_scores.py | 7KB | Scoring script |
| quality_scores_collected.json | 9KB | Manual assessments |
