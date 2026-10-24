# Questionnaire v2 Flow (v2.1)

Branching per the v2.1 jump-logic table (doc numbering Q1–Q24 + Q11a/Q18a/Q18b;
WJX display numbers 1–27, map in `deploy/DEPLOY.md`).

```mermaid
flowchart TD
    A["Start Survey"] --> B["Q1<br/>Consent"]

    B --> C{"Q1: Voluntary<br/>consent?"}
    C -->|"No"| END["End Survey"]
    C -->|"Yes"| BG["Q2–Q6<br/>Background: pathway, prior field,<br/>gender, age, AI experience"]

    BG --> AW["Q7–Q8<br/>Awareness & Ever-use of XJTLU AI"]

    AW --> E{"Q9: AI use for ADS401<br/>in past 4 weeks"}

    E -->|"Both"| G1["G1: Both AI"]
    E -->|"External AI only"| G2["G2: External AI Only"]
    E -->|"Neither"| G3["G3: No AI"]
    E -->|"XJTLU AI only"| G4["G4: XJTLU AI Only"]

    G1 --> X["Q10–Q15<br/>XJTLU AI usage, usefulness,<br/>verification, TAM, problems, intent"]
    G4 --> X

    G1 --> O["Q18–Q18b<br/>External AI usage & usefulness"]
    G2 --> O

    G2 --> N["Q16–Q17<br/>Non-use barriers &<br/>try/resume intention"]
    G3 --> N

    G1 --> COM["Q19<br/>Perceived comparison<br/>(per category + overall)"]

    X --> COM
    COM --> CH["Q20–Q22<br/>Choice factors, improvements,<br/>open feedback"]
    N --> CH

    CH --> K{"Q23: Optional<br/>interview opt-in"}
    K -->|"No"| END
    K -->|"Yes"| Q24["Q24<br/>Contact information<br/>(deleted ≤30 days after interviews)"]
    Q24 --> L["Submit Survey"]
```

## Jump-logic table (WJX configuration source)

| Condition | Action |
| --- | --- |
| Q1 = No | End survey |
| Q9 = Both | Show Q10–Q15, Q18–Q18b, Q19 |
| Q9 = External AI only | Show Q16–Q17, Q18–Q18b; skip Q19 |
| Q9 = Neither | Show Q16–Q17; skip Q18–Q18b, Q19 |
| Q9 = XJTLU AI only | Show Q10–Q15; skip Q16–Q17, Q18–Q18b, Q19 |
| Q23 = No | End survey |

## Notes

- Q7 (awareness) is asked of everyone; Q8 (ever-use) likewise — no skip.
- Q22 (comparison) requires dual use by construction: only the Both branch sees it.
- Groups: G1 Both AI / G2 External AI Only / G3 No AI / G4 XJTLU AI Only —
  same four-group plan as scripts.md.
- v1 comparison figure: `questionnaire_v1_flow_fig.svg`. Re-render this v2
  figure to SVG when the deck needs it (mermaid-cli or GitHub render).
