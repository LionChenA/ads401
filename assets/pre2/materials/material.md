# Presentation 2 Research Materials

**ADS401 Group A — Evaluating AI Integration at XJTLU**  
**Status:** Consolidated draft for group review, 16 October 2026.  
**Instrument:** Questionnaire version 1, labelled for pilot testing.


## Contents

- [1. Study overview](#1-study-overview)
- [2. Materials inventory](#2-materials-inventory)
- [3. Research questions and measures](#3-research-questions-and-measures)
- [4. Survey routing](#4-survey-routing)
- [5. Complete questionnaire](#5-complete-questionnaire)
- [6. Follow-up interview materials](#6-follow-up-interview-materials)
- [7. Participant information and consent](#7-participant-information-and-consent)
- [8. Pilot testing and revision record](#8-pilot-testing-and-revision-record)
- [9. Analysis and interpretation](#9-analysis-and-interpretation)
- [10. References](#10-references)

## 1. Study overview

Source: [Current presentation script](../scripts.md).

The study explores ADS401 students' use or non-use of XJTLU AI and the reasons behind their choices, to inform potential improvements. XJTLU AI includes student-accessible AI agent services officially provided by XJTLU, including but not limited to Junmou AI. Independently accessed services such as ChatGPT and DeepSeek are external AI.

调查范围是 ADS401 学习中的校内 AI 使用及其与外部 AI 的感知比较，不限于君谋 AI，也不是客观模型性能测试。除明确询问曾经使用外，问卷主要回忆过去四周（28天）的 ADS401 学习经历。

### Research questions

The following wording follows `scripts.md` and supersedes earlier working versions for this consolidation.

- **RQ1 — Awareness & Adoption:** To what extent are students in our ADS401 module aware of and adopting XJTLU AI?
- **RQ2 — Usage Patterns:** How do students in ADS401 use XJTLU AI for their academic tasks?
- **RQ3 — Adoption Factors & Perceived Comparison:** What perceived benefits, barriers, and differences between XJTLU AI and external AI services are associated with students' adoption and intentions to continue, try, or resume using XJTLU AI?

### Design and participants

The planned design is explanatory sequential mixed methods: a cross-sectional online questionnaire, preliminary survey analysis, semi-structured follow-up interviews, and integrated interpretation. Ivankova et al. (2006) supports the design rationale; Fetters et al. (2013) supports integration. Full references appear in Section 10.

The current script specifies **50 enrolled students, excluding 4 researchers, leaving 46 potentially eligible invitees**. These are planning figures from the script, not achieved response counts. Participation is voluntary; the achieved sample and response denominator must be reported after collection. The four usage groups are observed categories based on Q5, not randomly assigned experimental groups.

## 2. Materials inventory

| Material | Existing source | Current status |
| --- | --- | --- |
| Study scope, RQs, sampling and analysis plan | [scripts.md](../scripts.md) | Written plan available |
| Full questionnaire | [questionnaire_v1.md](survey/questionnaire_v1.md) | Version 1; explicitly labelled for pilot testing |
| Survey routing source | [questionnaire_v1_flow.md](survey/questionnaire_v1_flow.md) | Available; platform implementation still needs checking |
| Survey routing image | [SVG flowchart](survey/questionnaire_v1_flow_fig.svg) | Available |
| Reference list and source roles | [reference.md](reference.md) | Six references available |
| Participant information and survey consent | Questionnaire introduction and Q2 | Embedded text available; operational details remain to be confirmed |
| Optional interview recruitment | Q20–Q21 | Invitation and contact fields available |
| Complete interview guide and interview consent | No separate file found in current materials directory | To be supplied or confirmed |
| Internal-check/pilot findings and revision log | No record found in current materials directory | Completion not evidenced by current files |

"Available" means a document exists, not that it has been approved, implemented or tested. The current source files remain the editing references. If the questionnaire or references change, refresh the corresponding consolidated sections to avoid version drift.

## 3. Research questions and measures

This mapping is an integration aid, not a change to the source questionnaire. Some measures support more than one RQ.

| Research question | Relevant items | Evidence and interpretation |
| --- | --- | --- |
| RQ1: Awareness and adoption | Q3, Q4, Q5 | Awareness, ever-use and past-four-week usage groups; keep lifetime use separate from recent ADS401 use |
| RQ2: Usage patterns | Q6, Q7, Q8, Q14, Q14a, Q15 | Frequency, academic activity categories, checking behaviour, external AI use and relative reliance |
| RQ3: Adoption factors and perceived comparison | Q7a, Q9–Q13, Q14b, Q16–Q19 | Activity-specific usefulness, usefulness/ease/trust ratings, experienced problems, non-use reasons, intentions, comparisons and improvement priorities |
| Eligibility and consent | Q1–Q2 | Determines whether participation proceeds |
| Optional follow-up recruitment | Q20–Q21 | Contact permission and details; not a primary RQ outcome |

The activity categories are consistent across Q7/Q7a and Q14/Q14b: learning and understanding course materials; research planning and idea development; research design and data analysis; academic writing and content production; coursework planning and collaboration.

Davis (1989) provides a conceptual basis for usefulness and ease of use. The current items are exploratory, context-specific measures, not a complete validated TAM scale. Chung et al. (2024) is listed as a questionnaire-design resource, while Farinosi and Melchior (2025) supports the student-use and perception context. The supplied files do not establish a question-by-question adaptation history; this document does not claim one.

## 4. Survey routing

The table below summarises the existing flow file. Eligibility and consent are required before proceeding. Q5 determines the recent-use route; Q4 records ever-use and does not replace Q5 for grouping.

| Group from Q5 | Common opening | Group-specific questions | Common ending |
| --- | --- | --- | --- |
| G1: Both AI | Q1–Q5 | Q6–Q11, including Q7a; Q14, Q14a, Q14b; Q15–Q16 | Q17–Q20; Q21 only if Q20 = Yes |
| G2: Other AI Only | Q1–Q5 | Q12–Q13; Q14, Q14a, Q14b | Q17–Q20; Q21 only if Q20 = Yes |
| G3: No AI | Q1–Q5 | Q12–Q13 | Q17–Q20; Q21 only if Q20 = Yes |
| G4: XJTLU AI Only | Q1–Q5 | Q6–Q11, including Q7a | Q17–Q20; Q21 only if Q20 = Yes |

If Q1 = No or Q2 = No, end the survey. If Q20 = No, skip Q21 and submit. The existing flow diagram groups Q20–Q21 together; the conditional display of Q21 follows the explicit wording of Q20 and must be implemented in the survey platform.

![Existing questionnaire version 1 flowchart](survey/questionnaire_v1_flow_fig.svg)

[Open the flowchart image](survey/questionnaire_v1_flow_fig.svg) · [Open the Mermaid source](survey/questionnaire_v1_flow.md)

No routing changes have been written back to the source files. Before launch, test all four paths and confirm handling of missing or inconsistent screening answers. Do not silently classify unanswered Q5 responses as non-use.

## 5. Complete questionnaire

Source: [questionnaire_v1.md](survey/questionnaire_v1.md). The following reproduces the full source text, including the participant introduction, question numbering, options and rating tables. Only heading depth is changed to nest it within this document. These are blank research materials, not participant responses.

<!-- BEGIN questionnaire_v1.md: source wording preserved; heading depth +2 -->

### Questionnaire for ADS401 Students' Perspective on AI Agents at XJTLU

#### version: 1

> This version is used for pilot testing.

This voluntary ADS401 HCI coursework survey explores awareness, adoption, and use of university-provided AI agents. "XJTLU AI" refers to any student-accessible AI agent service officially provided by XJTLU, including but not limited to Junmou AI. Independently accessed ChatGPT, DeepSeek, and similar services count as external AI. Unless otherwise specified, answer about ADS401 learning in the past four weeks (28 days). Participation is voluntary. This survey does not ask for identity or contact details unless you choose Yes to the optional follow-up interview invitation (Q20). If you choose Yes, Q21 asks for an ID and an email address or telephone number so the research team can match your answers to a potential interview invitation; your responses will therefore not be anonymous to the research team. Such information will be used only for interview recruitment and scheduling, accessed only by authorised study-team members, and excluded from reports. You may decline an interview invitation later. Do not provide other sensitive information. Estimated completion time: 5–7 minutes.

#### Eligibility & consent

##### Q1. Are you currently enrolled in ADS401 at XJTLU?

- Yes

- No

##### Q2. Have you read the information above and do you voluntarily agree to participate?

- Yes, I agree

- No, I do not agree

#### Awareness & adoption

##### Q3. Before seeing this survey, how familiar were you with XJTLU-provided AI agent services?

- Heard of them and knew some functions

- Heard of them but knew little

- Had not heard of them

- Unsure whether known services were XJTLU-provided

##### Q4. Have you ever used any XJTLU-provided AI agent service?

- Yes

- No

- Not sure

#### Recent use

##### Q5. During the past four weeks, which types of AI did you actually use for ADS401 learning activities? (Select one.)

- Both XJTLU AI and Other AI

- Other AI only (no XJTLU AI)

- Neither XJTLU AI nor Other AI

- XJTLU AI only (no Other AI)

#### Recent user experience

##### Q6. How frequently did you use XJTLU AI for ADS401 learning during the past four weeks?

- 1–3 times in total

- 4–7 times in total

- 8 or more times

##### Q7. For which broad categories of ADS401 learning activities did you use XJTLU AI in the past four weeks? (Select all that apply.)

- A. Learning and understanding course materials

- B. Research planning and idea development

- C. Research design and data analysis

- D. Academic writing and content production

- E. Coursework planning and collaboration

- Other

##### Q7a. For each ADS401 activity category, rate how useful XJTLU AI was in your actual experience. Select N/A for categories you did not use it for.

| | 1 Not useful | 2 Slightly useful | 3 Moderately useful | 4 Useful | 5 Very useful | N/A Did not use this category |
| --- | --- | --- | --- | --- | --- | --- |
| A. Learning and understanding course materials |  |  |  |  |  |  |
| B. Research planning and idea development |  |  |  |  |  |  |
| C. Research design and data analysis |  |  |  |  |  |  |
| D. Academic writing and content production |  |  |  |  |  |  |
| E. Coursework planning and collaboration |  |  |  |  |  |  |

##### Q8. How often did you check XJTLU AI information against course materials or reliable sources before using it?

- Never

- Rarely

- Sometimes

- Often

- Every time

- I did not use its information in ADS401 work

- Unable to judge

##### Q9. Based on your overall experience using XJTLU AI in ADS401, how much do you agree with these statements? (Select N/A if you cannot judge.)

| | 1 Strongly disagree | 2 Disagree | 3 Neutral | 4 Agree | 5 Strongly agree | N/A |
| --- | --- | --- | --- | --- | --- | --- |
| PU1. Helps complete ADS401 tasks more effectively |  |  |  |  |  |  |
| PU2. Helps complete ADS401 tasks more efficiently |  |  |  |  |  |  |
| PEOU1. Easy to learn how to use |  |  |  |  |  |  |
| PEOU2. Easy to use for my ADS401 tasks |  |  |  |  |  |  |
| T1. Usually provides information I consider reliable |  |  |  |  |  |  |
| T2. I generally trust its explanations |  |  |  |  |  |  |

##### Q10. Which problems did you actually experience? (Select up to 3)

- Unclear which XJTLU AI to use

- Hard to formulate prompts

- Inaccurate, unclear or vague answers

- Answers not relevant to ADS401

- Time-consuming to verify or revise

- Inconvenient access/login/workflow

- Functions insufficient

- Uncertain about course permission

- Privacy or data concerns

- No notable problem

- Other

##### Q11. If you have a suitable ADS401 task in the next four weeks, how likely are you to continue using XJTLU AI?

- Very unlikely

- Unlikely

- Neither

- Likely

- Very likely

#### Non-use

##### Q12. What are your main reasons for NOT using XJTLU AI for ADS401 during the past four weeks? (Select up to 3.)

- Previously unaware

- Unclear what it can do

- Unsure how to access

- No suitable ADS401 task

- Prefer other AI tools

- Prefer non-AI methods

- Concerned about inaccurate answers

- Unsure if AI use permitted

- Privacy/data concerns

- Past experience unsatisfactory

- Access or operation seemed inconvenient

- Other

##### Q13. If you have a suitable ADS401 task in the next four weeks, how willing are you to try or resume XJTLU AI?

- Very unwilling

- Unwilling

- Unsure

- Willing

- Very willing

#### External AI

##### Q14. For which broad categories of ADS401 learning activities did you use Other AI (not officially provided by XJTLU) in the past four weeks? (Select all that apply.)

- A. Learning and understanding course materials

- B. Research planning and idea development

- C. Research design and data analysis

- D. Academic writing and content production

- E. Coursework planning and collaboration

- Other ADS401 learning activity

##### Q14a. How frequently did you use Other AI for ADS401 learning during the past four weeks?

- 1–3 times in total

- 4–7 times in total

- 8 or more times

##### Q14b. For each ADS401 activity category, rate how useful Other AI was in your actual experience. Select N/A for categories you did not use it for.

| | 1 Not useful | 2 Slightly useful | 3 Moderately useful | 4 Useful | 5 Very useful | N/A Did not use this category |
| --- | --- | --- | --- | --- | --- | --- |
| A. Learning and understanding course materials |  |  |  |  |  |  |
| B. Research planning and idea development |  |  |  |  |  |  |
| C. Research design and data analysis |  |  |  |  |  |  |
| D. Academic writing and content production |  |  |  |  |  |  |
| E. Coursework planning and collaboration |  |  |  |  |  |  |

#### Tool choice & comparison

##### Q15. When using both XJTLU AI and Other AI for ADS401 in the past four weeks, which category did you rely on more overall?

- XJTLU AI

- Other AI

- Both about equally

##### Q16. Based on ADS401 tasks where you used both types, how did XJTLU AI compare with Other AI in each respect? (Choose 'Unable to compare' when needed.)

| | XJTLU AI better | About the same | External AI better | Unable to compare |
| --- | --- | --- | --- | --- |
| Finding and starting the tool |  |  |  |  |
| Understanding my task |  |  |  |  |
| Relevance to ADS401 tasks |  |  |  |  |
| Perceived clarity and reliability of responses |  |  |  |  |
| Helping me progress |  |  |  |  |
| Overall preference |  |  |  |  |

##### Q17. Which factors matter most when choosing an AI tool for ADS401, or if you were to choose one? (Select up to 3.)

- Task relevance

- Accuracy or reliability

- Ease of use

- Speed

- Familiarity

- Course-material support

- Suitable features

- Accessibility

- Chinese support

- Quota or cost

- University recommendation

- Other

#### Improvement & follow-up

##### Q18. Which improvements should XJTLU AI prioritise for ADS401? (Select up to 3)

- More accurate course answers

- Research-method support

- Survey/interview design support

- Document/knowledge-base support

- Writing/summaries/planning

- Clearer navigation

- ADS401-specific examples

- Privacy/data transparency

- Clear course-use guidance

- Other

##### Q19. Anything else about XJTLU AI or other AI tools for ADS401? (Optional; no identifying information)

Optional response

##### Q20. Would you be willing to be contacted for an optional follow-up interview? If Yes, Q21 will ask for your ID and email address or telephone number.

- Yes

- No

##### Q21. Please leave your contact information (ID + email address or telephone number).

ID: ______  
Email or telephone: ______


<!-- END questionnaire_v1.md -->

## 6. Follow-up interview materials

### Existing plan

According to [scripts.md](../scripts.md), initial survey analysis will inform purposive selection among respondents who opt into follow-up contact. The plan is approximately **4–6 students**, prioritising **Both AI** and **Other AI Only**, with interviews lasting **15–20 minutes**. The stated focus is tool-choice motivations, adoption barriers and learning experiences.

访谈将在问卷初步分析之后开展，用于解释使用模式与选择原因。上述人数和时长是计划，不代表已经完成访谈；重点覆盖两组也意味着另外两组的观点可能覆盖不足。

The planned analysis codes interview material, develops themes and connects these themes with survey patterns. Braun and Clarke (2006) is the supplied reference for thematic analysis; Fetters et al. (2013) supports connecting the two phases.

### Materials still needed

No full interview-question file is included in the current directory. A final interview guide, participant information, consent procedure and any recording-consent wording must be supplied or confirmed before interviewing. Earlier chat drafts are not silently substituted for the current repository's study design.

The guide should be linked here once approved: **[Pending: interview guide path]**. Recruitment and scheduling records must remain outside this public repository.

## 7. Participant information and consent

### What the current questionnaire includes

The introduction states the study context, voluntary participation, the 28-day ADS401 recall period, an estimated 5–7-minute duration, and the use of contact details for follow-up recruitment. Q2 asks for consent. Q20 asks whether the respondent agrees to follow-up contact; Q21 requests an ID and an email address or telephone number only for those opting in.

The source explicitly states that responses linked to those details are **not anonymous to the research team**. Contact information is described as accessible only to authorised study-team members, excluded from reports, and used for recruitment and scheduling. Permission to be contacted is not consent to the interview itself or to recording it.

### Details requiring confirmation

- Research contact and a participant enquiry route.
- Storage location, authorised access, retention period and deletion arrangements.
- Withdrawal arrangements before and after submission, including limits on locating anonymous records.
- What "ID" in Q21 means and the minimum identifying information needed.
- Whether the survey platform collects account identifiers or other metadata, and whether anonymity claims match its actual settings.
- Interview information, consent and optional recording arrangements.

The README states that raw participant data and identifiable records must never be stored in this repository. This consolidated document contains only blank instruments and design information. No interview sign-up details, completed questionnaires, recordings or transcripts should be inserted here.

## 8. Pilot testing and revision record

The questionnaire is labelled as a pilot version. The script lists an internal questionnaire check by the four researchers before survey collection. The current files do not provide completed check records, participant pilot results or measured completion times. Therefore, the 5–7-minute estimate remains an estimate.

以下是待填写的记录模板，不是已发生的结果。只有实际检查完成后才能补入真实记录；内部检查与正式参与者数据应区分。

| Date | Version / route checked | Actual issue observed | Change made | Retest outcome |
| --- | --- | --- | --- | --- |
| Pending | Pending | Not yet documented | Pending | Pending |

Suggested implementation checks for the team, not claims of completed testing:

- Walk through all four Q5 routes and both eligibility/consent exit paths.
- Confirm Q21 appears only after opting into contact in Q20.
- Check Q7/Q7a and Q14/Q14b consistency, including N/A for unused activity categories.
- Check the three-selection limits in Q10, Q12, Q17 and Q18.
- Confirm how "No notable problem" in Q10 is kept exclusive of actual problem selections.
- Check item understanding, matrix readability and actual completion time.
- Record how Q4 ever-use inconsistencies with Q5 recent use are handled, without inventing a participant's answer.

## 9. Analysis and interpretation

The following summarises the current analysis plan and its implications for the materials:

- Report counts and percentages for awareness, ever-use and Q5 groups, with the valid-response denominator for each item.
- Describe usage frequency as ordered categories; category codes are not exact use counts.
- Summarise activity usefulness and Q9 items descriptively. Exclude N/A from numeric rating summaries and report its frequency where useful. Keep structural skips separate from unanswered displayed questions.
- Compare activity ratings within dual users only when both Q7a and Q14b contain valid ratings for the same activity. Report the number of valid pairs for each activity.
- Summarise Q16 direct comparisons separately, retaining "Unable to compare". External AI is a broad category in this instrument; the data cannot support rankings of individual external brands.
- Q11 measures continuation likelihood among recent users; Q13 measures willingness to try or resume among non-users. Their wording and response labels differ, so keep them distinguishable in reporting.
- Treat problems reported in Q10 separately from reasons or concerns in Q12. Do not classify every non-use reason as an experienced system failure.
- Connect interview themes to survey patterns after actual data collection; document both supporting and contrasting accounts.

The single-module voluntary sample may be self-selected. Findings describe participating ADS401 students, not all XJTLU students. The study is cross-sectional and self-reported; it cannot establish causation, objective system performance, learning gains or actual future continued use. The planned interview emphasis may underrepresent No AI and XJTLU AI Only perspectives.

## 10. References

Source: [reference.md](reference.md). The six entries and their supplied bilingual descriptions are reproduced below. Descriptions identify the roles assigned by the group; this compilation does not constitute an independent verification of all cited publications. Slide-number references are retained from the source list and should be checked against the final deck.

<!-- BEGIN reference.md: source text preserved -->

1. Braun, V., & Clarke, V. (2006). Using thematic analysis in psychology. *Qualitative Research in Psychology, 3*(2), 77–101. [https://doi.org/10.1191/1478088706qp063oa](https://doi.org/10.1191/1478088706qp063oa)

   **大致内容：**介绍如何对访谈等定性材料进行编码、识别和发展主题。对应第 4 页 **Follow-up Interviews & Integrated Analysis**，支持主题分析方法。

   **Overview:** Explains how to code qualitative materials, such as interview transcripts, and identify and develop themes. Supports the thematic analysis approach on Slide 4, **Follow-up Interviews & Integrated Analysis**.

2. Chung, J., Henderson, M., Pepperell, N., Slade, C., & Liang, Y. (2024). *Student perspectives on AI in Higher Education: Student Survey* [Survey instrument]. Student Perspectives on AI in Higher Education Project. [https://doi.org/10.26180/27915930](https://doi.org/10.26180/27915930)

   **大致内容：**提供高校学生生成式 AI 调查题目、问卷构建过程和项目背景，可参考其使用体验、有用性及信任等测量维度。对应第 3 页 **Research Methodology** 和第 5 页 **Materials**。这是问卷工具，不是期刊论文。

   **Overview:** Provides survey questions about university students' experiences with generative AI, alongside details of survey development and the project background. Offers a reference for measuring experiences, perceived usefulness, and trust. Supports Slide 3, **Research Methodology**, and Slide 5, **Materials**. This is a survey instrument, not a journal article.

3. Davis, F. D. (1989). Perceived usefulness, perceived ease of use, and user acceptance of information technology. *MIS Quarterly, 13*(3), 319–340. [https://doi.org/10.2307/249008](https://doi.org/10.2307/249008)

   **大致内容：**研究感知有用性、感知易用性与技术接受之间的关系，并开发和验证相关量表。对应第 2 页 **Research Questions** 和第 3 页 **Research Methodology**，为采纳因素及感知有用性与易用性的测量提供理论依据。

   **Overview:** Examines the relationships between perceived usefulness, perceived ease of use, and technology acceptance, and develops and validates measurement scales. Provides a theoretical basis for adoption factors and measures of usefulness and ease of use on Slide 2, **Research Questions**, and Slide 3, **Research Methodology**.

4. Farinosi, M., & Melchior, C. (2025). To adopt or to ban? Student perceptions and use of generative AI in higher education. *Humanities and Social Sciences Communications, 12*, Article 1684. [https://doi.org/10.1057/s41599-025-05982-7](https://doi.org/10.1057/s41599-025-05982-7)

   **大致内容：**调查 1,366 名意大利大学生的生成式 AI 使用、态度及伦理和政策看法，也讨论自我报告与抽样的局限。对应第 1 页 **Background**、第 2 页 **Research Questions** 和第 5 页 **Materials**。

   **Overview:** Surveys 1,366 Italian university students about their use of generative AI, attitudes, and views on ethics and institutional policies. Also discusses limitations related to self-reported data and sampling. Supports Slide 1, **Background**, Slide 2, **Research Questions**, and Slide 5, **Materials**.

5. Fetters, M. D., Curry, L. A., & Creswell, J. W. (2013). Achieving integration in mixed methods designs—Principles and practices. *Health Services Research, 48*(6 Pt 2), 2134–2156. [https://doi.org/10.1111/1475-6773.12117](https://doi.org/10.1111/1475-6773.12117)

   **大致内容：**解释如何在研究设计、数据收集及结果解释中整合定量和定性资料。对应第 4 页 **Follow-up Interviews & Integrated Analysis**，支持"根据问卷选择访谈对象，并用访谈解释问卷结果"的安排。

   **Overview:** Explains how to integrate quantitative and qualitative evidence across research design, data collection, and interpretation. Supports selecting interview participants based on survey findings and using interviews to explain survey results on Slide 4, **Follow-up Interviews & Integrated Analysis**.

6. Ivankova, N. V., Creswell, J. W., & Stick, S. L. (2006). Using mixed-methods sequential explanatory design: From theory to practice. *Field Methods, 18*(1), 3–20. [https://doi.org/10.1177/1525822X05282260](https://doi.org/10.1177/1525822X05282260)

   **大致内容：**介绍解释性顺序混合方法：先收集和分析定量数据，再用定性研究解释结果，并说明两阶段如何衔接。对应第 3 页 **Research Methodology**，支持"先问卷、后访谈"的整体设计。

   **Overview:** Introduces the sequential explanatory mixed-methods design: quantitative data are collected and analysed first, followed by qualitative research to explain the findings. Explains how to connect the two phases and supports the survey-first, interview-second design on Slide 3, **Research Methodology**.

<!-- END reference.md -->


