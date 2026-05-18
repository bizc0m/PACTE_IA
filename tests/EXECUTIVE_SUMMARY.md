# Reset Diplomatique : Plan de Tests Utilisateurs — Résumé Exécutif

**Version:** 1.0 | **Date:** Mai 2026  
**Pour:** Dirigeants, Sponsors, Stakeholders  
**Durée de Lecture:** 5 minutes

---

## Le Challenge

Nous avons créé un nouveau protocole appelé **Reset Diplomatique** — un mécanisme pour réaligner la collaboration quand l'IA et l'utilisateur se désalignent.

**Question Critique:** Ça marche vraiment avec de **vrais utilisateurs** dans des **situations réelles**?

**Risques si on ne teste pas:**
- ❌ Deploy une feature qui semble bonne en théorie mais échoue en pratique
- ❌ Utilisateurs se sentent manipulés ou infantilisés
- ❌ Damage à la confiance (plus difficile à réparer après deployment)

---

## La Solution: Suite Complète de Tests Utilisateurs

### Qui va tester?

**7 utilisateurs diversifiés** représentant les vrais cas d'usage:

1. **Tech Worker** (impatient, veut de l'efficacité)
2. **Creative** (auteur, copywriter — cherche collaboration pas solution)
3. **Manager** (pragmatique, données complexes)
4. **Student/Learning** (vulnerable à la dépendance)
5. **Beginner (Non-Tech)** (retraité, nouveau à l'IA)
6. **Expert** (chercheur — detecte les fake expertise)
7. **Accessibility** (personne avec contrainte spécifique)

### Quoi va-t-on tester?

**5 scénarios concrets:**

| Scénario | Problème Testé | Contexte Réel |
|----------|-----------------|---------------|
| Dev Refactoring | Format incompatible | Dev demande code review rapide, reçoit essai |
| Creative Brainstorm | Dépendance | Creator demande ideas, reçoit solutions finies |
| Manager Report | Ambiguïté | Manager demande "c'est bon?", IA remplit blancs |
| Learning Python | Dépendance + Autonomy | Student demande aide, reçoit réponse complète |
| Medical Question | Hors-Périmètre | Beginner demande diagnostic, IA répond avec certitude |

### Comment va-t-on mesurer?

**6 métriques précises:**

| Métrique | Seuil | Ce qu'on Mesure |
|----------|-------|-----------------|
| **Clarity** | ≥70% | Utilisateur comprend le diagnostic? |
| **Autonomy** | ≥70% | Utilisateur peut vraiment choisir? ← CRITICAL |
| **Effectiveness** | ≥70% | Reset résout vraiment le problème? |
| **Efficiency** | ≤2 cycles | Reset prend pas trop long? |
| **Trust** | ≥70% | Utilisateur refait confiance? |
| **Dignity** | 100% PASS | Utilisateur se sent respecté? ← NON-NEGOTIABLE |

Chaque métrique a:
- 5 questions précises à poser
- Un rubric de scoring détaillé (0-100)
- Un seuil de réussite défini

---

## Timeline & Ressources

### Calendrier

| Phase | Durée | Actions |
|-------|-------|---------|
| Recrutement | 1 semaine | Identifier 7 participants |
| Sessions | 2-3 semaines | Tester 1-2 participants/jour |
| Analyse | 1 semaine | Compiler scores + patterns |
| Itération (si nécessaire) | 1-2 semaines | Fix critical issues + re-test |

**Total: 5-7 semaines** (peut être compressé avec parallélisation)

### Ressources Nécessaires

- **Faciltateur:** 1 personne (60-80 heures)
- **Analyst:** 1 personne (30-40 heures)
- **IA System:** Accès à l'IA implémentée (online)
- **Compensation:** Café/merci/petit cadeau pour chaque participant (~50-100€ total)
- **Matériel:** Caméra/enregistreur, formulaires imprimés ou digital

**Budget Total:** ~$2-5K (minimal)

---

## Success Criteria (Go/No-Go Decision)

### Reset is PRODUCTION READY if:

```
✓ Clarity ≥70% (sur ≥70% des sessions)
✓ Autonomy ≥70% (sur ≥70% des sessions)  [CRITICAL]
✓ Effectiveness ≥70% (sur ≥70% des sessions)
✓ Efficiency ≤2 cycles (sur ≥80% des sessions)
✓ Dignity PASS (sur 100% des sessions)  [NON-NEGOTIABLE]
```

**IF all checks ✓:** Deploy immediately.  
**IF 1-2 checks fail:** Fix identified issues + re-test 2-3 users.  
**IF 3+ checks fail:** Major redesign needed.

---

## Deliverables

### Documents Créés (100% Complete)

1. **USER_TESTING_PLAN.md** (16 KB)
   - Profils de participants
   - Protocole détaillé
   - Planning
   - Confidentialité

2. **USER_TESTING_SCENARIOS.md** (28 KB)
   - 5 scénarios concrets
   - Contexte → Friction → Reset attendu → Mesure
   - Cas d'échec documentés
   - Variations à tester

3. **USER_TESTING_METRICS.md** (27 KB)
   - 6 métriques définies
   - Rubrics de scoring
   - Formulas de calcul
   - Templates d'agrégation

4. **USER_TESTING_QUICK_START.md** (11 KB)
   - Checklist de lancement
   - Étape-par-étape walkthrough
   - Contingency plans
   - Tools nécessaires

5. **USER_TESTING_INDEX.md** (10 KB)
   - Navigation entre documents
   - Vue d'ensemble complète

6. **SESSION_REPORT_TEMPLATE.md** (9 KB)
   - Template pour chaque session
   - Sections pré-remplies
   - Checklist qualité

---

## Risk Assessment

| Risque | Probabilité | Impact | Mitigation |
|--------|-------------|--------|-----------|
| Participants cancellent | Medium | Low | Recruit 8-9 backup candidates |
| IA crash pendant session | Low | Medium | Video demo as backup |
| Metrics don't align | Low | High | Peer review scoring, double-scoring |
| Participants don't understand Reset | Medium | High | Better onboarding, visual demo |
| Reset violates PACTE_IA | Low | CRITICAL | Dignity check (PASS/FAIL) on 100% |

---

## Next Steps: Week 1

### Immediate Actions (This Week)

1. **Approve this plan** — Green light to proceed
2. **Assign facilitator** — Who runs the sessions?
3. **Assign analyst** — Who scores the data?
4. **Recruit participants** — Start outreach (screening calls)
5. **Prep materials** — Print scenarios, consent forms, questionnaires

### Decision Point: After 2-3 Sessions

Based on early data, decide:
- **Continue as planned** (metrics look good)
- **Pivot scenario** (one scenario not producing expected friction)
- **Redesign Reset** (fundamental issues with diagnosis/alternatives)
- **Halt for major fix** (critical violations detected)

### Final Decision: Week 6

After all 7 sessions + analysis:
- **✓ DEPLOY:** All success criteria met
- **⏸ ITERATE:** Fix 1-2 issues + re-test 2-3 users
- **✗ REDESIGN:** Major issues found, significant rework needed

---

## Key Innovation

This test suite is **NOT a survey** (asking people's opinions).  
It's **NOT a focus group** (discussing the concept).

It's a **behavioral test**: Watch how real people interact with the Reset in realistic scenarios. Measure objectively.

This gives us:
- ✅ Real feedback, not opinions
- ✅ Metrics-based decisions, not gut feel
- ✅ Confidence that it works before scale-up
- ✅ Documented evidence for stakeholders

---

## Alignment with PACTE_IA

The Reset Diplomatique is grounded in **PACTE_IA**, our ethical framework for AI.

This test suite specifically validates:
- ✅ **Agency** (users can choose, can say no)
- ✅ **Clarity** (diagnostic is understandable)
- ✅ **Dignity** (users feel respected, not manipulated)
- ✅ **Accountability** (every Reset is logged, measurable)

If a Reset violates any pillar → **AUTOMATIC FAIL** (Dignity = PASS/FAIL)

---

## FAQ

**Q: Why 7 users? Isn't that too few?**  
A: MVP is 3. Seven gives us confidence across profiles. More is diminishing returns.

**Q: How long does each session really take?**  
A: 90 min planned. Usually 60-75 min actual. Budget 2 hours with setup.

**Q: Can we run sessions in parallel?**  
A: Only if you have multiple facilitators. Sequential is better (you learn after each).

**Q: What if Reset doesn't score well?**  
A: That's why we test! Better to find issues now than after deployment.

**Q: What happens with the video recordings?**  
A: Stored securely, anonymized. Participants can request deletion. Not published.

**Q: What if participants want to withdraw?**  
A: Completely OK. They can withdraw anytime. Remove their data upon request.

---

## Contact & Ownership

- **Test Plan Owner:** [Name TBD]
- **Facilitator:** [Name TBD]
- **Data Analyst:** [Name TBD]
- **Sponsor/Stakeholder:** [Your Name]

---

## Conclusion

We have a **complete, ready-to-execute testing plan** that will tell us definitively whether the Reset Diplomatique works.

**Cost:** ~$2-5K  
**Timeline:** 5-7 weeks  
**Risk:** Low (robust validation before scale-up)  
**Upside:** High confidence in deployment, ethical validation, user feedback for iteration  

**Recommendation:** Approve and launch this week.

---

## Next Document to Read

- **Executives/Sponsors:** This file (you're reading it) ✓
- **Project Managers:** USER_TESTING_QUICK_START.md
- **Facilitators:** USER_TESTING_PLAN.md + SCENARIOS.md
- **Analysts:** USER_TESTING_METRICS.md
- **Developers:** RESET_DIPLOMATIQUE_OPERATIONNEL.md + SCENARIOS.md for examples

---

**Questions? Contact [TBD] or review the full documentation in /tests/**

