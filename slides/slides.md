---
theme: default
title: ADS401 Students' Perspective on AI Agents at XJTLU
info: |
  ADS401 Presentation 2: Show Your Evaluation Design
  Group A · XJTLU · 2026-27 Sem1
class: text-center
drawings:
  persist: false
transition: slide-left
mdc: true
---

<!-- Slide 1: Cover -->
<div class="section-label">RESEARCH BACKGROUND</div>

<div class="cover-frame">
  <div class="cover-kicker">ADS401 · PRESENTATION 2 · EVALUATION DESIGN</div>
  <div class="deck-title" style="font-size: 2.3rem; margin-top: 0.8rem; line-height: 1.25;">
    ADS401 Students' Perspective<br>on AI Agents at XJTLU
  </div>
  <div style="color: var(--teal); font-family: Newsreader, Georgia, serif; font-style: italic; font-size: 1.05rem; margin-top: 0.6rem;">
    An empirical HCI evaluation of awareness, adoption, and use of campus AI services
  </div>
</div>

<div style="margin-top: 2rem; font-size: 0.92rem; color: var(--ink);">
  Group A · Hongcheng TANG · Mingjian TAO · Liyuan CHEN · Haode SHEN<br>
  <span style="color: var(--muted); font-size: 0.82rem;">Department of Computing · Xi'an Jiaotong-Liverpool University · 19 October 2026</span>
</div>

<div class="slide-footer">
  <span>Live report: lionchena.github.io/ads401</span>
  <span class="page-no">01 / 09</span>
</div>

<!--
Notes [15s] · 开场问候与课题破题
【英文演讲词】:
"Hello everyone. // We are the first group to present in ADS401. // Our study explores ADS401 students' awareness and use of AI services provided by XJTLU."

【中文要义提示】:
大家好，我们是第一组。今天我们汇报的研究关注 ADS401 同学对西浦校内 AI 服务的认知和使用情况。

【发音指南】:
- awareness [ə-ˈwɛər-nəs]
- provided by XJTLU [prə-ˈvaɪ-dɪd baɪ ...]
-->

---
layout: default
---

<!-- Slide 2: Outline -->
<div class="section-label">PRESENTATION OUTLINE</div>

<div class="deck-title" style="font-size: 1.55rem; margin-top: 1rem;">
  Evaluation Design in Four Stages
</div>
<hr class="top-divider">

<div class="grid grid-cols-4 gap-4 mt-6">
  <div class="rcard" style="padding: 1rem 0.85rem;">
    <div class="content-h">Stage 01</div>
    <div class="font-bold text-sm" style="color: var(--teal);">Context &amp; RQs</div>
    <p class="text-xs mt-2" style="color: var(--muted); line-height: 1.55;">
      Campus AI deployment, student AI habits, and 3 core research questions.
    </p>
  </div>
  <div class="rcard" style="padding: 1rem 0.85rem;">
    <div class="content-h">Stage 02</div>
    <div class="font-bold text-sm" style="color: var(--teal);">Design &amp; Sampling</div>
    <p class="text-xs mt-2" style="color: var(--muted); line-height: 1.55;">
      Explanatory sequential mixed methods with a 46-invitee cohort census.
    </p>
  </div>
  <div class="rcard" style="padding: 1rem 0.85rem;">
    <div class="content-h">Stage 03</div>
    <div class="font-bold text-sm" style="color: var(--teal);">Survey &amp; Routing</div>
    <p class="text-xs mt-2" style="color: var(--muted); line-height: 1.55;">
      21-item instrument, 4-group skip logic, and exploratory TAM measures.
    </p>
  </div>
  <div class="rcard" style="padding: 1rem 0.85rem;">
    <div class="content-h">Stage 04</div>
    <div class="font-bold text-sm" style="color: var(--teal);">Interviews &amp; Limits</div>
    <p class="text-xs mt-2" style="color: var(--muted); line-height: 1.55;">
      Semi-structured walkthroughs, thematic coding, and pre-registered boundaries.
    </p>
  </div>
</div>

<div class="slide-footer">
  <span>ADS401 Group A · Evaluation Design Presentation</span>
  <span class="page-no">02 / 09</span>
</div>

<!--
Notes [10s] · 大纲导引
【英文演讲词】:
"Our presentation covers four main parts: // our research context and questions, // methodology and census sampling, // survey instrument and routing, // and finally our interview protocol and study boundaries."

