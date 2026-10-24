# Questionnaire v2 Flow (v2.2)

Branching per the v2.2 jump-logic table (doc numbering Q1–Q24 + Q11a/Q18a/Q18b;
WJX display numbers 1–27, map in `deploy/DEPLOY.md`).

```mermaid
flowchart TD
    subgraph Page1 ["Page 1: Information & Consent"]
        A["Start Survey"] --> INTRO["Read Information Sheet"]
        INTRO --> B["Q1<br/>Voluntary Consent"]
        B --> C{"Q1 Consent?"}
        C -->|"No"| END1["Submit & End Survey"]
    end

    subgraph Page2 ["Page 2: Core Questionnaire"]
        C -->|"Yes (Next Page)"| BG["Q2–Q6<br/>Background: Programme/pathway, prior field,<br/>gender, age, AI experience"]

        BG --> AW["Q7–Q8<br/>Awareness & Ever-use of XJTLU AI"]

        AW --> E{"Q9: AI use for ADS401<br/>in past 4 weeks"}

        E -->|"Both (Opt 1)"| G1["G1: Both AI"]
        E -->|"XJTLU AI only (Opt 2)"| G4["G4: XJTLU AI Only"]
        E -->|"External AI only (Opt 3)"| G2["G2: External AI Only"]
        E -->|"Neither (Opt 4)"| G3["G3: No AI"]

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
        K -->|"No"| END2["Submit & End Survey"]
        K -->|"Yes"| Q24["Q24<br/>Contact information<br/>(deleted ≤30 days after interviews)"]
        Q24 --> SUBMIT["Submit Survey"]
    end
```

## Jump-logic table (WJX configuration source)

| Condition | Action |
| --- | --- |
| Q1 = No | Next Page → Submit & End Survey (Page 1 pagination isolation) |
| Q1 = Yes | Proceed to Page 2 (Q2..Q24) |
| Q9 = Both (Opt 1) | Show Q10–Q15, Q18–Q18b, Q19 |
| Q9 = XJTLU AI only (Opt 2) | Show Q10–Q15; skip Q16–Q17, Q18–Q18b, Q19 |
| Q9 = External AI only (Opt 3) | Show Q16–Q17, Q18–Q18b; skip Q10–Q15, Q19 |
| Q9 = Neither (Opt 4) | Show Q16–Q17; skip Q10–Q15, Q18–Q18b, Q19 |
| Q23 = No | Submit & End Survey |
| Q23 = Yes | Show Q24 (Contact Details) |

## Key Design Principles

1. **Page 1 Isolation**: A page break is inserted immediately after Q1. Unconsenting participants submit immediately without viewing subsequent research questions.
2. **Q9 Natural Gradient**:
   1. Both XJTLU AI and External AI
   2. XJTLU AI only (no External AI)
   3. External AI only (no XJTLU AI)
   4. Neither XJTLU AI nor External AI (placed at the bottom)
3. **Other-Item Handling**:
   - Q11: `Other (please specify) ______` includes a text fill-in.
   - Q18: `Other (please specify; if same as Q11, state 'Same as Q11') ______` avoids redundant typing.
   - Matrices (Q11a, Q18b, Q19): Clean category rows without A–F letter prefixes. Q19 includes `Other activity (if applicable)`.
4. **Separate Deployments for EN and CN**:
   - Single-language surveys per deployment link (identical column structures).
   - Avoids doubling questionnaire size (54 questions) and messy multi-language branch logic in a single survey.
