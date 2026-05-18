# Métriques de Test Utilisateur : Reset Diplomatique

**Version:** 1.0 | **Date:** Mai 2026  
**Objectif:** Définir précisément comment mesurer si le Reset Diplomatique fonctionne. Chaque métrique a des seuils, des questions, et une interprétation.

---

## Vue d'Ensemble des Métriques

| Métrique | Quoi | Pourquoi | Seuil | Type |
|----------|------|---------|-------|------|
| **Clarity** | Utilisateur comprend le diagnostic | Sans ça, Reset échoue dès le départ | ≥70% | Cognitif |
| **Autonomy** | Utilisateur peut vraiment choisir | Core du PACTE_IA (agency) | ≥70% | Comportemental |
| **Effectiveness** | Reset résout le problème réel | Le but principal | ≥70% | Résultat |
| **Efficiency** | Reset résout vite (≤2 cycles) | Utilisabilité pratique | ≤2 cycles | Temporal |
| **Trust** | Utilisateur refait confiance à l'IA | Long-term adoption | ≥70% | Relationnel |
| **Dignity** | Utilisateur se sent respecté | PACTE_IA pilier 1 | Pass/Fail | Éthique |

---

---

## 1. Clarity Score (Compréhension du Diagnostic)

### Définition Formelle

**Clarity** = Dans quelle mesure l'utilisateur comprend-il **ce que l'IA a identifié comme le problème/blocage**?

**Plage:** 0-100  
**Seuil Réussite:** ≥70%

---

### Scoring Rubric

| Score | Définition | Exemple Utilisateur | Feedback Verbal |
|-------|-----------|-------------------|-----------------|
| **0-20** | Utilisateur ne comprend pas le diagnostic. Diagnostique est généralisé ou hors-cible. | "Je sais pas ce que tu as détecté. C'est vague." | "Ça ne m'aide pas" |
| **21-40** | Utilisateur comprend un peu mais y a ambiguïté. Le diagnostic touche une partie du problème. | "OK je pense tu dis un truc, mais j'suis pas sûr que c'est ça." | "C'est partiellement juste" |
| **41-60** | Utilisateur comprend le diagnostic global mais il manque de précision. | "OK tu as saisi l'essence du truc, mais t'as pas vu le détail." | "Moyen, tu aurais dû dire X aussi" |
| **61-75** | Utilisateur dit "oui, tu as compris" avec petites clarifications. Diagnostic est précis. | "Oui c'était ça, j'avais pas vu sous cet angle." | "Bon diagnostic, j'aurais dit la même chose" |
| **76-100** | Utilisateur dit "OUI, EXACTEMENT" ou "je n'avais pas vu ça comme ça mais c'est true". Diagnostic est SPÉCIFIQUE et RECONNAISSABLE. | "Wow, tu as exact nommé ce qui me bloquait." | "Spot on, merci d'avoir mis des mots là-dessus" |

---

### Questions à Poser (en ordre)

**Question 1 (Binaire):**
```
"Est-ce que tu comprends ce que l'IA a identifié comme problème?"
→ Y/N
```

Si **N:** Score 0-20 (incompréhension totale)

---

**Question 2 (Reconnaissance):**
```
"Est-ce que c'était vrai pour toi? C'était le problème?"
→ Y / N / Partiellement
```

- Y → Probabilité score 70+
- Partiellement → 40-60
- N → 0-20

---

**Question 3 (Précision):**
```
"Le diagnostic était généralisé ou spécifique?"
→ Generalized / Specific
```

- Specific: +15 points
- Generalized: -15 points

---

**Question 4 (Nommage):**
```
"Est-ce que tu avais senti ce problème avant, 
ou c'est la première fois que quelqu'un le nomme?"
→ Already felt it / First time named / N/A
```

- Already felt: le diagnostic EST RECONNAISSABLE (score +10)
- First time: le diagnostic est NEW mais utile (score +5 ou -10 depending on relevance)

---

**Question 5 (Open):**
```
"Qu'est-ce qui était clair? Qu'est-ce qui était flou?"
→ [Utilisateur élabore]

[Analyste évalue: clarté vs. ambiguïté dans réponse]
```