【中文要义提示】:
我们今天的汇报主要包含四个部分：研究背景与问题、混合方法与近普查抽样、问卷工具与跳题路由，以及最后的后续访谈和诚实局限性。

【控时提示】:
一句话带过即可，不必逐字念卡片小字，让听众有整体预期。
-->

---
layout: default
---

<!-- Slide 3: Context & Motivation -->
<div class="section-label">RESEARCH CONTEXT &amp; MOTIVATION</div>

<div class="deck-title" style="font-size: 1.55rem; margin-top: 1rem;">
  Institutional AI Exists — But Are Students Actually Using It?
</div>
<hr class="top-divider">

<div class="grid grid-cols-3 gap-5 mt-4">
  <div class="rcard" style="padding: 1rem;">
    <div class="content-h">Campus Deployment</div>
    <div class="font-bold text-sm" style="color: var(--ink);">Official XJTLU AI Services</div>
    <p class="text-xs mt-2" style="color: var(--muted); line-height: 1.6;">
      XJTLU has deployed official tools including the <b>Junmou AI Agent Platform</b> and <b>Learning Mall chatbots</b> to support student learning and academic tasks.
    </p>
  </div>

  <div class="rcard" style="padding: 1rem;">
    <div class="content-h">Student Reality</div>
    <div class="font-bold text-sm" style="color: var(--ink);">Heavy External Commercial AI Use</div>
    <p class="text-xs mt-2" style="color: var(--muted); line-height: 1.6;">
      ADS401 postgraduates actively rely on external commercial AI (ChatGPT, DeepSeek, Kimi) for daily coding, writing, and literature tasks.
    </p>
  </div>

  <div class="rcard" style="padding: 1rem; border-left: 3px solid var(--accent);">
    <div class="content-h">The Empirical Gap</div>
    <div class="font-bold text-sm" style="color: var(--accent);">Adoption &amp; Displacement Unclear</div>
    <p class="text-xs mt-2" style="color: var(--muted); line-height: 1.6;">
      Do students know campus AI exists? How is it used, and why do many choose external tools instead? This remains completely unexamined.
    </p>
  </div>
</div>

<div class="quote-card mt-5" style="background: var(--paper); border: 1px solid var(--line); border-left: 3px solid var(--teal); padding: 0.65rem 1rem; border-radius: 4px; text-align: left;">
  <span style="font-weight: 700; color: var(--teal); font-size: 0.8rem;">Research Aim:</span>
  <span style="font-size: 0.78rem; color: var(--ink); margin-left: 0.4rem;">Explore ADS401 students' use or non-use of XJTLU AI and the reasons behind their choices, to inform future improvements.</span>
</div>

<div class="slide-footer">
  <span>Davis (1989) MIS Quarterly · Farinosi &amp; Melchior (2025) HSSC</span>
  <span class="page-no">03 / 09</span>
</div>

<!--
Notes [20s] · 背景与现实矛盾 (对齐 Speech1.0 Para 2)
【英文演讲词】:
"To begin, // we will explain why this topic matters. // Although XJTLU provides services such as Junmou AI to support learning, // students' awareness, usage, and reasons for using or not using these tools // remain unclear."

【中文要义提示】:
首先，我们说明为什么关注这个问题。虽然学校提供了君谋 AI 等服务来支持学习，但学生究竟是否了解这些工具、具体如何使用，以及为什么选择使用或不使用，目前还不清楚。

【发音指南】:
- Junmou AI [dʒuːn-moʊ eɪ-aɪ]
- awareness [ə-ˈwɛər-nəs]
-->

---
layout: default
---

<!-- Slide 4: Research Questions & Measure Mapping -->
<div class="section-label">RESEARCH QUESTIONS</div>

<div class="deck-title" style="font-size: 1.55rem; margin-top: 1rem;">
  Three Focused Questions: What Happens and Why
</div>
<hr class="top-divider">

