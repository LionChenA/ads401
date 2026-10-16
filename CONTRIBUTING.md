# CONTRIBUTING.md — How to work in this repo

Rules and conventions live in [AGENTS.md](AGENTS.md); decisions and rationale
in [DECISIONS.md](DECISIONS.md). This file is the practical how-to.

## Setup (once)

```bash
git clone git@github.com:LionChenA/ads401.git && cd ads401
npm install                 # root: Astro (web report)
cd slides && npm install    # Slidev (presentation deck)
```

Requirements: Node 20+. First `astro build`/`slidev export` downloads a
Chromium for rendering.

## Everyday flow

1. Branch from latest `main`: `infra/*` (toolchain/config) ·
   `content/*` (report/slides text) · `fix/*`.
2. Commit atomically — format and rules: AGENTS.md §Workflow.
3. Push the branch and open a PR (`gh pr create`, or the compare URL GitHub
   prints). **This includes the repository owner** — `main` takes PRs only.
4. Review the PR diff; merging to `main` deploys (GitHub Actions builds the
   site). Nothing else to operate.
5. Preview before pushing: `npm run dev` at root (page) and in `slides/`
   (deck).

## Content updates

Facts live in `assets/pre2/scripts.md` — change facts there first, then
propagate to `site/src/content/report.md` and `slides/slides.md` **in the
same PR**. Never let a derived file contradict the facts layer (AGENTS.md,
§Content architecture).

## Before every PR

- No raw participant data or identifiable records anywhere in the diff.
- No build output (`dist/`, `.astro/`, `node_modules/`, PDFs) in the diff.
- Findings/status claims match the current study phase.

## Slide styling

Read [`.agents/skills/slides-style/SKILL.md`](.agents/skills/slides-style/SKILL.md)
before changing deck layout or styling — spec there, style tokens in
`slides/styles/index.css`.