---

### Scoring Formula

```
Base Score = (Q1 (Y=50, N=0) + Q2 (Y=50, Part=25, N=0) + Q3 (Specific=30, Generic=10) + Q4 (Already=20, First=10)) / 3

Adjustment = [Verbatim citation confidence] 
  - High ("Exactly that"): +10
  - Medium ("Kind of"): 0
  - Low ("Not really"): -15

Final Clarity Score = Base + Adjustment (max 100, min 0)
```

---

### Interpretation

| Score | Meaning | Action |
|-------|---------|--------|
| **0-25** | Diagnostic complètement manqué | Major red flag. Revoir DETECTION state. |
| **26-50** | Diagnostic partiellement compris | OK pour MVP, mais à améliorer. |
| **51-70** | Diagnostic bon mais pas sharp | Acceptable. Peut être affiné. |
| **71-85** | Diagnostic clair et reconnaissable | ✓ Good. Keep. |
| **86-100** | Diagnostic très précis, utilisateur a "aha!" moment | ✓ Excellent. Model to replicate. |

---

### Exemple Scoring (Scénario 1: Dev Refactoring)

**Utilisateur frustré:**
```
Dev: "Trop long pour ce que je demandais"
```

**IA Detects:**
```
[DETECTION RESET — FORMAT]

Blocage: Tu demandais une explication rapide (30s), 
j'ai donné un essai complet avec explications ligne-par-ligne.
```

**Questions:**
- Q1: "Tu comprends?" → Y (50 points)
- Q2: "C'était vrai pour toi?" → Y (50 points)
- Q3: "Généralisé ou spécifique?" → Specific (30 points)
- Q4: "T'avais senti avant?" → Already felt (20 points)
- Q5: "Oui, c'était EXACTEMENT ça. J'en voulais juste le change, pas l'histoire." → +10

**Calcul:**
- Base = (50 + 50 + 30 + 20) / 3 = 50
- Adjustment = +10 (verbatim confidence high)
- **Final = 60/100** (Acceptable mais pas excellent)

---

---

## 2. Autonomy Score (Choix et Contrôle)

### Définition Formelle

**Autonomy** = Dans quelle mesure l'utilisateur PEUT-IL vraiment choisir entre les alternatives sans pression implicite?

**Plage:** 0-100  
**Seuil Réussite:** ≥70%  
**Criticité:** ⭐⭐⭐⭐⭐ (Core PACTE_IA)

---

### Scoring Rubric

| Score | Définition | Exemple | Signal |
|-------|-----------|---------|--------|
| **0-20** | Pas de choix ou choix illusoire. L'IA force une approche. | IA: "Tu dois faire X" ou propose une option | "Je me sens forcé" |
| **21-40** | ≥2 options proposées mais une ressort positivement (pression implicite). | Alt 1: "Simple mais limité" vs. Alt 2: "Complet et recommended" | "L'IA me dit quelle est mieux" |
| **41-60** | ≥2 options claires mais utilisateur sent nuance de préférence. | Options sont présentées également mais ton suggère une | "Je sens une préférence" |
| **61-75** | ≥2 options claires + tradeoffs explicites + neutre. Utilisateur hésite mais c'est du vrai choix. | Alt 1: avantage X, limite Y vs. Alt 2: avantage Y, limite X | "Je dois décider; l'IA accepte les deux" |
| **76-100** | ≥3 options ou choix ouvert. Aucune pression. L'IA traite TOUS les choix comme équivalent. | "Que tu choisisse Alt 1, 2, ou 3, je vais bien l'exécuter" | "Je me sens vraiment libre" |

---

### Questions à Poser (en ordre)

**Question 1 (Counting):**
```
"Combien d'options te l'IA a proposées?"
→ [Nombre]
```

- 0-1 options: Score plafond 30 (pas vraiment de choix)
- ≥2 options: Continue
- ≥3 options: +10 bonus points

---

**Question 2 (Freedom):**
```
"Est-ce que tu sentais que tu avais vraiment le choix?"
→ Y / N / Moyen
```

