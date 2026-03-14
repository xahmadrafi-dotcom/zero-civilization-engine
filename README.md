# ZERO ০ — Civilization Engine

শূন্যকে কেন্দ্র করে মানবসভ্যতার জ্ঞান-মানচিত্র। গণিত, দর্শন, প্রযুক্তি ও ইতিহাসে শূন্যের উৎস, বিস্তার ও প্রভাবকে একটি ইন্টারঅ্যাকটিভ ভিজ্যুয়াল নলেজ ইঞ্জিনে উপস্থাপন।

An interactive visual knowledge engine exploring the origin, spread, and impact of **zero** across mathematics, philosophy, technology, and history.

---

## Features

- **Interactive Knowledge Graph** — Explore 6 main branches with 36 interconnected knowledge nodes centered around zero
- **D3.js Visualization** — Force-directed graph with animated SVG nodes, cross-links, and geometric overlays
- **AI Explorer** — Built-in Claude AI panel for contextual Q&A about any concept in the graph
- **Historical Timeline** — 10 major milestones from Pingala (~300 BCE) to the 2038 Problem
- **Story Mode** — Narrative panel with philosophical context about zero's role in civilization
- **Particle Effects** — Canvas-based animated particles flowing between knowledge nodes
- **PNG Export** — Download the current visualization as a high-resolution PNG image
- **Responsive** — Touch-enabled zoom and pan, works on desktop and mobile

## Knowledge Branches

| Branch | বাংলা | Topics |
|--------|-------|--------|
| **Mathematics** | গণিত | Bakhshali Manuscript, Aryabhata, Brahmagupta, Place Value, Calculus, Binary |
| **Consciousness** | চেতনা | Buddhist Śūnyatā, Vedantic Zero, Jain Infinity, Sufi Fanā, Meditation, Quantum Zero |
| **Civilization** | সভ্যতা | Indus Valley, Indian Origin, Arab Transmission, European Spread, Colonial Erasure, Reclamation |
| **Technology** | প্রযুক্তি | Binary 0/1, Computing, AI, Banking, IEEE 754, 2038 Problem |
| **Language** | ভাষা | Sanskrit Śūnya, Arabic Etymology, Bengali ০, Glyph Evolution, Pingala's Meters, Digital Codes |
| **Creation** | সৃষ্টি | Big Bang, Quantum Vacuum, Fibonacci, Sacred Geometry, Quran 94:7, Manifesto |

## Getting Started

### Prerequisites

- A modern web browser (Chrome, Firefox, Safari, or Edge)
- No build tools, package managers, or installation required

### Run Locally

**Option 1 — Open directly:**

```bash
# Simply open index.html in your browser
open index.html          # macOS
xdg-open index.html      # Linux
start index.html         # Windows
```

**Option 2 — Local HTTP server (recommended for AI features):**

```bash
# Python 3
python -m http.server 8000

# Node.js
npx http-server -p 8000
```

Then visit `http://localhost:8000` in your browser.

### Deploy to GitHub Pages

1. Push `index.html` to the `main` branch
2. Go to **Settings → Pages** and set the source to the `main` branch
3. Your site will be available at `https://<username>.github.io/zero-civilization-engine/`

## Usage Guide

### Navigation

| Action | Desktop | Mobile |
|--------|---------|--------|
| Pan the canvas | Click and drag | Touch and drag |
| Zoom in/out | Scroll wheel | Pinch gesture |
| Select a branch | Click a branch node | Tap a branch node |
| View child node details | Click a child node | Tap a child node |
| Return to overview | Click the `⟳ Reset` button or the breadcrumb | Tap `⟳ Reset` |

### Toolbar Buttons

| Button | Function |
|--------|----------|
| `✦ AI Explorer` | Opens the Claude AI side panel for contextual analysis |
| `⏱ Timeline` | Displays a horizontal bar of 10 major historical events |
| `◈ Story` | Opens a narrative panel about zero's philosophical significance |
| `◎ Minimal` | Toggles minimal mode (hides decorative visual effects) |
| `⟳ Reset` | Resets zoom and clears all selections |
| `↓ PNG` | Exports the current view as a 2× resolution PNG image |

### AI Explorer Panel

The AI Explorer panel uses Claude to provide context-aware analysis of any selected node:

1. Click a branch or child node to select it
2. Click `✦ AI Explorer` to open the panel
3. Use the **pre-written prompt pills** or type a custom question
4. The panel also shows connected nodes with their relationships

> **Note:** The AI Explorer makes requests to the Anthropic API (`https://api.anthropic.com/v1/messages`). Browsers block direct cross-origin requests to this endpoint, so you need a server-side proxy that forwards requests and attaches your Anthropic API key. A minimal example using Node.js:
>
> ```bash
> npx cors-anywhere          # or any reverse proxy
> ```
>
> Alternatively, deploy a small proxy (e.g., a Cloudflare Worker or an Express middleware) that receives requests from the frontend, adds the `x-api-key` and `anthropic-version` headers, and forwards them to `https://api.anthropic.com/v1/messages`.

### Knowledge Card

When you click a child node, a knowledge card appears at the bottom of the screen showing:

- Node title, description, time period, and civilization
- A mini-timeline of related historical events
- An **AI বিশ্লেষণ** (AI Analysis) button to send the topic to the AI Explorer

### Zoom Controls

Use the `+` / `−` buttons in the bottom-right corner, or scroll/pinch to zoom.

## Technology Stack

- **[D3.js v7](https://d3js.org/)** — SVG-based data visualization and force-directed layouts
- **HTML5 Canvas** — Particle effects system
- **CSS3** — Animations, transitions, and dark theme styling
- **Vanilla JavaScript (ES6+)** — Application logic, no build step required

## Customization

The entire application is contained in a single `index.html` file. Key areas to customize:

| What | Where | Description |
|------|-------|-------------|
| **Branch data** | `BRANCHES` array | Add/edit knowledge branches and child nodes |
| **Timeline events** | `TIMELINE_EVENTS` array | Modify the historical timeline |
| **Cross-links** | `CROSS_LINKS` array | Change connections between branches |
| **Colors** | `color` field in each branch | Each branch has a hex color used for nodes, links, and glows |
| **Layout** | `BRANCH_R`, `CHILD_R` constants | Adjust node positioning radius |
| **AI model** | `model` field in `callClaude()` | Switch Claude model version (default: `claude-sonnet-4-20250514`) |
| **Language** | `lang="bn"` in `<html>` tag | Change the base document language |

## Browser Compatibility

| Browser | Supported |
|---------|-----------|
| Chrome / Edge 70+ | ✅ |
| Firefox 60+ | ✅ |
| Safari 12+ | ✅ |
| Mobile Safari / Chrome | ✅ (touch-enabled) |
| IE 11 | ❌ |

## License

See repository for license details.
