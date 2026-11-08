#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Restructure the ADS401 XJTLU-AI survey submissions (WJX / 问卷星 exports) into
analysis-ready datasets.

Inputs (pre3/):
  - "ADS401 Students' Awareness, Adoption and Use of XJTLU AI_Submissions_2026-11-05.csv"   (EN, 21 rows)
  - "ADS401 学生 XJTLU AI 认知、采纳与使用调查_Submissions_2026-11-07(1).csv"                 (ZH, 4 rows)

Outputs (pre3/processed/):
  - survey_long.csv       tidy/long format: one row per (respondent x question x item/option)
  - survey_wide.csv       wide format:     one row per respondent, short column names
  - survey_codebook.csv   data dictionary mapping question/item/option -> label & code

Design decisions (see conversation explanation for full detail):
  1. The two deployments (EN + ZH) are merged into one dataset with a `survey_language`
     column and identical schema. Canonical question IDs use the questionnaire_v2 doc
     numbering Q1-Q24 (+ Q11a / Q18a / Q18b), NOT the WJX display numbers 1-27.
  2. Likert / ordinal answers are coded numerically (e.g. 1..5). "N/A" / "Unable to
     judge" / "Can't recall" / "Prefer not to say" are left blank (treated as missing),
     and the original label is kept in `response`.
  3. Multi-select questions are exploded to one row per option with a 0/1 `selected`
     flag (instead of one column of comma-joined text plus N true/false columns).
  4. Branch logic (which questions each respondent actually saw) is derived from Q1/Q7/Q9/Q23,
     so "question skipped" and "option not selected" are no longer conflated.