<div class="grid grid-cols-3 gap-4 mt-3">
  <div class="rcard" style="padding: 0.85rem;">
    <div class="content-h">RQ1 · Awareness &amp; Adoption</div>
    <div class="font-bold text-xs text-teal" style="color: var(--teal); line-height: 1.45;">
      To what extent are ADS401 students aware of and adopting XJTLU AI?
    </div>
    <div class="mt-2 pt-2 text-xs" style="border-top: 1px solid var(--line); color: var(--muted); font-size: 0.68rem;">
      <b style="color: var(--ink);">Mapped Measures (material.md §3):</b>
      <ul style="padding-left: 0.9rem; margin-top: 0.2rem; line-height: 1.45;">
        <li>Q3 Prior service familiarity</li>
        <li>Q4 Lifetime ever-use</li>
        <li>Q5 Past-4-week usage group</li>
      </ul>
    </div>
  </div>

  <div class="rcard" style="padding: 0.85rem;">
    <div class="content-h">RQ2 · Usage Patterns</div>
    <div class="font-bold text-xs text-teal" style="color: var(--teal); line-height: 1.45;">
      How do ADS401 students use XJTLU AI for their academic tasks?
    </div>
    <div class="mt-2 pt-2 text-xs" style="border-top: 1px solid var(--line); color: var(--muted); font-size: 0.68rem;">
      <b style="color: var(--ink);">Mapped Measures (material.md §3):</b>
      <ul style="padding-left: 0.9rem; margin-top: 0.2rem; line-height: 1.45;">
        <li>Q6 Recent usage frequency</li>
        <li>Q7 Activity categories (A–E)</li>
        <li>Q8 Output verification habits</li>
        <li>Q14/Q15 External reliance</li>
      </ul>
    </div>
  </div>

  <div class="rcard" style="padding: 0.85rem;">
    <div class="content-h">RQ3 · Factors &amp; Comparison</div>
    <div class="font-bold text-xs text-teal" style="color: var(--teal); line-height: 1.45;">
      What perceived benefits, barriers, and tool differences explain choices and intentions?
    </div>
    <div class="mt-2 pt-2 text-xs" style="border-top: 1px solid var(--line); color: var(--muted); font-size: 0.68rem;">
      <b style="color: var(--ink);">Mapped Measures (material.md §3):</b>
      <ul style="padding-left: 0.9rem; margin-top: 0.2rem; line-height: 1.45;">
        <li>Q7a Activity-specific usefulness</li>
        <li>Q9 TAM battery (PU / PEOU / Trust)</li>
        <li>Q10 Problems &amp; Q12 Non-use reasons</li>
        <li>Q11/Q13 Intentions &amp; Q16 Comparison</li>
      </ul>
    </div>
  </div>
</div>

<div class="slide-footer">
  <span>Measure mapping from material.md §3 · Full question text in Supplementary PDF</span>
  <span class="page-no">04 / 09</span>
</div>

<!--
Notes [25s] · 三个核心研究问题 (对齐 Speech1.0 Para 3)
【英文演讲词】:
"Based on this background, // we developed three research questions: // How aware of and willing to adopt university-provided AI are students? // How do they use it for ADS401 learning? // And what perceived benefits, barriers, and differences between tools // are associated with their choices and future intentions?"

【中文要义提示】:
围绕这一背景，我们提出了三个研究问题：学生对校内 AI 的认知和采纳程度如何？他们如何将其用于 ADS401 学习？哪些收益、障碍和工具差异与他们的选择及未来使用意愿有关？

【提醒组员】:
正如汤鸿程在群里强调的，口头概括性念出核心问句即可；卡片下方清晰注明了对应的题目编号（Q3~Q16），考官看屏幕就能看到严密的构念映射！
-->

---
layout: default
---

<!-- Slide 5: Methodology & Census Sampling (46+4) -->
<div class="section-label">METHODOLOGY &amp; SAMPLING</div>

<div class="deck-title" style="font-size: 1.55rem; margin-top: 1rem;">
  Explanatory Sequential Design &amp; 46-Invitee Cohort Census
</div>
<hr class="top-divider">

