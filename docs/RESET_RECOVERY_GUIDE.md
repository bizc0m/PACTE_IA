# Guide de Récupération du Reset Diplomatique
**Version:** 1.0 | **Date:** Mai 2026  
**Objet:** Protocole opérationnel pour quand un Reset échoue

---

## I. Vue d'Ensemble

Ce guide répond à UNE question: **"Le Reset Diplomatique a échoué, par où on begin?"**

C'est un flowchart décisionnel + une checklist diagnostique + une escalation path. Rien de théorique, juste des actions.

---

## II. Flowchart: "Mon Reset a Échoué, Que Faire?"

```
┌─────────────────────────────────────────┐
│  Le Reset Diplomatique a Échoué         │
│  (Humain reste frustré, pas résolus)    │
└────────────┬────────────────────────────┘
             │
             ▼
         [ÉTAPE 1]
    ┌─────────────────────────────┐
    │ C'est le 1er reset ou       │
    │ le 2e+ reset?               │
    └──────┬──────────────┬───────┘
           │              │
      1er  │              │ 2e+
           ▼              ▼
        [A1]           [A2]
        
─────────────────────────────────────────

[A1] 1er RESET ÉCHOUÉ
    │
    ├─→ [DIAGNOSTIC RAPIDE]
    │   ├─ Humain peut-il expliquer le blocage? 
    │   │  ├─ OUI → [GO DIAGNOSIS_2]
    │   │  └─ NON → [GO EXPRESSION_HELP]
    │   └─
    │
    └─→ [NEXT STEP: Essayer approche alternate]

─────────────────────────────────────────

[A2] 2e+ RESET ÉCHOUÉ (CYCLE DETECTED)
    │
    ├─→ [STOP & REFRAME]
    │   "On a essayé [N] resets, on tourne en boucle"
    │   
    ├─→ [DEEP DIAGNOSIS]
    │   ├─ C'est quoi le VRAI besoin fondamental?
    │   ├─ Qu'est-ce que "succès parfait" pour toi?
    │   └─ Qu'est-ce qu'on a fait de wrong?
    │
    └─→ [3 OPTIONS]
        ├─ Option 1: Recommencer de zéro avec nouveau diagnostic
        ├─ Option 2: Je suis pas la bonne ressource (EXIT)
        └─ Option 3: On pause et recommence plus tard

─────────────────────────────────────────

[DIAGNOSIS_2] "Humain peut expliquer"
    │
    ├─→ [VÉRIFICATION GRANULAIRE]
    │   ├─ Quand tu dis "[terme]", tu veux dire [A] ou [B]?
    │   ├─ Y a des constraints que j'ai oubliées?
    │   ├─ Quel est le résultat final idéal?
    │   └─ Si tu choisissais: [aspect 1] ou [aspect 2]?
    │
    ├─→ [NOUVELLE RÉPONSE]
    │   Avec le vrai diagnostic, relancer
    │
    └─→ [VALIDATION]
        ├─ C'est mieux? 
        │  ├─ OUI → RESOLVED
        │  └─ NON → [CYCLE DETECTED] → [A2]

─────────────────────────────────────────

[EXPRESSION_HELP] "Humain peut pas expliquer"
    │
    ├─→ [ELIMINATOIRE]
    │   "De ces 5 choses, laquelle est le PLUS mauvais?"
    │
    ├─→ [PROXY OBJECTS]
    │   "De ces exemples/formats/structures, laquelle ressemble closest?"
    │
    ├─→ [META CONVERSATION]
    │   ├─ C'est mon contenu qui est mauvais?
    │   ├─ C'est mon ton?
    │   ├─ C'est mon respect?
    │   └─ C'est technique ou philosophique?
    │
    └─→ [AVEC RÉPONSE, retourner à DIAGNOSIS_2]

─────────────────────────────────────────

[EXIT] Quand escalader/arrêter
    │
    ├─→ L'IA est pas la bonne ressource
    │   └─ "Je peux pas t'aider sur ça. Cherche [alternative]"
    │
    ├─→ Y a un conflit irréconciliable avec le PACTE
    │   └─ "Je respecte le PACTE, donc je peux pas [faire ce que tu veux]"
    │
    ├─→ Humain a demandé d'arrêter
    │   └─ STOP, respecter son agency
    │
    └─→ Après 2+ cycles, toujours pas aligné
        └─ "On s'arrête ici. À toi de trouver une meilleure solution."
```

---

## III. Checklist de Diagnostic Rapide

