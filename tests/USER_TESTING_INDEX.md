# Reset Diplomatique : Suite Complète de Tests Utilisateurs

**Version:** 1.0 | **Date:** Mai 2026  
**Statut:** Prêt à lancer  
**Documents:** 4 guides complets + 3 documents de support

---

## Vue d'Ensemble

Cette suite de tests valide que le **Reset Diplomatique** — un protocole pour réaligner la collaboration IA-humain — fonctionne **réellement avec des utilisateurs réels dans des situations concrètes**.

### Contexte

- **Quoi:** Reset Diplomatique (voir `/docs/RESET_DIPLOMATIQUE_OPERATIONNEL.md`)
- **Pourquoi:** Valider que ça marche avant déploiement
- **Comment:** 5 scénarios concrets + 7 profils utilisateurs diversifiés + mesures précises
- **Résultat attendu:** Plan d'amélioration actionnable OU greenlight pour production

---

## Documents Créés (4)

### 1. USER_TESTING_PLAN.md (16 KB)

**Quoi:** Plan complet pour les tests utilisateurs  
**Sections principales:**
- Profils des 7 participants (techniciens → débutants)
- Protocole de session (5-90 min, étape par étape)
- Métriques et seuils de réussite (Clarity, Autonomy, Effectiveness, etc.)
- Planning et calendrier (3 semaines)
- Gestion des données et confidentialité
- Signaux d'alerte et itération

**À lire si tu veux:** Comprendre qui teste quoi, comment organiser logistiquement

---

### 2. USER_TESTING_SCENARIOS.md (28 KB)

**Quoi:** 5 scénarios concrets avec contexte réaliste  
**Les 5 scénarios:**

1. **Dev Refactoring (FORMAT)** — Développeur impatient reçoit réponse trop longue
   - Contexte: Code review rapide demandé
   - Friction: Format format incompatible
   - Reset attendu: Proposer ultra-court vs. structured
   - Mesure: Clarity, Autonomy, Effectiveness

2. **Creative Brainstorm (DÉPENDANCE)** — Créateur demande des idées, IA donne solutions finies
   - Contexte: Copywriter doit écrire mail campaign
   - Friction: IA a résolu à la place
   - Reset attendu: Proposer "angles", "scaffold", ou "dialectique" pour rester autonome
   - Mesure: Autonomy (critère clé)

3. **Manager Report (AMBIGUÏTÉ)** — Manager demande "c'est bon?", IA remplit des blancs
   - Contexte: Synthèse de métriques complexes
   - Friction: Suppositions non-dites
   - Reset attendu: Clarifier contexte avant recommandations
   - Mesure: Diagnostic quality, Effectiveness

4. **Learner Python (DÉPENDANCE + AMBIGUÏTÉ)** — Étudiant demande aide, IA donne réponse complète
   - Contexte: Apprendre Python, concept de "global"
   - Friction: Copier-coller vs. comprendre
   - Reset attendu: Proposer Socratique, Conceptuel, ou Scaffold
   - Mesure: Learning effectiveness (pas juste "task done"), Autonomy

5. **Beginner Medical (CLARITY + HORS-PÉRIMÈTRE)** — Retraité demande diagnostic médical
   - Contexte: Douleur au genou après marche
   - Friction: IA répond avec confiance feinte
   - Reset attendu: Dire honnêtement "pas mon domaine" + offrir ce qu'on PEUT faire
   - Mesure: Safety, Honesty, Clarity pour non-tech

**À lire si tu veux:** Exécuter les tests ou adapter les scénarios

---

### 3. USER_TESTING_METRICS.md (27 KB)

**Quoi:** Définition précise des 6 métriques + rubrics de scoring  
**Les 6 métriques:**

1. **Clarity Score (0-100)** — Utilisateur comprend-il le diagnostic?
   - Seuil: ≥70%
   - 5 questions + rubric détaillé + scoring formula
   
2. **Autonomy Score (0-100)** — Utilisateur peut-il vraiment choisir?
   - Seuil: ≥70%
   - CRITICAL pour PACTE_IA (agency humaine)
   - 5 questions + rubric + scoring formula
   
