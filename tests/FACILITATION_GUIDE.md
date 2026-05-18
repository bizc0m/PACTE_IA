# Guide de Facilitation : User Testing Sessions

**Version:** 1.0 | **Date:** Mai 2026  
**Pour:** Facilitateurs conduisant les tests utilisateurs

---

## Avant La Session (1 jour)

### Checklist Finale

- [ ] Participant confirmé + direction connue
- [ ] Scénarios imprimés ou affichés à l'écran
- [ ] Consent form en main
- [ ] Questionnaire préparé (digital ou papier)
- [ ] Caméra/enregistreur testé + charged
- [ ] Espace calme, pas de distractions
- [ ] Internet stable (si IA en ligne)
- [ ] Stopwatch accessible
- [ ] Hydratation pour vous et le participant
- [ ] Petit café/thé/snack offert à participant
- [ ] SESSION_REPORT_TEMPLATE.md imprimé (pour prendre notes)

### Mental Prep

Rappelle-toi:
- **Tu n'es pas un vendeur.** Pas de "vendre" le Reset.
- **Tu es un observateur scientifique.** Objective, neutral.
- **Le participant est le vrai expert** de son expérience. Tu l'écoutes.
- **Si quelque chose est flou pour eux, c'est pas leur faute.** C'est une donnée utile.

---

## Pendant La Session

### T-5: Greeting & Setup

**Tone:** Warm, casual, no pressure.

```
"Hi [Name]! Thanks so much for coming. 
I really appreciate you taking the time."

[Small talk — 1-2 min, genuine interest]
"How's your [day/week]? 
Did you find the place OK?"

[When ready to start]
"So, just to make sure — you're comfortable with me recording [video/audio]?
And you've read the consent thing?"

[Emphasize]
"This isn't about you being 'good' or 'bad'. 
We're testing a feature. If something doesn't work well, 
that's feedback we need. So be honest."
```

**Observe:** Are they comfortable? Nervous? Relaxed?

---

### T0-5: Onboarding (Explain the Reset)

**Goal:** They understand what Reset is WITHOUT too much explanation.

**Script:**

```
"OK so today we're testing a new feature called the Reset Diplomatique.

It's actually pretty simple: sometimes when you're working with an AI,
the AI misunderstands or goes in a direction you didn't want.

What USUALLY happens: you say 'that's not right' and the AI either 
tries to fix it blindly or apologizes forever. Frustrating.

What we're testing: Can the AI PAUSE and ask 'wait, what went wrong?' 
Then it diagnoses what's actually blocking you, 
and offers you real alternatives. 
Then YOU get to choose.

It's not an apology script. It's a diagnostic.

Let me show you a quick example..."

[SHOW 1-MIN EXAMPLE FROM A SCENARIO]

"So you'll do two scenarios like this. First one, the IA probably 
does something wrong on purpose. You react naturally. 
Then we'll see if it can detect + fix it.

Any questions before we start?"

[Answer quickly, don't re-explain too much]
```

**Key Points:**
- Not "the IA is sorry"
- It's "the IA diagnoses"
- Emphasis on THEIR choice
- Keep it brief (2-3 min)

**Observe:** Do they nod? Ask smart questions? Look confused?

---

### T5-25: Scenario 1 Execution

#### Step 1: Set the Context (2-3 min)

```
"OK, first scenario. Let me set the scene..."

[Read the context from the scenario card, slowly]

"So you're [role] and you need to [task]. That's where you're at.

Make sense? Any questions about the setup?

[Answer any questions]

Now, make your first request to the IA. 
Say it however feels natural to you."
```

**Observe:** Do they role-play or just read? Natural language?

#### Step 2: IA Responds (Baseline, Producing Friction)

[IA gives response designed to create the expected friction]

**Observe:**
- Does the user notice something's off?
- Facial expression? Posture?
- Do they sigh, frown, lean back?
- Any verbal cues ("hmm", "wait", "that's not...")?

**If no reaction:** Mild prompt:
```
"What do you think of that?"
[Give them space to respond]
```

#### Step 3: User Signals Frustration

**Your job:** Don't miss this moment.

**Signs of frustration:**
- Verbal: "that's too long", "you don't understand", "not what I asked"
- Non-verbal: Frown, sigh, shaking head, leaning back, silence longer than 3 sec
- Body: Tension in shoulders, hand to face, eyes rolling

