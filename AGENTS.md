# Blog Agent Instructions

## Structure

- **Posts**: `_posts/YYYY-MM-DD-title.md` (required naming format)
- **Layouts**: `_layouts/default.html` (main), `_layouts/post.html` (posts)
- **Config**: `_config.yml`

## Writing Posts

Create new posts in `_posts/` with this frontmatter:

```yaml
---
layout: post
title: your title here
date: YYYY-MM-DD
---
```

## Available Features

### Code Blocks
Standard fenced markdown with syntax highlighting:

```python
def example():
    return "highlighted"
```

### Mermaid Charts
Use for flowcharts, sequence diagrams, etc:

```html
<div class="mermaid">
graph LR
    A[Start] --> B[End]
</div>
```

Supported chart types: flowchart, sequence, class, state, gantt, pie, er

## Style Guidelines

- Keep titles lowercase
- Use simple, direct language
- Code-heavy posts are encouraged
- No fluff or filler content
- Monospace aesthetic - let the content speak

## Deployment

Push to `main` branch. GitHub Pages auto-builds and deploys to https://skyfallsin.github.io

## Commands

```bash
# Local dev (requires Docker)
docker run --rm -v "$PWD:/srv/jekyll" -p 4000:4000 jekyll/jekyll:4.2.2 jekyll serve --watch --force_polling

# Deploy
git add -A && git commit -m "message" && git push
```
