# Design System — PRADEEP.md

## Product Context
- **What this is:** Personal technical blog and portfolio for a hacker/founder
- **Who it's for:** Engineers, hackers, builders — people who read code and ship products
- **Space/industry:** Personal tech blog, YC founder portfolio
- **Project type:** Static site (Jekyll), editorial + portfolio hybrid

## Aesthetic Direction
- **Direction:** Retro-Futuristic / Industrial
- **Decoration level:** Intentional — graph-paper grid background, subtle noise texture in dark mode
- **Mood:** An engineer's notebook. Precise, sparse, confident. The graph-paper grid says "I measure things." The monospace font says "I write code." The phosphor green dark mode says "I've been doing this since before it was cool."
- **Identity elements:** Graph-paper grid background, crosshair cursor, "PRADEEP.md" handle with typing animation, profile photo with glow ring (dark mode), retro 88×31 badge footer

## Typography
- **Display/Hero:** JetBrains Mono 600 — used for post titles, site handle
- **Body:** JetBrains Mono 400 — used everywhere, single-font system
- **UI/Labels:** JetBrains Mono 700 — uppercase section labels with letter-spacing
- **Data/Tables:** JetBrains Mono 300 — lighter weight for table content
- **Code:** JetBrains Mono 300 — same font, lighter weight distinguishes code blocks
- **Loading:** Google Fonts CDN, `font-display: swap`
- **Scale:** Golden ratio (φ = 1.618)
  - 3xs: `calc(1rem / φ³)` ≈ 0.236rem
  - 2xs: `calc(1rem / φ²)` ≈ 0.382rem
  - xs: `calc(1rem / φ)` ≈ 0.618rem
  - sm: `calc(1rem / 1.272)` ≈ 0.786rem
  - md: `1rem` (16px base)
  - lg: `calc(1rem × φ)` ≈ 1.618rem
  - xl: `calc(1rem × φ²)` ≈ 2.618rem
  - 2xl: `calc(1rem × φ³)` ≈ 4.236rem
  - 3xl: `calc(1rem × φ⁴)` ≈ 6.854rem

## Color

### Light Mode
- **Approach:** Restrained — 1 accent + neutrals
- **Surface:** `#ffffff`
- **On-surface (text):** `#111111`
- **Muted text:** `#555555`
- **Primary accent:** `#0066cc` — links, interactive elements
- **Hover accent:** `#0044aa` — darker blue on hover
- **Outline/borders:** `#e0e0e0`
- **Surface container:** `#f5f5f5` — code blocks, cards
- **Selection:** `#b3d4fc`
- **Grid:** `color-mix(in srgb, #111 3%, transparent)`

### Dark Mode
- **Approach:** Neon monochrome — phosphor green CRT terminal
- **Surface:** `#0d0d0d`
- **On-surface (text):** `#e8e8e8`
- **Primary accent:** `#39FF14` — links, interactive elements, profile glow
- **Secondary:** `#2ECC71` — muted text, dates, section labels
- **Tertiary:** `#00FF88` — hover states
- **Outline/borders:** `#1A5C2E`
- **Surface container:** `#0a1a0f` — code blocks, TOC background
- **Surface container high:** `#0f2a17` — elevated surfaces
- **Selection:** `#1A5C2E`
- **Grid:** `color-mix(in srgb, #39FF14 3%, transparent)`
- **Glow effects:** `0 0 12px rgba(57, 255, 20, 0.4)` on profile photo, code blocks, link hover
- **Noise overlay:** SVG fractalNoise at 3% opacity

### Semantic Colors (both modes)
- Success: inherits from primary accent
- Warning: `#F59E0B`
- Error: `#EF4444`
- Info: inherits from primary accent

## Spacing
- **Base unit:** Golden ratio derived (not 4px/8px grid)
- **Density:** Comfortable — generous whitespace is intentional
- **Scale:** Same φ-based scale as typography (3xs through 3xl)
- **Leading:** tight `1.272`, normal `1.618`, loose `1.618 × 1.128`
- **Tracking:** tight `-0.022em`, snug `-0.012em`, normal `-0.004em`, wide `0.006em`

## Layout
- **Approach:** Grid-disciplined
- **Homepage max-width:** `720px`
- **Post layout max-width:** `1020px` (280px TOC sidebar + content)
- **Grid:** Single column with date/content split on homepage
- **Border radius:** Minimal — `3xs` for code blocks and images, `50%` for profile photo only
- **Breakpoints:**
  - Mobile: `max-width: 768px` — smaller handle, code blocks edge-to-edge
  - Tablet/Desktop: `max-width: 1199px` — single column post layout, collapsible TOC
  - Wide: `min-width: 1200px` — two-column post layout with sticky sidebar TOC

## Motion
- **Approach:** Intentional
- **Easing:** ease-out for enter, ease-in for exit, ease-in-out for move
- **Duration:** 150ms links, 200ms profile photo/code blocks, 300ms handle underline, 500ms scroll-in
- **Effects:**
  - Scroll-in: `translateY(20px)` + opacity fade, staggered by 50ms per element
  - Handle hover: animated underline gradient + glitch effect (dark mode)
  - Profile photo hover: `scale(1.08) rotate(-2deg)` with shadow elevation
  - Link hover (dark mode): neon text-shadow glow
  - Code blocks (dark mode): inset neon border glow
- **Respects `prefers-reduced-motion`:** All animations disabled

## Decisions Log
| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-03-31 | Initial design system created | Codified from existing site by /design-consultation |
| 2026-03-31 | Dark mode shifted from purple to phosphor green | Purple triggered AI slop pattern #1; green is more authentic to the retro-terminal aesthetic |
| 2026-03-31 | Single-font system (JetBrains Mono) retained | Bold choice that reinforces engineer identity; hierarchy achieved through weight, size, and color instead of font variety |
| 2026-03-31 | Golden ratio scale retained | Unusual but distinctive; creates natural visual rhythm |