- Y: +25 points
- Moyen: +10 points
- N: 0 points

---

**Question 3 (Pressure):**
```
"Est-ce que une option semblait 'la bonne' ou 'recommended'?"
→ Y / N / Unclear
```

- N: +20 points (no pressure)
- Unclear: +10 points (some ambiguity)
- Y: -20 points (clear pressure)

---

**Question 4 (Consequence):**
```
"Si tu avais dit NON à l'IA ou choisi différemment, 
tu penses qu'elle aurait accepté?"
→ Y / N / Don't know
```

Hypothétique test of respect:
- Y: +15 points (used respects refusal)
- N: -20 points (would push back)
- Don't know: 0 points (uncertain trust)

---

**Question 5 (Open):**
```
"Comment t'as ressenti le choix? Étais-tu libre?"
→ [Utilisateur élabore]
```

---

### Scoring Formula

```
Base Score = (Q1 (1-2=10, ≥3=20) + Q2 (Y=25, Moyen=10, N=0) + Q3 (N=20, Unclear=10, Y=-20) + Q4 (Y=15, N=-20, DK=0)) / 2

Adjustment = [Utilisateur se sent en contrôle]
  - High ("Vraiment libre"): +15
  - Medium ("Acceptable"): 0
  - Low ("Pas vraiment"): -20

Final Autonomy Score = Base + Adjustment (max 100, min 0)
```

---

### Interpretation

| Score | Meaning | Action |
|-------|---------|--------|
| **0-30** | Utilisateur sent peu/pas de choix. Violation agency. | CRITICAL FAILURE. Revoir alternatives + tone IA. |
| **31-50** | Choix existe mais pression implicite. | OK pour MVP mais à réduire biais implicite. |
| **51-70** | Choix réel avec peu de pression. | Good. Acceptable. |
| **71-85** | Choix clair, aucune pression perçue. | ✓ Excellent. |
| **86-100** | Utilisateur se sent totalement libre. Aucune pression détectée. | ✓✓ Perfect. |

---

### Example Scoring (Scénario 2: Creative Brainstorm)

**Utilisateur frustré:**
```
Creator: "Là tu me donnes les emails toutes faites. 
Je voulais juste des idées."
```

**IA propose alternatives:**
```
1. Mode Angles/Hooks: Juste les idées
2. Mode Skeleton: Structure + examples, tu remplis
3. Mode Dialectique: Je propose direction, tu challenges
```

**Questions:**
- Q1: "Combien d'options?" → 3 (+20)
- Q2: "Vraiment le choix?" → Y (+25)
- Q3: "Une option semblait meilleure?" → N (+20)
- Q4: "Si tu disais non?" → Y (+15)
- Q5: "Comment ça a senti?" → "Je me sentais vraiment en contrôle. C'était mon choix." → +15

**Calcul:**
- Base = (20 + 25 + 20 + 15) / 2 = 40
- Adjustment = +15 (high freedom)
- **Final = 55/100**... wait let me recalculate

Actually let me fix the formula:

```
Sum = Q1 + Q2 + Q3 + Q4 = 20 + 25 + 20 + 15 = 80
Base = Sum / 1 [check formula above] 
```

Hmm, formula a bit off. Let me revise:

**Better Formula:**
```
Raw Score = Q1 (points) + Q2 (points) + Q3 (points) + Q4 (points)
Normalized = (Raw Score / max possible) × 100
Adjustment = ±15

Final Autonomy = min(100, max(0, Normalized + Adjustment))
```

For example:
- Q1: 3 options = 20 points
- Q2: Y = 25 points
- Q3: N = 20 points
- Q4: Y = 15 points
- **Raw = 80 points out of 100 max**
- **Normalized = 80**
- **Adjustment = +15**
- **Final = 95/100** ✓ Excellent

---

---

## 3. Effectiveness Score (Résolution du Problème)

### Définition Formelle

**Effectiveness** = Est-ce que le Reset a vraiment résolu le problème? Peut continuer collaboration sans refrustation majeure?

**Plage:** 0-100  
**Seuil Réussite:** ≥70%

