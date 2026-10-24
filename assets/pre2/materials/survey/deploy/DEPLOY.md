# WJX (问卷星) deployment — questionnaire v2.1 (EN)

Deployment record for the pilot instrument. Created 2026-10-24 via official
`wjx-cli` 0.4.5 (github.com/wjxcom/wjx-ai-kit), API-Key auth.

## Deployed artifact

- Survey vid `390541662`, sid `Ot88BRn` — https://www.wjx.cn/vm/Ot88BRn.aspx
- Source: `wjx_survey.jsonl` (this directory) — 27 questions, EN, created with
  `wjx survey create --file wjx_survey.jsonl`
- Status at creation: **draft** (do not distribute before logic config + sign-off)

## WJX ↔ document question-number map

WJX numbers questions 1–27 sequentially; the repo uses Q1–Q24 + Q11a/Q18a/Q18b.

| Doc | WJX | Doc | WJX | Doc | WJX | Doc | WJX |
|---|---|---|---|---|---|---|---|
| Q1 | 1 | Q11 | 11 | Q15 | 16 | Q20 | 23 |
| Q2 | 2 | Q11a | 12 | Q16 | 17 | Q21 | 24 |
| Q3 | 3 | Q12 | 13 | Q17 | 18 | Q22 | 25 |
| Q4 | 4 | Q13 | 14 | Q18 | 19 | Q23 | 26 |
| Q5 | 5 | Q14 | 15 | Q18a | 20 | Q24 | 27 |
| Q6–Q10 | 6–10 | | | Q18b | 21 | Q19 | 22 |

## Manual steps required after CLI create (official CLI gaps)

`survey.branching` is an intentional gap in wjx-ai-kit (capability matrix);
multi-select limits are not exposed either. Configure in the web editor
(designnew):

1. Display logic (题目关联), driven by WJX9 (doc Q9):
   - WJX10–16 shown if WJX9 = Both OR XJTLU AI only
   - WJX17–18 shown if WJX9 = External AI only OR Neither
   - WJX19–21 shown if WJX9 = Both OR External AI only
   - WJX22 shown if WJX9 = Both
2. Jump-to-end: WJX1 = No → survey ends; WJX26 = No → survey ends
3. Show WJX27 only if WJX26 = Yes
4. Multi-select limits (最多选3项): WJX15, WJX17, WJX23, WJX24
5. "Other: please state your programme" (WJX2) — enable the option's
   fill-in box if not active

## Known WJX text-import limitations (why JSONL, not text import)

- Text import splits option lines on half-width commas and matrix column
  labels on spaces/commas; multi-word column labels (e.g. "Not useful")
  cannot survive any text channel (import page and in-editor 批量添加 share
  the same parser).
- The JSONL `矩阵单选` path carries columns as a JSON array — labels exact.
- CN variant: create from a CN JSONL (translate `wjx_survey.jsonl`) when the
  CN link is needed; structure must stay identical for column-aligned merge.

## End-to-end workflow (pilot)

1. **Build** — `wjx survey create --file wjx_survey.jsonl` (done: vid
   390541662, draft). CN variant: translate JSONL → same command → second
   link; keep structure identical.
2. **Web-editor pass (human, ~10 min)** — configure display logic (table in
   `questionnaire_v2_flow.md`), multi-select limits (WJX15/17/23/24 = max 3),
   WJX2 Other-fill box, and replace the survey description with
   `wjx_description_en.txt` (paragraph breaks; JSONL intro renders as one
   block). Delete broken drafts 390520971 / 390534909 (API delete needs
   account-manager permission).
3. **Verify** — full preview walk of all 27 items and both end paths; spot-
   check branch display per Q9 group (G1–G4) and Q23→Q24.
4. **Publish** — explicit sign-off, then `wjx survey status --vid 390541662
   --status 1` (or editor 发布). Record fill URL + start date.
5. **Distribute** — per-person links (EN first; CN link if created),
   invitation message states voluntary participation and retention promise.
6. **Collect & export** — monitor `wjx response count`; export with
   `wjx response download` (or web export) after close; merge EN/CN by
   column alignment; delete contact column per retention promise after
   interviews.
7. **Archive** — record final n, fieldwork dates, and any deviation in
   scripts.md (same-PR rule).

## Old drafts

390520971 / 390534909 (broken text-import attempts) — API delete requires
account-manager permission; delete manually in 我的问卷 or leave as hidden
drafts.
