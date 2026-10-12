# Design System — PRADEEP.md

## Product Context
- **What this is:** Personal technical blog and portfolio for a hacker/founder
- **Who it's for:** Engineers, hackers, builders — people who read code and ship products
- **Space/industry:** Personal tech blog, YC founder portfolio
- **Project type:** Static site (Jekyll), editorial + portfolio hybrid

## Aesthetic Direction
- **Direction:** Editorial index — a quiet, typographic personal site
- **Decoration level:** Minimal — the type and hairline rules do all the work; no textures, grids, glows, or shadows
- **Mood:** A well-set table of contents. Large serif headings, a fixed left rail, and generous whitespace. Confident and unhurried.
- **Identity elements:** Sticky left rail with the serif `Pradeep` masthead and a baseline mono `.md` with no added gap, unnumbered navigation and sections, italic section headings without outer rules, mono dates in a left column

## Typography
- **Display/Hero:** Michelangelus 400 — masthead, upright post titles, post list titles, project names
- **Display italic:** Michelangelus italic — index section headings, tagline, `h3` inside posts, blockquotes
- **Body:** Instrument Sans 400 — paragraphs, descriptions, navigation
- **Meta:** Xanh Mono 400 — dates, labels (`Contents`, `TL;DR`, `built with`), table headers
- **Code:** JetBrains Mono 400 — inline code and code blocks
- **Loading:** Michelangelus self-hosted WOFF2; other fonts through Google Fonts CDN; `font-display: swap`
- **License note:** The downloaded Michelangelus EULA does not grant distribution rights. The owner explicitly directed publication despite that unresolved licensing risk; this is not evidence of permission.
- **Sizes:** masthead 2.75rem; section `h2` 2rem; post list title 1.5rem; post title `clamp(2.4rem, 4.2vw, 3.5rem)`; body 1rem (index) / 1.0625rem (posts); meta 0.8rem; code 0.84rem
- **Measure:** 42rem for prose and lists

## Color

### Light Mode
- **Surface:** `#ffffff`
- **Surface container:** `#f6f5f2` — code blocks
- **Text:** `#161514`
- **Muted text:** `#6f6a63`
- **Accent:** `#9b2d30` (madder red) — hover states only
- **Accent hover:** `#6e1d20`
- **Hairline:** `#e6e3dd`
- **Section rule:** `#161514`
- **Selection:** `#f1d9d6`

### Dark Mode
- **Surface:** `#100f0e`
- **Surface container:** `#1a1816`
- **Text:** `#ebe6dc`
- **Muted text:** `#948d83`
- **Accent:** `#e0a458` (ochre) — hover states only
- **Accent hover:** `#f0c37f`
- **Hairline:** `#2c2925`
- **Section rule:** `#ebe6dc`
- **Selection:** `#4a3a22`

Links are the text color with a thin underline; color appears only on hover.

## Spacing
- **Scale:** `0.25 / 0.5 / 0.75 / 1 / 1.5 / 2 / 3 / 4.5 / 7rem`
- **Density:** Generous — sections are separated by 7rem on desktop, 4.5rem on mobile
- **Rules:** 1px row separators; no rules above index section headings

## Layout
- **Canvas:** max 1240px, centered, 3rem side padding
- **Grid:** two columns — 240px rail + content, 7rem gutter. Content is left-aligned against the rail, not centered.
- **Rail:** sticky on the index (masthead, unnumbered nav, social + theme toggle pinned to the bottom); static on posts, where the table of contents sits beneath it and becomes the sticky element
- **Post list:** two-column rows — mono date (7.5rem column) then serif title — separated by hairlines
- **Projects:** 40px flat logo + serif name and sans description, separated by hairlines
- **Photos:** 4-column masonry, 2px radius, capped at 320px with a fade and `show more`
- **Border radius:** 2px everywhere; 50% for the profile photo only
- **Breakpoints:**
  - ≤1100px: rail narrows to 200px, photos 3 columns
  - ≤860px: single column; rail becomes a top header (masthead left, icons right, nav row beneath); post list stacks title over date; TOC becomes a collapsible box; code blocks run edge to edge

## Motion
- **Approach:** Almost none
- **Effects:** 150ms color transitions on hover; profile photo is grayscale and regains color when the rail is hovered; below-fold sections fade in by 6px. On devices without hover, photos use full color and icons and badges use full opacity.
- **Respects `prefers-reduced-motion`:** all transitions and animations disabled

## Decisions Log
| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-03-31 | Initial design system created | Codified from existing site by /design-consultation |
| 2026-03-31 | Dark mode shifted from purple to phosphor green | Purple triggered AI slop pattern #1; green is more authentic to the retro-terminal aesthetic |
| 2026-03-31 | Golden ratio scale retained | Unusual but distinctive; creates natural visual rhythm |
| 2026-09-14 | Instrument Sans for the site, IBM Plex Mono for `PRADEEP.md` | The readable sans-serif keeps long posts light while the site handle preserves the technical character |
| 2026-10-11 | Light mode flattened: white surface, no grid/noise, flat logos | Cleaner reading surface |
| 2026-10-12 | Editorial redesign: serif display type, left rail, numbered sections, hairline rules, warm dark mode | Make the site typographically distinct rather than another monospace developer blog; drop the retro-terminal decoration |
