# Survey Deployment Record — ADS401 Group A

Deployment records for the ADS401 questionnaire across platforms.

## Official Primary Deployment (Tally — English)

| Platform | Form ID | Fill URL | Architecture | Status |
|---|---|---|---|---|
| **Tally (EN)** | `xVXO6r` | **https://tally.so/r/xVXO6r** | 9-Page Streamlined Flow | **PUBLISHED** |

- Verified 27-question instrument with native inline Other inputs, presence-linked evaluation matrices, and ethics information sheet integration.
- Full technical specification, validation logs, and audit records: see [`../TALLY_MIGRATION.md`](../TALLY_MIGRATION.md).

---

## Secondary / Prototype Platform (WJX / 问卷星 — 未启用)

> **注**：问卷星方案仅作为早期测试与技术预研，**未启用、未投放**。全量正式调查统一通过上方 Tally 官方英文部署执行。

### 归档测试链接（未启用）

| Version | vid | sid | Fill URL | Preview / Testing URL |
|---|---|---|---|---|
| **English (EN)** | `390558834` | `r1EXPZE` | https://v.wjx.cn/vm/r1EXPZE.aspx | https://www.wjx.cn/wjx/design/previewmobile.aspx?activity=390558834 |
| **Chinese (CN)** | `390558808` | `exccUo8` | https://v.wjx.cn/vm/exccUo8.aspx | https://www.wjx.cn/wjx/design/previewmobile.aspx?activity=390558808 |

Both deployments share the identical 5-page, 27-question structure for 1-to-1 column-aligned merging.

## 5-Page Modular Architecture (Scheme A)

```text
Page 1: Information Sheet + Q1 (Consent)
        └─ If No: Next Page -> Submits and ends survey immediately.
        └─ If Yes: Next Page -> Enters Page 2.

Page 2: Eligibility & Background (Q2..Q6)
        └─ Q2 (degree prefixes unified), Q3 (prior field), Q4 (gender), Q5 (age), Q6 (AI experience).

Page 3: Awareness, Ever-use & Branching Hub (Q7..Q9)
        └─ Q7 (familiarity), Q8 (ever-used), Q9 (past-4-week usage category).
        └─ Q9 natural gradient: 1=Both, 2=XJTLU only, 3=External only, 4=Neither.
        └─ Clicking "Next Page" seamlessly enters Page 4 customized to the Q9 choice!

Page 4: Usage / Non-use / Comparison Modules (conditioned on Q9)
        ├─ Both (Opt 1): Q10–Q15 (XJTLU), Q18–Q18b (External), Q19 (Comparison).
        ├─ XJTLU Only (Opt 2): Q10–Q15.
        ├─ External Only (Opt 3): Q16–Q17 (Non-use), Q18–Q18b (External).
        └─ Neither (Opt 4): Q16–Q17 (Non-use).

Page 5: Convergence, Feedback & Interview (Q20..Q24)
        ├─ Q20 (Tool choice factors, max 3), Q21 (Improvements, max 3), Q22 (Open feedback).
        ├─ Q23: Interview invitation. If Yes -> Q24 contact details revealed; if No -> submits.
```

## Configured & Verified Behaviors

1. **Other Formatting Unified Across All Questions**:
   - Q2: `Other (please specify) ______` / `其他（请注明）______` (fill-in enabled)
   - Q3: `Other (please specify) ______` / `其他（请注明）______` (fill-in enabled)
   - Q11: `Other (please specify) ______` / `其他（请注明）______` (fill-in enabled)
   - Q14: `Other (please specify) ______` / `其他（请注明）______` (fill-in enabled)
   - Q16: `Other (please specify) ______` / `其他（请注明）______` (fill-in enabled)
   - Q18: `Other (please specify; if same as Q11, state 'Same as Q11') ______` / `其他（请注明；若与 Q11 相同可填“同 Q11”）______` (fill-in enabled)
   - Q20: `Other (please specify) ______` / `其他（请注明）______` (fill-in enabled)
   - Q21: `Other (please specify) ______` / `其他（请注明）______` (fill-in enabled)
2. **Matrix Row Labels (A–F Removed)**:
   - Q11a, Q18b, Q19: Pure category labels without letters.
   - Q11a row: `Other activity (as specified in Q11)`
   - Q18b row: `Other activity (as specified in Q18)`
   - Q19 row: `Other activity (if applicable)`
3. **Q14 Mutual Exclusion**:
   - `No notable problem` / `无明显问题` has mutual exclusion enabled (`_item_huchi = true`); selecting it automatically unchecks any other selected problems.
4. **Multi-Select Limits**:
   - Maximum 3 choices strictly enforced on Q14, Q16, Q20, Q21 (`_upLimit = "3"`).
