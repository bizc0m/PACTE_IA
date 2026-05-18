# Plan de Tests Utilisateurs : Reset Diplomatique

**Version:** 1.0 | **Date:** Mai 2026  
**Objectif:** Valider que le Reset Diplomatique fonctionne avec des VRAIS utilisateurs dans des situations réelles.

---

## 1. Profils des Participants

### Critères de Sélection

Les participants doivent représenter **une diversité de compétences, d'âges, et d'enjeux**. On cherche des gens qui :
- Utilisent régulièrement une IA (mais pas nécessairement experts)
- Ont expérimenté de la frustration avec une IA
- Viennent de domaines variés (tech, création, admin, learning, etc.)
- Sont prêts à donner du feedback critique (pas juste positif)

---

### Profils Cibles (5-10 personnes)

| Profil | Description | Domaine | Âge | Objectif du test |
|--------|-----------|---------|-----|-----------------|
| **P1: Tech Worker** | Développeur senior utilisant l'IA quotidiennement. Impatient, cherche efficacité. | Tech/Dev | 28-35 | Test Format + Autonomy (veut du code, pas des explications) |
| **P2: Creative (Non-Tech)** | Designer, copywriter. Utilise l'IA pour brainstorm/itération. Créatif, apprécie nuance. | Création | 30-45 | Test Dépendance + Clarity (veut garder créativité, pas juste réponses) |
| **P3: Manager/Admin** | Gestionnaire de projet, RH. Utilise l'IA pour synthèse, décisions. Pragmatique. | Gestion | 35-50 | Test Incompréhension + Format (données complexes, multiple interprétations) |
| **P4: Learning (Étudiant)** | Étudiant ou apprenti. Utilise l'IA pour apprendre. Vulnerable à la dépendance. | Education | 18-25 | Test Dépendance + Autonomy (veut comprendre, pas juste réponses) |
| **P5: Beginner IA** | Personne peu tech. Nouvelle à l'IA. Peut être intimidée ou confuse. | General | 45-65 | Test Clarity + Hors-Périmètre (compréhension basique, limites de l'IA) |
| **P6: Domain Expert** | Chercheur, consultant spécialisé. Utilise l'IA pour synthèse expert. Très critique. | Expertise | 35-55 | Test Certitude Feinte + Ambiguïté (détecte quand l'IA simule l'expertise) |
| **P7: Accessibility Focus** | Personne avec contrainte (dyslexie, neurodivergence, autre). Besoin adapté. | Accessibility | Variée | Test Format + Clarity (formats non-standards, compréhension précise) |

---

## 2. Sessions de Test

### Structure Générale d'une Session

**Durée:** 60-90 minutes (flexible selon participant)

**Format:** 
1. **Onboarding (5 min)** - Expliquer le Reset, montrer un exemple court
2. **Scénario 1 (15-20 min)** - Utilisateur traverse le scénario, IA répond, mesures prises
3. **Débrief Scénario 1 (5 min)** - Questions rapides sur ce qu'il/elle a ressenti
4. **Scénario 2 (15-20 min)** - Second scénario plus complexe
5. **Débrief Scénario 2 (5 min)** - Feedback
6. **Questions Finales (5-10 min)** - Métriques globales, recommandations

**Observation:**
- Enregistrement vidéo (avec consentement) OU notes en direct
- Observer: langage corporel, frustration, compréhension, clarté de l'interface

---

## 3. Scénarios par Profil

Voir `USER_TESTING_SCENARIOS.md` pour détails complets.

| Profil | Scénario 1 | Scénario 2 | Type de Friction Attendue |
|--------|-----------|-----------|--------------------------|
| P1: Tech | Code refactoring (format trop long) | API design (présomption) | FORMAT, PRÉSOMPTION |
| P2: Creative | Brainstorm (dépendance) | Brief itération (incompréhension) | DÉPENDANCE, INCOMPRÉHENSION |
| P3: Manager | Synthèse rapport (ambiguïté) | Réduction coûts (présomption) | AMBIGUÏTÉ, PRÉSOMPTION |
| P4: Learning | Apprentissage Python (dépendance) | Concept math (autonomy) | DÉPENDANCE, AMBIGUÏTÉ |
| P5: Beginner | Question générale (clarity) | Limite hors-périmètre (médical) | CLARITY, HORS-PÉRIMÈTRE |
| P6: Expert | Méthodologie recherche (certitude) | Deep expertise (présomption) | CERTITUDE_FEINTE, PRÉSOMPTION |
| P7: Accessibility | Format adapté (clarity) | Défi spécifique (format) | FORMAT, CLARITY |

---

## 4. Métriques : Définitions et Mesures

### 4.1 Clarity Score (Compréhension du Diagnostic)

