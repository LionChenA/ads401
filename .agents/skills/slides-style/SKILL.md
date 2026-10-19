---
name: slides-style
description: >
  ADS401 Group A deck visual spec. Load before creating or restyling slides
  in slides/slides.md — flat layout, palette tokens, and research-integrity
  rules for this coursework deck.
---

# slides-style — deck visual specification

**Scope**: `slides/slides.md` only. This file is the spec; the executable
style tokens live in `slides/styles/index.css`. Change spec and CSS together
in one commit. Facts come from `assets/pre2/scripts.md` — never from memory.

## Provenance

2026-10-18: the team's hand-built master deck (`ADS401_Cover_Updated.pptx`,
flat sans) superseded the earlier Academic-Teal serif deck style (R-14).
R-14 continues to govern the **web report page**; the deck follows the flat
master. Web deployment of the deck is retired (entrance closed; the deck's
distribution channel is the exported LMS PDF).

## Canvas & palette

- 16:9, white background, single sans family (Inter + system fallbacks).
- Tokens (on `.slidev-layout`): `--ink #172327` primary text ·
  `--muted #687780` secondary text · `--line #CED5D7` hairlines ·
  `--accent #1683A5` emphasis labels, links, numerals.
- Decoration is absent by design: no cards, no frames, no takeaway bands.
  Hierarchy comes from weight, size, whitespace and hairline separators.
- Legibility floor: body text ≥ 20px (1.25rem) on the 980×540 canvas.

## Regions (every content slide)

1. **Running head** — top-left, tiny muted (`.run-head`): the study title,
   identical on every slide.
2. **Title** — large extra-bold ink (`.deck-title`), thin divider below
   (`.top-divider`).
3. **Main content** — flat patterns only: two-column with centre hairline
   (`.two-col`), definition rows (`.def-row`), G-rows, stat numerals
   (`.stat`), step grid (`.steps-grid`). Accent headings teal (`.col-h--accent`).
4. **Bottom references** — bottom-left, tiny muted (`.slide-refs`), only
   sources actually used on the slide, one entry = title line + author line
   with DOI link. Omit when the slide cites nothing.
5. **Page number** — bottom-right `NN / 09` (`.page-no`); cover unnumbered.

Cover: centred, module topic as main title, study title as muted subtitle,
members line, project-resource link (`.cover-*`).

Speaker notes: HTML comment block at the **end** of a slide (`<!-- … -->`).
English is the visible language; Chinese glosses and the Q&A crib sheet live
in notes only.

## Research-integrity rules

- Preserve RQ wording, target population, sampling numbers, methodology and
  study status exactly as stated in `scripts.md`. Do not introduce new RQs.
- Distinguish planned vs collected data; distinguish recruitment targets from
  achieved samples; no causal claims from the cross-sectional survey.
- Pending materials are labelled **Pending**, never implied done.
- AI-use disclosure is non-substantive only (layout, formatting,
  proofreading, reference formatting), matching the teacher's criterion:
  graded intellectual work is human; technical/assembly help may be AI.
- If a source file contradicts the deck, **flag it to the author** — never
  silently "fix" facts on a slide.
