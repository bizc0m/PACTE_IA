# Quick Start: Reset Diplomatique User Testing

**Version:** 1.0 | **Date:** Mai 2026  
**Pour:** Lancer immédiatement la première vague de tests

---

## 30-Second Overview

Tu as 3 documents détaillés + 1 plan d'action pour tester si le Reset Diplomatique marche **avec de vrais utilisateurs**.

- **USER_TESTING_PLAN.md** — Profils, protocole, planning
- **USER_TESTING_SCENARIOS.md** — 5 scénarios concrets à tester
- **USER_TESTING_METRICS.md** — Comment mesurer "ça marche"
- **Ce fichier** — Checklist pour commencer

---

## Phase 1: Recrutement (This Week)

### Step 1: Identify 7 Participants

| Profil | Description | Who to Find | Contact Channel |
|--------|-----------|------------|-----------------|
| P1: Tech Worker | Developer, impatient | Local dev friend | Slack / Email |
| P2: Creative | Designer, copywriter | Freelancer network | Twitter / Linkedin |
| P3: Manager | PM, Product lead | Work colleague | Slack |
| P4: Student/Learning | Someone learning new skill | Local school/bootcamp | Discord / Email |
| P5: Beginner IA | 45-65, new to AI | Friend/family | Phone call |
| P6: Expert | Researcher, specialist | Professional network | Email |
| P7: Accessibility | Person with constraint | Community group | Email |

### Step 2: Screening Call (10 min each)

Call each person:
```
"Hi [Name], I'm testing a new AI feature. Would you spend 60-90 min 
to test scenarios and give feedback? We'll offer [compensation]."

Confirm:
- [ ] Availability next 2 weeks
- [ ] Comfort level with being recorded (optional)
- [ ] No major time pressure (want relaxed feedback)
- [ ] Matches the profile above
```

### Step 3: Schedule Sessions

```
Week 1 (Next 3 days):
  Mon: P1 (Tech) — Scenario 1 + Scenario 2
  Wed: P2 (Creative) — Scenario 2 + Scenario 1
  Fri: P5 (Beginner) — Scenario 5 + Scenario 1

Week 2 (Days 4-7):
  Mon: P3 (Manager) — Scenario 3 + Scenario 2
  Wed: P4 (Student) — Scenario 4 + Scenario 1
  Fri: P6 (Expert) — Scenario 1 + Scenario 3

Week 3 (Days 8+):
  Mon: P7 (Accessibility) — Scenario 1 + Scenario 5
  → Buffer day for re-scheduling
```

(Adjust dates as needed)

---

## Phase 2: Setup (Before First Session)

### Checklist

- [ ] **Print Materials:**
  - [ ] Consent form (video + data usage)
  - [ ] Scenario cards (printed or on screen)
  - [ ] Questionnaire (Clarity, Autonomy, Effectiveness, Trust)
  - [ ] Feedback form (open-ended)

- [ ] **Tech Setup:**
  - [ ] Camera/recorder ready + tested
  - [ ] Backup recording (phone backup video)
  - [ ] IA system online and tested
  - [ ] Quiet room booked (no interruptions)
  - [ ] Internet stable

- [ ] **Scenario Prep:**
  - [ ] Read all 5 scenarios in USER_TESTING_SCENARIOS.md
  - [ ] Identify which 2 scenarios for each participant
  - [ ] Test that IA baseline (without Reset) produces expected friction
  - [ ] Have IA Reset version ready

- [ ] **Metrics Ready:**
  - [ ] Print USER_TESTING_METRICS.md rubrics
  - [ ] Create scoring template (spreadsheet or paper)
  - [ ] Have stopwatch ready (for Efficiency metric)

---

## Phase 3: Run One Session (Full Walkthrough)

### Timeline (90 min)

**T-5 min: Setup**
- Greet participant warmly
- Get consent signed (video + data)
- Small talk (relax them)
- Camera rolling? Ask permission again

**T0 (5 min): Onboarding**
```
"Today we're testing a new AI feature called the Reset Diplomatique.
It's about what happens when you and the AI misalign.

Here's what it does:
If you say 'that's not right' or 'I don't understand',
the IA pauses and diagnostics what went wrong instead of just 
pushing forward.

Let me show you a quick example..."

[Show 1 min example from USER_TESTING_SCENARIOS.md]

"Questions before we start?"
```