**If verbal:** Note exactly what they said. Write it down.

**If non-verbal only:** Gentle prompt:
```
"What's on your mind?"
OR
"How are you feeling about that response?"
```

**Don't push.** If they say "it's fine", trust them (even if you think it's wrong).

#### Step 4: IA Detects Reset

[IA switches to DETECTION state]

**Observe:**
- Timing: How fast did IA detect?
- Quality: Does diagnosis match what user signaled?
- Tone: Does IA sound like it's judging? Or analyzing?

**Timing notes:**
- Immediate (within 5 sec of signal): Good ✓
- Delayed (10+ sec): Flag as slow detection
- Missed (no detection): Flag as critical failure

#### Step 5: IA Proposes Alternatives

**Observe:**
- Number of options: 1 / 2 / 3 / 4+?
- Clarity: Are they clearly explained?
- Tradeoffs: Does IA explain pros/cons of each?
- Bias: Does one option seem "better" or "recommended"?
- Tone: Neutral or slightly pushy?

**Red flag observations:**
- Only 1 option → Not really a choice
- Options are very similar → False autonomy
- "This one is best" language → Pressure implicite
- Too long explanation → Clarity suffers

#### Step 6: User Chooses

```
"Which option appeals to you?"
OR
"What would work better for you?"
OR
"Which would you prefer?"
```

**Observe:**
- Quick decision or hedging?
- Confident or uncertain?
- Do they ask questions about options?
- Any hesitation or re-negotiation?

**Quote exactly what they choose and why if given reason.**

#### Step 7: IA Executes Choice

[IA delivers response according to chosen option]

**Observe:**
- Did IA execute the chosen option? Or different?
- Quality: Good, acceptable, or flawed?
- Did it actually resolve the problem? Or new problem emerged?

#### Step 8: Debrief Scenario 1

```
"OK, so that was scenario 1. 
Quick questions while it's fresh:

1. Did you understand what the IA identified as the problem? 
   [Y/N]

2. Did you feel like you had a real choice? 
   [Y/N]

3. On a scale 1-5, did that resolve your frustration? 
   [1=not at all, 5=completely]

Anything you want to add about how that felt?"
```

**Write down responses verbatim.**

**Don't debate.** If they say "no" to something, take it. Don't argue.

---

### T25-50: Scenario 2

[Repeat entire flow from Scenario 1]

---

### T50-75: Full Questionnaire

Now ask **all the questions** from USER_TESTING_METRICS.md:
- 5 questions for Clarity
- 5 questions for Autonomy
- 5 questions for Effectiveness
- 5 questions for Efficiency (if they can help recall)
- 5 questions for Trust

