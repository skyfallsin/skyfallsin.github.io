---
layout: post
title: "safe-skill-search: Quality-Filtered Local Search for Agent Skills"
date: 2026-02-03
published: true
---

In my [previous post](/2026/02/03/ai-agent-skills-database.html), I analyzed 4,784 AI agent skills across 5 registries. An agent needs to navigate this space quickly and safely.

[safe-skill-search](https://github.com/jo-inc/safe-skill-search) is a Rust CLI that searches 4,700+ skills locally in under 100ms with quality filtering. By default, it only shows skills with a quality score ≥ 80.

## Why local search

Skill discovery is part of the agent loop: plan → find capability → act. If it takes seconds, the loop stalls. Under 100ms keeps things responsive.

A web API can't reliably hit that bar:

| Issue | Impact |
|-------|--------|
| Network + TLS | 50-200ms baseline |
| Cold starts | Serverless adds 200-800ms |
| Rate limits | Queuing under load |
| Tail latency | p95 > p50, agents feel the worst case |

Other considerations:
- **Offline/CI environments**: Agents run in places with no internet
- **Privacy**: Search queries contain project context
- **Determinism**: Local indexes don't go down

## The stack: git → SQLite → Tantivy

Three layers, each with a reason to exist:

```text
GitHub repos (registries)
        │
        │  git clone --depth 1
        ▼
   repos/  ──────▶ parse SKILL.md frontmatter + content
        │                         │
        │                         ▼
        │                  SQLite skills.db
        │                  (metadata + full SKILL.md)
        │                         │
        │                         ▼
        └──────────────▶ Tantivy index/
                        (BM25 full-text search)
                                  │
                                  ▼
                          query → ranked results
```

### Git = distribution

The registries are already GitHub repos. Clone them locally with shallow fetch:

```bash
git clone --depth 1 https://github.com/openclaw/skills.git
```

Git becomes the package index transport. No custom sync protocol needed.

### SQLite = metadata cache

Store structured fields: slug, name, description, registry, trust level, stars, full SKILL.md content. Makes it trivial to build other views (`skill-search top`, `skill-search show`).

```sql
CREATE TABLE skills (
    slug TEXT NOT NULL,
    name TEXT NOT NULL,
    registry TEXT NOT NULL,
    description TEXT DEFAULT '',
    skill_md TEXT DEFAULT '',
    github_url TEXT NOT NULL,
    stars INTEGER DEFAULT 0,
    trusted INTEGER DEFAULT 0,
    UNIQUE(registry, slug)
);
```

### Tantivy = search engine

[Tantivy](https://github.com/quickwit-oss/tantivy) is a Rust search library with [BM25](https://en.wikipedia.org/wiki/Okapi_BM25) ranking. The index combines name, description, and full SKILL.md content for recall:

```rust
let content = format!("{} {} {}", skill.name, skill.description, skill.skill_md);
doc.add_text(self.content_field, &content);
```

Query parsing supports multi-field search with optional registry filtering:

```rust
let query_parser = QueryParser::for_index(
    &self.index,
    vec![self.name_field, self.description_field, self.content_field],
);
```

Result: sub-100ms queries across 4,700+ skills.

## Quality filtering: the safe in safe-skill-search

The [skills analysis](/2026/02/03/ai-agent-skills-database.html) showed only ~31% of skills score 90+. Many have placeholder content, broken scripts, or security concerns.

safe-skill-search embeds the quality scores directly into the binary:

```rust
pub struct QualityScores {
    scores: HashMap<String, QualityEntry>,
}

impl QualityScores {
    pub fn load() -> Self {
        let json_data = include_str!("../skills.json");  // frozen at build time
        // ...
    }
}
```

Search results are filtered before display:

```rust
.filter(|r| r["quality_score"].as_i64().unwrap_or(0) >= min_score)
```

The default `--min-score 80` means you only see skills that passed quality review. Override with `--min-score 0` to see everything.

Output now shows quality scores inline:

```bash
$ safe-skill-search search "browser"
1. [✓] puppeteer (anthropic) [Q:95] - Browser automation with Puppeteer
2. [⚠] smooth-browser ★1 (clawdhub) [Q:95] - Browser automation with error handling
3. [⚠] browserwing (clawdhub) [Q:80] - Browser automation toolkit
```

## End-to-end flow

### 1. Install

```bash
curl -fsSL https://github.com/jo-inc/safe-skill-search/releases/latest/download/install.sh | bash
```

The script detects your platform and downloads the right release. No Rust toolchain required.

### 2. First run: auto-sync

On first launch, safe-skill-search detects an empty database and syncs automatically:

```bash
$ safe-skill-search search "trello"
First launch detected, syncing skills...
Syncing registry: clawdhub
Syncing registry: anthropic
Syncing registry: openai
Indexing 4784 skills
```

This happens once. Takes ~10 seconds to clone 5 registries and build the index.

### 3. Search (with quality filtering)

```bash
$ safe-skill-search search "browser automation"
1. [✓] puppeteer (anthropic) [Q:95] - Browser automation with Puppeteer
   https://github.com/anthropics/skills/tree/main/skills/puppeteer

2. [⚠] smooth-browser ★1 (clawdhub) [Q:95] - Browser automation with error handling
   https://github.com/openclaw/skills/tree/main/skills/antoniocirclemind/smooth-browser
```

`[✓]` = trusted (anthropic, openai curated). `[⚠]` = community/experimental. `[Q:95]` = quality score.

Low-quality skills are filtered out by default. Show everything with `--min-score 0`.

For programmatic use:

```bash
$ safe-skill-search search "pdf" --json --limit 3
```

```json
[
  {
    "slug": "pdf",
    "name": "pdf",
    "registry": "anthropic",
    "description": "Comprehensive PDF manipulation toolkit...",
    "github_url": "https://github.com/anthropics/skills/tree/main/skills/pdf",
    "stars": 0,
    "trusted": true,
    "search_score": 25.3,
    "quality_score": 95
  }
]
```

### 4. Get install URL

```bash
$ safe-skill-search url trello
https://github.com/openclaw/skills/tree/main/skills/steipete/trello
```

## Bootstrapping your agent's toolkit

safe-skill-search is a CLI tool that helps you discover and vet skills before installing them.

The workflow:

```bash
safe-skill-search search "calendar"      # Find (quality filtered)
safe-skill-search show google-calendar   # Inspect (shows quality score)
safe-skill-search url google-calendar    # Get install URL
# → install in your agent
```

With 4,700+ skills, discovery with filtering is necessary infrastructure.

## Data storage

Everything lives in `~/.local/share/skill-search/`:

| Path | Contents | Size |
|------|----------|------|
| `skills.db` | SQLite with all skill metadata | ~2MB |
| `index/` | Tantivy search index | ~5MB |
| `repos/` | Cloned git repositories | ~100MB |

Update with `skill-search sync`. Force refresh with `skill-search sync --force`.

## Why not vector search

Why BM25 instead of embeddings?

| Approach | Pros | Cons |
|----------|------|------|
| BM25 | Zero dependencies, instant indexing, predictable | Keyword-based, no semantic understanding |
| Vectors | Semantic matching, handles synonyms | Requires embedding model, larger index, slower indexing |

For skill search specifically:

1. **Skills have good keywords.** Names like `trello`, `pdf`, `browser-automation` are already descriptive. You're usually searching for what you know you want.

2. **SKILL.md content is dense.** The full markdown includes examples, commands, trigger phrases. BM25 over this content catches most queries.

3. **Embedding adds latency at index time.** Generating embeddings for 4,700 skills means either shipping a model or calling an API. Both add friction to the "just works" goal.

4. **No model dependency.** The binary is self-contained. No Python, no ONNX runtime, no API keys.

Vector search makes sense when:
- Queries are vague ("something that helps with meetings")
- You're building a recommendation system
- Semantic similarity matters more than keyword match

BM25 covers most cases. Hybrid search (BM25 + vectors) is an option if recall becomes a problem.

## What's next

- ~~Quality scoring in CLI output (filter before installing)~~ ✓ Done
- Field boosts for better ranking (name > description > content)
- Maybe: prebuilt index distribution for faster first-run
- Periodic refresh of embedded quality scores

Local-first with quality filtering is the core constraint.

---

- [safe-skill-search on GitHub](https://github.com/jo-inc/safe-skill-search)
- [Skills analysis: 4,784 skills scored →](/2026/02/03/ai-agent-skills-database.html)
- [Browse the skills database →](/skills/)
