# Tally Survey Deployment — Official English Release

> Official English survey deployment record for the ADS401 coursework investigation. Fully verified, audited, and published on Tally.

---

## 1. Live Deployment Details

- **Public Survey Link**: **https://tally.so/r/xVXO6r**
- **Form ID**: `xVXO6r`
- **Status**: `PUBLISHED`
- **Total Blocks**: 241
- **Paging Architecture**: **9-Page Streamlined Flow** (designed to minimise drop-off and eliminate page-turning fatigue)
- **Language**: `en` (Pure English UI: buttons `Next` / `Submit`, validation `Maximum 3 required`)
- **API Access**: Tally MCP (`https://api.tally.so/mcp`) & REST API (`https://api.tally.so`)

---

## 2. 9-Page Instrument Structure

| Page | Section | Questions | Interactions & Branching Rules |
|---|---|---|---|
| **P1** | Information & Voluntary Consent | Q1 | • Participant Information Sheet (PDF) linked directly above Q1<br>• Q1 = No: Submits and ends survey immediately (`JUMP TO END`) |
| **P2** | Eligibility & Background | Q2–Q6 | Programme/pathway, prior field, gender, age, AI experience (includes native `Other` and `Prefer not to say`; Q3 contains all 11 standardized categories) |
| **P3** | Awareness & Branching Hub | Q7–Q9 | • Q7 = Had not heard: Hides Q8, and disables XJTLU AI options in Q9<br>• Q8 = No: Disables XJTLU AI options in Q9 (prevents contradictory data)<br>• Q9: 4-way branching hub (`Both` / `XJTLU only` / `External only` / `Neither`) |
| **P4** | XJTLU AI Usage & Experience | Q10–Q16 | • Q10 Frequency → Q11 Activities (`Other activity (please specify)`)<br>• **Q11→Q12 Presence Linkage**: Q12 matrix displays **only the activity categories checked in Q11**; unchecked categories are hidden<br>• Q12 Utility Matrix: 5-point scale (`Not useful` to `Very useful`) with standard compact row headers<br>• Q13 Verification frequency → Q14 TAM Attitude Matrix<br>• **Q15 Problem Checklist**: Top option `No notable problem (selecting this will hide other options)` with bidirectional mutual exclusion (max 3)<br>• Q16 Future continuation intent<br>• Branching: Both → P6; XJTLU only → P8 |
| **P5** | Non-use Module | Q17–Q18 | • Q17 Non-use barriers (max 3)<br>• Q18 Try/resume willingness<br>• Neither → P8 |
| **P6** | External AI Usage | Q19–Q21 | • Q19 Frequency → Q20 Activities (`Other activity (please specify...)`)<br>• **Q20→Q21 Presence Linkage**: Q21 matrix displays only checked activities<br>• External only → P8 |
| **P7** | Tool Comparison Matrix | Q22 | Direct comparative rating per activity + overall preference (exclusive to `Both` users; isolated page prevents cognitive fatigue) |
| **P8** | Convergence & Follow-up | Q23–Q27 | • Q23 Tool choice criteria (max 3) → Q24 Improvement priorities (max 3) → Q25 Open feedback (optional)<br>• **Q26 Follow-up Invitation**: If No → hides all 5 blocks of Q27 immediately and displays `Submit`<br>• If Yes: Q27 reveals preferred name (optional) and phone/email (required) |
| **P9** | Completion | Thank You | Submission acknowledgement and confirmation |

---

## 3. Verified Technical Highlights

1. **Native Inline Other Inputs**:
   - Q11 and Q20 use Tally's native `isOtherOption: true` on `Other activity (please specify)`;
   - Displays an inline input box on check without awkward split sub-questions or broken underlines.
2. **Matrix Row Presence Linkage**:
   - Evaluates only the activities the respondent selected;
   - Eliminates redundant N/A columns, giving the 5 rating columns 20% extra horizontal width for comfortable mobile viewing.
3. **PIS Documentation Linkage**:
   - Full 6-page Participant Information Sheet (PDF) hosted in the repository and linked directly on Page 1 before Question 1.
4. **Ghost UUID Audit**:
   - 24 core conditional logic rules verified with zero ghost or dangling references.
