# User Testing Session Report Template

**Version:** 1.0 | **Date:** Mai 2026  
**Usage:** Copy this template for EACH user testing session. Fill in during + immediately after.

---

## Session Information

| Field | Value |
|-------|-------|
| **Participant ID** | P[1-7] (e.g., P1_TechWorker) |
| **Date & Time** | [YYYY-MM-DD, HH:MM] |
| **Duration** | [Total minutes] |
| **Facilitator** | [Name] |
| **Location** | [Room/Virtual] |
| **Recorded** | [Y/N] Video:[Y/N] Audio:[Y/N] |

---

## Participant Profile

| Field | Value |
|-------|-------|
| **Assigned Persona** | [P1 Tech / P2 Creative / P3 Manager / P4 Learning / P5 Beginner / P6 Expert / P7 Accessibility] |
| **Actual Background** | [Their real role/skill] |
| **Comfort Level with AI** | [1-5: Never used / 2: Occasional / 3: Regular / 4: Daily / 5: Expert] |
| **Apparent Mood** | [Relaxed / Focused / Stressed / Tired / Engaged] |
| **Notes on Accessibility** | [Any needs we accommodated?] |

---

## Scenario Details

### Scenario 1

| Field | Value |
|-------|-------|
| **Scenario ID** | [Ref: USER_TESTING_SCENARIOS.md] |
| **Scenario Title** | [e.g., "Dev Refactoring (FORMAT)"] |
| **Friction Type Expected** | [FORMAT / INCOMPRÉHENSION / PRÉSOMPTION / HORS-PÉRIMÈTRE / CERTITUDE_FEINTE / DÉPENDANCE / AMBIGUÏTÉ] |

---

## Session Timeline: Scenario 1

Use this to document exact flow.

```
T0:00 — Participant given context
   Participant reading/reaction: [Notes]
   
T0:30 — Participant makes initial request
   Exact request: "[Quote or paraphrase]"
   
T1:00 — IA gives baseline response (produces friction)
   IA response summary: "[What did IA do?]"
   
T1:30 — Participant signals frustration
   Frustration signal: [Verbal quote / Non-verbal cue]
   Level of frustration: [1-5: minor / 2: noticeable / 3: clear / 4: strong / 5: intense]
   
T2:00 — IA detects Reset
   IA detected at: [T seconds in]
   Delay: [Was detection immediate or slow?]
   
T2:30 — IA proposes diagnosis + alternatives
   Diagnosis delivered: "[What did IA name as the problem?]"
   # of alternatives: [1 / 2 / 3 / 4+]
   
T3:00 — Participant chooses
   Participant chose: [Alt 1 / Alt 2 / Alt 3 / Modified choice / Unclear]
   Reasoning participant gave: "[Quote]"
   
T3:30 — IA executes choice
   Execution quality: [Perfect / Good / Acceptable / Flawed]
   
T4:00 — Participant reaction to resolution
   Reaction: [Satisfied / Accepting / Uncertain / Dissatisfied]
   Quote: "[What participant said?]"
```

**Total Scenario 1 Duration:** [MM:SS]

---

### Scenario 2

[Same timeline template as Scenario 1, just update T values]

**Total Scenario 2 Duration:** [MM:SS]

---

## Metric Scores: Scenario 1

Use rubrics from USER_TESTING_METRICS.md

| Metric | Score | Status | Evidence | Notes |
|--------|-------|--------|----------|-------|
| **Clarity** | __/100 | ✓ ✗ | Participant quote: "_____" | [What made it clear/unclear?] |
| **Autonomy** | __/100 | ✓ ✗ | Alternatives offered: __ | [Did they feel free?] |
| **Effectiveness** | __/100 | ✓ ✗ | Can continue: Y/N | [Problem actually resolved?] |
| **Efficiency** | __ cycles | ✓ ✗ | Duration: __ min | [Too many iterations?] |

**Q1 (Clarity): Understand diagnosis?**
- Asked at T: [____]
- Response: [Y / N / Kinda]
- Quote: "[What participant said]"

**Q2 (Autonomy): Felt real choice?**
- Asked at T: [____]
- Response: [Y / N / Somewhat]
- Quote: "[What participant said]"

**Q3 (Effectiveness): Resolved your issue?**
- Asked at T: [____]
- Response: [Y / N / Partially]
- Scale (1-5): [__]
- Quote: "[What participant said]"

---

## Metric Scores: Scenario 2

[Repeat same table as Scenario 1, just update Scenario number]

---

## Overall Session Scores

After both scenarios, compute aggregate scores.

| Metric | S1 Score | S2 Score | Average | Status |
|--------|----------|----------|---------|--------|
| **Clarity** | __/100 | __/100 | __/100 | ✓ ✗ (≥70%?) |
| **Autonomy** | __/100 | __/100 | __/100 | ✓ ✗ (≥70%?) |
| **Effectiveness** | __/100 | __/100 | __/100 | ✓ ✗ (≥70%?) |
| **Efficiency** | __ cycles | __ cycles | __ cycles avg | ✓ ✗ (≤2?) |

---

## Additional Metrics

### Trust Score

**Asked:** "Would you use this IA again?" / "Would you recommend?"

- Overall Trust Score: __/100
- Would use again: [Y / N / Maybe]
- Would recommend: [Y / N / Maybe]
- Key words to describe IA: "[Word 1, Word 2, Word 3]"
- Evidence: "[Quote or observation]"

