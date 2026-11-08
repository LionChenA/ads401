# pre3/data — 问卷 + 访谈数据目录

ADS401「学生对 XJTLU AI 的认知、采纳与使用」研究的数据资产，按**问卷数据**与**访谈数据**两类归类整理。

## 目录结构

```
data/
├── survey/                     # 问卷数据（QUAN）
│   ├── raw/                    #   问卷导出（已去标识化：删除 Respondent ID 与 Q24 联系方式列）
│   │   ├── ADS401 Students…_Submissions_2026-11-07.csv          # 英文问卷（23 条，最新）
│   │   ├── ADS401 学生…_Submissions_2026-11-07(1).csv           # 中文问卷（4 条，最新）
│   │   └── archive/            #   旧版子集导出（已并入最新，勿重复计入）
│   ├── processed/              #   重构/汇总后的分析就绪数据
│   │   ├── survey_long.csv     #     tidy 长表（题目×条目，Likert 数值编码）
│   │   ├── survey_wide.csv     #     宽表（一行一名受访者）
│   │   ├── survey_codebook.csv #     数据字典（题目/条目/选项↔编码）
│   │   ├── summary_*.csv       #     频数/百分比/Likert 分布/构念/采纳漏斗
│   │   ├── summary.json        #     描述性统计 JSON
│   │   └── results.json        #     描述 + 推断检验 JSON（Wilson CI / Spearman / Wilcoxon / 符号检验 / Mann-Whitney）
│   └── scripts/                #   数据处理脚本（可复现）
│       ├── build.py            #     原始 CSV → tidy/wide/codebook
│       ├── summarize.py        #     tidy → 汇总 CSV/JSON
│       └── analysis.py         #     推断统计 + results.json
└── interview/                  # 访谈数据（QUAL）
    ├── transcripts/            #   逐字稿（P00x_refined.md + _en.md，中英对照）
    ├── field_notes/            #   现场速记（P001–P007）
    ├── synthesis/              #   访谈合成 + 主持指南
    │   ├── interview_guide_v2.md
    │   ├── interview_synthesis.md        # P001–P004
    │   ├── interview_synthesis_en.md
    │   └── interview_synthesis_all.md    # P005–P007 补充（_all）
    ├── coded/                  #   编码产物
    │   ├── 00_codebook.md      #     25 个编码 ↔ RQ ↔ 问卷题
    │   ├── P00x_coded.md       #     逐受访者双语编码记录（EN 一段 + CN 一段）
    │   └── conclusions.md      #     问卷×访谈三角验证的 7 条真实结论
    └── derived/                #   结构化访谈数据
        └── interview_data.json #     供 result-3.html 访谈可视化的 JSON
```

## 关键口径

- **样本规模**：有效提交 **27** 条 = 英文 23 + 中文 4；**唯一受访者 26 人**（见下）。
- **跨语言重复**：`respondent_id = 44M6z7O` 同时出现在英文（`Dq622ob`）与中文（`yX5Oy5d`）两份问卷，背景四要素（专业方向/性别/年龄/AI 经验）一致，判定为**同一设备/同一人双份作答**（部分选项有漂移：Q3 专业、Q7 熟悉度、Q17 意愿方向、Q23 访谈意愿相反）。按独立受访者统计用 **n=26**。
- **P001–P004 与 P005–P007 口径**：P001–P004 沿用旧访谈方案（行为模式/核查税/生态挤压框架），仅保留映射到问卷构念的内容；P005–P007 按问卷与已知 RQ 设计，为主要佐证。
- **统计均为探索性**：小样本 + 横断面 + 自我报告 → 仅供课程研究，不可外推、不作因果。