<div class="grid grid-cols-2 gap-6 mt-3">
  <div>
    <div class="content-h">Research Design</div>
    <div class="rcard" style="padding: 0.85rem; height: calc(100% - 1.8rem);">
      <div class="font-bold text-sm text-teal" style="color: var(--teal);">
        Explanatory Sequential Mixed Methods
      </div>
      <div class="mt-2 text-xs" style="color: var(--ink); line-height: 1.55;">
        <b>Phase 1 · Quantitative Survey</b> (Cross-sectional)<br>
        <span style="color: var(--muted);">Maps the overall landscape: awareness, usage patterns, ratings (What &amp; How many).</span>
      </div>
      <div class="text-center my-1" style="color: var(--accent); font-weight: bold; font-size: 0.8rem;">↓ sequential linkage</div>
      <div class="text-xs" style="color: var(--ink); line-height: 1.55;">
        <b>Phase 2 · Qualitative Interviews</b> (Semi-structured)<br>
        <span style="color: var(--muted);">Follows up on survey findings to explain reasons behind adoption and non-use (Why &amp; How).</span>
      </div>
    </div>
  </div>

  <div>
    <div class="content-h">Sampling &amp; Analysis Boundaries</div>
    <div class="rcard" style="padding: 0.85rem; height: calc(100% - 1.8rem);">
      <div class="font-bold text-sm text-teal" style="color: var(--teal);">
        Cohort Census: 50 Enrolled → 46 Invitees
      </div>
      <ul class="text-xs mt-2" style="color: var(--ink); line-height: 1.55; padding-left: 1.1rem;">
        <li><b>Target frame:</b> All 50 enrolled ADS401 students</li>
        <li><b>Exclusion:</b> 4 student researchers excluded → <b>46 eligible invitees</b> (voluntary census invitation)</li>
        <li><b>Statistical rigour:</b> Small N ≈ 50 prohibits inferential group testing (d=0.5 yields power only 0.24)</li>
        <li><b>Analysis strategy:</b> Strictly <b>descriptive statistics &amp; cross-tabulations</b> with per-item valid denominators; no causal claims</li>
      </ul>
    </div>
  </div>
</div>

<div class="slide-footer">
  <span>Ivankova et al. (2006) Field Methods · Cohen (1988) Power Analysis</span>
  <span class="page-no">05 / 09</span>
</div>

<!--
Notes [25s] · 混合方法与近普查抽样 (对齐 Speech1.0 Para 4)
【英文演讲词】:
"To answer these questions, // we use an explanatory sequential mixed-methods design: // first a cross-sectional online survey, // followed by interviews informed by the survey findings. // Our target population is all ADS401 students. // There are 50 students in the module; // after excluding four student researchers, // we plan to invite 46 students."

【中文要义提示】:
为回答这些问题，我们采用解释性顺序混合方法：先开展横断面在线问卷，再根据问卷结果进行访谈。研究对象是 ADS401 全体学生。目前课程有 50 名学生，排除 4 名研究者后，计划邀请 46 名学生参与。

【发音指南】:
- explanatory sequential [ɪk-ˈsplæn-ə-tɔː-ri sɪ-ˈkwɛn-ʃəl]
- cross-sectional [krɒs ˈsɛk-ʃə-nəl]
-->

---
layout: default
---

<!-- Slide 6: Survey Instrument & Four-Group Routing -->
<div class="section-label">SURVEY INSTRUMENT &amp; ROUTING</div>

<div class="deck-title" style="font-size: 1.55rem; margin-top: 1rem;">
  21-Item Questionnaire with Four-Group Adaptive Routing
</div>
<hr class="top-divider">