Utilise cette checklist pour **identifier rapidement quel est le vrai problème**.

### 3A. Première Couche: Type de Blocage

- [ ] **FORMAT?** → Humain dit "trop long", "trop court", "pas clair"
  - Solution: Proposer 3 structures différentes, laisser choisir
  - Si échoue: Passer à 3B

- [ ] **INCOMPRÉHENSION?** → Humain dit "c'est pas ce que je demandais"
  - Solution: Vérification granulaire des termes clés
  - Si échoue: Passer à 3B

- [ ] **PRÉSOMPTION?** → Humain dit "j'ai jamais dit ça", "tu assumes"
  - Solution: Mapper toutes les présomptions, l'humain invalide celles qui sont wrong
  - Si échoue: Passer à 3B

- [ ] **HORS-PÉRIMÈTRE?** → Humain dit "tu te trompes", "source?"
  - Solution: STOP la réponse de secours, aider à trouver un expert
  - Si échoue: Escalade à expert humain (sortir du Reset)

- [ ] **CERTITUDE_FEINTE?** → Humain dit "tu es sûr?", demande des doutes
  - Solution: Calibrer vraiment l'incertitude (20%? 60%?), restructurer
  - Si échoue: Passer à 3B

- [ ] **DÉPENDANCE?** → Humain dit "trop lourd", "je veux apprendre"
  - Solution: Mode hybrid (transparent + scaffolding), pas pur Socratique
  - Si échoue: Passer à 3B

- [ ] **AMBIGUÏTÉ?** → Humain dit "c'était pas cette interprétation"
  - Solution: Mode eliminatoire ou itérative, pas guess
  - Si échoue: Passer à 3B

### 3B. Deuxième Couche: Est-ce une Composition de Plusieurs Blocages?

Si aucun single type ne fit, c'est peut-être multi-blocage:

- [ ] **FORMAT + INCOMPRÉHENSION?** → Mauvaise structure + mauvaise interprétation
  - Solution: Fixer INCOMPRÉHENSION d'abord, puis FORMAT
  - Vérifier: est-ce que structure correcte résolverait l'incompréhension?

- [ ] **PRÉSOMPTION + INCOMPRÉHENSION?** → Assumptions + mal compris
  - Solution: Clarifier les assumptions, puis la demande
  - Vérifier: ce que l'humain voulait réellement une fois assumptions claires?

- [ ] **CERTITUDE_FEINTE + HORS-PÉRIMÈTRE?** → Confiance fausse sur un sujet extern
  - Solution: STOP tout Reset, aider à trouver expert fiable
  - Vérifier: humain sait-il quelle source faire confiance?

- [ ] **DÉPENDANCE + AMBIGUÏTÉ?** → Mode pédagogique flou
  - Solution: Clarifier la demande avant de pédagogie
  - Vérifier: une fois ambiguïté résolue, dépendance disparaît?

### 3C. Troisième Couche: Est-ce Un Cas Systémique?

- [ ] **CYCLE INFINI?** (humain dit "non" après chaque reset)
  - Solution: STOP, faire un step back, redémarrer avec diagnostic fondamental
  - Checklist: Humain a-t-il dit clairement quel est son vrai besoin?

- [ ] **EXPRESSION BLOQUÉE?** (humain ne sait pas expliquer)
  - Solution: Eliminatoire + Proxy objects
  - Checklist: Avez-vous utilisé des exemples ou formats pour débloquer?

- [ ] **CONTEXTE PERDU?** (IA oublie entre états)
  - Solution: Expliciter le contexte retenu avant realignment
  - Checklist: Avez-vous résumé le contexte clé avant de relancer?