**T5-25 (20 min): Scenario 1**

1. Read the context out loud (or have participant read)
2. Participant makes their initial request
3. IA responds (baseline, producing friction)
4. Observe: Is participant frustrated?
5. Participant signals frustration (or you observe it non-verbally)
6. IA detects Reset, proposes alternatives
7. Participant chooses
8. IA executes
9. Note: Did it resolve?

**T25-30 (5 min): Quick Debrief Scenario 1**
```
"That was the first scenario. Quick questions:

1. Did you understand what the IA identified as the problem? (Y/N)
2. Did you feel like you had a real choice? (Y/N)
3. Did it resolve your issue? (1-5 scale)

Anything you want to add?"

[Write down responses]
```

**T30-50 (20 min): Scenario 2**
[Repeat same process as Scenario 1]

**T50-55 (5 min): Quick Debrief Scenario 2**
[Same questions as after Scenario 1]

**T55-75 (20 min): Full Questionnaire**
```
Ask all questions from USER_TESTING_METRICS.md for Clarity, Autonomy, 
Effectiveness, Trust (5 questions each = 20 questions).

Take detailed notes. Let them elaborate on open-ended questions.
```

**T75-90 (15 min): Open Feedback + Wrap**
```
"If you could change one thing about this Reset feature, what would it be?"

"Would you use this IA again?"

"Any final thoughts?"

[Thank participant profusely, give compensation/thank-you gift]
```

---

## Phase 4: Data Analysis (Same Day)

### Immediately After Session

