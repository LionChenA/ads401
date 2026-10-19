---
title: "ADS401 Students' Perspective on AI Agents at XJTLU"
---


*This page reports the evaluation design; findings will be added after
collection (November 2026).*

## 1. Project at a glance

We are evaluating how students in ADS401 (Evaluation Methods and Statistics,
2026–27) become aware of, adopt, and use **XJTLU AI** — any AI agent service
officially provided by XJTLU, including but not limited to the **Junmou AI**
agent platform — in their ADS401 learning, and why some students instead rely
on external commercial AI (ChatGPT, DeepSeek, Kimi and similar independently
accessed services).

The study is an **explanatory sequential mixed-methods design**: a
cross-sectional online questionnaire first maps awareness, usage patterns and
perceptions; semi-structured follow-up interviews then explain the choices
behind those patterns.

- **Evaluated system:** XJTLU AI Agent Platform (Junmou AI)
- **Target users:** ADS401 2026-cohort students (N = 50 enrolled)
- **Methods:** online survey (census-adjacent invitation) → purposive
  follow-up interviews
- **Presentation deck:** PDF (LMS submission) — source:
  [slides/slides.md](https://github.com/LionChenA/ads401/blob/main/slides/slides.md)

## 2. Problem, motivation and research questions

### Intended users and context

XJTLU provides AI services such as Junmou AI to support learning. ADS401
students are simultaneously heavy users of external AI for coursework — yet
the module team has no systematic evidence of whether the institutional
services are known, tried, adopted, or why students choose one over the other.
This matters now: the same cohort is both the subject of AI-supported learning
and the population future iterations of these services must serve.

### Research questions

1. **RQ1 — Awareness & Adoption.** To what extent are students in our ADS401
   module aware of and adopting XJTLU AI?
2. **RQ2 — Usage Patterns.** How do students in ADS401 use XJTLU AI for their
   academic tasks?
3. **RQ3 — Adoption Factors & Perceived Comparison.** What perceived benefits,
   barriers, and differences between XJTLU AI and external AI services are
   associated with students' adoption and intentions to continue, try, or
   resume using XJTLU AI?

### Scope of claims

Findings will describe participating ADS401 students only. Voluntary
participation limits representativeness even within the module; results do not
generalise to all XJTLU students, and the cross-sectional design supports
association claims, not causal effects.

## 3. Background and related work

Technology-acceptance research establishes perceived usefulness and perceived
ease of use as central antecedents of adoption<sup><a href="#ref-1">1</a></sup>. Recent work on generative
AI in higher education documents widespread student use alongside sharp
institutional policy divergence — adopt or ban — and warns that self-reported
use is shaped by self-selection<sup><a href="#ref-2">2</a></sup>. Surveys of student AI use in higher
education provide validated question stems for experience, usefulness and
trust items<sup><a href="#ref-3">3</a></sup>.

**Gap.** These strands have not been brought together for XJTLU's own
institutional agent platform: we lack evidence on whether official services
are even known to the students they target, and how perceived differences
against commercial tools shape adoption intentions. **Evaluation rationale.**
A census-adjacent survey quantifies the adoption landscape (RQ1–RQ2);
interviews then explain the perception drivers (RQ3), following the sequential
explanatory logic of Ivankova et al.<sup><a href="#ref-4">4</a></sup> and the integration principles of
Fetters et al.<sup><a href="#ref-5">5</a></sup>.

## 4. System and evaluation design

*Instrument v1 in pilot.*

### Evaluated interaction

XJTLU AI agents support question answering, document/knowledge-base
interaction, writing and study-planning tasks inside coursework. We evaluate
students' self-reported encounters: awareness, first use, recent academic use,
verification behaviour before relying on outputs, and intentions — not system
internals or logs.

### Participants, recruitment and sampling

All 50 ADS401 2026-cohort students form the sampling frame; the 4 group
researchers are excluded, leaving **46 potentially eligible invitees**. We
invite the full frame (census-adjacent, voluntary participation); the achieved
sample will be reported after collection. No usability-task sample is
involved, so the 12-participant usability floor is not triggered; our
sample-size rationale is full-frame coverage rather than inferential power.

### Study design and grouping

The questionnaire (v1, in pilot) first screens eligibility and consent, then
awareness (Q3) and ever-use (Q4). Respondents are grouped by reported ADS401
AI use in the past four weeks, with skip logic so each group answers only
relevant modules:

| Group | Definition | Modules answered |
|---|---|---|
| G1 · Both AI | XJTLU AI + external AI | use experience (Q6–Q11, incl. Q7a), other-AI use (Q14, Q14a, Q14b), comparison (Q15–Q16) |
| G2 · Other AI only | external AI only | non-adoption barriers & intention (Q12–Q13), other-AI use (Q14, Q14a, Q14b) |
| G3 · No AI | neither | non-adoption barriers & intention (Q12–Q13) |
| G4 · XJTLU AI only | XJTLU AI only | use experience (Q6–Q11, incl. Q7a) |

All paths converge on tool-choice factors and improvement priorities
(Q17–Q19) and an optional interview opt-in (Q20–Q21; Q21 only if Q20 =
Yes). Interview contact details are collected in-questionnaire (Q21) only from
respondents opting in; responses contain no identity fields otherwise.

### Research materials and status

The full instrument and supporting documents are consolidated in the
repository (`assets/pre2/materials/`); the slide-deck inventory matches it:

| Material | Status |
|---|---|
| Questionnaire v1 (pilot version) | Available — labelled for pilot testing |
| [Survey routing (flow source + diagram)](https://github.com/LionChenA/ads401/blob/main/assets/pre2/materials/survey/questionnaire_v1_flow.md) | Available |
| Participant information & consent (survey intro + Q1–Q2) | Available — operational details to confirm |
| Optional interview recruitment (Q20–Q21) | Available |
| References (six entries) | Available |
| Interview guide & interview consent | **Pending** — to be supplied and confirmed before interviewing |
| Internal-check & pilot record | **Pending** — logged after the four-researcher questionnaire check |

### Variables and measures

| Construct | Operationalisation (survey) |
|---|---|
| Awareness | Self-rated familiarity with XJTLU-provided AI services (Q3) |
| Ever-use / recent use | Any use ever (Q4); past-four-week usage type (Q5, single-select) → group assignment (G1–G4); usage frequency asked only within groups (Q6, Q14a) |
| Recent academic usage | Five broad activity categories (Q7 / Q14): learning & understanding course materials · research planning & idea development · research design & data analysis · academic writing & content production · coursework planning & collaboration |
| Verification behaviour | Frequency of checking outputs against course materials or reliable sources (Q8) |
| Perceived usefulness / ease of use / trust | Activity-specific usefulness ratings (Q7a, Q14b) and 5-point Likert items (Q9), treated as *exploratory, context-specific* measures — not the full validated TAM scales<sup><a href="#ref-1">1</a></sup> |
| Barriers | Experienced problems (Q10, ≤3) and non-adoption reasons (Q12, ≤3) |
| Future-use intention | Continue (Q11) / try-or-resume (Q13) likelihood |
| Perceived comparison | Dual users compare XJTLU AI vs external AI per activity category (Q15–Q16) |

The Technology Acceptance Model (TAM) includes validated scales for perceived
usefulness and perceived ease of use (Davis, 1989)<sup><a href="#ref-1">1</a></sup>; these constructs inform
the questionnaire items adapted to the XJTLU AI context. The adapted items
remain exploratory, context-specific measures — not the complete validated
scales.

### Ethics, consent, privacy and bias mitigation

- Participation is voluntary with an explicit informed-consent gate (Q1–Q2);
  respondents may end the survey at any branching exit.
- No names are collected; the optional Q21 asks only for an ID + email/telephone, used solely for interview recruitment and scheduling.
- Skip logic prevents non-users from rating experiences they never had.
- Usefulness/ease-of-use items are labelled exploratory to avoid over-claiming
  construct validity.
- Self-reported use will be described as self-report, never as system-log
  evidence.
- Pilot: internal questionnaire check with the 4 researchers precedes
  fielding; pilot-driven changes will be logged on this page.

## 5. Data preparation and analysis plan

### Quantitative (survey)

- **Descriptive statistics:** counts and percentages for awareness, ever-use
  and past-four-week usage, each with its valid-response denominator.
- **Cross-tabulation:** usage patterns compared across the four groups.
- **Rating analysis:** activity-specific ratings and intentions summarised
  descriptively; N/A excluded from rating summaries.
- **Perceived comparison:** paired activity ratings only where dual users
  rated both tools for the same category; direct comparison responses
  reported separately, including "unable to compare".

### Qualitative (interviews) and integration

- **Sampling:** purposive, among survey respondents who opt into follow-up
  contact (Q20–Q21), informed by initial survey analysis; about 4–6 students,
  prioritising G1 (Both AI) and G2 (Other AI Only).
- **Format:** semi-structured, 15–20 minutes; focus on tool-choice
  motivations, adoption barriers and learning experiences.
- **Thematic analysis:** coding and theme development following Braun &
  Clarke<sup><a href="#ref-6">6</a></sup>.
- **Integration:** interview themes are mapped onto survey patterns to explain
  adoption decisions and identify improvement directions — the survey says
  *what*, the interviews explain *why*<sup><a href="#ref-5">5</a></sup>.

> Analysis is deliberately descriptive and exploratory: with a single-module
> voluntary sample we report distributions and patterns, and we do not run
> group-inferential tests or claim causal effects.

### Next steps

Research materials → internal questionnaire check (4 researchers) → survey
data collection → preliminary survey analysis → follow-up interviews →
thematic analysis & integration. The achieved sample is reported after
collection; findings on this page remain pending until then.

## 6. Findings

*Pending — survey not yet fielded.* Data collection starts after Presentation
2 feedback and the instrument pilot. This section will present, per research
question: awareness and adoption rates (RQ1), usage-pattern cross-tabulations
by group (RQ2), and barrier/intention/comparison summaries with interview
themes (RQ3) — with figures, exact denominators and anonymised quotes.

## 7. Discussion, limitations and recommendations (planned)

Discussion will interpret findings for the ADS401 context and propose
evidence-based improvements to XJTLU AI services. We pre-register the
following limitations to bound claims:

- **Single-module sample** — results describe participating ADS401 students;
  voluntary participation may limit representativeness even within ADS401; no
  generalisation to all XJTLU students.
- **Self-reported data** — the study relies on students' reported behaviours
  and perceptions.
- **Interview coverage** — prioritising G1/G2 may under-represent G3 (No AI)
  and G4 (XJTLU AI only) perspectives.
- **Cross-sectional design** — captures recent use and intentions, not causal
  effects or observed long-term continued use.
- **Perception-based comparison** — comparisons with external tools do not
  establish objective system-capability differences.

## 8. Transparency and references

### Contribution statement

Study design, instrument and interview protocol: all four members (work split
recorded in the group agreement). Repository/site assembly: Liyuan CHEN.
Survey scripts and materials integration: Mingjian TAO. Slide narrative:
Hongcheng TANG. (Final wording to be confirmed at submission.)

### AI-use statement

Permitted non-substantive AI use only. GLM-5.3 Flash (Zhipu AI) and Gemini
3.8 Flash (Google), operated through the omp open-source coding harness, were
used for slide layout and formatting, language proofreading, reference
formatting, and build/assembly automation for the presentation slides, web
report, and supplementary materials. All research questions, methodological
decisions, sampling frames, variable operationalisations, questionnaire items,
interview protocols, and critical evaluations were conceived, drafted, and
verified entirely by the student authors.

### Data and materials availability

No raw participant data is stored in this repository or on this site
(coursework red line). Anonymised, aggregated results and the analysis syntax
will be linked here after collection. The survey instrument (pilot v1) is archived in the group's working
repository; the interview guide will be added once finalised.

### References (IEEE, order of first citation)

1. <a id="ref-1"></a>F. D. Davis, "Perceived usefulness, perceived ease of use, and user
   acceptance of information technology," *MIS Quarterly*, 13(3), pp. 319–340,
   1989. [doi:10.2307/249008](https://doi.org/10.2307/249008)
2. <a id="ref-2"></a>M. Farinosi and C. Melchior, "To adopt or to ban? Student perceptions and
   use of generative AI in higher education," *Humanities and Social Sciences
   Communications*, 12, Art. 1684, 2025.
   [doi:10.1057/s41599-025-05982-7](https://doi.org/10.1057/s41599-025-05982-7)
3. <a id="ref-3"></a>J. Chung, M. Henderson, N. Pepperell, C. Slade, and Y. Liang, "Student
   perspectives on AI in Higher Education: Student Survey," Student
   Perspectives on AI in Higher Education Project, 2024.
   [doi:10.26180/27915930](https://doi.org/10.26180/27915930)
4. <a id="ref-4"></a>N. V. Ivankova, J. W. Creswell, and S. L. Stick, "Using mixed-methods
   sequential explanatory design: From theory to practice," *Field Methods*,
   18(1), pp. 3–20, 2006.
   [doi:10.1177/1525822X05282260](https://doi.org/10.1177/1525822X05282260)
5. <a id="ref-5"></a>M. D. Fetters, L. A. Curry, and J. W. Creswell, "Achieving integration in
   mixed methods designs—Principles and practices," *Health Services
   Research*, 48(6 Pt 2), pp. 2134–2156, 2013.
   [doi:10.1111/1475-6773.12117](https://doi.org/10.1111/1475-6773.12117)
6. <a id="ref-6"></a>V. Braun and V. Clarke, "Using thematic analysis in psychology,"
   *Qualitative Research in Psychology*, 3(2), pp. 77–101, 2006.
   [doi:10.1191/1478088706qp063oa](https://doi.org/10.1191/1478088706qp063oa)