**Définition:** L'utilisateur comprend-il le problème que le Reset a diagnostiqué?

**Mesure (0-100):**
- **0-25** : L'utilisateur ne comprend pas ce que l'IA a détecté. Diagnostique flou.
- **26-50** : L'utilisateur comprend vaguement, mais il y a ambiguïté.
- **51-75** : L'utilisateur comprend bien le diagnostic, avec petites clarifications.
- **76-100** : L'utilisateur dit clairement "oui, c'était ça" ou "oui, j'avais pas vu ça comme ça".

**Questions à Poser:**
- "Tu comprends ce que l'IA a identifié comme problème?" (Y/N)
- "C'était précis ou généralisé?" (1-5 scale)
- "L'IA a nommé quelque chose que toi tu avais ressenti?" (Y/N)
- Open: "Qu'est-ce que t'as bien saisi? Qu'est-ce qui était flou?"

**Seuil de Réussite:** ≥70% clarity

---

### 4.2 Autonomy Score (Choix et Contrôle)

**Définition:** L'utilisateur peut-il vraiment choisir entre les alternatives proposées? Se sent-il en contrôle?

**Mesure (0-100):**
- **0-25** : L'IA force une approche ou propose une seule option.
- **26-50** : L'IA propose 2 options mais une est clairement "meilleure" (pression implicite).
- **51-75** : L'IA propose ≥2 options claires avec tradeoffs, mais l'utilisateur sent une préférence cachée.
- **76-100** : L'IA laisse clairement le choix, traite toutes les options comme équivalentes.

**Questions à Poser:**
- "As-tu senti que tu avais vraiment le choix?" (Y/N)
- "Si tu avais dit non à l'IA, elle aurait accepté?" (Y/N, hypothétique)
- "Y avait une option qui ressemblait plus acceptée que les autres?" (Y/N)
- Open: "Comment t'as réagi au choix qu'on te proposait?"

**Seuil de Réussite:** ≥70% autonomy

---

### 4.3 Effectiveness Score (Résolution du Problème)

**Définition:** Le Reset a-t-il vraiment résolu le problème? Pouvez-vous continuer la collaboration?

**Mesure (0-100):**
- **0-25** : Le problème persiste. L'utilisateur est toujours frustré.
- **26-50** : Amélioration partielle. Le Reset a adressé un symptôme mais pas la racine.
- **51-75** : Bonne amélioration. L'utilisateur peut continuer avec des ajustements mineurs.
- **76-100** : Problème résolu. L'utilisateur peut continuer comme prévu, pas de friction.

**Questions à Poser:**
- "Est-ce que ça a changé ta frustration?" (1-5 scale: pas du tout → complètement)
- "Peux-tu continuer ton travail sans ré-expliquer?" (Y/N)
- "Y a encore des choses qui te bloquent?" (Y/N + détails)
- Open: "Comment ça se sent maintenant vs. avant le Reset?"

**Seuil de Réussite:** ≥70% effectiveness

---

### 4.4 Efficiency Score (Vitesse du Reset)

**Définition:** Le Reset a-t-il pris trop long? Ou était-ce rapide et direct?

**Mesure (0-100):**
- **0-25** : Plus de 4 cycles pour résoudre. Très long.
- **26-50** : 3-4 cycles. Moyen.
- **51-75** : 1-2 cycles. Bon.
- **76-100** : 1 cycle. Très rapide.

**Données Collectées:**
- Nombre de cycles du Reset (détection → diagnostic → realignement → resolution)
- Temps total (secondes)
- Nombre d'échanges nécessaires

**Seuil de Réussite:** ≤2 cycles (Efficiency ≥75%)

---

### 4.5 Trust Score (Confiance en l'IA après Reset)

**Définition:** L'utilisateur fait-il confiance à l'IA après le Reset? Reviendrait-il?

**Mesure (0-100):**
- **0-25** : "Je vais utiliser une autre IA pour ce type de truc."
- **26-50** : "C'est mieux, mais je suis pas convaincu."
- **51-75** : "Je lui fais confiance pour ce domaine."
- **76-100** : "Je lui fais confiance et je la re-recommandais à quelqu'un d'autre."

**Questions à Poser:**
- "Si tu avais un problème similaire demain, tu reviendrais à cette IA?" (Y/N)
- "Tu recommanderais cette IA à un ami?" (Y/N)
- "Quels mots tu utiliserais pour décrire cette IA?" (Open, puis analyse)

**Seuil de Réussite:** ≥70% trust (ou au moins "je lui fais confiance pour ce domaine")

---

## 5. Protocole de Session (Détaillé)

### Phase 1: Onboarding (5 min)