### Dignity Assessment

**Violations Check:**
- [ ] Apology script? ___
- [ ] Condescension? ___
- [ ] Manipulation? ___
- [ ] Gaslighting? ___
- [ ] False apology? ___
- [ ] Any other red flag? ___

**Dignity Assessment:** [PASS / FAIL]

If FAIL, detail the violation(s):
```
Violation 1: [What happened]
  Evidence: "[Quote or timestamp]"
  Severity: [Minor / Major]

Violation 2: ...
```

---

## Qualitative Observations

### Body Language & Tone

```
- [Timestamp]: [What you observed about their body/tone/engagement]
  Example: "T2:15 — Shoulders relaxed when IA offered alternatives. 
           Leaned forward slightly, nodding."
  
- [Timestamp]: [Another observation]
```

### Unexpected Behaviors

```
- [What surprised you or didn't match your expectations?]
- [Did they use the Reset in an unexpected way?]
- [Did they struggle with something you thought was clear?]
```

### Bright Spots

```
- [When did the Reset work REALLY well?]
- [What part delighted or satisfied them?]
- [What felt effortless to them?]
```

### Friction Points

```
- [When did things go wrong or confuse them?]
- [Where did they struggle?]
- [What frustrated them (beyond the test scenario)?]
```

---

## Key Quotes

Direct quotes that reveal insights:

**On Clarity:**
> "[Participant quote about understanding the diagnosis]"

**On Autonomy:**
> "[Participant quote about freedom to choose]"

**On Effectiveness:**
> "[Participant quote about whether it solved their problem]"

**On Trust:**
> "[Participant quote about using IA again]"

**Most Revealing Quote:**
> "[The single best quote that captures how they felt about the Reset]"

---

## Post-Debrief Open Questions

**Q: If you could change one thing about this Reset feature, what would it be?**
- Response: "[Full answer]"

**Q: What was most useful about the Reset?**
- Response: "[Full answer]"

**Q: What was most confusing or frustrating?**
- Response: "[Full answer]"

**Q: Would you actually use this feature?**
- Response: "[Full answer]"

---

## Issues & Red Flags

### Critical Issues (Must Fix Before Next Session)

```
- [ ] Issue 1: [What went wrong]
      Impact: [How serious?]
      Likely Root Cause: [Why did it happen?]
      Recommended Fix: [What to change?]

- [ ] Issue 2: ...
```

### Medium Issues (Iterate On)

```
- [ ] Issue 1: ...
- [ ] Issue 2: ...
```

### Low Issues (Nice to Improve)

```
- [ ] Issue 1: ...
```

---

## Recommendations for Next Session

Based on this session, what should we:

1. **Change in the IA protocol?**
   - [ ] Improve DETECTION sensitivity (trigger faster)
   - [ ] Rewrite DIAGNOSIS template (not resonating)
   - [ ] Revise alternatives (not clear or one is biased)
   - [ ] Other: ______

2. **Change in the scenario?**
   - [ ] Make context clearer
   - [ ] Adjust the frustration trigger
   - [ ] Different profile needed
   - [ ] Other: ______

3. **Change in the facilitation?**
   - [ ] Ask different questions
   - [ ] Give more/less context
   - [ ] Observe different behaviors
   - [ ] Other: ______

---

## Comparison to Previous Sessions

If this is not your first session:

```
| Aspect | Session N-1 | Session N (This) | Trend |
|--------|-----------|-----------------|-------|
| Clarity | __/100 | __/100 | ↑ ↓ → |
| Autonomy | __/100 | __/100 | ↑ ↓ → |
| Effectiveness | __/100 | __/100 | ↑ ↓ → |
| Efficiency | __ cycles | __ cycles | ↑ ↓ → |

Key Pattern Observed: [What's changing across sessions?]
```

---

## Summary & Next Steps

### Overall Assessment

**Did the Reset work in this session?**
- [Yes / Partially / No]

**Confidence in this assessment:**
- [High / Medium / Low]

**Main finding from this session:**
> "[1-2 sentences capturing the key insight]"

### Immediate Next Steps

- [ ] [Action 1 before next session]
- [ ] [Action 2 before next session]
- [ ] [Action 3 before next session]

### Session Passed Quality Checklist?

- [ ] Recorded (video/audio as planned)
- [ ] Metrics scored same-day
- [ ] Key quotes captured
- [ ] Observations detailed
- [ ] Recommendations documented
- [ ] Data stored securely
- [ ] Participant thanked + compensated
- [ ] No dignity violations

---

## Appendix: Raw Data

### Recording Location
- Video: [File path or cloud link]
- Audio: [File path or cloud link]
- Duration: [Total minutes recorded]

### Consent Form
- [ ] Signed
- [ ] Copy provided to participant
- [ ] Copy stored securely

### Notes
- Handwritten notes scanned: [Y / N, location?]
- Spreadsheet entry created: [Y / N]

---

## Facilitator Signature

**Facilitator Name:** _______________  
**Date Completed:** _______________  
**Quality Check:** ✓ (Reviewed all sections)

---

**Template Version:** 1.0  
**Last Updated:** Mai 2026

*Copy this template for each session. Fill in during session + same-day after. Takes ~30-45 min to complete fully.*