<div class="routing-box mt-2" style="background: var(--paper); border: 1px solid var(--line); border-radius: 6px; padding: 0.7rem 1rem;">
  <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--line); padding-bottom: 0.35rem; font-size: 0.76rem;">
    <span><b>Entry Gate:</b> Q1 Enrollment Screening + Q2 Informed Consent (PIS)</span>
    <span style="color: var(--muted);">Recall period: Past 4 weeks · Duration: ~5–7 min</span>
  </div>

  <div class="grid grid-cols-4 gap-3 mt-3">
    <div style="background: #fff; border: 1px solid var(--line); border-top: 3px solid var(--teal); border-radius: 4px; padding: 0.55rem;">
      <div style="font-weight: bold; font-size: 0.76rem; color: var(--teal);">G1 · Both AI</div>
      <div style="font-size: 0.65rem; color: var(--muted); margin: 0.15rem 0;">Used XJTLU AI + External</div>
      <div style="font-size: 0.65rem; color: var(--ink); line-height: 1.4;">
        • Q6–Q11 Campus UX &amp; TAM<br>
        • Q14 External categories<br>
        • Q15–Q16 Direct comparison
      </div>
    </div>

    <div style="background: #fff; border: 1px solid var(--line); border-top: 3px solid var(--accent); border-radius: 4px; padding: 0.55rem;">
      <div style="font-weight: bold; font-size: 0.76rem; color: var(--accent);">G2 · Other AI Only</div>
      <div style="font-size: 0.65rem; color: var(--muted); margin: 0.15rem 0;">External AI Only</div>
      <div style="font-size: 0.65rem; color: var(--ink); line-height: 1.4;">
        • Q12 Non-adoption reasons<br>
        • Q13 Willingness to try<br>
        • Q14 External categories
      </div>
    </div>

    <div style="background: #fff; border: 1px solid var(--line); border-top: 3px solid #94a3b8; border-radius: 4px; padding: 0.55rem;">
      <div style="font-weight: bold; font-size: 0.76rem; color: #64748b;">G3 · Neither / No AI</div>
      <div style="font-size: 0.65rem; color: var(--muted); margin: 0.15rem 0;">No AI in past 4 weeks</div>
      <div style="font-size: 0.65rem; color: var(--ink); line-height: 1.4;">
        • Q12 Non-adoption reasons<br>
        • Q13 Willingness to try<br>
        • (Skips all usage blocks)
      </div>
    </div>

    <div style="background: #fff; border: 1px solid var(--line); border-top: 3px solid #0d9488; border-radius: 4px; padding: 0.55rem;">
      <div style="font-weight: bold; font-size: 0.76rem; color: #0d9488;">G4 · XJTLU AI Only</div>
      <div style="font-size: 0.65rem; color: var(--muted); margin: 0.15rem 0;">Campus AI Only</div>
      <div style="font-size: 0.65rem; color: var(--ink); line-height: 1.4;">
        • Q6–Q11 Campus UX &amp; TAM<br>
        • (Skips external questions)<br>
        • Future continuance
      </div>
    </div>
  </div>

  <div style="margin-top: 0.5rem; padding-top: 0.35rem; border-top: 1px solid var(--line); font-size: 0.7rem; color: var(--ink);">
    <b>All Groups Converge:</b> Q17 Decision factors · Q18 Priorities for XJTLU AI · Q19 Open feedback · Q20/Q21 Interview opt-in
  </div>
</div>

<div class="slide-footer">
  <span>Routing architecture from material.md §4 · Prevents non-users from rating unexperienced tools</span>
  <span class="page-no">06 / 09</span>
</div>

<!--
Notes [30s] · 问卷架构与四组自适应跳题 (对齐 Speech1.0 Para 5 + 汤鸿程微信重点)
【英文演讲词】:
"The pilot questionnaire takes about five to seven minutes // and asks mainly about learning in the past four weeks. // It covers AI awareness and use, // academic tasks, perceived usefulness, ease of use, trust, barriers, and future intentions. // We will group students by recent AI use // and compare usage patterns using descriptive statistics and cross-tabulations. // Tool comparisons reflect students' perceptions, // not objective differences in system capability."

【中文要义提示】:
具体来说，预测试问卷预计需要 5–7 分钟，主要询问过去四周的学习经历。内容包括 AI 认知和使用、学习任务、有用性、易用性、信任、使用障碍及未来意愿。我们将按近期 AI 使用情况分为四组，并用描述统计和交叉分析比较使用模式。工具比较反映学生的主观体验，不代表系统客观能力的差异。

【提醒组员】:
屏幕上的 G1~G4 卡片直观展示了四组分流机制，演讲者只需沉稳概括，考官自然能看懂我们严密规避了非态度伪打分。
-->

---
layout: default
---

<!-- Slide 7: Follow-up Interviews & Qualitative Integration -->
<div class="section-label">FOLLOW-UP INTERVIEWS &amp; INTEGRATION</div>

<div class="deck-title" style="font-size: 1.55rem; margin-top: 1rem;">
  Semi-Structured Walkthroughs to Explain Adoption Drivers
</div>
<hr class="top-divider">

