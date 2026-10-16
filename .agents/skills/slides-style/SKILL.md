---
name: slides-style
description: >
  ADS401 Group A deck visual spec. Load before creating or restyling slides
  in slides/slides.md — seven-region layout, palette tokens, and
  research-integrity rules for this coursework deck.
---

# slides-style — deck visual specification

**Scope**: `slides/slides.md` only. This file is the spec; the executable
style tokens live in `slides/styles/index.css`. Change spec and CSS together
in one commit. Facts come from `assets/pre2/scripts.md` — never from memory.

## Canvas & palette

- 16:9, white background, widely available sans-serif only (no decorative
  fonts).
- Tokens (defined on `.slidev-layout` in `styles/index.css`):
  `--ink #172327` primary text · `--teal #183F46` labels/takeaway ·
  `--muted #687780` secondary text · `--line #CED5D7` dividers ·
  `--accent #1683A5` highlights/links.

## Seven regions (every content slide)

1. **Section label** — top-left, small bold uppercase teal
   (`.section-label`). Examples: RESEARCH QUESTIONS, RESEARCH METHODOLOGY.
2. **Title** — declarative, ≤ 2 lines, large bold ink (`.deck-title`);
   avoid generic titles like "Introduction". Thin divider below
   (`.top-divider`).
3. **Content heading** — small uppercase muted (`.content-h`), above each
   content block.
4. **Main content** — cards (`.rcard`), two/three columns, or diagrams;
   concise phrases, never paragraph dumps. One idea per slide; explanations
   go to speaker notes.
5. **Key takeaway** — bottom, one bold teal sentence < 18 words
   (`.takeaway`). States the slide's conclusion or question. Do not invent
   findings.
6. **Bottom divider**, then **references** — bottom-left, tiny muted
   (`.slide-refs`). Only sources actually used on the slide, with DOI.
7. **Page number** — bottom-right, `NN / TT` (`.page-no`), consistent
   across the deck.

Speaker notes: HTML comment block at the **end** of a slide (`<!-- … -->`).
English is the visible language; Chinese glosses live in notes only.

## Research-integrity rules

- Preserve RQ wording, target population, sampling numbers, methodology and
  study status exactly as stated in `scripts.md`. Do not introduce new RQs.
- Distinguish planned vs collected data; distinguish recruitment targets from
  achieved samples; no causal claims from the cross-sectional survey.
- Show representative survey/interview items; mention consent; never claim
  materials are finished unless they are.
- If a source file contradicts the deck, **flag it to the author** — never
  silently "fix" facts on a slide.
