# AGENTS.md — ads401 Operating Rules

Rules agents and contributors must follow. Rationale: [DECISIONS.md](DECISIONS.md) ·
Orientation: [README.md](README.md).

## Non-negotiables

- **No raw participant data or identifiable records** — ever, even in history.
- AI help on graded artifacts is **non-substantive only** (proofread, format,
  generic suggestions), cited in the report.
- Findings say **pending** until data exists. No invented numbers, no causal
  claims from this cross-sectional design.
- **`main` is deploy-on-merge** (branch Pages) and takes **PRs only** — owner
  included. Never push directly.
- Artifact naming per coursework sheet: `ADS401_GroupA_*`.

## Content architecture (three layers)

- `assets/pre2/scripts.md` — **facts SSOT**: RQs, sampling numbers, claims,
  limitations. Change facts here first.
- Derived layers, updated in the **same PR** as any fact change:
  `site/src/content/report.md` → `index.html` (Astro) ·
  `slides/slides.md` (Slidev). Never contradict the facts layer.
- Visible content in **English**; Chinese only in speaker notes and working
  docs.

## Workflow

- Branches: `infra/*` | `content/*` | `fix/*`. Waves ride one batch branch
  with **atomic commits**: `type(scope): subject`
  (docs|feat|fix|chore|refactor|ci × site|slides|infra|decisions|skills),
  one logical change each, stage by name — never `git add .` / `-A`.
- Build via `package.json` scripts (root = page, `slides/` = deck). Commit the
  rendered `index.html`; never `node_modules/`, `dist/`, `.astro/`, PDFs.

## Skills

- `.agents/skills/slides-style/` — load before touching deck layout or style
  (spec lives there; tokens in `slides/styles/index.css`).