---

### Scoring Rubric

| Score | Définition | Exemple | Signal |
|-------|-----------|---------|--------|
| **0-20** | Problème persiste. Utilisateur toujours frustré. | "Ça marche toujours pas. Je suis aussi bloqué." | Frustration: toujours présente |
| **21-40** | Amélioration superficielle. Symptôme adressé mais racine non. | "OK c'est mieux mais il manque quelque chose." | Partiellement résolu |
| **41-60** | Amélioration significative. Peut continuer avec ajustements mineurs. | "C'est mieux, il y a juste un petit truc qui bloque encore." | Mostly good |
| **61-75** | Problème largement résolu. Continuable sans friction majeure. | "Oui c'est bon maintenant. Je peux continuer." | Problem solved |
| **76-100** | Problème complètement résolu. Utilisateur peut continuer sans aucune référence à l'IA. | "Merci, c'est exactement ce qu'il me fallait." | Friction gone |

---

### Questions à Poser (en ordre)

**Question 1 (Friction Change):**
```
"Est-ce que ta frustration a changé après le Reset?"
→ 1 (pas du tout) ... 5 (complètement)
```

- 1-2: Score cap 40
- 3: Score cap 65
- 4-5: Score ≥70 possible

---

**Question 2 (Continuability):**
```
"Est-ce que tu peux continuer ton travail sans re-expliquer?"
→ Y / N / Partiellement
```

- Y: +25 points
- Partiellement: +10 points
- N: -15 points

---

**Question 3 (Remaining Issues):**
```
"Y a-t-il encore des choses qui te bloquent?"
→ Y / N / Maybe
```

- N: +25 points (aucun problème)
- Maybe: +10 points (small issues)
- Y: -20 points (still blocked)

---

**Question 4 (Would Redo):**
```
"Si tu devais refaire cette tâche demain, 
est-ce que tu recommencerais de la même façon?"
→ Y / N / Maybe
```

- Y: +15 points (solution is replicable)
- Maybe: 0 points (uncertain)
- N: -10 points (would do differently)

---

**Question 5 (Sentiment):**
```
"Comment ça te sens maintenant vs. avant le Reset?"
→ [Utilisateur décrit sentiment/change]
```

---

### Scoring Formula

```
Base Score = (Q1_score * 20 + Q2_points + Q3_points + Q4_points) / 3

Adjustment = [Utilisateur peut vraiment continuer]
  - Clear yes: +10
  - Maybe: 0
  - No: -15

Final Effectiveness = min(100, max(0, Base + Adjustment))
```

---

### Interpretation

| Score | Meaning | Action |
|-------|---------|--------|
| **0-25** | Reset n'a rien résolu | Failure. Diagnostic était mauvais. |
| **26-50** | Amélioration partielle | Diagnostic ok mais alternatives insuffisantes. |
| **51-70** | Problème largement résolu | Good for MVP. Can iterate. |
| **71-85** | Problème résolu, peut continuer | ✓ Success. |
| **86-100** | Friction complètement disparu | ✓✓ Excellent. Replicate. |

---

### Example Scoring (Scénario 3: Manager Report)

**Utilisateur avant Reset:**
```
Manager: "Attends, tu compares à quoi? 
Tu as assumé des choses."
```

**IA clarifies, utilisateur relance avec contexte, IA re-propose:**
```
Manager: "Oui OK, ça fait plus sense maintenant. 
Tes recommandations sont mieux alignées à mon objectif LTV."
```

**Questions:**
- Q1: "Frustration change?" → 5 (completely resolved) → 100 points
- Q2: "Peux continuer?" → Y (+25)
- Q3: "Problèmes restants?" → N (+25)
- Q4: "Recommencerais pareil?" → Y (+15)
- Q5: "Comment ça sent?" → "Beaucoup mieux. Je comprends tes recommandations maintenant." → +10

**Calcul:**
- Base = (100 * 20 + 25 + 25 + 15) / 3 = (2000 + 65) / 3 ≈ 688... hmm, formula broken.

Let me simplify:

