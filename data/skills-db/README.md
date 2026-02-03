# AI Agent Skills Database

SQLite database of 4,784 AI agent skills from 5 registries with quality scores.

## Files

- `skills.db` - SQLite database (37MB)
- `quality_scores_collected.json` - Manual quality assessments
- `apply_quality_scores.py` - Scoring script

## Schema

```sql
CREATE TABLE skills (
    id INTEGER PRIMARY KEY,
    slug TEXT,
    name TEXT,
    registry TEXT,
    description TEXT,
    skill_md TEXT,
    github_url TEXT,
    version TEXT,
    stars INTEGER,
    trusted INTEGER,
    updated_at TEXT,
    quality_score INTEGER,
    quality_rationale TEXT
);
```

## Quick Start

```bash
# Download
curl -LO https://skyfallsin.github.io/data/skills-db/skills.db

# Query
sqlite3 skills.db "SELECT name, registry, quality_score FROM skills ORDER BY quality_score DESC LIMIT 20"
```

## Example Queries

```sql
-- Top skills by quality
SELECT name, registry, quality_score, substr(quality_rationale, 1, 60)
FROM skills
WHERE quality_score >= 90
ORDER BY quality_score DESC;

-- Skills by registry
SELECT registry, COUNT(*), ROUND(AVG(quality_score), 1) as avg
FROM skills
GROUP BY registry
ORDER BY avg DESC;

-- Search by topic
SELECT name, registry, quality_score
FROM skills
WHERE skill_md LIKE '%playwright%'
ORDER BY quality_score DESC
LIMIT 10;

-- High quality with bundled scripts
SELECT name, registry, quality_score
FROM skills
WHERE quality_rationale LIKE '%scripts%'
  AND quality_score > 80
ORDER BY quality_score DESC;
```

## Registries

| Registry | Count | Avg Score |
|----------|-------|-----------|
| openai-experimental | 5 | 83.0 |
| openai | 31 | 81.2 |
| anthropic | 16 | 78.6 |
| clawdhub | 3,764 | 62.5 |
| skillssh | 968 | 59.7 |

## License

Data scraped from public registries. Use responsibly.
