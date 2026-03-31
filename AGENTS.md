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

### Charts (Chart.js)
Charts animate when scrolled into view. Use `data-chart` attribute:

```html
<canvas id="myChart" width="400" height="200" data-chart="
new Chart(document.getElementById('myChart'), {
  type: 'line',
  data: {
    labels: ['Jan', 'Feb', 'Mar'],
    datasets: [{
      label: 'Values',
      data: [10, 20, 15],
      borderColor: '#b58900',
      tension: 0.3
    }]
  }
});
"></canvas>
```

Chart types: line, bar, pie, doughnut, radar, scatter, bubble

## Style Guidelines

- Use natural title case for headings
- Use simple, direct language
- Code-heavy posts are encouraged
- No fluff or filler content
- Monospace aesthetic - let the content speak

## Images
- **All images < 500KB**. Resize with `sips -Z 1200`.
- Image responsiveness: `style="max-width: 550px; width: 100%; height: auto;"` not `width="550"`.
- Use `loading="lazy"` on below-fold images.

## CSS & Responsiveness
- Test mobile breakpoints for CSS changes. Use responsive units.

## Design System
Always read `DESIGN.md` before making visual or UI decisions.
All font choices, colors, spacing, and aesthetic direction are defined there.
Do not deviate without explicit user approval.

## Local Dev
```bash
bundle exec jekyll serve --drafts --unpublished --livereload  # in tmux `blog`
```

## Deployment

Push to `main` branch. GitHub Pages auto-builds and deploys to https://skyfallsin.github.io
