# ADS401 Group A — Evaluating AI Integration at XJTLU

**Live report:** https://lionchena.github.io/ads401/

Group A · Hongcheng TANG · Mingjian TAO · Liyuan CHEN · Haode SHEN
ADS401 Evaluation Methods and Statistics · Xi'an Jiaotong-Liverpool University · 2026–27 Sem1

An empirical HCI evaluation of ADS401 students' awareness, adoption and use of
XJTLU-provided AI agents (including Junmou AI), using an explanatory sequential
mixed-methods design: a cross-sectional survey first, purposive follow-up
interviews second.

**Status:** design stage — data collection pending. Findings will be published
here after collection (November 2026).

## Repository map

| Path | What it is |
|---|---|
| `site/` | Astro project — the graded single-page web report (`src/content/report.md` = content, built & published by GitHub Actions on push to `main`) |
| `slides/` | Slidev project — presentation deck source (`slides/slides.md`); the exported PDF is the LMS submission artifact, not committed |
| `assets/pre2/` | Research materials: `scripts.md` (facts single source of truth), survey instrument v1, reference list |
| `.agents/skills/slides-style/` | Slide visual spec (seven-region layout, palette) — load before touching deck styling |
| [`AGENTS.md`](AGENTS.md) | Operating rules (agents & contributors) |
| [`DECISIONS.md`](DECISIONS.md) | Decision log with rationale (`R-x` entries) |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Setup, branch/PR flow, pre-PR checklist |

## Quick start

```bash
npm install && npm run dev        # web report preview (root)
cd slides && npm install && npm run dev   # deck preview
```

Merging to `main` publishes the site automatically (no manual build step).

## Red line

No raw participant data or identifiable records in this repository or on the
published site — ever, even in history.

## License

[CC BY 4.0](LICENSE). Third-party assets (fonts, libraries, cited figures)
keep their own licenses and are acknowledged in the report.