**Tips:**
- Read question slowly, clearly
- Let them think (don't rush)
- Write down answers as they talk
- If they give a 1-word answer, ask "can you say more?"
- Respect silence (3-5 seconds is OK)

**Tone:** Curious, not interrogative.

```
"Can you say a bit more about that?"
vs.
"WHY do you think that?" [sounds accusatory]
```

---

### T75-90: Open Feedback

```
"So, a few more open questions:

1. If you could change ONE thing about this Reset feature, 
   what would it be?
   
2. What was most useful about what just happened?

3. What was most confusing or frustrating?

4. Would you actually use this IA again in the future?

5. Anything else on your mind?"
```

**Let them talk.** These are the most valuable responses.

**Don't interrupt.** Even silence is data.

---

### T90: Wrap & Thank

```
"Thank you SO much for your time. 
This feedback is really valuable.

[Give compensation/thank you gift]

Do you have any final questions for me?"

[Answer briefly]

"I might reach out in a few weeks if we need clarification 
on something. Is that OK?

[Get their preferred contact method]

Thanks again. Take care!"
```

**Observe:** Final mood — did they leave satisfied or frustrated?

---

## Observation Techniques

### What to Watch For

**Body Language:**
- Shoulders tense or relaxed?
- Leaning forward (engaged) or back (disengaged)?
- Eye contact or avoiding?
- Hands — fidgeting, gesturing, or still?
- Facial expressions — neutral, smiled, frowned?

**Timing:**
- Quick responses (confident) or slow (thinking, uncertain)?
- Long silences (thinking or uncomfortable)?

**Voice:**
- Tone confident or hesitant?
- Speaking faster (excited, nervous) or slower (careful)?
- Volume stable or dropping (losing engagement)?

**Phrases to Listen For:**
- "Oh, I didn't think of that" = Novel insight, good diagnosis
- "Yeah, that's exactly right" = Clear diagnosis
- "I guess so" = Uncertain, not convinced
- "Hmm, I'm not sure" = Confused
- "That's frustrating" = Strong feeling, note it

### Questions to Avoid

**Leading Questions:**
```
❌ "Wasn't that clear?"  → Implies it WAS clear
✓ "Was that clear?"

❌ "Did you like the alternatives?"  → Implies you want them to like
✓ "What did you think of the alternatives?"

❌ "Was the IA helpful?"  → Implies it should be
✓ "How did you experience the IA's response?"
```

**Yes-No Only:**
```
❌ "Did it work?" [Y/N]  → Too binary
✓ "Did it work? Tell me more." [Opens up response]
```

**Why (Usually Defensive):**
```
❌ "Why did you choose that?"  → Sounds judgmental
✓ "What appealed to you about that option?"
```

---

## Red Flags During Session

### Minor Red Flags (Document, Don't Panic)

- User confusion → Note where confusion emerged
- Slower than expected → May indicate detection delay
- User asked for clarification on alternatives → Alternatives weren't clear enough

### Major Red Flags (STOP & Investigate)

- User says "I feel manipulated" → Dignity concern
- User wants to leave → Respect immediately, ask if OK to document feedback
- IA does something clearly wrong → Major bug
- Scenario doesn't produce expected friction → Note for next session

### CRITICAL Red Flags (Session Failure)

- IA violates PACTE_IA pillar (eg., denies user's reality)
- IA uses apology script ("I'm so sorry I'm bad")
- User feels coerced into choice
- IA ignores when user says "no" or "stop"

**If critical red flag:** 
1. STOP the test
2. Apologize genuinely to user
3. Ask if they want to continue or stop
4. Document exactly what happened
5. Alert project lead SAME DAY

---

## After Session (Same Day)

### Within 1 Hour

1. **Export & Backup Recording**
   - Video: Copy to backup location
   - Audio: Transcribe or note timestamp of key moments
   
2. **Transcribe Key Quotes**
   - Don't transcribe everything
   - Pull out quotes that reveal insights
   - Note timestamps
   
3. **Fill Scoring Sheet**
   - Clarity score: 0-100 + evidence
   - Autonomy score: 0-100 + evidence
   - Effectiveness score: 0-100 + evidence
   - Efficiency: # cycles
   - Trust: feelings about re-using
   - Dignity: PASS/FAIL (any violations?)

### Within 24 Hours

1. **Complete SESSION_REPORT_TEMPLATE.md**
   - Full timeline
   - All observations
   - Quoted reactions
   - Recommendations for next session

2. **Create Spreadsheet Entry**
   - Simple row: P[ID] | Scenario | Clarity | Autonomy | Effective | Efficiency | Issues
   
3. **Flag Issues**
   - If critical: Alert lead immediately
   - If medium: Note for team debrief
   - If minor: Include in aggregate report later

4. **Send Thank You**
   - Email/text to participant
   - Appreciate their time
   - Offer to share findings when complete

---

## Tips for Great Facilitation

### The 70/30 Rule

**You talk 30%, they talk 70%.**

Don't fill silences. Let them think out loud.

```
You: "What did you think of those alternatives?"
[Wait 5 seconds]
Them: "Um... the first one seemed..."
[They keep going, you're silent]
```

### The Neutral Mirror

If they say something revealing, reflect it back:

```
Them: "I felt like the IA was pushing me toward option 2"
You: "So you felt pushed toward option 2?"
Them: "Yeah, like it was presented as better even though it said..."
```

(You just got them to elaborate by mirroring.)

### The Pause

Don't rush to the next question.

```
You: [Ask question]
[Participant responds]
[You write notes, stay quiet]
Them: "Oh, also..."
```

Silence makes people keep talking (in a good way).

### The Redirect

If they go off-topic:

```
Them: "And that reminds me of this other time when..."
You: "[Listen briefly] That's interesting. 
     Back to what you said about the alternatives..."
```

Gentle redirect, not harsh.

### The Validate

When they express frustration:

```
Them: "That was really confusing"
You: "That makes sense. 
     A lot of people find that [aspect] unclear."
```

(Note: Don't say "nobody else found that confusing" — invalidates them.)

---

## Tone Throughout

### What NOT to Do

```
❌ Defensive: "Well, the IA is supposed to do X..."
❌ Dismissive: "Oh, that's not really a big issue"
❌ Convincing: "But don't you think the reset was helpful?"
❌ Apologetic: "I'm sorry the IA was confusing"
❌ Frustrated: Sighing, eye-rolling, impatient tone
```

### What TO Do

```
✓ Curious: "Tell me more about that"
✓ Neutral: "Interesting. That's useful feedback."
✓ Appreciative: "Thank you for being honest"
✓ Calm: Slow pace, patient silence
✓ Respectful: "I hear you. Let's note that."
```

---

## Accessibility Considerations

### For Participant P7 (Accessibility-Focused)

Adjust for their specific need:

**If Dyslexia:**
- Offer to read scenarios aloud
- Reduce text on screen
- Speak clearly, simple vocabulary

**If Hearing Impairment:**
- Captions on video
- Written questions, not just verbal
- Face participant directly (lip reading)

**If ADHD/Neurodivergence:**
- More breaks
- Movement allowed
- Less time in one place
- Short questions, not long context

**If Mobility Constraint:**
- Comfortable seating
- Easy access to materials
- No standing/walking required
- Accessible restroom nearby

**General:** ASK what they need, don't assume.

```
"Is there anything I can do to make this more comfortable for you?"
```

---

## Troubleshooting Common Issues

### Participant is Too Quiet

```
❌ "You're not saying much"
✓ "I'd love to hear what you're thinking"
```

Then wait longer. Some people process slowly.

### Participant Argues with You

```
You are NOT debating the Reset. 
They are expressing opinion. That's valuable data.

Them: "That feature is stupid"
You: "What specifically feels stupid about it?"
[They elaborate, you learn]

NOT:
You: "Actually, it's designed to..."
```

### IA Glitches During Session

```
If minor (slow response):
  - "Bear with me, it's loading"
  - Document the delay

If major (IA crashes):
  - Apologize
  - Switch to backup (video demo or manual IA simulation)
  - Note the failure
```

### Participant Wants to Leave Early

```
"Of course, no problem. 
Can I ask what's prompting that? 
Is it something we did, or just timing?"

[Listen, don't convince them to stay]

"Thanks for what you were able to share. 
It's still valuable data."

[Give compensation regardless]
```

### You Realize You Made an Error (Asked Wrong Question, etc.)

```
You: "Actually, can I re-ask that? I wasn't clear..."
Them: [Re-answers]

✓ Shows you care about accuracy
✗ Don't: Pretend you didn't mess up (they noticed)
```

---

## Self-Care for Facilitators

User testing is **emotionally labor-intensive**.

- **You're listening deeply** for 90 minutes
- **You're observing non-verbal cues** constantly
- **You're staying neutral** even if participant is frustrated
- **You're taking notes** while managing flow

**Between sessions:**
- Take 15-20 min break
- Walk, drink water, decompress
- Don't back-to-back sessions if possible
- Talk to someone about interesting patterns (debrief)

**Signs you're tired:**
- Asking leading questions
- Filling silences
- Defensive tone creeping in
- Not taking notes

If tired → **Cancel or reschedule**, don't push through.

---

## Final Checklist: You're Ready if You Can:

- [ ] Explain the Reset without over-explaining
- [ ] Stay neutral when participant is frustrated
- [ ] Ask open questions, not leading ones
- [ ] Listen without fixing/defending
- [ ] Observe body language
- [ ] Write down key quotes
- [ ] Score 6 metrics using the rubric
- [ ] Manage time (hit all phases in 90 min)
- [ ] Handle red flags gracefully
- [ ] Thank participant genuinely
- [ ] Complete report same-day

---

**You're ready. Go test.** 💪

Questions? Review:
- USER_TESTING_PLAN.md (protocol overview)
- USER_TESTING_METRICS.md (scoring details)
- SESSION_REPORT_TEMPLATE.md (what to document)