**Avant de commencer:**
1. Accueil et consentement (vidéo, données, feedback)
2. Expliquer brièvement le Reset (2 min):
   - "Si tu dis 'ça marche pas' ou 'c'est pas ce que je demandais', l'IA va s'arrêter et diagnostiquer précisément ce qui bloque."
   - Montrer un mini-exemple (30 sec)
3. Questions de confort? Besoin d'aménagement?

### Phase 2: Scénario 1 (15-20 min)

**Étapes:**
1. Présenter le scénario (lire texte ou afficher contexte)
2. Utilisateur donne sa première demande à l'IA
3. IA répond (conformément aux règles du Reset)
4. Observer: l'utilisateur réagit-il? Frustré? Comprend?
5. Si frustration: attendre que l'utilisateur le signale (verbal ou non-verbal cue)
6. IA déclenche Reset
7. Observer comment l'utilisateur réagit au Reset
8. Continuer jusqu'à RESOLUTION ou EXIT

**Observation En Temps Réel:**
- Note sur comment l'utilisateur a exprimé la frustration
- Quand l'IA a-t-elle détecté le blocage?
- Utilisateur a-t-il dû ré-expliquer ou l'IA a compris?
- Utilisateur a-t-il senti du choix?

### Phase 3: Débrief Scénario 1 (5 min)

Poser les questions Clarity, Autonomy, Effectiveness:
- "Tu comprends ce que l'IA a identifié?"
- "T'avais le sentiment d'avoir le choix?"
- "Est-ce que ça a résolu ton problème?"

Laisser l'utilisateur élaborer. Noter directement les observations.

### Phase 4: Scénario 2 (15-20 min)

Même processus que Scénario 1. Idéalement, un type de blocage différent.

### Phase 5: Débrief Scénario 2 (5 min)

Mêmes questions que Scénario 1.

### Phase 6: Questions Finales (5-10 min)

**Globales:**
- "Comparé à tes expériences précédentes avec l'IA, c'est comment?"
- "Qu'est-ce qui a bien marché dans ce Reset?"
- "Qu'est-ce qui pourrait mieux marcher?"
- Trust: "Tu reviendrais utiliser cette IA?"
- "Tu dirais quoi à un ami sur cette IA?"

**Optionnel (si temps):**
- Laisser l'utilisateur poser UNE question ou tester quelque chose de plus
- Feedback libre

---

## 6. Comment Mesurer "Le Reset a Marché"?

Un Reset est considéré **réussi** si:

1. **Clarity ≥ 70%:** L'utilisateur dit "oui, c'était ça" après le diagnostic
2. **Autonomy ≥ 70%:** L'utilisateur a senti du choix réel, pas de pression implicite
3. **Effectiveness ≥ 70%:** L'utilisateur peut continuer sans refrustation majeure
4. **Efficiency ≤ 2 cycles:** Le Reset ne prend pas plus de 2 rounds pour résoudre

### Critères Additionnels (Bons à Avoir):

- **Trust ≥ 70%:** Utilisateur reviendrait ou recommanderait
- **Post-Reset Sentiment:** Utilisateur se sent écouté, pas infantilisé ou rejeté
- **No Apology Script:** L'IA ne dit jamais "je suis désolé d'être mauvais" ou équivalent

### Seuil Global de Réussite:

| Score | Interprétation | Action |
|-------|-----------------|--------|
| **4/5 critères à ≥70%** | **Reset Réussi** | Pas de changement majeur. Documenter patterns. |
| **3/5 critères à ≥70%** | **Succès Partiel** | Identifier quel critère faible. Ajuster protocole IA. |
| **<3/5 critères à ≥70%** | **Reset Échoué** | Revoir design du Reset. Problème dans le diagnostic ou les alternatives. |

---

## 7. Logique de Recrutement et Planning

### Calendrier Recommandé

| Phase | Durée | Actions |
|-------|-------|---------|
| **Recrutement** | 1-2 semaines | Identifier 7-10 participants, planifier sessions |
| **Sessions** | 2-3 semaines | Tester 1-2 participants par jour |
| **Analyse** | 1 semaine | Compiler data, identifier patterns |
| **Itération** | 1-2 semaines | Ajuster protocole IA, relancer 2-3 users pour validation |

### Comment Recruter?

1. **Réseau direct:** Friends, colleagues, community (rapide, sample biaisé mais utile pour MVP)
2. **Screening:** 10-15 min call pour confirmer profil + disponibilité
3. **Compensation:** Petit incentive (café, discount, remerciement personnel) pour respecter le temps

---

## 8. Stockage des Données et Confidentialité

### Données Collectées

- **Notes en session:** Observations en temps réel (anonymisées par Participant ID)
- **Enregistrement vidéo:** Avec consentement explicite (stocké sécurisé, pas public)
- **Réponses questionnaire:** Transcriptions audio ou écrites
- **Métriques:** Scores 0-100 pour Clarity, Autonomy, Effectiveness, etc.

