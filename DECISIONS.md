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

## R-3 · Single-page report, deploy on merge
- **Status**: Accepted (2026-10-17, user-approved; deployment reworked same day)
- **Decision**: The web report is **one static page** (no sub-pages, sticky
  anchor navigation). Pushing to `main` triggers the **official Astro GitHub
  Pages workflow**, which builds the site and deploys it: merge = deploy. No
  extra deployment gates or preview environments — review happens at the PR.
  Build output is never committed to the repository.
- **Rationale**: The coursework sheet mandates a single hosted page and
  encourages anchor navigation; code quality is unmarked. CI deploy is the
  official Astro path and eliminates the stale-artifact failure mode of
  committing build output by hand.

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
  `build.inlineStylesheets: 'always'`. Deployment runs via the official
  Astro GitHub Pages workflow (R-3); build output stays out of git. Evaluated
  alternatives: Pandoc (fewer deps, no dev server) and Eleventy; Astro won on
  content/layout separation, dev-server iteration, and agent-ecosystem
  maturity.
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
- **Decision**: The teammate's `slides-promt.md` (sic — original filename) is
  abstracted into the
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

## R-13 · Rendered-output feedback loop: agent-browser
- **Status**: Accepted (2026-10-17, user-selected)
- **Decision**: Agents verify rendered output through
  [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)
  (install: `npm install -g agent-browser`), not by hand-editing and eyeballing.
  Loop: `npm run dev` → `agent-browser open <url>` → `snapshot` / `eval` /
  `read --outline` (structure assertions) → `errors` + `console` (runtime) →
  `screenshot --if-changed` (visual). Usage instructions are **not vendored**:
  run `agent-browser skills get` — the CLI serves version-matched skill content.
  Evaluated alternatives: chrome-devtools-mcp (official Google), playwright-mcp
  (official Microsoft), built-in harness tools (harness-private, not shareable).
- **Rationale**: Bash-native CLI (no resident MCP server/context overhead),
  first-class console/error capture, token-thrifty change-aware screenshots,
  official skill channel that never goes stale, Apache-2.0, Vercel Labs.
  Performance tracing was the only advantage of chrome-devtools-mcp and is
  irrelevant to a zero-JS static site.

## R-14 · Style system: Academic Teal, Direction A (journal serif)
- **Status**: Accepted (2026-10-17, user-selected via huashu-design
  three-direction gate; issue #6 open for team objections — 24h window)
- **Decision**: Web report and deck share one visual system, "Academic Teal":
  5-token palette (ink/teal/muted/line/accent), white paper, Newsreader serif
  display + Inter body. Web report = left sidebar layout (§01–08 + status
  pills + material links) with journal masthead. Deck = same serif family,
  seven-region structure kept, journal frame cover with status pills.
  Status pills: `Design stage` (teal) / `Findings pending` (amber);
  `In pilot` reserved. Current-section nav highlight = pure CSS
  view-timelines (zero JS; unsupported browsers degrade to hover-only).
  Poster (30 Nov) deliberately breaks style → Big-Type Editorial direction
  is reserved for it. Selected via the huashu-design three-direction gate:
  journal (chosen) / engineering-docs (rejected) / big-type (reserved for
  poster); harness-only tooling rejected as non-shareable.
- **Rationale**: slide–page unification principle — same kicker/divider/
  takeaway/pill vocabulary across surfaces; academic register fits coursework
  marking; white theme is print/project safe.

## R-15 · Deck style handover: flat master; web deck retired
- **Status**: Accepted (2026-10-18, user-approved)
- **Decision**: The deck follows the team's hand-built flat master
  (`ADS401_Cover_Updated.pptx`): single sans family, running head + `NN / 09`
  page numbers, hairline separators, no cards/frames/takeaways; palette keeps
  the R-14 tokens. `slides/slides.md` + `styles/index.css` + the
  slides-style skill were rewritten to this system; per-page bottom
  references replace the full references slide; the closing slide carries
  Materials inventory (Pending items labelled) + Q&A + the non-substantive
  AI-use disclosure line. The deployed **web deck is retired**: the slidev
  build step was removed from `deploy.yml` and the sidebar entrance deleted —
  it duplicated the submitted PDF. Initially R-14 continued to govern the web report
  page; amended the same day (user-approved): the report page's visual system
  is also unified onto the flat deck style (Inter only, ink 800 titles,
  accent h3, hairline dividers), retiring the serif on both surfaces.
  slides-style SKILL.md is the deck spec (updated in the same commit).
- **Rationale**: the hand-built master is the group's newest approved visual
  decision; one distribution channel (LMS PDF) avoids dual-source drift
  between the deck PDF and its web copy.