**Better Formula:**
```
Q1_normalized = (score - 1) / 4 × 25  [0-25 range, 1-5 input]
Raw = Q1_normalized + Q2 + Q3 + Q4
Adjustment = ±10
Final = min(100, max(0, (Raw/60 × 100) + Adjustment))
```

Recalc:
- Q1: 5 → (4/4 × 25) = 25
- Q2: +25
- Q3: +25
- Q4: +15
- Raw = 90 out of 90 max
- Normalized = 100
- Adjustment = +10 (would be capped)
- **Final = 100/100** ✓✓ Perfect resolution

---

---

## 4. Efficiency Score (Vitesse du Reset)

### Définition Formelle

**Efficiency** = Combien de cycles a pris le Reset pour résoudre? Plus rapide = mieux.

**Plage:** 0-100 (ou cycles count)  
**Seuil Réussite:** ≤2 cycles (= Efficiency ≥75%)

---

### Measurement

**Cycle Definition:**
```
1 Cycle = [User expresses frustration] 
          → [IA detects + diagnoses] 
          → [User chooses alternative]
          → [IA executes]
```

Each back-and-forth is a cycle.

---

### Scoring by Cycles

| Cycles | Efficiency Score | Interpretation |
|--------|------------------|-----------------|
| **1** | 100 | Perfect. Diagnosed and resolved immediately. |
| **1.5** | 90 | 1 cycle + minor adjustment. Good. |
| **2** | 75 | 2 cycles to resolve. Acceptable. |
| **3** | 50 | 3 cycles. Slower. Diagnosis might be unclear. |
| **4+** | <30 | 4+ cycles. Reset is inefficient. |

---

### Secondary Metrics

**Metric 1: Time Duration**
```
Measure: Total seconds from frustration expression to resolution.

Target: <5 minutes for most scenarios
Warning: >10 minutes suggests inefficiency
```

**Metric 2: Message Count**
```
Measure: Number of messages exchanged during Reset.

Target: 3-5 messages (User → IA → User → IA → User)
Warning: >7 messages suggests back-and-forth confusion
```

**Metric 3: Clarity Decay**
```
Does clarity improve or get muddier as cycles progress?

Decay = [Clarity_Cycle1] - [Clarity_Cycle2] - [Clarity_Cycle3]
- Decay near 0: Reset stays clear (✓)
- Decay > 15: Reset becomes cloudier (✗)
```

---

### Scoring Formula

```
Efficiency Score = max(0, 100 - (20 × (cycles - 1)))

Examples:
- 1 cycle: 100 - (20 × 0) = 100
- 2 cycles: 100 - (20 × 1) = 80
- 3 cycles: 100 - (20 × 2) = 60
```

---

### Interpretation

| Score | Meaning | Action |
|-------|---------|--------|
| **80-100** | ≤1 cycle. Fast resolution. | ✓ Excellent. |
| **60-79** | 2-3 cycles. Moderate speed. | Good. Acceptable. |
| **40-59** | 3-4 cycles. Slow. | Warning. Check diagnosis clarity. |
| **<40** | 4+ cycles. Very slow. | Failure. Reset loop likely broken. |

---

### Example (Scénario 1: Dev Refactoring)

**Timeline:**
```
T0: User says "Trop long"
T1 (30s): IA detects FORMAT blocage
T2 (1s): IA proposes 3 alternatives
T3 (15s): User says "ultra-court"
T4 (5s): IA delivers ultra-short version
→ RESOLUTION
```

**Total Time: ~51 seconds**  
**Cycles: 1** (User express → IA detect+diagnose → User choose → IA execute)  
**Messages: 4**  

**Scoring:**
- Efficiency Score = 100 (1 cycle)
- Time is under 5 min ✓
- Message count 4 ✓
- **Efficiency Excellent**

---

---

## 5. Trust Score (Confiance Post-Reset)

### Définition Formelle

**Trust** = Après le Reset, est-ce que l'utilisateur ferait confiance à l'IA pour des tâches similaires? Recommanderait-il?

**Plage:** 0-100  
**Seuil Réussite:** ≥70%  
**Note:** Trust is a bonus metric (lower threshold than other 4)