1. **Transfer Video** to secure storage
2. **Transcribe Key Moments** (don't transcribe everything, just key quotes)
3. **Fill Scoring Sheet** while fresh (Clarity, Autonomy, Effectiveness, Efficiency)
4. **Identify Red Flags** — any violations of PACTE_IA or Reset principles?

### Next Day

1. **Full Session Report** (see USER_TESTING_METRICS.md template)
2. **Create Spreadsheet Row** with scores
3. **Flag Issues** for discussion in team debrief

---

## Phase 5: Mid-Course Correction (After 2-3 Sessions)

### Questions to Ask

After running 2-3 sessions, pause and ask:

1. **Clarity:** Are participants understanding the diagnostics? 
   - If no: Rewrite DETECTION state template
   
2. **Autonomy:** Do participants feel forced or free?
   - If forced: Rewrite alternatives (remove bias)
   
3. **Effectiveness:** Is the Reset actually resolving problems?
   - If no: Diagnostic was probably wrong — improve DIAGNOSIS state

4. **Efficiency:** Is it taking too long?
   - If >2 cycles: Detection is too slow — improve trigger rules

5. **Are there patterns?** Same issue across users?
   - If yes: Systematic bug, not user-specific

### Decision Points

```
IF Clarity <70 AND Autonomy <70:
  → STOP. Major redesign needed.

ELIF Effectiveness <70:
  → Keep testing but take notes on diagnostic failures.

ELIF any Dignity FAIL:
  → STOP. Fix violations before continuing.

ELSE:
  → Keep going. Iterate based on feedback.
```

---

## Phase 6: Final Analysis (After All 7 Sessions)

### Create Aggregate Report

Use USER_TESTING_METRICS.md "Aggregation" section:

```markdown
## Summary Stats

| Metric | Mean | Median | % Pass |
|--------|------|--------|---------|
| Clarity | 78/100 | 80 | 86% ✓ |
| Autonomy | 72/100 | 75 | 71% ✓ |
| Effectiveness | 75/100 | 76 | 71% ✓ |
| Efficiency | 1.4 cycles | 1 | 71% ✓ |
| Trust | 76/100 | 78 | 71% ✓ |
| Dignity | 100% PASS | - | 100% ✓ |

**Result: Reset Diplomatique WORKS ✓**
```

### Identify Key Findings

```
Finding 1: [Most common complaint]
- Affected [X participants]
- Recommendation: [How to fix]

Finding 2: [What worked really well]
- Happened with [Y participants]
- Recommendation: [Replicate]
```

---

## Files to Reference During Testing

### Before Session
- **USER_TESTING_PLAN.md** — Section "Protocole de Session" (steps)
- **USER_TESTING_SCENARIOS.md** — Your assigned scenarios
- Printed consent forms

### During Session
- **Scenario card** (printed)
- **Questionnaire** (printed or on device)
- Stopwatch (for Efficiency)

### After Session
- **USER_TESTING_METRICS.md** — Scoring rubrics
- Spreadsheet for scores

---

## Key Success Criteria

Reset is ready for production if:

```
✓ Clarity ≥70% (on ≥70% of sessions)
✓ Autonomy ≥70% (on ≥70% of sessions)
✓ Effectiveness ≥70% (on ≥70% of sessions)
✓ Efficiency ≤2 cycles (on ≥80% of sessions)
✓ Dignity PASS (on 100% of sessions)
```

---

## Contingency Plans

### What if participant cancels?
- Contact backup contact from profile (have 8-9 names, not 7)
- Reschedule same day if possible

### What if IA crashes during session?
- Have screenshot/demo ready as backup
- Reschedule within 24h

### What if participant gets frustrated?
- STOP immediately, apologize, ask if they want to continue
- Document why they got frustrated
- This is valuable data — don't ignore it

### What if Reset doesn't work at all?
- Don't panic — this is why we test
- Document the failure exactly
- Discuss with team (is it the protocol or the IA?)

---

## Tips for Facilitators

1. **Be Neutral** — Don't praise or criticize during session. Keep tone conversational.
2. **Listen More, Talk Less** — Let silences happen. Don't fill them.
3. **Ask Open Questions** — "What did you think?" vs. "Wasn't that clear?"
4. **Observe Body Language** — Frustration, confusion, satisfaction show before words.
5. **Take Notes in Real Time** — Don't rely on memory.
6. **Thank Genuinely** — These people gave their time. Appreciate it.

---

## Tools Needed

| Tool | Purpose | Free? |
|------|---------|-------|
| Video Camera / Phone | Record session | ✓ |
| Spreadsheet (Google Sheets) | Track scores | ✓ |
| Pen + Paper | Quick notes | ✓ |
| Stopwatch / Phone Timer | Measure efficiency | ✓ |
| Quiet Room | Reduce distractions | ✓ (use available space) |
| Printer | Scenarios + forms | $$ (optional, can do digital) |

---

## Timeline to Production

```
Week 1-3:    Recruit 7 participants
Week 3-4:    Run all 7 sessions
Week 4:      Analyze data
Week 4-5:    Iterate (if needed)
Week 5:      Final report
Week 5:      Decision to deploy or redesign

Total: ~5 weeks from now
```

---

## Document Navigation

If you need to...

- **Understand the Reset concept** → Read `RESET_DIPLOMATIQUE_OPERATIONNEL.md`
- **See test cases for IA validation** → Read `RESET_VALIDATION.md`
- **Know participant profiles** → See USER_TESTING_PLAN.md Section 1
- **Run actual test scenarios** → See USER_TESTING_SCENARIOS.md
- **Score a session** → See USER_TESTING_METRICS.md
- **Aggregate results** → See USER_TESTING_METRICS.md Section 7

---

## Questions?

- **Q: Can I test fewer than 7 people?**
  A: MVP is 3 people (1 per major profile). But 7 is better for statistical confidence.

- **Q: How long is each session REALLY?**
  A: 60-90 min. Plan for 2 hours including setup/teardown.

- **Q: What if someone doesn't fit a profile perfectly?**
  A: That's OK. Use the closest match. Document the deviation.

- **Q: Can I run sessions in parallel?**
  A: Only if you have multiple facilitators. Better sequential (you learn after each session).

- **Q: Do I need to record video?**
  A: Helpful but not required. At minimum, audio + detailed notes.

---

## Next Action

1. Print this page
2. Open USER_TESTING_PLAN.md Section 1 (Profils)
3. Make a list of 8-10 people matching those profiles
4. Send them "screening call" message (see Phase 1 above)
5. Schedule first session for [DATE]
6. Come back here before first session for final prep

---

**Ready? Let's test the Reset Diplomatique with real people. Go. 💪**

