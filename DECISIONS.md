# DECISIONS.md — ads401 Repo Decision Log

> Human-readable log of binding decisions for **this repository** (governance,
> toolchain, content architecture). Operating rules derived from these live in
> [AGENTS.md](AGENTS.md).
>
> IDs are prefixed `R-` (repo) to avoid collision with the group's working-repo
> decision IDs (`D-xx`), which are maintained outside this repository.
> Status values: `Accepted` · `Superseded (→ R-x)`.

---

## R-1 · Repository scope: public deliverable surface only
- **Status**: Accepted (2026-10-05, inherited from initial setup)
- **Decision**: This repo hosts only public deliverables — the single-page web
  report (`index.html`, GitHub Pages), slides source, and submission artifacts.
  Working documents (research notes, survey drafts, group decision records)
  stay outside.
- **Rationale**: The coursework marks the public page, not internal process;
  a clean public surface limits leak risk.

## R-2 · Red line: no raw participant data
- **Status**: Accepted (2026-10-05, inherited)
- **Decision**: No raw participant data or identifiable records in this repo,
  ever — not in history, not if the repo were private. Public outputs use
  aggregate/anonymised results only.
- **Rationale**: Coursework sheet rule and ethics; public repo makes the
  constraint self-enforcing.

## R-3 · Single-page SPA, deploy on merge
- **Status**: Accepted (2026-10-17, user-approved)
- **Decision**: The web report is **one page** (`index.html` at repo root,
  sticky anchor navigation, no sub-pages), hosted by **branch Pages from
  `main`**: merging to `main` publishes. No extra deployment gate, no preview
  environment — review happens at the PR.
- **Rationale**: Coursework sheet mandates a single hosted page and encourages
  anchor navigation; code quality is unmarked, so the simplest pipeline wins.

## R-4 · Three-layer content sources (CORE maintenance contract)
- **Status**: Accepted (2026-10-17, user-approved)
- **Decision**: `assets/pre2/scripts.md` is the **facts layer** (single source
  of truth for RQs, sampling numbers, method claims, limitations, status).
  Two derived presentation layers: `site/src/content/report.md` (page prose →
  Astro build → `index.html`) and `slides/slides.md` (deck → Slidev). Facts
  change first; derived layers propagate in the same PR; drift is controlled
  by PR review, not automation. A single markdown driving both outputs was
  evaluated and rejected — the page (~2,000-word narrative) and the 3-minute
  deck (compressed takeaways) have incompatible lengths by design.
- **Rationale**: Coursework requires a ~10-minute read on the page and a
  3-minute talk on stage; one text cannot serve both.

## R-5 · Page toolchain: Astro
- **Status**: Accepted (2026-10-17, user-approved)
- **Decision**: The page is built with **Astro**, initialised per official
  docs (`npm create astro@latest`, minimal template) into `site/` — no
  hand-rolled scaffolding. Config: `output: 'static'`, zero client JS,
  `build.inlineStylesheets: 'always'`. The rendered `index.html` is committed
  at the repo root (deploy mechanism unchanged). Evaluated alternatives:
  Pandoc (fewer deps, no dev server) and Eleventy; Astro won on content/layout
  separation, dev-server iteration, and agent-ecosystem maturity.
- **Rationale**: The repository owner maintains the toolchain long-term and
  wants content/style separation with fast style iteration.

## R-6 · Slides toolchain: Slidev, source tracked in repo
- **Status**: Accepted (2026-10-17, user-approved)
- **Decision**: Slides stay on **Slidev** (`slides/`, own `package.json`).
  Deck source (`slides/slides.md`, `slides/styles/`, `package.json`) is
  version-controlled in this repo; `node_modules/`, `dist/` and exported PDFs
  are ignored. The exported
  `ADS401_GroupA_Presentation2Slides.pdf` is the LMS submission artifact and
  is not normally committed.
- **Rationale**: Untracked source was a single point of failure (no history,
  invisible to teammates); artifacts are reproducible from source.

## R-7 · Slide visual spec as a project skill
- **Status**: Accepted (2026-10-17, user-approved)
- **Decision**: The teammate's `slides-promt.md` is abstracted into the
  project skill [`.agents/skills/slides-style/SKILL.md`](.agents/skills/slides-style/SKILL.md)
  (seven-region layout, palette tokens, research-integrity rules; PPTX-output
  noise removed, repo paths bound). Skill = design spec; executable tokens
  live in `slides/styles/index.css`. Agents must load it before touching deck
  layout or styling (declared in AGENTS.md §5).
- **Rationale**: Keeps the spec versioned with the deck and discoverable by
  agent sessions; the `.agents/skills/` project location mirrors the
  user-level convention.

## R-8 · Meta file set and split of concerns
- **Status**: Accepted (2026-10-17, user-approved)
- **Decision**: Governance uses five files: `README.md` (orientation + file
  map), `AGENTS.md` (operating rules for agents and contributors),
  `DECISIONS.md` (this log), `CONTRIBUTING.md` (contribution mechanics),
  `LICENSE`. Rules and decision rationale are deliberately split — AGENTS.md
  states binding rules without history; this log keeps rationale without
  rules.
- **Rationale**: Agent-instruction files and human decision records serve
  different audiences; mixing them serves neither.

## R-9 · Branching and PR-only landing
- **Status**: Accepted (2026-10-17, user-approved)
- **Decision**: Direct pushes to `main` are forbidden. All changes — the
  repository owner's included — land via PR. Branch prefixes: `infra/*`,
  `content/*`, `fix/*`. Multi-item waves ride a single named batch branch
  (e.g. `infra/repo-governance`) with **atomic commits**, one final review PR.
- **Context**: Adopted after an unaudited direct push on 2026-10-15
  (`fc14d3d`) had to be force-pushed back (`aa0cfe1`); the PR gate makes
  review-before-landing structural instead of discretionary.

## R-10 · Commit conventions: atomic
- **Status**: Accepted (2026-10-17, user-approved)
- **Decision**: `type(scope): subject` with
  `type` ∈ docs|feat|fix|chore|refactor|ci and
  `scope` ∈ site|slides|infra|decisions|skills. One logical change per commit;
  content and infrastructure changes never share a commit; stage by name
  (`git add <paths>`), never `git add .`/`-A`. Full text: AGENTS.md §4.
- **Rationale**: The PR diff is the review surface; atomic commits keep each
  hunk reviewable and revertible.

## R-11 · License: CC BY 4.0
- **Status**: Accepted (2026-10-17, user-approved)
- **Decision**: The repository is licensed under **Creative Commons
  Attribution 4.0 International**. Third-party assets (fonts, libraries,
  cited figures) keep their own licenses and are acknowledged in the report.
- **Rationale**: The repo's substance is academic text and slides; CC BY 4.0
  carries the attribution semantics that MIT does not.

## R-12 · Content language: English
- **Status**: Accepted (2026-10-17, user-approved)
- **Decision**: Visible page and slide content is English (course language).
  Chinese glosses are allowed in speaker notes and internal working docs only.
- **Rationale**: The assessed artifacts are presented and marked in English;
  bilingual slide text would overcrowd the seven-region layout.