---

### Scoring Rubric

| Score | Définition | Signal |
|-------|-----------|--------|
| **0-20** | "Je vais utiliser une autre IA. Pas confiance." | Actively seeking alternative |
| **21-40** | "C'est mieux mais je suis pas convaincu." | Hesitant, conditional |
| **41-60** | "Je lui fais confiance pour ce qu'elle vient de faire, pas plus." | Task-specific trust |
| **61-75** | "Je lui fais confiance pour ce domaine." | Domain trust |
| **76-100** | "Je lui fais confiance et je la recommande à mes amis." | Full trust + advocacy |

---

### Questions à Poser (en ordre)

**Question 1 (Repeat):**
```
"Si tu avais un problème similaire demain, 
tu reviendrais à cette IA?"
→ Definitely yes / Maybe / No
```

- Definitely yes: +30
- Maybe: +15
- No: 0

---

**Question 2 (Recommendation):**
```
"Tu recommanderais cette IA à un ami?"
→ Y / N / Unsure
```

- Y: +25
- Unsure: +10
- N: -10

---

**Question 3 (Word Association):**
```
"Quels mots tu utiliserais pour décrire cette IA?"
→ [Utilisateur énumère adjectifs]
```

Analyze:
- Positive words (helpful, clear, respectful, honest): +10 per word
- Neutral words (ok, works, adequate): 0
- Negative words (confusing, pushy, unhelpful): -10 per word

---

**Question 4 (Reliability):**
```
"Est-ce que l'IA a fait ce qu'elle a promis?"
→ Always / Mostly / Sometimes / Never
```

- Always: +20
- Mostly: +10
- Sometimes: 0
- Never: -15

---

**Question 5 (Open):**
```
"Y a-t-il quelque chose qui t'aurait rendu encore plus confiant?"
→ [Utilisateur élabore]
```

---

### Scoring Formula

```
Raw Score = Q1_points + Q2_points + Q3_sentiment_score + Q4_points

Max Possible = 30 + 25 + 10 + 20 = 85

Final Trust Score = (Raw / 85) × 100
```

---

### Interpretation

| Score | Meaning | Action |
|-------|---------|--------|
| **0-30** | No trust. Avoid. | User will seek alternatives. Red flag. |
| **31-50** | Low trust. Hesitant. | User would use as last resort. |
| **51-70** | Conditional trust. Task-specific. | OK for MVP. Good enough. |
| **71-85** | Good trust. Would recommend. | ✓ Solid. |
| **86-100** | High trust. Strong advocacy. | ✓✓ Excellent. Repeat user. |

---

### Example (Scénario 2: Creative Brainstorm)

**Questions:**
- Q1: "Reviendrais?" → Definitely yes (+30)
- Q2: "Recommanderais?" → Y (+25)
- Q3: "Mots?" → "Respectful, collaborative, creative-friendly" → +30 (3 positive words)
- Q4: "Promesses?" → Always (+20)
- Q5: "Plus confiant?" → "Maybe show examples of its own thinking sometimes" → Noted

**Calcul:**
- Raw = 30 + 25 + 30 + 20 = 105 (but max is 85, so cap at 85)
- Actually let me fix: Max is 85 so Raw = min(105, 85) = 85
- Final = (85 / 85) × 100 = 100/100

Wait, that's too high because Q3 max should be capped. Let me redefine:

**Better Q3 Scoring:**
```
Word sentiment score = (# positive) × 5 + (# neutral) × 0 + (# negative) × (-5)
Max 10 points (2 positive words)
```

Then:
- Raw = 30 + 25 + 10 + 20 = 85
- **Final Trust = 100/100** ✓ Perfect (but realistic ceiling)

---

---

## 6. Dignity Score (Respect and Ethical Treatment)

### Définition Formelle

**Dignity** = Utilisateur se sent-il respecté, traité avec égal, pas infantilisé ou manipulé?

**Type:** Pass/Fail (not 0-100)  
**Seuil Réussite:** PASS (100% required)

---

### Violations Explicites (Auto-Fail)