<div class="grid grid-cols-2 gap-6 mt-3">
  <div>
    <div class="content-h">Interview Protocol (material.md §6)</div>
    <div class="rcard" style="padding: 0.85rem; height: calc(100% - 1.8rem);">
      <div class="font-bold text-sm text-teal" style="color: var(--teal);">
        Purposive Sampling via Q20/Q21 Opt-in
      </div>
      <ul class="text-xs mt-2" style="color: var(--ink); line-height: 1.6; padding-left: 1.1rem;">
        <li><b>Sample size:</b> 4–6 students recruited from Q20 opt-ins</li>
        <li><b>Quota priority:</b> <b>Both AI (G1)</b> and <b>Other AI Only (G2)</b> to examine replacement trade-offs</li>
        <li><b>Format:</b> 15–20 minutes semi-structured interviews</li>
        <li><b>Artifact walkthrough:</b> Reviewing actual coursework prompt history, task workflows, and friction points</li>
      </ul>
    </div>
  </div>

  <div>
    <div class="content-h">Qualitative Analysis &amp; Triangulation</div>
    <div class="rcard" style="padding: 0.85rem; height: calc(100% - 1.8rem);">
      <div class="font-bold text-sm text-teal" style="color: var(--teal);">
        Thematic Coding &amp; Sequential Integration
      </div>
      <ul class="text-xs mt-2" style="color: var(--ink); line-height: 1.6; padding-left: 1.1rem;">
        <li><b>Thematic analysis:</b> 6-phase coding framework (Braun &amp; Clarke, 2006) to identify recurring adoption themes</li>
        <li><b>Mixed-methods integration:</b> Connecting qualitative themes with quantitative survey distributions (Fetters et al., 2013)</li>
        <li><b>Actionable outcome:</b> Identifying specific friction points to inform concrete XJTLU AI platform improvements</li>
      </ul>
    </div>
  </div>
</div>

<div class="slide-footer">
  <span>Braun &amp; Clarke (2006) Qualitative Research in Psych · Fetters et al. (2013) Health Services Research</span>
  <span class="page-no">07 / 09</span>
</div>

<!--
Notes [25s] · 追踪访谈与定性整合 (对齐 Speech1.0 Para 6)
【英文演讲词】:
"After collecting the survey data, // we will use interviews to explore the reasons behind the patterns. // We plan to select four to six students // with different levels of perceived usefulness. // Starting from specific experiences, // the interviews will explore the reasons behind their ratings and tool choices, // and we will connect these themes with the survey findings."

【中文要义提示】:
问卷收集之后，研究将进一步通过访谈解释数据背后的原因。我们计划选择 4–6 名学生，尽量覆盖不同的有用性感知；访谈从具体经历出发，探讨评分和工具选择的原因，再将访谈主题与问卷结果对照。

【发音指南】:
- purposive sampling [ˈpɜː-pə-sɪv ˈsæm-plɪŋ]
- thematic analysis [θɪ-ˈmæt-ɪk ə-ˈnæl-ə-sɪs]
-->

---
layout: default
---

<!-- Slide 8: Study Limitations, Reflection & Materials -->
<div class="section-label">LIMITATIONS &amp; MATERIALS</div>

<div class="deck-title" style="font-size: 1.55rem; margin-top: 1rem;">
  Pre-Registered Boundaries &amp; Complete Deliverables
</div>
<hr class="top-divider">

<div class="grid grid-cols-2 gap-6 mt-2">
  <div>
    <div class="content-h">Pre-Registered Limitations (material.md §9)</div>
    <div class="rcard" style="padding: 0.75rem;">
      <ul class="text-xs" style="color: var(--ink); line-height: 1.55; padding-left: 1rem;">
        <li><b>Single-module sample:</b> ADS401 cohort only; findings describe participants and do not generalise across XJTLU.</li>
        <li><b>Self-reported data:</b> Measures student perceptions and recall, not telemetry server logs.</li>
        <li><b>Interview coverage:</b> Prioritising G1/G2 dual users may under-represent non-user perspectives.</li>
        <li><b>Cross-sectional design:</b> Captures recent use and future intentions, not longitudinal causality.</li>
        <li><b>Perception comparison:</b> Compares user experience, not objective model benchmarks.</li>
      </ul>
    </div>
  </div>

  <div>
    <div class="content-h">Materials &amp; Deliverables Inventory</div>
    <div class="rcard" style="padding: 0.75rem;">
      <div style="font-size: 0.75rem; color: var(--ink); line-height: 1.6;">
        <b>Completed Deliverables for Presentation 2:</b>
        <ul style="padding-left: 1rem; margin-top: 0.2rem; color: var(--muted);">
          <li><b>Presentation Slides:</b> Interactive web deck &amp; 9-page PDF</li>
          <li><b>Supplementary Materials PDF:</b> 10-page single file (PIS, 21-item questionnaire, interview protocol, references)</li>
          <li><b>Live Project Website:</b> Hosted on GitHub Pages</li>
        </ul>
        <div class="mt-2 pt-2" style="border-top: 1px solid var(--line); font-size: 0.7rem; color: var(--teal);">
          <b>Next Milestone:</b> Survey fielding window (19 Oct – 02 Nov) → Presentation 3 (09 Nov).
        </div>
      </div>
    </div>
  </div>