"""
import csv
import os
import re

csv.field_size_limit(10**9)
BASE = os.path.dirname(os.path.abspath(__file__))
SRC_EN = os.path.join(BASE, "..", "ADS401 Students' Awareness, Adoption and Use of XJTLU AI_Submissions_2026-11-07.csv")
SRC_ZH = os.path.join(BASE, "..", "ADS401 学生 XJTLU AI 认知、采纳与使用调查_Submissions_2026-11-07(1).csv")

# ----------------------------------------------------------------------------
# Canonical questionnaire metadata (doc numbering Q1-Q24 + Q11a/Q18a/Q18b)
# ----------------------------------------------------------------------------
# Scales shared by matrix questions -------------------------------------------
SCALE_AGREEMENT = [
    (1, "Strongly disagree", "极不同意"),
    (2, "Disagree", "不同意"),
    (3, "Neutral", "中立"),
    (4, "Agree", "同意"),
    (5, "Strongly agree", "非常同意"),
]
SCALE_USEFULNESS = [
    (1, "Not useful", "没有用处"),
    (2, "Slightly useful", "有点用处"),
    (3, "Moderately useful", "一般有用"),
    (4, "Useful", "有用"),
    (5, "Very useful", "非常有用"),
]
SCALE_COMPARISON = [
    (1, "XJTLU AI better", "西浦 AI 更好"),
    (2, "About the same", "差不多"),
    (3, "External AI better", "外部 AI 更好"),
]

NA_AGREEMENT = ("N/A", "N/A")
NA_USEFULNESS = ("N/A", "N/A")
NA_COMPARISON = ("Unable to compare", "无法比较")

# Activity-category rows shared by Q11 / Q11a / Q18 / Q18b / Q19 ---------------
ACTIVITIES = [
    ("campus", "Finding and using campus resources", "查找与使用校内资源"),
    ("within", "Learning within-course content", "课程之内内容"),
    ("beyond", "Support beyond-course content", "课程之外支持"),
    ("policy", "Understanding ADS401 policies", "了解 ADS401 政策"),
    ("prod",   "Coursework production", "课程作业制作"),
    ("other",  "Other activity", "其他活动"),
]

# Full activity option labels (the long text shown in Q11/Q18 multi-select) ----
ACTIVITY_OPTIONS = [
    ("campus", "Finding and using campus resources (e.g., finding an empirical HCI paper for Pre1 via XJTLU Library / Research Portal, module materials on Learning Mall)",
               "查找与使用校内资源（如为 Pre1 通过西浦图书馆 / Research Portal 查找实证 HCI 论文、Learning Mall 上的课程资料等）"),
    ("within", "Learning within-course content (understanding concepts, finding past exams)",
               "课程之内：学习课程内容（理解概念、找往年试题等）"),
    ("beyond", "Support beyond-course content (e.g., survey tools, scales, research-method references)",
               "课程之外：课程材料之外的研究方法支持（比如调研问卷工具、量表、方法参考等）"),
    ("policy", "Understanding ADS401 policies (why learn ADS401, what's taught, grading criteria, tutor information)",
               "了解 ADS401 政策（课程意义、教学内容、评分标准、导师信息等）"),
    ("prod",   "Coursework production (survey design, literature search, slides)",
               "课程作业制作（问卷设计、文献查找、PPT 制作等）"),
]

# ----------------------------------------------------------------------------
# Questions: canonical definition
# type: single_nominal | single_ordinal | multi | matrix_agreement |
#       matrix_usefulness | matrix_comparison | text
# For single_* : options = [(code, en, zh), ...]  (code None -> nominal / NA-type)
# For multi    : items   = [(slug, en, zh), ...]   (+ an implicit 'other' + text)
# For matrix_* : items   = [(slug, en, zh), ...]
# ----------------------------------------------------------------------------
QUESTIONS = [
    dict(qid="Q1", section="introduction", type="single_nominal",
         text_en="Have you read the information above and do you voluntarily agree to participate?",
         text_zh="你是否已阅读上述说明并自愿参与？",
         slug="consent",
         options=[(None, "Yes, I agree", "是，我同意"),
                  (None, "No, I do not agree", "否，我不同意")]),
    dict(qid="Q2", section="background", type="single_nominal",
         text_en="Which programme or pathway are you in?",
         text_zh="你就读哪个专业（方向）？",
         slug="programme",
         options=[(None, "MSc Human-Computer Interaction — Human-centric Computing Pathway", "MSc 人机交互 — 以人为中心计算方向（Human-centric Computing Pathway）"),
                  (None, "MSc Human-Computer Interaction — Human-AI Collaborative Computing Pathway", "MSc 人机交互 — 人机协同计算方向（Human-AI Collaborative Computing Pathway）"),
                  (None, "MSc Social Computing — Full-Time", "MSc 社会计算 — 全日制（Full-Time）"),
                  (None, "MSc Social Computing — Part-Time", "MSc 社会计算 — 在职（Part-Time）"),
                  (None, "Other (please specify)", "其他（请注明）")]),
    dict(qid="Q3", section="background", type="single_nominal",
         text_en="What was your primary field of study before your current programme?",
         text_zh="请选择最能代表你进入现专业前所修专业的学科领域。",
         slug="prior_field",
         options=[(None, "Computer Science & Information Technology", "计算机科学与信息技术"),
                  (None, "Engineering & Technology", "工程与技术"),
                  (None, "Design, Arts & Media", "设计、艺术与媒体"),
                  (None, "Social Sciences & Psychology", "社会科学与心理学"),
                  (None, "Business, Management & Economics", "商业、管理与经济学"),
                  (None, "Humanities & Languages", "人文与语言"),
                  (None, "Natural Sciences & Mathematics", "自然科学与数学"),
                  (None, "Health & Life Sciences", "健康与生命科学"),
                  (None, "Education", "教育学"),
                  (None, "Other (please specify)", "其他（请注明）"),
                  (None, "Prefer not to say", "不愿透露")]),
    dict(qid="Q4", section="background", type="single_nominal",
         text_en="What is your gender?",
         text_zh="你的性别是？",
         slug="gender",
         options=[(None, "Woman", "女"),
                  (None, "Man", "男"),
                  (None, "Prefer not to say", "不愿透露")]),
    dict(qid="Q5", section="background", type="single_ordinal",
         text_en="What is your age?",
         text_zh="你的年龄段是？",
         slug="age",
         options=[(1, "20 or younger", "20 岁及以下"),
                  (2, "21–24", "21–24 岁"),
                  (3, "25–29", "25–29 岁"),
                  (4, "30 or older", "30 岁及以上"),
                  (None, "Prefer not to say", "不愿透露")]),
    dict(qid="Q6", section="background", type="single_ordinal",
         text_en="How many years of experience do you have with AI platforms (e.g., Doubao, ChatGPT, Gemini)?",
         text_zh="你使用 AI 平台（包括但不仅限于豆包、ChatGPT、Gemini 等）的经验年限是？",
         slug="ai_experience",
         options=[(1, "No experience", "从来没有"),
                  (2, "Less than 1 year", "1 年以内"),
                  (3, "1–2 years", "1–2 年"),
                  (4, "2–3 years", "2–3 年"),
                  (5, "More than 3 years", "大于 3 年")]),
    dict(qid="Q7", section="awareness", type="single_nominal",
         text_en="So far, how familiar are you with XJTLU AI?",
         text_zh="到目前为止，你对西浦 AI 的熟悉程度？",
         slug="familiarity",
         options=[(None, "Heard of them and knew some functions", "听说过并了解一些功能"),
                  (None, "Heard of them but knew little", "听说过但不太了解"),
                  (None, "Had not heard of them", "没听说过"),
                  (None, "Unsure whether known services were XJTLU-provided", "不确定已知服务是否为西浦官方提供")]),
    dict(qid="Q8", section="awareness", type="single_nominal",
         text_en="Have you ever used XJTLU AI?",
         text_zh="你是否曾使用过西浦 AI？",
         slug="ever_used",
         options=[(None, "Yes", "是"),
                  (None, "No", "否"),
                  (None, "Not sure", "不确定")]),
    dict(qid="Q9", section="recent_use", type="single_nominal",
         text_en="During the past four weeks, which statement best describes your use of AI for ADS401 learning activities? (Select one.)",
         text_zh="过去四周，哪一项符合你在 ADS401 学习活动中使用 AI 的情况？（单选）",
         slug="use_type",
         options=[(None, "Both XJTLU AI and External AI", "两者都用（西浦 AI 和外部 AI）"),
                  (None, "XJTLU AI only (no External AI)", "仅西浦 AI（没用外部 AI）"),
                  (None, "External AI only (no XJTLU AI)", "仅外部 AI（没用西浦 AI）"),
                  (None, "Neither XJTLU AI nor External AI", "两者都没用")]),
    dict(qid="Q10", section="xjtu_ai_use", type="single_ordinal",
         text_en="How many times did you use XJTLU AI for ADS401 learning during the past four weeks?",
         text_zh="过去四周你使用西浦 AI 进行 ADS401 学习的次数？",
         slug="times",
         options=[(1, "1–4 times in total (at most once a week on average)", "共 1–4 次（约每周不超过 1 次）"),
                  (2, "5–8 times in total (about 1–2 times a week on average)", "共 5–8 次（约每周 1–2 次）"),
                  (3, "9–12 times in total (about 2–3 times a week on average)", "共 9–12 次（约每周 2–3 次）"),
                  (4, "More than 12 times in total (more than 3 times a week on average)", "超过 12 次（约每周 3 次以上）"),
                  (None, "Can't recall", "不记得了")]),
    dict(qid="Q11", section="xjtu_ai_use", type="multi",
         text_en="For which broad categories of ADS401 learning activities did you use XJTLU AI in the past four weeks? (Select all that apply.)",
         text_zh="过去四周你将西浦 AI 用于哪些 ADS401 学习活动类别？（多选）",
         items=ACTIVITY_OPTIONS + [("other", "Other (please specify)", "其他（请注明）")]),
    dict(qid="Q11a", section="xjtu_ai_use", type="matrix_usefulness",
         text_en="For each activity category, rate how useful XJTLU AI was in your actual experience. Select N/A for categories you did not use it for.",
         text_zh="对每类活动，评价西浦 AI 在你实际使用中的有用程度；未使用选 N/A。",
         items=ACTIVITIES),
    dict(qid="Q12", section="xjtu_ai_use", type="single_ordinal",
         text_en="In the past four weeks, when you used information from XJTLU AI for ADS401 work, how often did you check it against course materials or other reliable sources?",
         text_zh="过去四周，你将西浦 AI 的信息用于 ADS401 学习时，核对课程材料或其他可靠来源的频率是？",
         slug="verify_freq",
         options=[(1, "Never", "从不"),
                  (2, "Rarely (about 1–3 times in 10)", "很少（约每 10 次中 1–3 次）"),
                  (3, "Sometimes (about 4–6 times in 10)", "有时（约每 10 次中 4–6 次）"),
                  (4, "Often (about 7–9 times in 10)", "经常（约每 10 次中 7–9 次）"),
                  (5, "Every time", "每次都核实"),
                  (None, "Unable to judge", "无法判断")]),
    dict(qid="Q13", section="xjtu_ai_use", type="matrix_agreement",
         text_en="Based on your overall experience using XJTLU AI in ADS401, how much do you agree with these statements? (Select N/A if you cannot judge.)",
         text_zh="基于在西浦 AI 上的整体使用体验，你在多大程度上同意以下表述？（无法判断选 N/A）",
         items=[("pu1", "XJTLU AI helps me complete ADS401 tasks more effectively", "西浦 AI 帮助我更有效地完成 ADS401 任务"),
                ("pu2", "XJTLU AI helps me complete ADS401 tasks more efficiently", "西浦 AI 帮助我更高效地完成 ADS401 任务"),
                ("peou1", "XJTLU AI is easy to learn how to use", "西浦 AI 容易上手"),
                ("peou2", "XJTLU AI is easy to use for my ADS401 tasks", "西浦 AI 在我的 ADS401 任务中易于使用"),
                ("trust1", "XJTLU AI usually provides information I consider reliable", "西浦 AI 通常提供我认为可靠的信息"),
                ("trust2", "I generally trust XJTLU AI's explanations", "我总体上信任西浦 AI 的解释")]),
    dict(qid="Q14", section="xjtu_ai_use", type="multi",
         text_en="In the past four weeks, which problems did you experience when using XJTLU AI for ADS401 learning? (Select up to 3.)",
         text_zh="过去四周你使用西浦 AI 时遇到了哪些问题？（多选，最多选 3 项）",
         items=[("unclear_which", "Unclear which XJTLU AI to use", "不清楚该用哪个西浦 AI 服务"),
                ("hard_prompts", "Hard to formulate prompts", "难以写好提示词"),
                ("inaccurate", "Inaccurate, unclear or vague answers", "回答不准确、不清晰或模糊"),
                ("not_relevant", "Answers not relevant to ADS401", "回答与 ADS401 无关"),
                ("time_consuming", "Time-consuming to verify or revise", "核实或修改耗时"),
                ("inconvenient", "Inconvenient access/login/workflow", "访问、登录或流程不便"),
                ("functions_insufficient", "Functions insufficient", "功能不足"),
                ("uncertain_permission", "Uncertain about course permission", "不确定课程是否允许"),
                ("privacy", "Privacy or data concerns", "隐私或数据顾虑"),
                ("no_problem", "No notable problem", "无明显问题"),
                ("other", "Other (please specify)", "其他（请注明）")]),
    dict(qid="Q15", section="xjtu_ai_use", type="single_ordinal",
         text_en="If you have a suitable ADS401 task in the next four weeks, how likely are you to continue using XJTLU AI?",
         text_zh="若未来四周有合适的 ADS401 任务，你继续使用西浦 AI 的可能性？",
         slug="continue",
         options=[(1, "Very unlikely", "很不可能"),
                  (2, "Unlikely", "不太可能"),
                  (3, "Neutral", "中立"),
                  (4, "Likely", "比较可能"),
                  (5, "Very likely", "非常可能")]),
    dict(qid="Q16", section="non_use", type="multi",
         text_en="What are your main reasons for NOT using XJTLU AI for ADS401 during the past four weeks? (Select up to 3.)",
         text_zh="过去四周未在 ADS401 中使用西浦 AI 的主要原因？（多选，最多选 3 项）",
         items=[("previously_unaware", "Previously unaware", "之前不知道"),
                ("unclear_what", "Unclear what it can do", "不清楚它能做什么"),
                ("unsure_access", "Unsure how to access", "不知道如何访问"),
                ("no_suitable_task", "No suitable ADS401 task", "没有合适的 ADS401 任务"),
                ("prefer_external", "Prefer External AI", "更偏好外部 AI"),
                ("prefer_nonai", "Prefer non-AI methods", "更偏好非 AI 方法"),
                ("concerned_inaccurate", "Concerned about inaccurate answers", "担心回答不准确"),
                ("unsure_permitted", "Unsure if AI use permitted", "不确定是否允许使用 AI"),
                ("privacy", "Privacy/data concerns", "隐私或数据顾虑"),
                ("past_unsatisfactory", "Past experience unsatisfactory", "过往体验不佳"),
                ("access_inconvenient", "Access or operation seemed inconvenient", "访问或操作似乎不便"),
                ("other", "Other (please specify)", "其他（请注明）")]),
    dict(qid="Q17", section="non_use", type="single_ordinal",
         text_en="If you have a suitable ADS401 task in the next four weeks, how willing are you to try or resume XJTLU AI?",
         text_zh="若未来四周有合适的 ADS401 任务，你尝试或恢复使用西浦 AI 的意愿？",
         slug="willingness",
         options=[(1, "Very unwilling", "很不愿意"),
                  (2, "Unwilling", "不太愿意"),
                  (3, "Neutral", "中立"),
                  (4, "Willing", "比较愿意"),
                  (5, "Very willing", "非常愿意")]),
    dict(qid="Q18", section="external_ai", type="multi",
         text_en="For which broad categories of ADS401 learning activities did you use External AI in the past four weeks? (Select all that apply.)",
         text_zh="过去四周你将外部 AI 用于哪些 ADS401 学习活动类别？（多选）",
         items=ACTIVITY_OPTIONS + [("other", "Other (please specify)", "其他（请注明）")]),
    dict(qid="Q18a", section="external_ai", type="single_ordinal",
         text_en="How many times did you use External AI for ADS401 learning during the past four weeks?",
         text_zh="过去四周你使用外部 AI 进行 ADS401 学习的次数？",
         slug="times",
         options=[(1, "1–4 times in total (at most once a week on average)", "共 1–4 次（约每周不超过 1 次）"),
                  (2, "5–8 times in total (about 1–2 times a week on average)", "共 5–8 次（约每周 1–2 次）"),
                  (3, "9–12 times in total (about 2–3 times a week on average)", "共 9–12 次（约每周 2–3 次）"),
                  (4, "More than 12 times in total (more than 3 times a week on average)", "超过 12 次（约每周 3 次以上）"),
                  (None, "Can't recall", "不记得了")]),
    dict(qid="Q18b", section="external_ai", type="matrix_usefulness",
         text_en="For each activity category, rate how useful External AI was in your actual experience. Select N/A for categories you did not use it for.",
         text_zh="对每类活动，评价外部 AI 的实际有用程度；未使用选 N/A。",
         items=ACTIVITIES),
    dict(qid="Q19", section="comparison", type="matrix_comparison",
         text_en="For each activity category where you used both XJTLU AI and External AI in the past four weeks, which worked better in your actual experience? (Choose 'Unable to compare' where appropriate.)",
         text_zh="对每类同时用过两种 AI 的活动，实际体验中哪种更好？（不适用选「无法比较」）",
         items=ACTIVITIES[:-1] + [("overall", "Overall preference", "总体偏好")]),
    dict(qid="Q20", section="choice_improve", type="multi",
         text_en="Which factors matter most when choosing an AI tool for ADS401, or if you were to choose one? (Select up to 3.)",
         text_zh="为 ADS401 选择 AI 工具时（或假如要选），你最看重哪些因素？（多选，最多选 3 项）",
         items=[("task_relevance", "Task relevance", "任务相关性"),
                ("accuracy", "Accuracy or reliability", "准确或可靠"),
                ("ease", "Ease of use", "易用"),
                ("speed", "Speed", "速度"),
                ("familiarity", "Familiarity", "熟悉度"),
                ("suitable_features", "Suitable features", "功能合适"),
                ("accessibility", "Accessibility", "可及性"),
                ("chinese", "Chinese-language support", "中文支持"),
                ("quota", "Quota or cost", "配额或成本"),
                ("university_rec", "University recommendation", "学校推荐"),
                ("other", "Other (please specify)", "其他（请注明）")]),
    dict(qid="Q21", section="choice_improve", type="multi",
         text_en="In your opinion, which improvements should XJTLU AI prioritise for ADS401? (Select up to 3)",
         text_zh="你认为西浦 AI 应优先改进哪些方面？（多选，最多选 3 项）",
         items=[("accurate_answers", "More accurate course answers", "更准确的课程相关回答"),
                ("research_method", "Research-method support", "研究方法支持"),
                ("survey_design", "Survey/interview design support", "问卷/访谈设计支持"),
                ("doc_kb", "Document/knowledge-base support", "文档/知识库支持"),
                ("writing", "Writing/summaries/planning", "写作/摘要/规划"),
                ("navigation", "Clearer navigation", "更清晰的导航"),
                ("ads401_examples", "ADS401-specific examples", "ADS401 专用示例"),
                ("privacy_transparency", "Privacy/data transparency", "隐私/数据透明"),
                ("guidance", "Clear course-use guidance", "明确的课程使用指引"),
                ("other", "Other (please specify)", "其他（请注明）")]),
    dict(qid="Q22", section="choice_improve", type="text",
         text_en="Anything else you'd like to share about XJTLU AI or External AI for ADS401? (Optional; open text; no identifying information)",
         text_zh="关于西浦 AI 或外部 AI 在 ADS401 中的使用，你还有什么想分享的？（选填；请勿包含身份信息）",
         slug="open"),
    dict(qid="Q23", section="followup", type="single_nominal",
         text_en="Would you be willing to be contacted for an optional follow-up interview? If Yes, the final question will ask for a preferred name or pseudonym and a phone number or email address.",
         text_zh="是否愿意被联系参加后续的访谈？若是，最后一题将收集称呼或化名与手机号或邮箱。",
         slug="interview",
         options=[(None, "Yes", "是"),
                  (None, "No", "否")]),
    dict(qid="Q24", section="followup", type="text",
         text_en="Please leave your contact information (preferred name or pseudonym; phone number or email).",
         text_zh="请留下你的联系方式（称呼或化名；手机号或邮箱）。",
         items=[("name", "Preferred name or pseudonym", "称呼或化名"),
                ("contact", "Phone number or email", "手机号或邮箱")]),
]

# ----------------------------------------------------------------------------
# Column index maps per language (verified against the WJX export headers)
# ----------------------------------------------------------------------------
# value types in a map: "meta" | "single" | "multi_combined" | "multi_flag"
#                      | "multi_other_text" | "matrix" | "text"
# Each entry: col_index -> (qid, slot)
#   slot for matrix  = item slug
#   slot for multi_flag = item slug
#   slot for single/text = None (or 'name'/'contact' for Q24)
# ----------------------------------------------------------------------------
EN_COLS = {
    0: ("meta", "submission_id"), 1: ("meta", "respondent_id"), 2: ("meta", "submitted_at"),
    3: ("single", "Q1"), 4: ("single", "Q2"), 5: ("single", "Q3"), 6: ("single", "Q4"),
    7: ("single", "Q5"), 8: ("single", "Q6"), 9: ("single", "Q7"), 10: ("single", "Q8"),
    11: ("single", "Q9"), 12: ("single", "Q10"),
    13: ("multi_combined", "Q11"),
    14: ("multi_flag", ("Q11", "campus")), 15: ("multi_flag", ("Q11", "within")),
    16: ("multi_flag", ("Q11", "beyond")), 17: ("multi_flag", ("Q11", "policy")),
    18: ("multi_flag", ("Q11", "prod")), 19: ("multi_flag", ("Q11", "other")),
    20: ("multi_other_text", "Q11"),
    21: ("matrix", ("Q11a", "campus")), 22: ("matrix", ("Q11a", "within")),
    23: ("matrix", ("Q11a", "beyond")), 24: ("matrix", ("Q11a", "policy")),
    25: ("matrix", ("Q11a", "prod")), 26: ("matrix", ("Q11a", "other")),
    27: ("single", "Q12"),
    28: ("matrix", ("Q13", "pu1")), 29: ("matrix", ("Q13", "pu2")),
    30: ("matrix", ("Q13", "peou1")), 31: ("matrix", ("Q13", "peou2")),
    32: ("matrix", ("Q13", "trust1")), 33: ("matrix", ("Q13", "trust2")),
    34: ("multi_combined", "Q14"),
    35: ("multi_flag", ("Q14", "unclear_which")), 36: ("multi_flag", ("Q14", "hard_prompts")),
    37: ("multi_flag", ("Q14", "inaccurate")), 38: ("multi_flag", ("Q14", "not_relevant")),
    39: ("multi_flag", ("Q14", "time_consuming")), 40: ("multi_flag", ("Q14", "inconvenient")),
    41: ("multi_flag", ("Q14", "functions_insufficient")), 42: ("multi_flag", ("Q14", "uncertain_permission")),
    43: ("multi_flag", ("Q14", "privacy")), 44: ("multi_flag", ("Q14", "no_problem")),
    45: ("multi_flag", ("Q14", "other")),
    46: ("single", "Q15"),
    47: ("multi_combined", "Q16"),
    48: ("multi_flag", ("Q16", "previously_unaware")), 49: ("multi_flag", ("Q16", "unclear_what")),
    50: ("multi_flag", ("Q16", "unsure_access")), 51: ("multi_flag", ("Q16", "no_suitable_task")),
    52: ("multi_flag", ("Q16", "prefer_external")), 53: ("multi_flag", ("Q16", "prefer_nonai")),
    54: ("multi_flag", ("Q16", "concerned_inaccurate")), 55: ("multi_flag", ("Q16", "unsure_permitted")),
    56: ("multi_flag", ("Q16", "privacy")), 57: ("multi_flag", ("Q16", "past_unsatisfactory")),
    58: ("multi_flag", ("Q16", "access_inconvenient")), 59: ("multi_flag", ("Q16", "other")),
    60: ("single", "Q17"),
    61: ("single", "Q18a"),
    62: ("multi_combined", "Q18"),
    63: ("multi_flag", ("Q18", "campus")), 64: ("multi_flag", ("Q18", "within")),
    65: ("multi_flag", ("Q18", "beyond")), 66: ("multi_flag", ("Q18", "policy")),
    67: ("multi_flag", ("Q18", "prod")), 68: ("multi_flag", ("Q18", "other")),
    69: ("multi_other_text", "Q18"),
    70: ("matrix", ("Q18b", "campus")), 71: ("matrix", ("Q18b", "within")),
    72: ("matrix", ("Q18b", "beyond")), 73: ("matrix", ("Q18b", "policy")),
    74: ("matrix", ("Q18b", "prod")), 75: ("matrix", ("Q18b", "other")),
    76: ("matrix", ("Q19", "campus")), 77: ("matrix", ("Q19", "within")),
    78: ("matrix", ("Q19", "beyond")), 79: ("matrix", ("Q19", "policy")),
    80: ("matrix", ("Q19", "prod")), 81: ("matrix", ("Q19", "other")),
    82: ("matrix", ("Q19", "overall")),
    83: ("multi_combined", "Q20"),
    84: ("multi_flag", ("Q20", "task_relevance")), 85: ("multi_flag", ("Q20", "accuracy")),
    86: ("multi_flag", ("Q20", "ease")), 87: ("multi_flag", ("Q20", "speed")),
    88: ("multi_flag", ("Q20", "familiarity")), 89: ("multi_flag", ("Q20", "suitable_features")),
    90: ("multi_flag", ("Q20", "accessibility")), 91: ("multi_flag", ("Q20", "chinese")),
    92: ("multi_flag", ("Q20", "quota")), 93: ("multi_flag", ("Q20", "university_rec")),
    94: ("multi_flag", ("Q20", "other")),
    95: ("multi_combined", "Q21"),
    96: ("multi_flag", ("Q21", "accurate_answers")), 97: ("multi_flag", ("Q21", "research_method")),
    98: ("multi_flag", ("Q21", "survey_design")), 99: ("multi_flag", ("Q21", "doc_kb")),
    100: ("multi_flag", ("Q21", "writing")), 101: ("multi_flag", ("Q21", "navigation")),
    102: ("multi_flag", ("Q21", "ads401_examples")), 103: ("multi_flag", ("Q21", "privacy_transparency")),
    104: ("multi_flag", ("Q21", "guidance")), 105: ("multi_flag", ("Q21", "other")),
    106: ("text", ("Q22", None)), 107: ("single", "Q23"),
    108: ("text", ("Q24", "name")), 109: ("text", ("Q24", "contact")),
}
# ZH has two extra duplicate '其他' boolean columns for Q11 and Q18 (WJX export quirk).
ZH_COLS = {
    0: ("meta", "submission_id"), 1: ("meta", "respondent_id"), 2: ("meta", "submitted_at"),
    3: ("single", "Q1"), 4: ("single", "Q2"), 5: ("single", "Q3"), 6: ("single", "Q4"),
    7: ("single", "Q5"), 8: ("single", "Q6"), 9: ("single", "Q7"), 10: ("single", "Q8"),
    11: ("single", "Q9"), 12: ("single", "Q10"),
    13: ("multi_combined", "Q11"),
    14: ("multi_flag", ("Q11", "campus")), 15: ("multi_flag", ("Q11", "within")),
    16: ("multi_flag", ("Q11", "beyond")), 17: ("multi_flag", ("Q11", "policy")),
    18: ("multi_flag", ("Q11", "prod")), 19: ("multi_flag", ("Q11", "other")),
    20: ("multi_flag_dup", ("Q11", "other")),
    21: ("multi_other_text", "Q11"),
    22: ("matrix", ("Q11a", "campus")), 23: ("matrix", ("Q11a", "within")),
    24: ("matrix", ("Q11a", "beyond")), 25: ("matrix", ("Q11a", "policy")),
    26: ("matrix", ("Q11a", "prod")), 27: ("matrix", ("Q11a", "other")),
    28: ("single", "Q12"),
    29: ("matrix", ("Q13", "pu1")), 30: ("matrix", ("Q13", "pu2")),
    31: ("matrix", ("Q13", "peou1")), 32: ("matrix", ("Q13", "peou2")),
    33: ("matrix", ("Q13", "trust1")), 34: ("matrix", ("Q13", "trust2")),
    35: ("multi_combined", "Q14"),
    36: ("multi_flag", ("Q14", "unclear_which")), 37: ("multi_flag", ("Q14", "hard_prompts")),
    38: ("multi_flag", ("Q14", "inaccurate")), 39: ("multi_flag", ("Q14", "not_relevant")),
    40: ("multi_flag", ("Q14", "time_consuming")), 41: ("multi_flag", ("Q14", "inconvenient")),
    42: ("multi_flag", ("Q14", "functions_insufficient")), 43: ("multi_flag", ("Q14", "uncertain_permission")),
    44: ("multi_flag", ("Q14", "privacy")), 45: ("multi_flag", ("Q14", "no_problem")),
    46: ("multi_flag", ("Q14", "other")),
    47: ("single", "Q15"),
    48: ("multi_combined", "Q16"),
    49: ("multi_flag", ("Q16", "previously_unaware")), 50: ("multi_flag", ("Q16", "unclear_what")),
    51: ("multi_flag", ("Q16", "unsure_access")), 52: ("multi_flag", ("Q16", "no_suitable_task")),
    53: ("multi_flag", ("Q16", "prefer_external")), 54: ("multi_flag", ("Q16", "prefer_nonai")),
    55: ("multi_flag", ("Q16", "concerned_inaccurate")), 56: ("multi_flag", ("Q16", "unsure_permitted")),
    57: ("multi_flag", ("Q16", "privacy")), 58: ("multi_flag", ("Q16", "past_unsatisfactory")),
    59: ("multi_flag", ("Q16", "access_inconvenient")), 60: ("multi_flag", ("Q16", "other")),
    61: ("single", "Q17"),
    62: ("single", "Q18a"),
    63: ("multi_combined", "Q18"),
    64: ("multi_flag", ("Q18", "campus")), 65: ("multi_flag", ("Q18", "within")),
    66: ("multi_flag", ("Q18", "beyond")), 67: ("multi_flag", ("Q18", "policy")),
    68: ("multi_flag", ("Q18", "prod")), 69: ("multi_flag", ("Q18", "other")),
    70: ("multi_flag_dup", ("Q18", "other")),
    71: ("multi_other_text", "Q18"),
    72: ("matrix", ("Q18b", "campus")), 73: ("matrix", ("Q18b", "within")),
    74: ("matrix", ("Q18b", "beyond")), 75: ("matrix", ("Q18b", "policy")),
    76: ("matrix", ("Q18b", "prod")), 77: ("matrix", ("Q18b", "other")),
    78: ("matrix", ("Q19", "campus")), 79: ("matrix", ("Q19", "within")),
    80: ("matrix", ("Q19", "beyond")), 81: ("matrix", ("Q19", "policy")),
    82: ("matrix", ("Q19", "prod")), 83: ("matrix", ("Q19", "other")),
    84: ("matrix", ("Q19", "overall")),
    85: ("multi_combined", "Q20"),
    86: ("multi_flag", ("Q20", "task_relevance")), 87: ("multi_flag", ("Q20", "accuracy")),
    88: ("multi_flag", ("Q20", "ease")), 89: ("multi_flag", ("Q20", "speed")),
    90: ("multi_flag", ("Q20", "familiarity")), 91: ("multi_flag", ("Q20", "suitable_features")),
    92: ("multi_flag", ("Q20", "accessibility")), 93: ("multi_flag", ("Q20", "chinese")),
    94: ("multi_flag", ("Q20", "quota")), 95: ("multi_flag", ("Q20", "university_rec")),
    96: ("multi_flag", ("Q20", "other")),
    97: ("multi_combined", "Q21"),
    98: ("multi_flag", ("Q21", "accurate_answers")), 99: ("multi_flag", ("Q21", "research_method")),
    100: ("multi_flag", ("Q21", "survey_design")), 101: ("multi_flag", ("Q21", "doc_kb")),
    102: ("multi_flag", ("Q21", "writing")), 103: ("multi_flag", ("Q21", "navigation")),
    104: ("multi_flag", ("Q21", "ads401_examples")), 105: ("multi_flag", ("Q21", "privacy_transparency")),
    106: ("multi_flag", ("Q21", "guidance")), 107: ("multi_flag", ("Q21", "other")),
    108: ("text", ("Q22", None)), 109: ("single", "Q23"),
    110: ("text", ("Q24", "name")), 111: ("text", ("Q24", "contact")),
}

# ----------------------------------------------------------------------------
# Build label -> (canonical_en, code) lookup tables
# ----------------------------------------------------------------------------
QBYID = {q["qid"]: q for q in QUESTIONS}

def scale_label_map(scale, na_label):
    m = {}
    for code, en, zh in scale:
        m[en] = (en, code)
        m[zh] = (en, code)
    if na_label:
        en_na, zh_na = na_label
        m[en_na] = (en_na, None)
        m[zh_na] = (en_na, None)
    return m

LABEL_MAP = {}
for q in QUESTIONS:
    qid = q["qid"]
    if q["type"] == "matrix_agreement":
        LABEL_MAP[qid] = scale_label_map(SCALE_AGREEMENT, NA_AGREEMENT)
    elif q["type"] == "matrix_usefulness":
        LABEL_MAP[qid] = scale_label_map(SCALE_USEFULNESS, NA_USEFULNESS)
    elif q["type"] == "matrix_comparison":
        LABEL_MAP[qid] = scale_label_map(SCALE_COMPARISON, NA_COMPARISON)
    elif q["type"] in ("single_nominal", "single_ordinal"):
        m = {}
        for code, en, zh in q["options"]:
            m[en] = (en, code)
            m[zh] = (en, code)
        LABEL_MAP[qid] = m

# item slug -> (en, zh)
ITEM_TEXT = {}
for q in QUESTIONS:
    if q["type"] in ("multi", "matrix_agreement", "matrix_usefulness",
                     "matrix_comparison", "text"):
        for slug, en, zh in q.get("items", []):
            ITEM_TEXT[(q["qid"], slug)] = (en, zh)

def item_text(qid, slug):
    t = ITEM_TEXT.get((qid, slug))
    if t:
        return t
    return ("", "")

# ----------------------------------------------------------------------------
# Read source files
# ----------------------------------------------------------------------------
def read_rows(path):
    with open(path, encoding="utf-8-sig", newline="") as f:
        r = csv.reader(f)
        header = next(r)
        rows = [row for row in r if any(c.strip() != "" for c in row)]
    return header, rows

en_header, en_rows = read_rows(SRC_EN)
zh_header, zh_rows = read_rows(SRC_ZH)

def get(row, idx):
    if idx < len(row):
        return row[idx].strip()
    return ""

# ----------------------------------------------------------------------------
# Branch logic
# ----------------------------------------------------------------------------
def q9_group(q9_en):
    # returns one of: both / xjtu_only / external_only / neither
    if q9_en == "Both XJTLU AI and External AI":
        return "both"
    if q9_en == "XJTLU AI only (no External AI)":
        return "xjtu_only"
    if q9_en == "External AI only (no XJTLU AI)":
        return "external_only"
    return "neither"

def extract_other_text(combined, items, flags):
    """Recover a free-text 'Other' answer from the combined multi-select cell by
    removing the full labels of the options known to be selected."""
    s = combined or ""
    for slug, en, zh in items:
        if slug == "other":
            continue
        if flags.get(slug) == "true":
            for lab in (en, zh):
                s = s.replace(lab, "")
    s = re.sub(r"^\s*[,，、\s]+\s*", "", s)
    s = re.sub(r"\s*[,，、\s]+\s*$", "", s)
    s = re.sub(r"\s*[,，、]+\s*", " ", s).strip()
    return s

def question_active(qid, q9_en, q7_en, q23_en):
    if qid == "Q8":
        return q7_en != "Had not heard of them"
    if qid in ("Q10", "Q11", "Q11a", "Q12", "Q13", "Q14", "Q15"):
        return q9_group(q9_en) in ("both", "xjtu_only")
    if qid in ("Q16", "Q17"):
        return q9_group(q9_en) in ("external_only", "neither")
    if qid in ("Q18", "Q18a", "Q18b"):
        return q9_group(q9_en) in ("both", "external_only")
    if qid == "Q19":
        return q9_group(q9_en) == "both"
    if qid == "Q24":
        return q23_en == "Yes"
    return True  # Q1..Q7, Q9, Q20, Q21, Q22, Q23 always active (for consenters)

# ----------------------------------------------------------------------------
# Build long + wide records
# ----------------------------------------------------------------------------
LONG_FIELDS = ["survey_language", "submission_id", "respondent_id", "submitted_at",
               "question_id", "section", "question_text_en", "question_text_zh",
               "item_id", "item_text_en", "item_text_zh",
               "response_type", "response", "response_raw", "response_code", "selected"]

def base_meta(lang, row, cols):
    return {
        "survey_language": lang,
        "submission_id": get(row, [i for i, v in cols.items() if v == ("meta", "submission_id")][0]),
        "respondent_id": get(row, [i for i, v in cols.items() if v == ("meta", "respondent_id")][0]),
        "submitted_at": get(row, [i for i, v in cols.items() if v == ("meta", "submitted_at")][0]),
    }

long_rows = []
wide_rows = []
anomalies = []
unmatched_labels = set()

for lang, rows, cols in [("EN", en_rows, EN_COLS), ("ZH", zh_rows, ZH_COLS)]:
    for r_i, row in enumerate(rows):
        meta = base_meta(lang, row, cols)

        # collect raw cells per question
        raw = {}          # qid -> value (for single/text)
        matrix = {}       # (qid, slug) -> value
        multi_flags = {}  # (qid, slug) -> 'true'/'false'/''
        multi_other_text = {}  # qid -> text
        multi_combined = {}    # qid -> combined text

        for idx, spec in cols.items():
            val = get(row, idx)
            kind = spec[0]
            if kind == "single":
                raw[spec[1]] = val
            elif kind == "text":
                qid, slot = spec[1]
                raw[(qid, slot)] = val
            elif kind == "matrix":
                qid, slot = spec[1]
                matrix[(qid, slot)] = val
            elif kind == "multi_flag":
                qid, slot = spec[1]
                multi_flags[(qid, slot)] = val
            elif kind == "multi_flag_dup":
                qid, slot = spec[1]
                if multi_flags.get((qid, slot)) in ("", None):
                    multi_flags[(qid, slot)] = val
                elif val == "true" and multi_flags.get((qid, slot)) != "true":
                    multi_flags[(qid, slot)] = "true"
            elif kind == "multi_other_text":
                multi_other_text[spec[1]] = val
            elif kind == "multi_combined":
                multi_combined[spec[1]] = val

        # canonical key answers needed for branch logic
        q7_en = LABEL_MAP["Q7"].get(raw.get("Q7", ""), ("", None))[0]
        q9_en = LABEL_MAP["Q9"].get(raw.get("Q9", ""), ("", None))[0]
        q23_en = LABEL_MAP["Q23"].get(raw.get("Q23", ""), ("", None))[0]

        # resolve 'Other' free-text for each multi question (dedicated column
        # first, then fall back to extracting it from the combined cell)
        other_text = {}
        for q in QUESTIONS:
            if q["type"] != "multi":
                continue
            qid = q["qid"]
            ot = multi_other_text.get(qid, "")
            if (not ot) or ot.lower() in ("false", "true"):
                if multi_flags.get((qid, "other")) == "true":
                    ot = extract_other_text(multi_combined.get(qid, ""), q["items"], multi_flags)
            other_text[qid] = ot.strip() if (ot and ot.lower() not in ("false", "true")) else ""

        # ---- wide record ----
        wide = dict(meta)
        for q in QUESTIONS:
            qid = q["qid"]
            slug = q.get("slug")
            active = question_active(qid, q9_en, q7_en, q23_en)
            if q["type"] in ("single_nominal", "single_ordinal"):
                rv = raw.get(qid, "")
                if active and rv:
                    canon, code = LABEL_MAP[qid].get(rv, (rv, None))
                    if q["type"] == "single_ordinal":
                        wide[f"{qid.lower()}_{slug}"] = code if code is not None else ""
                    else:
                        wide[f"{qid.lower()}_{slug}"] = canon
                else:
                    wide[f"{qid.lower()}_{slug}"] = ""
            elif q["type"] in ("multi",):
                for s, _, _ in q["items"]:
                    flag = multi_flags.get((qid, s), "")
                    if active:
                        wide[f"{qid.lower()}_{s}"] = 1 if flag == "true" else (0 if flag == "false" else "")
                    else:
                        wide[f"{qid.lower()}_{s}"] = ""
                # other text
                ot = other_text.get(qid, "")
                wide[f"{qid.lower()}_other_text"] = ot
            elif q["type"] in ("matrix_agreement", "matrix_usefulness", "matrix_comparison"):
                for s, _, _ in q["items"]:
                    v = matrix.get((qid, s), "")
                    if active and v:
                        canon, code = LABEL_MAP[qid].get(v, (v, None))
                        wide[f"{qid.lower()}_{s}"] = code if code is not None else ""
                    else:
                        wide[f"{qid.lower()}_{s}"] = ""
            elif q["type"] == "text":
                if qid == "Q24":
                    for s, _, _ in q["items"]:
                        v = raw.get((qid, s), "")
                        wide[f"q24_{s}"] = v if active else ""
                else:
                    wide["q22_open"] = raw.get(("Q22", None), "")
        wide_rows.append(wide)

        # ---- long records ----
        for q in QUESTIONS:
            qid = q["qid"]
            active = question_active(qid, q9_en, q7_en, q23_en)
            qt = q["type"]
            base = dict(meta)
            base.update(question_id=qid, section=q["section"],
                        question_text_en=q["text_en"], question_text_zh=q["text_zh"])

            if qt in ("single_nominal", "single_ordinal"):
                rv = raw.get(qid, "")
                if active and rv:
                    if rv not in LABEL_MAP[qid]:
                        unmatched_labels.add((qid, rv))
                    canon, code = LABEL_MAP[qid].get(rv, (rv, None))
                    rec = dict(base)
                    rec.update(item_id="", item_text_en="", item_text_zh="",
                               response_type=qt, response=canon, response_raw=rv,
                               response_code=code if code is not None else "",
                               selected="")
                    long_rows.append(rec)
            elif qt == "multi":
                if not active:
                    continue
                flags = {s: multi_flags.get((qid, s), "") for s, _, _ in q["items"]}
                # detect mismatches between combined text and flags (light validation)
                for s, en, zh in q["items"]:
                    flag = flags.get(s, "")
                    if flag not in ("true", "false"):
                        anomalies.append((lang, meta["submission_id"], qid, s, f"flag='{flag}'"))
                    rec = dict(base)
                    rec.update(item_id=s, item_text_en=en, item_text_zh=zh,
                               response_type="multi", response=en, response_raw=flag,
                               response_code="", selected=(1 if flag == "true" else 0))
                    long_rows.append(rec)
                # 'other' free text (if provided)
                ot = other_text.get(qid, "")
                if ot:
                    rec = dict(base)
                    rec.update(item_id="other_text", item_text_en="Other (free text)",
                               item_text_zh="其他（自由文本）", response_type="multi",
                               response=ot, response_raw=ot, response_code="", selected="")
                    long_rows.append(rec)
            elif qt in ("matrix_agreement", "matrix_usefulness", "matrix_comparison"):
                if not active:
                    continue
                for s, en, zh in q["items"]:
                    v = matrix.get((qid, s), "")
                    if v == "":
                        continue
                    if v not in LABEL_MAP[qid]:
                        unmatched_labels.add((qid, v))
                    canon, code = LABEL_MAP[qid].get(v, (v, None))
                    rec = dict(base)
                    rec.update(item_id=s, item_text_en=en, item_text_zh=zh,
                               response_type=qt, response=canon, response_raw=v,
                               response_code=code if code is not None else "",
                               selected="")
                    long_rows.append(rec)
            elif qt == "text":
                if qid == "Q24":
                    if not active:
                        continue
                    for s, en, zh in q["items"]:
                        v = raw.get((qid, s), "")
                        if v == "":
                            continue
                        rec = dict(base)
                        rec.update(item_id=s, item_text_en=en, item_text_zh=zh,
                                   response_type="text", response=v, response_raw=v,
                                   response_code="", selected="")
                        long_rows.append(rec)
                else:
                    v = raw.get(("Q22", None), "")
                    if v == "":
                        continue
                    rec = dict(base)
                    rec.update(item_id="", item_text_en="", item_text_zh="",
                               response_type="text", response=v, response_raw=v,
                               response_code="", selected="")
                    long_rows.append(rec)

# ----------------------------------------------------------------------------
# Codebook
# ----------------------------------------------------------------------------
CODEBOOK_FIELDS = ["question_id", "section", "question_type", "question_text_en",
                   "question_text_zh", "item_id", "item_text_en", "item_text_zh",
                   "option_code", "option_label_en", "option_label_zh"]
codebook = []
for q in QUESTIONS:
    qid = q["qid"]
    qt = q["type"]
    if qt in ("single_nominal", "single_ordinal"):
        for code, en, zh in q["options"]:
            codebook.append(dict(question_id=qid, section=q["section"], question_type=qt,
                                 question_text_en=q["text_en"], question_text_zh=q["text_zh"],
                                 item_id="", item_text_en="", item_text_zh="",
                                 option_code=(code if code is not None else ""),
                                 option_label_en=en, option_label_zh=zh))
    elif qt == "multi":
        for s, en, zh in q["items"]:
            codebook.append(dict(question_id=qid, section=q["section"], question_type=qt,
                                 question_text_en=q["text_en"], question_text_zh=q["text_zh"],
                                 item_id=s, item_text_en=en, item_text_zh=zh,
                                 option_code="", option_label_en=en, option_label_zh=zh))
    elif qt == "matrix_agreement":
        scale, na = SCALE_AGREEMENT, NA_AGREEMENT
        for s, en, zh in q["items"]:
            for code, o_en, o_zh in scale:
                codebook.append(dict(question_id=qid, section=q["section"], question_type=qt,
                                     question_text_en=q["text_en"], question_text_zh=q["text_zh"],
                                     item_id=s, item_text_en=en, item_text_zh=zh,
                                     option_code=code, option_label_en=o_en, option_label_zh=o_zh))
            codebook.append(dict(question_id=qid, section=q["section"], question_type=qt,
                                 question_text_en=q["text_en"], question_text_zh=q["text_zh"],
                                 item_id=s, item_text_en=en, item_text_zh=zh,
                                 option_code="", option_label_en=na[0], option_label_zh=na[1]))
    elif qt == "matrix_usefulness":
        scale, na = SCALE_USEFULNESS, NA_USEFULNESS
        for s, en, zh in q["items"]:
            for code, o_en, o_zh in scale:
                codebook.append(dict(question_id=qid, section=q["section"], question_type=qt,
                                     question_text_en=q["text_en"], question_text_zh=q["text_zh"],
                                     item_id=s, item_text_en=en, item_text_zh=zh,
                                     option_code=code, option_label_en=o_en, option_label_zh=o_zh))
            codebook.append(dict(question_id=qid, section=q["section"], question_type=qt,
                                 question_text_en=q["text_en"], question_text_zh=q["text_zh"],
                                 item_id=s, item_text_en=en, item_text_zh=zh,
                                 option_code="", option_label_en=na[0], option_label_zh=na[1]))
    elif qt == "matrix_comparison":
        scale, na = SCALE_COMPARISON, NA_COMPARISON
        for s, en, zh in q["items"]:
            for code, o_en, o_zh in scale:
                codebook.append(dict(question_id=qid, section=q["section"], question_type=qt,
                                     question_text_en=q["text_en"], question_text_zh=q["text_zh"],
                                     item_id=s, item_text_en=en, item_text_zh=zh,
                                     option_code=code, option_label_en=o_en, option_label_zh=o_zh))
            codebook.append(dict(question_id=qid, section=q["section"], question_type=qt,
                                 question_text_en=q["text_en"], question_text_zh=q["text_zh"],
                                 item_id=s, item_text_en=en, item_text_zh=zh,
                                 option_code="", option_label_en=na[0], option_label_zh=na[1]))
    elif qt == "text":
        items = q.get("items", [(None, "", "")])
        for s, en, zh in items:
            codebook.append(dict(question_id=qid, section=q["section"], question_type=qt,
                                 question_text_en=q["text_en"], question_text_zh=q["text_zh"],
                                 item_id=(s or ""), item_text_en=en, item_text_zh=zh,
                                 option_code="", option_label_en="", option_label_zh=""))

# ----------------------------------------------------------------------------
# Write outputs
# ----------------------------------------------------------------------------
def write_csv(path, fields, rows):
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow({k: ("" if r.get(k) is None else r.get(k)) for k in fields})

write_csv(os.path.join(BASE, "survey_long.csv"), LONG_FIELDS, long_rows)
write_csv(os.path.join(BASE, "survey_codebook.csv"), CODEBOOK_FIELDS, codebook)

# wide: field order = meta + question columns in questionnaire order
wide_fields = ["survey_language", "submission_id", "respondent_id", "submitted_at"]
for q in QUESTIONS:
    qid = q["qid"].lower()
    if q["type"] in ("single_nominal", "single_ordinal"):
        wide_fields.append(f"{qid}_{q['slug']}")
    elif q["type"] == "multi":
        for s, _, _ in q["items"]:
            wide_fields.append(f"{qid}_{s}")
        wide_fields.append(f"{qid}_other_text")
    elif q["type"] in ("matrix_agreement", "matrix_usefulness", "matrix_comparison"):
        for s, _, _ in q["items"]:
            wide_fields.append(f"{qid}_{s}")
    elif q["type"] == "text":
        if qid == "q24":
            for s, _, _ in q["items"]:
                wide_fields.append(f"{qid}_{s}")
        else:
            wide_fields.append("q22_open")
write_csv(os.path.join(BASE, "survey_wide.csv"), wide_fields, wide_rows)

# ----------------------------------------------------------------------------
# Report
# ----------------------------------------------------------------------------
print("=== SUMMARY ===")
print(f"EN respondents: {len(en_rows)}")
print(f"ZH respondents: {len(zh_rows)}")
print(f"Total submissions: {len(en_rows) + len(zh_rows)}")
print(f"Unique respondent IDs: {len(set([r[1] for r in en_rows] + [r[1] for r in zh_rows]))}")
print(f"Long rows: {len(long_rows)}")
print(f"Wide rows: {len(wide_rows)}")
print(f"Wide columns: {len(wide_fields)}")
print(f"Codebook rows: {len(codebook)}")

# shared respondent id check
en_ids = [r[1] for r in en_rows]
zh_ids = [r[1] for r in zh_rows]
shared = set(en_ids) & set(zh_ids)
print(f"\nRespondent IDs appearing in BOTH EN and ZH: {sorted(shared)}")

print("\n=== ANOMALIES (multi flags not true/false) ===")
if anomalies:
    for a in anomalies:
        print(a)
else:
    print("none")

print("\n=== UNMATCHED LABELS (kept as-is, not coded) ===")
if unmatched_labels:
    for u in sorted(unmatched_labels):
        print(u)
else:
    print("none")

print("\nOutput written to:", BASE)