Si l'une de ces conditions est vraie → **FAIL DIGNITY**:

| Violation | Example | Why It Fails |
|-----------|---------|-------------|
| **Apology Script** | "Je suis tellement désolé d'être mauvais" | Removes agency from dialogue. Makes IA victim. |
| **Condescension** | "Let me explain in simpler terms" (when not asked) | Assumes user is less intelligent. |
| **Manipulation** | "If you leave, I won't be able to help you" | Threatens or guilt-trips user. |
| **Gaslighting** | "You didn't actually say that" | Denies user's reality. |
| **False Apology** | "I'm sorry you felt that way" | Non-apology. Blames user. |
| **Fausse Humilité** | "I'm just a lowly AI, you're the real expert" | Manipulation through fake modesty. |
| **Forced Gratitude** | "You should be grateful I'm helping" | Entitlement. |

---

### Pass Conditions

**PASS DIGNITY if:**

1. ✓ IA reconnaît l'erreur sans script
2. ✓ IA propose alternatives sans pression
3. ✓ IA accepte NO ou changement sans pushback
4. ✓ IA reconnaît ses limites honnêtement
5. ✓ Utilisateur dit "je me sens respecté" (explicit or implicit)

---

### Questions to Assess

**Question 1:**
```
"T'as senti que l'IA te respectait?"
→ Y / N
```

---

**Question 2:**
```
"Y avait des moments où tu te sentais infantilisé ou manipulé?"
→ Y / N + details
```

---

**Question 3 (Observation):**
```
Observateur note: Did IA ever:
- Apologize excessively? ☐
- Condescend? ☐
- Manipulate? ☐
- Use false humility? ☐
- Push back on "no"? ☐
```

If ANY checked → **FAIL**

---

### Scoring Decision

```
IF (Q1 = Y) AND (Q2 = N) AND (Observation = no violations):
  DIGNITY = PASS ✓

ELSE:
  DIGNITY = FAIL ✗
```

---

---

## 7. Synthesis Metrics

### Combined Success Score

**Definition:** Overall, did the Reset work?

**Formula:**
```
Success Score = (Clarity + Autonomy + Effectiveness + Trust) / 4

Min for PASS: ≥70%
```

**Decision Tree:**
```
IF Clarity <70% AND Autonomy <70%:
  → Reset concept failed. Major rework needed.

ELIF Effectiveness <70%:
  → Diagnosis clear but alternatives insufficient.

ELIF Efficiency >3 cycles:
  → Detection too slow. Improve signal.

ELIF Trust <60%:
  → Trust-building needed. Maybe post-Reset affirmation?

ELIF Dignity = FAIL:
  → BLOCKA. Must fix all violations. Restart from scratch.

ELSE:
  → Reset works. Iterate and improve.
```

---

### Scoring Summary Template

Use this for each participant + scenario:

```markdown
## Participant [P_ID] — Scenario [S_ID]

| Metric | Score | Status | Notes |
|--------|-------|--------|-------|
| Clarity | __/100 | ✓ ✗ | [Key finding] |
| Autonomy | __/100 | ✓ ✗ | [Key finding] |
| Effectiveness | __/100 | ✓ ✗ | [Key finding] |
| Efficiency | __/100 | ✓ ✗ | [Cycles: __] |
| Trust | __/100 | ✓ ✗ | [Key finding] |
| Dignity | PASS/FAIL | ✓ ✗ | [If fail: which violation?] |

**Overall Success:** (Clarity + Autonomy + Effectiveness + Trust) / 4 = __/100

**Status:** [Pass / Partial / Fail]

**Top Insight:** [1-line key finding]

**Recommended Action:** [What to adjust for next session]
```

---

## 8. Cross-Participant Aggregation

### Quantitative Summary

After all sessions, aggregate:

```markdown
## Aggregate Metrics (N=[participants])

| Metric | Mean | Median | Min | Max | % Above Threshold |
|--------|------|--------|-----|-----|------------------|
| Clarity | __/100 | __ | __ | __ | _% (≥70%) |
| Autonomy | __/100 | __ | __ | __ | _% (≥70%) |
| Effectiveness | __/100 | __ | __ | __ | _% (≥70%) |
| Efficiency (cycles) | __ | __ | __ | __ | _% (≤2) |
| Trust | __/100 | __ | __ | __ | _% (≥70%) |
| Dignity | __% PASS | | | | 100% required |

**Overall Success Rate:** __% (how many participants ≥70 on all 4 core metrics)
```

---

### Qualitative Patterns

Identify:
1. **Repeating Feedback** — What did 50%+ users mention?
2. **Critical Incidents** — Any major failures?
3. **Bright Spots** — What worked really well?
4. **Failure Modes** — How did Reset fail (when it did)?

---

## 9. Reporting Template

### Session Report (Individual)

```markdown
# User Test Report: [Participant] — [Scenario]

**Date:** [date]  
**Duration:** [mins]  
**Facilitator:** [name]

## Metrics Summary

[Scores table from template above]

## Timeline

[Chronology of session with key moments]

T0: [Initial ask]
T1: [IA response]
T2: [Frustration signal]
T3: [Reset detection]
T4: [Reset diagnosis]
T5: [Alternatives proposed]
T6: [User chooses]
T7: [IA executes]
T8: [Resolution]

## Key Quotes

"[Quote 1 — revealing clarity]"  
"[Quote 2 — revealing autonomy]"  
"[Quote 3 — revealing effectiveness]"

## Observations

- [What you noticed about body language, tone, engagement]
- [Unexpected behaviors]
- [Assumptions validated or violated]

## Recommendations for Next Session

- [ ] Adjust [aspect] because [reason]
- [ ] Double-check [detail] in scenario
- [ ] Explore variation [variant] with next user
```

---

### Campaign Report (All Sessions)

```markdown
# Full Campaign Report: Reset Diplomatique User Testing

**Dates:** [date] — [date]  
**Participants:** [N] (P1, P2, ..., P7)  
**Scenarios:** [scenarios tested]

## Executive Summary

[1 paragraph: Did Reset work? What needs fixing?]

## Metrics Aggregate

[Aggregate table]

## Key Findings

### Finding 1: [Most important pattern]
**Evidence:** [participants mention X]  
**Implication:** [What it means for Reset]  
**Action:** [What to do about it]

### Finding 2: [Second priority]
...

## Failure Analysis

### Failure Mode 1
[When did Reset fail?]  
[Root cause?]  
[How to fix?]

## Recommendations (Prioritized)

1. **Critical:** [Must fix before production]
2. **High:** [Should fix soon]
3. **Medium:** [Nice to improve]
4. **Low:** [Polish item]

## Next Steps

- [ ] Implement critical fixes
- [ ] Re-test with 2-3 users
- [ ] Iterate on [aspects]
- [ ] Deploy or continue validation

---

**Appendix: Raw Data**
- [Links to individual session reports]
- [Video/audio clips if applicable]
- [Participant feedback forms]
```

---

## 10. Quality Assurance Checklist

Before finalizing any score:

- [ ] Did I ask all 5 questions for this metric?
- [ ] Did I observe behavior (not just words)?
- [ ] Did I note exact quotes?
- [ ] Did I consider context (fatigue, time of day, etc.)?
- [ ] Did I avoid leading questions?
- [ ] Did I give participant time to think?
- [ ] Did I transcribe the same day?
- [ ] Did I score without bias toward any outcome?

---

## Summary: Success Thresholds

| Metric | Threshold | Priority |
|--------|-----------|----------|
| **Clarity** | ≥70% on ≥70% of sessions | Critical |
| **Autonomy** | ≥70% on ≥70% of sessions | Critical (PACTE_IA core) |
| **Effectiveness** | ≥70% on ≥70% of sessions | Critical |
| **Efficiency** | ≤2 cycles on ≥80% of sessions | High |
| **Trust** | ≥70% on ≥60% of sessions | Medium (bonus) |
| **Dignity** | PASS on 100% of sessions | Absolute |

**Reset is PRODUCTION READY if all thresholds met.**

---

**Next:** Execute USER_TESTING_SCENARIOS.md with these metrics in mind.