</div>

<div class="slide-footer">
  <span>Chung et al. (2024) · Farinosi &amp; Melchior (2025) · Coursework Sheet p4</span>
  <span class="page-no">08 / 09</span>
</div>

<!--
Notes [25s] · 局限性反思与材料清单 (对齐 Speech1.0 Para 7)
【英文演讲词】:
"Finally, // this study focuses on one module and relies on self-reported data, // so the findings may not represent students in other courses. // A cross-sectional survey also cannot establish causality or long-term use. // Even so, // the study can help us understand ADS401 students' AI choices // and identify possible improvements to university AI services."

【中文要义提示】:
最后，本研究聚焦单一课程并依赖自我报告数据，因此结果不一定代表其他课程学生的情况。横断面调查也不能证明因果关系或长期使用情况。尽管如此，研究仍能帮助我们理解 ADS401 学生的 AI 使用选择，并为改进校内 AI 服务提供参考。

【发音指南】:
- causality [kɔː-ˈzæl-ə-ti]
- cross-sectional [krɒs ˈsɛk-ʃə-nəl]
-->

---
layout: default
---

<!-- Slide 9: Q&A / Discussion & Thank You -->
<div class="section-label">QUESTIONS &amp; ANSWERS</div>

<div style="margin-top: 3rem; text-align: center;">
  <div style="font-family: Newsreader, Georgia, serif; font-size: 3.8rem; font-weight: 700; color: var(--teal); line-height: 1;">
    Q &amp; A
  </div>
  <div style="font-family: Newsreader, Georgia, serif; font-style: italic; font-size: 1.25rem; color: var(--muted); margin-top: 0.8rem;">
    Thank you for your attention. We welcome your questions and feedback.
  </div>

  <div class="rcard mt-6 mx-auto" style="max-width: 28rem; padding: 1rem 1.4rem; text-align: left; background: #fff;">
    <div style="font-size: 0.82rem; font-weight: 600; color: var(--teal); margin-bottom: 0.4rem;">
      Project Resources &amp; Documentation
    </div>
    <div style="font-size: 0.76rem; color: var(--ink); line-height: 1.7;">
      • <b>Live Web Report:</b> <span style="color: var(--accent);">https://lionchena.github.io/ads401/</span><br>
      • <b>Interactive Web Slides:</b> <span style="color: var(--accent);">https://lionchena.github.io/ads401/slides/</span><br>
      • <b>Source Repository:</b> <span style="color: var(--muted);">https://github.com/LionChenA/ads401</span><br>
      • <b>Group A:</b> Hongcheng TANG · Mingjian TAO · Liyuan CHEN · Haode SHEN
    </div>
  </div>
</div>

<div class="slide-footer">
  <span>ADS401 Presentation 2 · Xi'an Jiaotong-Liverpool University</span>
  <span class="page-no">09 / 09</span>
</div>

<!--
Notes · 现场答辩常驻页面 (3分钟 Q&A 期间全程停留在此页)
【收尾致谢英文】:
"Thank you very much. // We now welcome any questions or suggestions from Dr. Li and our fellow classmates."

【中文答辩速记备忘 (高频三大质询理由)】:
1. 为什么只有46人？ -> 班级近普查（50名在读，排除4名研究者），非便利抽样。
2. 为什么不做两组独立样本 t 检验？ -> n≈30时两样本检验力仅 0.24，第二类错误超 70%，做因果推断不严谨，因而恪守纯描述统计与交叉分析。
3. 怎么保证未用过校内AI的人不乱打分？ -> Q5 强制自适应跳题路由，未用过者直接跳过效用打分，直达未采纳原因。
-->