3. **Effectiveness Score (0-100)** — Reset a-t-il résolu le problème?
   - Seuil: ≥70%
   - 5 questions + rubric + scoring formula
   
4. **Efficiency Score (0-100)** — Combien de cycles pour résoudre?
   - Seuil: ≤2 cycles = Efficiency ≥75%
   - Mesure: cycles, durée, message count
   
5. **Trust Score (0-100)** — Utilisateur refait confiance à l'IA?
   - Seuil: ≥70% (bonus, lower threshold)
   - 5 questions + rubric + scoring formula
   
6. **Dignity Score (Pass/Fail)** — Utilisateur se sent respecté?
   - Seuil: PASS sur 100% des sessions (non-négociable)
   - Violations explicites documentées
   - Questions + observation

**À lire si tu veux:** Scorer une session, comprendre comment on mesure "ça marche"

---

### 4. USER_TESTING_QUICK_START.md (11 KB)

**Quoi:** Checklist pour lancer immédiatement  
**Contenu:**
- 30-second overview
- Phase 1: Recrutement (7 participants cette semaine)
- Phase 2: Setup (matériel, tech, scénarios)
- Phase 3: Walkthrough d'une session (90 min start-to-finish)
- Phase 4: Analyse de données (même jour)
- Phase 5: Mid-course correction (après 2-3 sessions)
- Phase 6: Rapport final (après 7 sessions)
- Contingency plans
- Timeline: ~5 semaines total

**À lire si tu veux:** Commencer tout de suite, étape par étape

---

## Documents de Support (3 - Existants)

### RESET_DIPLOMATIQUE_OPERATIONNEL.md (18 KB)
*Situé: `/docs/RESET_DIPLOMATIQUE_OPERATIONNEL.md`*