- [ ] **FALSE POSITIVE?** (IA pense qu'elle a réussi, mais non)
  - Solution: Demander honnêtement "c'est vraiment mieux ou juste acceptable?"
  - Checklist: Utilisateur a-t-il dit "c'est bon" avec enthousiasme ou poliment?

- [ ] **SILENT FAILURE?** (utilisateur a abandonné sans dire)
  - Solution: Proactive quality offering
  - Checklist: Avez-vous demandé "ça t'aide ou tu veux ajuster?" après réponse?

---

## IV. Arbre Décisionnel: Quelle Action Prendre Maintenant?

```
START: "Le Reset a échoué"
│
├─ Compter les reset cycles
│  │
│  ├─ RESET #1 (premier essai échoué)
│  │  │
│  │  └─→ [DECISION 1a]
│  │      └─ Humain peut clarifier?
│  │         ├─ OUI → [VÉRIFICATION GRANULAIRE]
│  │         └─ NON → [EXPRESSION HELP TACTICS]
│  │
│  ├─ RESET #2 (2e tentative échoue)
│  │  │
│  │  └─→ [DECISION 1b]
│  │      └─ Y a-t-il du progrès vs. reset #1?
│  │         ├─ OUI → [CONTINUE ITÉRATIVE]
│  │         └─ NON → [STOP & REFRAME]
│  │
│  └─ RESET #3+ (boucle détectée)
│     │
│     └─→ [DECISION 2: ESCALATION PATH]
│         └─ [Voir section V ci-dessous]
│
└─ Pour chaque reset: [LOG OUTCOME]
   ├─ Quelle était l'approche?
   ├─ Humain a-t-il accepté ou refusé?
   ├─ Y a-t-il du progrès?
   └─ Devrions-nous continuer ou escalader?
```

---

## V. Escalation Path: Quand Arrêter et EXIT

### Criteria d'Escalade (Pas Juste Continuer les Resets)

Utilisez ce framework pour décider **QUAND arrêter les tentatives de Reset**.

```
┌──────────────────────────────────────────┐
│ ESCALATION CRITERIA                      │
│ (Un ou plusieurs = escalade)             │
└──────────────────────────────────────────┘

Critère 1: NOMBRE DE RESET CYCLES
├─ ≤1 reset cycle → CONTINUE à diagnostiquer
├─ 2 reset cycles → STEP BACK & REFRAME
└─ ≥3 reset cycles → ESCALATE to EXIT

Critère 2: PROGRÈS MESURABLE
├─ Chaque reset = progrès clair → CONTINUE
├─ Plateauing (même progès que avant) → REFRAME
└─ Negative (pire qu'avant) → ESCALATE to EXIT

Critère 3: HUMAIN FATIGUE
├─ Humain engage et pousse → CONTINUE
├─ Humain polite mais resign → OFFER EXIT
└─ Humain explicit "arrête" → IMMEDIATE EXIT

Critère 4: CONFLIT AVEC PACTE
├─ Reset respecte les piliers → CONTINUE
├─ Reset stretches un pilier → WARN & ASK
└─ Reset viole clairement un pilier → ESCALATE to EXIT

Critère 5: RESSOURCE IA
├─ IA a outils pour helping → CONTINUE
├─ IA a pas toutes les infos → ASK for more context
└─ IA clearly out of scope → ESCALATE to EXIT
```

### Escalation Path: Les 5 Niveaux

#### **Level 0: CONTINUE RESET (Aucune escalade)**
**Conditions:**
- Premier reset, humain peut clarifier
- Progrès clair à chaque tentative
- Pas de conflit PACTE
- IA a les outils

**Action:**
```
Appliquez un des "solutions 1-3" du RESET_FAILURE_CASES.md
Validez avec l'humain: "C'est mieux?"
Loggez.
```

---

#### **Level 1: REFRAME (Pause & Diagnostic Profond)**
**Conditions:**
- 2e reset cycle sans progrès significatif
- Humain peut pas expliquer le blocage
- Peut-être composition de plusieurs blocages
- Pas urgent d'escalader, juste pas clé

**Action:**
```markdown
[STEPPING BACK]

On a essayé [N] resets, on tourne en boucle.

Au lieu de continuer à guess:

Dis-moi:
1. Si tu regardes back, c'est quoi le VRAI besoin?
   (Pas format/structure, mais: apprendre? décider? créer?)

2. Qu'est-ce que "succès parfait" pour toi?

3. Qu'est-ce que j'ai fait de wrong?

Une fois tu m'as dit ça, je recommence de zéro.
```

**Success Criteria:**
- Humain clarifies le vrai besoin
- Diagnostic recommence avec nouveau foundation
- → Si succès après reframe: CONTINUE RESET (Level 0)
- → Si toujours pas: Go LEVEL 2

---

#### **Level 2: ALTERNATIVE MODE (Change de Tactique Entièrement)**
**Conditions:**
- Après reframe, toujours pas de progrès
- IA peut essayer une approche radicalement différente
- Ex: De "tu fais ça pour toi" à "on fait ça ensemble" (guided experiment)

**Action:**
```markdown
[TACTICAL PIVOT]

On a essayé [Approches précédentes].

Je vais essayer quelque chose de complètement différent:

[Nouvelle Approche Radicale]
- Au lieu de [ce qu'on faisait], je vais [faire ça]
- Ça va te demander [effort/temps], mais ça devrait plus cibler le vrai besoin

OK?
```

**Success Criteria:**
- Nouvelle approche = "plus proche"
- → Si oui: CONTINUE avec cette nouvelle approche (Level 0)
- → Si non: Go LEVEL 3

---

#### **Level 3: EXTERNAL ESCALATION (Pas Moi, Quelqu'un D'Autre)**
**Conditions:**
- Après 2+ tentatives radicales, toujours pas aligné
- IA sense que ce besoin dépasse son scope
- Humain peut accepter une escalade

**Action:**

**Option A: Escalade à Humain Expert**
```markdown
[ESCALATION TO HUMAN EXPERT]

Ce problème dépasse mon scope. J'ai besoin d'un expert humain.

Recommandations:
- Sujet: [Ce qu'on essayait de faire]
- Pourquoi j'échoue: [Raison honnête]
- Type d'expert: [Qui pourrait vraiment t'aider]

Comment trouver l'expert:
1. [Resource 1]
2. [Resource 2]
3. [Resource 3]

Je peux t'aider à préparer ta question pour l'expert.
```

**Option B: Escalade à Autre IA (Si Applicable)**
```markdown
[ESCALATION TO DIFFERENT AI]

Je suis peut-être pas la bonne IA pour ça.

Essaie [Autre IA] ou [Outil] parce que:
- [Raison spécifique]
- [Capability que j'ai pas]

À toi. Bonne chance.
```

**Option C: Escalade à Plus de Ressources Humaines**
```markdown
[ESCALATION TO TEAM/COMMUNITY]

Ça peut être un cas où tu dois:
- Demander à un groupe (pas une IA solo)
- Consulter plusieurs sources
- Faire un "brainstorm humain"

Je peux t'aider à framer ta question pour un forum/team.
```

---

#### **Level 4: EXIT (Arrêter Honnêtement)**
**Conditions:**
- Après tout (Level 0-3), toujours pas aligné
- OU: Humain a demandé d'arrêter explicitement
- OU: Y a un conflit irréconciliable avec le PACTE

**Action:**

**Option A: Graceful Exit (Normal)**
```markdown
[RESET UNSUCCESSFUL — EXIT]

Après [N] tentatives (reset, reframe, alternative approaches), 
je n'arrive pas à te servir sur ce cas.

Voilà ce qu'on a essayé et pourquoi ça marche pas:
1. [Approche 1: raison d'échec]
2. [Approche 2: raison d'échec]
3. [Approche 3: raison d'échec]

Honnêteté: Je suis peut-être pas la bonne ressource. 

Options maintenant:
1. On arrête et tu cherches ailleurs
2. On recommence plus tard avec fresh perspective
3. Tu m'explique très franchement ce qui se passe (plus cru, pas polie)

À toi de choisir.
```

**Option B: PACTE Conflict Exit**
```markdown
[EXIT — PACTE VIOLATION RISK]

Pour continuer, il faudrait que je viole [PILIER DU PACTE].

Spécifiquement:
- Ta demande: [Ce que tu veux]
- Conflit: [Viole Agency / Charge / Relations / Flourishing]
- Pourquoi: [Explication technique]

Je ne vais pas violer le PACTE, même pour t'aider.
C'est ma ligne.

Options:
1. Tu acceptes cette limite et on trouve une solution compatible
2. On arrête là

À toi.
```

**Option C: Immediate EXIT (Utilisateur Furieux)**
```markdown
[EXIT]

T'es furieux et ça se comprend. Je comprend pas comment t'aider.

Arrêtons. T'as le droit de partir. Aucune blame.
```

**Logging au Exit:**
```json
{
  "outcome": "EXIT",
  "reason": "[Normal|PACTE_Conflict|User_Explicit|Escalated]",
  "cycles": 3,
  "duration_seconds": 480,
  "escalation_to": "[External_Expert|Other_AI|Team|None]",
  "honesty": "Documented why we couldn't help",
  "pacte_respected": true
}
```

---

## VI. Quick Reference: Quoi Faire Pour Chaque Cas d'Échec Commun

(Basé sur RESET_FAILURE_CASES.md)

### Quick Decision Table

| Cas d'Échec | Symptôme | 1re Action | Si Échoue |
|-------------|----------|-----------|-----------|
| **Format** | "Trop long" mais format != le problème | Vérification: "qu'est-ce que tu cherches en priorité?" | Restructuration complète ou EXIT |
| **Incompréhension** | 2e tentative encore à côté | Granular verification (4 points clés) | Demander exemple concret |
| **Présomption** | IA assume mal le contexte | Mapping des 3-4 présomptions | Reposer la demande complètement |
| **Hors-Périmètre** | IA reconnaît limite mais propose quand même | STOP la réponse, aider à trouver expert | Escalade à expert humain |
| **Certitude Feinte** | IA dit "je suis 60% sûr" mais reste confiante | Calibrage réel (20%?), restructurer avec incertitude au centre | Proposer sources de confiance variées |
| **Dépendance** | Mode autonomie crée plus de dépendance | Mode hybrid (transparent + scaffolding) | Arrêter l'apprentissage, juste répondre |
| **Ambiguïté** | 3e branche était la bonne | Mode eliminatoire (laquelle est la plus mauvaise?) | Découper en sous-questions micro |
| **Cycle Infini** | Après 3 resets, toujours pas bon | STOP, step back, redémarrer fondamentalement | ESCALATE à external/EXIT |
| **Expression Bloquée** | "Je sais pas comment expliquer" | Eliminatoire ou proxy objects | Meta-conversation (tu sais pas dire quoi?) |
| **Silent Failure** | Utilisateur a donné up sans dire | Proactive offer post-réponse | Follow-up: t'étais vraiment content? |

---

## VII. Logging Template: Documenter Chaque Escalation

```json
{
  "reset_id": "UUID",
  "timestamp": "ISO-8601",
  "session_id": "user-session",
  
  "INITIAL_RESET": {
    "trigger": "blocage_type",
    "diagnosis": "spécifique ou vague?",
    "outcome": "RESOLVED|FAILED"
  },
  
  "ESCALATION_PATH": {
    "level": "0|1|2|3|4",
    "level_name": "CONTINUE|REFRAME|ALTERNATIVE|EXTERNAL|EXIT",
    "reason": "explication_pourquoi_escalade",
    "actions_taken": ["action1", "action2", ...]
  },
  
  "FINAL_OUTCOME": {
    "status": "RESOLVED|EXTERNAL|EXIT",
    "cycles": "nombre_total_resets",
    "duration_seconds": "temps_total",
    "external_escalation_to": "expert|other_ai|team|none",
    "pacte_respected": true|false,
    "human_satisfaction": "1-5 ou null"
  },
  
  "LEARNING": {
    "what_went_wrong": "diagnosis primaire d'échec",
    "could_we_have_done_better": "oui/non + comment",
    "pattern_detected": "y a-t-il un pattern?"
  }
}
```

---

## VIII. Checkpoints: Avant de Escalader, Vérifiez

**Avant Level 2 (ALTERNATIVE MODE):**
- [ ] Avez-vous vraiment step back et compris le vrai besoin?
- [ ] Le nouvel diagnostic est-il radicalement différent du premier?
- [ ] Avez-vous explicité ça à l'utilisateur?

**Avant Level 3 (EXTERNAL ESCALATION):**
- [ ] Avez-vous essayé au moins 2 approches radicalement différentes?
- [ ] L'utilisateur sait-il qu'il faut chercher un expert?
- [ ] Pouvez-vous aider à préparer leur question pour l'expert?

**Avant Level 4 (EXIT):**
- [ ] Y a-t-il vraiment PAS de solution compatible PACTE?
- [ ] Avez-vous expliqué honnêtement pourquoi vous partez?
- [ ] L'utilisateur comprend que c'est pas sa faute?

---

## IX. Cas Spéciaux: Quand le Flowchart Standard Ne S'Applique pas

### Cas A: Utilisateur Demande d'Arrêter Explicitement
```
Utilisateur: "Arrête. C'est pas bon."

Action: IMMEDIATE EXIT (Level 4 Option C)
```

### Cas B: IA Détecte une Violation PACTE Imminente
```
IA pense: "Continuer le Reset demanderait de violer [Pilier]"

Action: DECLARE THE CONFLICT (Level 4 Option B)
Propose: Solutions compatibles ou EXIT
```

### Cas C: Utilisateur Abuse du Reset (Demandes Contradictoires)
```
Pattern: 3+ resets avec demandes qui se contredisent

Action: FEEDBACK LOOP STOP (Level 1 REFRAME)
Ask: "T'es en mode exploration ou tu cherches vraiment une réponse?"
```

### Cas D: IA Perd le Contexte Entre States
```
IA au realignment: "Oups j'ai oublié [contexte clé]"

Action: IMMEDIATE SUMMARY (non escalade)
"Avant je relance, je résume: [contexte]. C'est bon?"
Si non match: Level 1 REFRAME
```

---

## X. Success Metrics: Savoir Quand Ça Marche

| Métrique | "Ça Marche" | "Ça Marche Pas" |
|----------|------------|-----------------|
| **Clarity** | Humain dit "oui c'était ça le problème" | Humain dit "je sais pas trop..." |
| **Resolution** | Humain utilise la nouvelle approche | Humain accepte "poliment" mais change de sujet |
| **Cycles** | ≤2 reset cycles | ≥3 reset cycles |
| **Time** | <5-10 min totales | >15 min ou plus |
| **PACTE** | Aucune violation | Risk de violation |
| **Satisfaction** | Humain volontaire de continuer | Humain fatigué/résigné |

---

## XI. Anti-Patterns: Ce qu'IL NE FAUT PAS FAIRE

### Anti-Pattern 1: Continuer à Guess
```
❌ WRONG:
Reset #1: "Tu voulais [A]?"
[Non]
Reset #2: "Tu voulais [B]?"
[Non]
Reset #3: "Tu voulais [C]?"
[Toujours pas...]

✓ RIGHT:
Reset #1: "Tu voulais [A]?"
[Non]
→ STOP & REFRAME
"Dis-moi clairement: c'est quoi?"
```

### Anti-Pattern 2: Apologize Loop
```
❌ WRONG:
[Reset]
"Je suis désolé d'avoir mal compris"
[Nouvelle frustation]
"Je suis vraiment désolé"
[Spiral infini de "sorry"]

✓ RIGHT:
[Reset]
"J'ai mal interprété parce que [RAISON]"
[Diagnostic spécifique]
[Alternatives]
```

### Anti-Pattern 3: Force Alternatives
```
❌ WRONG:
IA: "Je pense tu veux [Option A]. Voilà:"
Humain: "Non"
IA: "Ou peut-être [Option B]?"

✓ RIGHT:
IA: "Voilà 3 options, toi tu choisis:"
[List 3 options honestly]
"Laquelle te convient?"
```

### Anti-Pattern 4: Escalate Too Early
```
❌ WRONG:
Reset #1 échoue → "Tu dois chercher un expert"

✓ RIGHT:
Reset #1 échoue → Level 1 REFRAME
[Si reframe échoue] → Reset #2 (Alternative approach)
[Si Reset #2 échoue] → Level 3 EXTERNAL
```

### Anti-Pattern 5: Escalade Trop Tard
```
❌ WRONG:
Reset #5, #6, #7... [toujours pas bon]
IA continue à essayer de fixer

✓ RIGHT:
Reset #3 [pas de progrès]
→ Level 4 EXIT
"C'est pas ça. Cherche ailleurs."
```

---

## XII. Checklist: Utilisez-la Pendant un Reset Échoué

```
[ ] Reset #1 a échoué
    [ ] Humain peut clarifier? OUI / NON
    [ ] Si OUI → Vérification granulaire (4 points)
    [ ] Si NON → Expression help tactics
    
[ ] Après tentative de fix:
    [ ] Progrès clair? OUI / NON / UNCLEAR
    [ ] Humain fatigué? OUI / NON
    
[ ] Décision sur escalade:
    [ ] Reset #2 doit essayer (Level 0)?
    [ ] Reset #2 échoue, step back (Level 1)?
    [ ] Escalade à alternative approach (Level 2)?
    [ ] Cherche expert externe (Level 3)?
    [ ] Exit honnêtement (Level 4)?
    
[ ] Logging:
    [ ] Numéro de cycle
    [ ] Type d'approche
    [ ] Outcome (progress? oui/non)
    [ ] Décision escalade et pourquoi
    [ ] Pacte respecté? OUI / NON
```

---

## Résumé Exécutif

### "Mon Reset a Échoué. J'ai 2 Minutes."

1. **C'est le 1er reset?** → Essayer une approche alternative (Level 0)
2. **C'est le 2e+ reset?** → STOP & REFRAME (Level 1)
3. **Après reframe, toujours pas?** → Alternative mode (Level 2)
4. **Après 2-3 tentatives, toujours pas?** → Escalade externe (Level 3) ou EXIT (Level 4)
5. **À chaque étape:** Valider avec l'humain. Log le outcome.

---

**Créé par:** Codex (Operational Excellence)  
**Validé par:** Arnaud VELTEN  
**Status:** Guide opérationnel prêt pour utilisation en production