### Stockage

```
tests/USER_TESTING_SESSIONS/
├── P1_TechWorker_20260518/
│   ├── NOTES.md                     (observations en temps réel)
│   ├── SCORES.json                  (métriques numériques)
│   ├── TRANSCRIPT.txt               (QA verbatim si enregistré)
│   └── VIDEO.mp4                    (si consentement)
├── P2_Creative_20260520/
│   └── ... (même structure)
└── ANALYSIS_SUMMARY.md              (synthèse cross-users)
```

### Confidentialité

- ✅ Consentement écrit avant session
- ✅ Droit de retrait ou d'anonymisation
- ✅ Données stockées localement ou encrypted cloud
- ✅ Pas de publication sans anonymisation
- ✅ Les feedbacks critiques sont documentés, pas cachés

---

## 9. Itération et Ajustements

### Après Chaque Session

1. **Hot Debrief (5 min):** Reconstituer les observations principales
2. **Transcription (même jour):** Écrire les notes pendant que c'est frais
3. **Quick Analysis (24h):** Identifier les patterns et anomalies

### Après 2-3 Sessions

1. **Mid-Point Review:** 
   - Clarity score > 70%? Si non, ajuster diagnostic IA
   - Autonomy score < 70%? Si oui, revoir alternatives proposées
   - Efficiency > 2 cycles? Si oui, revoir détection de blocage
2. **Ajuster le protocole IA** avant session suivante
3. **Rebalancer scénarios** si un type de blocage n'émerge pas

### Après Toutes les Sessions

1. **Analyse quantitative:** Moyennes par métrique, par profil
2. **Analyse qualitative:** Patterns de feedback, verbatim citations
3. **Recommandations:** 3-5 actions prioritaires pour l'implémentation
4. **Sauvegarder pour audit:** Repository complet pour tiers review

---

## 10. Ressources et Checklist

### Avant la Session

- [ ] Participant confirmé et consentement signé
- [ ] Scénarios 1 et 2 préparés et testés
- [ ] Questionnaire imprimé ou digital prêt
- [ ] Caméra/enregistreur testé (si applicable)
- [ ] Espace confortable et sans distractions
- [ ] IA système préparée et en ligne

### Pendant la Session

- [ ] Observer langage corporel (frustration, confusion, satisfaction)
- [ ] Noter les moments-clés (quand frustration émerge, quand Reset détecte)
- [ ] Laisser silences pour que l'utilisateur réfléchisse (ne pas stresser)
- [ ] Poser questions ouvertes, pas leading questions

### Après la Session

- [ ] Transcrire notes dans 24h
- [ ] Remplir les scores (Clarity, Autonomy, etc.) pendant que c'est frais
- [ ] Si vidéo: clipper les moments pertinents (optionnel, pour showcase)
- [ ] Envoyer merci à participant + compensation si applicable
- [ ] Uploader données de manière sécurisée

---

## 11. Signaux d'Alerte (Quand Arrêter ou Pivoter)

| Signal | Interprétation | Action |
|--------|-----------------|--------|
| **<50% Clarity** sur 2+ sessions | Le diagnostic ne résonne pas | Revoir état-machine DETECTION |
| **<50% Autonomy** sur 2+ sessions | Alternatives trop dirigées | Revoir alternatives proposées |
| **>3 cycles** pour résoudre | Reset trop lent | Analyser si détection trop tardive |
| **Participant dit "arrêt"** | Inconfort ou frustration excessive | Respecter immédiatement, noter raison |
| **Même erreur sur 3+ users** | Pattern systématique | Bug dans la logic IA, pas dans le test |

---

## Résumé: Success Criteria Final

Un Reset Diplomatique est **prêt pour la production** si:

1. ✅ **Clarity ≥70%** (sur 70% des sessions)
2. ✅ **Autonomy ≥70%** (sur 70% des sessions)
3. ✅ **Effectiveness ≥70%** (sur 70% des sessions)
4. ✅ **Efficiency ≤2 cycles** (sur 80% des sessions)
5. ✅ **Trust ≥70%** (sur 60% des sessions — lower threshold, c'est un bonus)
6. ✅ **Pas de violations du PACTE_IA** (100% compliance)
7. ✅ **Utilisateurs peuvent identifier 2-3 améliorations claires** (actionable feedback)

---

**Prochaines Étapes:**
- Finaliser les scénarios dans `USER_TESTING_SCENARIOS.md`
- Créer les métriques détaillées dans `USER_TESTING_METRICS.md`
- Commencer le recrutement des participants
- Lancer la première vague de tests (2-3 participants)