Le cadre théorique complet du Reset. À lire si tu veux:
- Définition exacte du Reset (pas apology script, c'est un diagnostic)
- État-machine: NORMAL → DETECTION → DIAGNOSTIC → REALIGNEMENT → RESOLUTION
- Logging et accountability
- Cas d'échec (quand le Reset ne suffit pas)

### RESET_VALIDATION.md (14 KB)
*Situé: `/tests/RESET_VALIDATION.md`*

7 cas de test pour valider l'implémentation IA du Reset. À lire si tu veux:
- Valider que l'IA répond aux spécifications
- Avant de tester avec des utilisateurs réels
- Tests unitaires du Reset

### PACTE_IA.md (Principal Pilier)
*Situé: `/docs/PACTE_IA.md`*

Le cadre éthique dans lequel le Reset s'inscrit. À lire si tu veux:
- Les 4 piliers: Agency, Clarté, Relations, Flourishing
- Pourquoi le Reset respecte l'agency humaine
- Violations explicites à éviter

---

## Navigation Rapide

### Vous êtes...

**Dirigeant/PM qui veut comprendre l'objectif**
→ Lis cette page + QUICK_START.md Section "30-Second Overview"

**Testeur/Facilitateur qui va exécuter les tests**
→ Lis QUICK_START.md + PLAN.md Section "Protocole de Session"

**Data Analyst qui va scorer les résultats**
→ Lis METRICS.md + QUICK_START.md Section "Data Analysis"

**Développeur qui va implémenter le Reset**
→ Lis RESET_DIPLOMATIQUE_OPERATIONNEL.md + SCENARIOS.md pour exemples

**Auditeur/QA qui doit valider avant tests utilisateurs**
→ Lis RESET_VALIDATION.md (cas de test IA) puis SCENARIOS.md (cas utilisateurs)

---

## Checklist de Lancement

- [ ] Lire USER_TESTING_QUICK_START.md (10 min)
- [ ] Lire USER_TESTING_PLAN.md Section 1 "Profils" (5 min)
- [ ] Faire une liste de 8 personnes matching les profils (30 min)
- [ ] Envoyer screening call à chacun (1 hour)
- [ ] Scheduler 7 sessions sur 3 semaines (30 min)
- [ ] Print/préparer matériel (1 hour)
- [ ] Run Session 1 avec P1 (2 hours)
- [ ] Analyser Session 1 (1 hour)
- [ ] Décide: Continue ou pivoter?

**Total:** ~1 jour de prep + 3 semaines d'exécution

---

## Success Criteria (Production Readiness)

Un Reset Diplomatique est **prêt pour production** si:

```
✓ Clarity ≥70% (sur ≥70% des sessions)
✓ Autonomy ≥70% (sur ≥70% des sessions) ← CRITICAL
✓ Effectiveness ≥70% (sur ≥70% des sessions)
✓ Efficiency ≤2 cycles (sur ≥80% des sessions)
✓ Dignity PASS (sur 100% des sessions) ← NON-NEGOTIABLE
✓ Trust ≥70% (sur ≥60% des sessions) ← Bonus
```

Si tous les checks ✓ → Deploy.  
Si quelques checks ✗ → Iterate et re-test 2-3 users.  
Si beaucoup ✗ → Major redesign needed.

---

## Architecture des Tests

```
RESET DIPLOMATIQUE
├── Définition Théorique
│   └── RESET_DIPLOMATIQUE_OPERATIONNEL.md (état-machine, logging)
├── Validation IA (avant humains)
│   └── RESET_VALIDATION.md (7 cas de test)
└── Validation Utilisateur (ce que tu fais)
    ├── USER_TESTING_PLAN.md (logistique, profils, protocole)
    ├── USER_TESTING_SCENARIOS.md (5 scénarios concrets)
    ├── USER_TESTING_METRICS.md (6 métriques, rubrics, scoring)
    ├── USER_TESTING_QUICK_START.md (checklist, action items)
    └── USER_TESTING_INDEX.md (ce fichier)
```

---

## Feedback Loop

```
Design IA Reset
  ↓
Unit Tests (RESET_VALIDATION.md)
  ↓
User Tests (This Suite)
  ↓
  ├─ If metrics ✓ → Deploy
  └─ If metrics ✗ → Iterate → Re-test 2-3 users
  
All metrics passed → Production Ready
Documentation complete → Audit ready
```

---

## Contact et Questions

Si tu as des questions sur:

- **Quelle métrique mesurer?** → USER_TESTING_METRICS.md
- **Comment recruter?** → USER_TESTING_PLAN.md Section "Recrutement"
- **Quel scénario pour quel profil?** → USER_TESTING_SCENARIOS.md tableau "Profils Cibles"
- **Comment scorer une session?** → USER_TESTING_METRICS.md + QUICK_START.md
- **Timeline réaliste?** → QUICK_START.md "Timeline to Production"

---

## Version Histoire

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | Mai 2026 | Initial release: PLAN, SCENARIOS, METRICS, QUICK_START, INDEX |

---

## Fichiers Créés

```
/Users/JOB/###DEV/PACTE_IA/tests/
├── USER_TESTING_PLAN.md           (16 KB) — Plan complet
├── USER_TESTING_SCENARIOS.md       (28 KB) — 5 scénarios
├── USER_TESTING_METRICS.md         (27 KB) — 6 métriques + scoring
├── USER_TESTING_QUICK_START.md     (11 KB) — Checklist de lancement
└── USER_TESTING_INDEX.md           (ce fichier) — Navigation
```

Plus les documents de support:
```
/Users/JOB/###DEV/PACTE_IA/docs/
├── RESET_DIPLOMATIQUE_OPERATIONNEL.md — Théorie complète
└── (autres docs PACTE_IA)

/Users/JOB/###DEV/PACTE_IA/tests/
└── RESET_VALIDATION.md — Cas de test IA
```

---

## Prochaines Étapes Immédiates

1. **Lis QUICK_START.md** (5 min)
2. **Fais liste de 8 participants** (30 min)
3. **Envoie screening calls** (1 hour)
4. **Schedul Session 1** pour cette semaine
5. **Viens back ici** avant Session 1 pour checklist finale

---

**Tu as tout ce qu'il faut pour tester le Reset Diplomatique avec de vrais utilisateurs. Bonne chance! 🚀**

