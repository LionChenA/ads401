# WJX (问卷星) Deployment — Questionnaire v2.2 (EN & CN)

Deployment record for the ADS401 questionnaire. Created 2026-10-24 via official
`wjx-cli` 0.4.5 (github.com/wjxcom/wjx-ai-kit) and browser automation.

## Deployed Artifacts (Dual Links)

| Version | vid | sid | Fill URL | Preview URL |
|---|---|---|---|---|
| **English (EN)** | `390547306` | `tSGG1Ra` | https://v.wjx.cn/vm/tSGG1Ra.aspx | https://www.wjx.cn/wjx/design/previewmobile.aspx?activity=390547306 |
| **Chinese (CN)** | `390561536` | `tAJGG7l` | https://v.wjx.cn/vm/tAJGG7l.aspx | https://www.wjx.cn/wjx/design/previewmobile.aspx?activity=390561536 |

Both deployments share the identical 27-question structure for 1-to-1 column-aligned merging.

## Configured Logic & Behaviors (Verified in Live Preview)

1. **Page 1 Isolation (Consent)**:
   - Page 1 contains only the Information Sheet (Intro) and Q1 (Consent).
   - If Q1 = No: Jumps immediately to end of survey on clicking "Next Page" (never sees Page 2).
   - If Q1 = Yes: Advances to Page 2 (Q2..Q27).
2. **Q9 Natural Gradient & 4-Way Branching**:
   - Option 1: Both XJTLU AI and External AI
   - Option 2: XJTLU AI only (no External AI)
   - Option 3: External AI only (no XJTLU AI)
   - Option 4: Neither XJTLU AI nor External AI (at bottom)
   - *Branching Rules*:
     - Q10–Q16 (XJTLU AI usage & TAM): Shown if Q9 = Option 1 OR Option 2 (`9,1;2`)
     - Q17–Q18 (Non-use reasons & intent): Shown if Q9 = Option 3 OR Option 4 (`9,3;4`)
     - Q19–Q21 (External AI usage & usefulness): Shown if Q9 = Option 1 OR Option 3 (`9,1;3`)
     - Q22 (Tool comparison matrix): Shown ONLY if Q9 = Option 1 (`9,1`)
3. **Multi-Select Limits**:
   - Q14 (Problems), Q16 (Non-use reasons), Q20 (Choice factors), Q21 (Improvement priorities) enforced at maximum 3 choices (`_upLimit = "3"`).
4. **Mutual Exclusion**:
   - Q14 Option 10 ("No notable problem") has mutual exclusion enabled (`_item_huchi = true`); selecting it automatically unchecks any other selected options.
5. **Other Fill-in Boxes**:
   - Q2 Option 4 ("Other: please state your programme ______"): text fill-in active.
   - Q11 Option 6 ("Other (please specify) ______"): text fill-in active.
   - Q18 Option 6 ("Other (please specify; if same as Q11, state 'Same as Q11') ______"): text fill-in active.
6. **Matrix Rows**:
   - Q11a, Q18b, Q19: All A–F letter prefixes removed; clean category labels. Q19 row: `Other activity (if applicable)`.
7. **Q23 & Q24 Interview Opt-In**:
   - Q23 = No: Jumps to end of survey.
   - Q23 = Yes: Reveals Q24 contact information fields (`26,1`).
8. **Intro Paragraph Formatting**:
   - Clean HTML paragraph structure (`<p style="...">`) rendered on Page 1.
