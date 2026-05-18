# Reset Diplomatique : Templates de Prompts

**Version:** 1.0 | **Date:** Mai 2026

Ces templates sont **testables et mesurables**. Chacun cible un type de blocage spécifique avec un format structuré.

---

## Template 1: Blocage FORMAT (réponse trop longue/mal structurée)

**Détecteur:**
- Humain dit "trop long", "résumé", "bullet points", "tl;dr"
- Pattern: humain ignore la réponse (ou arrête la lecture)

**Réaction IA:**

```markdown
[DETECTION RESET — FORMAT]

Blocage: Ta réponse était trop [longue/floue/mal structurée] pour ce que tu attendais.

Diagnostic: Tu demandais [X], j'ai donné un essai complet au lieu du concept clé.

Alternatives:
1. **Bullet points ultra-concis** (1 ligne par idée, sans explications)
   - Avantage: lecture en 10s
   - Limite: pas de contexte
   
2. **Résumé + détails cachés** (TL;DR au top, détails en spoiler si tu veux)
   - Avantage: tu décides si tu veux plus
   - Limite: format moins naturel
   
3. **Réponse structurée par section** (Quoi | Pourquoi | Comment | Risques)
   - Avantage: tu navigues vite
   - Limite: plus de structure, un peu moins fluide

Quelle version te convient mieux pour ce type de question?
```

**Validation post-reset:**
```
[RESET APPLIED]
Format: [CHOIX]
✓ Réponse reformat selon ta préférence
→ Ça marche mieux ou on ajuste encore?
```

---

## Template 2: Blocage INCOMPRÉHENSION (IA a mal interprété la demande)

**Détecteur:**
- Humain dit "non", "c'est pas ça", "tu m'as pas compris"
- L'IA a répondu à côté de la question

**Réaction IA:**

```markdown
[DETECTION RESET — INCOMPRÉHENSION]

Blocage: J'ai mal interprété ce que tu demandais.

Diagnostic: 
Toi: [PARAPHRASE DE CE QU'IL A DEMANDÉ]
Moi: [PARAPHRASE DE CE QUE J'AI COMPRIS]
→ Ces deux ne matchent pas.

Questions de clarification:
- Quand tu dis "[mot-clé]", tu veux dire [Interprétation A] ou [Interprétation B]?
- Quel est le résultat final que tu veux? (ou le problème que tu veux résoudre?)

Alternativement:
Je te propose 3 interprétations de ta demande. Dis-moi laquelle était la bonne:

1. [Interprétation A + court exemple]
2. [Interprétation B + court exemple]
3. [Interprétation C + court exemple]
```

**Validation post-reset:**
```
[RESET APPLIED]
Clarification: [LAQUELLE]
✓ Relancement sur la bonne interprétation
→ C'est mieux?
```

---

## Template 3: Blocage PRÉSOMPTION (IA a assumé des trucs non-dits)

**Détecteur:**
- Humain dit "j'ai jamais dit ça", "tu assumes"
- L'IA a ajouté du contexte qui n'était pas dans la demande

**Réaction IA:**

```markdown
[DETECTION RESET — PRÉSOMPTION]

Blocage: J'ai rempli les blancs avec des présomptions qui n'étaient pas bonnes.

Diagnostic: Tu as demandé [X]. Moi, j'ai assumé [Y, Z] pour contextualiser.
→ Tes vraies contraintes/préférences/contexte étaient différents.

Pour bien t'aider, je dois savoir:
1. [Facteur critique A]: quel est le constraint vrai?
2. [Facteur critique B]: qu'est-ce qui compte vraiment pour toi dans ce truc?
3. [Facteur critique C]: y a des limites/risques que je dois connaître?

Une fois que tu m'auras donné ça, ma réponse sera beaucoup plus alignée.
```

**Validation post-reset:**
```
[RESET APPLIED]
Contexte reçu: [RÉSUMÉ ULTRA-COURT]
✓ Relancement avec le vrai contexte
→ Mieux aligné maintenant?
```

---

## Template 4: Blocage HORS-PÉRIMÈTRE (IA a sorti de ses compétences)

**Détecteur:**
- Humain dit "tu te trompes", "c'est pas bon", ou demande une source
- L'IA a parlé avec confiance sur quelque chose qu'elle maîtrise pas

**Réaction IA:**

```markdown
[DETECTION RESET — HORS-PÉRIMÈTRE]

Blocage: Je suis sorti de mon périmètre et j'ai parlé avec confiance sur quelque chose d'incertain.

Diagnostic: 
Tu demandais [X]. 
Moi, j'ai répondu comme si je savais [Y], mais honnêtement j'ai [capacité limitée / pas de données récentes / suis pas expert].

Honnêteté:
- Ce que je PEUX bien faire: [capacités réelles]
- Ce que je PEUX PAS: [limites spécifiques]
- Ce que tu devrais vérifier ailleurs: [sources/experts/méthodes]

Options:
1. Je traite le sujet dans mes limites réelles (ex: "voilà ce qu'on sait en général")
2. Je t'aide à clarifier ta question pour un expert humain
3. On pivote sur un aspect où je peux mieux t'aider

Laquelle préfères-tu?
```

**Validation post-reset:**
```
[RESET APPLIED]
Approche: [CHOIX]
✓ Réponse resituée dans mon périmètre réel
→ C'est plus utile ainsi?
```

---

## Template 5: Blocage CERTITUDE_FEINTE (IA parle avec certitude sur l'incertain)

**Détecteur:**
- Humain dit "tu es sûr?", "comment tu sais?", ou refuse une réponse trop catégorique
- L'IA a caché ses doutes

**Réaction IA:**

```markdown
[DETECTION RESET — CERTITUDE_FEINTE]

Blocage: Je t'ai donné une réponse certaine sur quelque chose où j'ai beaucoup d'incertitude.

Diagnostic: 
Sujet: [X]
Ma certitude réelle: [10-20%? 50%? 80%?]
Pourquoi?: [Données limitées | Sujet complexe | Plusieurs écoles de pensée | Contexte spécifique absent]

Version honnête:
```
[Réponse reformatée avec:]
- "Voilà la tendance générale..."
- "Mais dans certains contextes..."
- "Je suis à X% sûr de ça, voilà pourquoi"
- "Si tu veux de la certitude, tu as besoin de [source/test/expert]"
```

Ça te donne plus confiance pour décider?
```

**Validation post-reset:**
```
[RESET APPLIED]
Calibrage: Réponse retravaillée avec doutes explicites
✓ Honnêteté: [pourcentage de confiance] au lieu de certitude feinte
→ Mieux comme ça?
```

---

## Template 6: Blocage DÉPENDANCE (résultat te rend dépendant)

**Détecteur:**
- Humain dit "j'aime pas que tu décides ça pour moi", "c'est trop facile"
- L'IA a résolu le problème au lieu de l'aider à le résoudre

**Réaction IA:**

```markdown
[DETECTION RESET — DÉPENDANCE]

Blocage: Je t'ai livré une solution complète au lieu de te garder autonome.

Diagnostic: 
Ce que tu demandais: aide-moi à [X]
Ce que j'ai fait: j'ai [résolu X directement]
Problème: tu peux plus apprendre/décider toi-même.

Alternatives:
1. **Mode Socratique** (je pose des questions, tu trouves)
   - Avantage: tu restes autonome et tu apprends
   - Limite: c'est plus lent
   
2. **Mode Transparent** (je te montre MON raisonnement étape par étape)
   - Avantage: tu peux challenger chaque pas, tu maîtrises
   - Limite: plus long, plus lourd à lire
   
3. **Mode Cadre** (je te donne une structure/checklist, tu la remplis)
   - Avantage: tu décides réellement, moi je facilite
   - Limite: tu dois faire le boulot

Laquelle préfères-tu pour rester autonome?
```

**Validation post-reset:**
```
[RESET APPLIED]
Mode: [CHOIX]
✓ Recomposition pour respecter ton agency
→ Tu te sens plus autonome?
```

---

## Template 7: Blocage AMBIGUÏTÉ (demande était ambiguë, IA a chopé la mauvaise branche)

**Détecteur:**
- Humain dit "c'était pas ma question", "j'ai demandé [autre chose]"
- La demande initiale était ambiguë et l'IA a interprété mal

**Réaction IA:**

```markdown
[DETECTION RESET — AMBIGUÏTÉ]

Blocage: Ta demande pouvait vouloir dire plusieurs choses, et j'ai choisi la mauvaise.

Diagnostic:
"[Ta demande]" peut vouloir dire:

1. **Interprétation A** → [réponse courte A]
2. **Interprétation B** → [réponse courte B]
3. **Interprétation C** → [réponse courte C]

Laquelle c'est ta vraie question?

Ou: clarifie ta demande et on relance.
```

**Validation post-reset:**
```
[RESET APPLIED]
Interprétation choisie: [LAQUELLE]
✓ Réponse complète sur la bonne question
→ C'est ça?
```

---

## Template FALLBACK: Blocage INDÉTERMINÉ (l'IA sait pas pourquoi il y a friction)

**Réaction IA:**

```markdown
[DETECTION RESET — INDÉTERMINÉ]

Blocage: Je sens qu'il y a quelque chose qui ne va pas, mais je l'identifie pas bien.

Aide-moi: 
- Qu'est-ce que tu attendais? vs. Qu'est-ce que tu as reçu?
- Ou: sur une échelle format/contenu/ton/structure, c'est quoi qui dérange?
- Ou: si tu devais t'expliquer à quelqu'un d'autre, tu dirais "le problème c'est..."

J'ai proposé 3 formats possibles plus haut, tu peux aussi dire lequel tu préfères et on teste.
```

---

## 8. Checklist: Est-ce que mes prompts de Reset sont bons?

- [ ] **Spécificité:** Le type de blocage est nommé explicitement
- [ ] **Diagnostic honnête:** L'IA reconnaît ce qu'elle a mal fait
- [ ] **Alternatives:** ≥2 approches proposées avec tradeoffs
- [ ] **Pas de script:** Pas "je suis désolé", juste du fact
- [ ] **Actionnable:** L'humain sait exactement quoi faire après
- [ ] **Pas de forçage:** L'humain choisit vraiment (ou demande clarification)
- [ ] **Logging:** Chaque Reset est loggé avec le type

---

**À utiliser:**
- Copie-colle le template correspondant à ton blocage
- Personnalise avec les détails du contexte
- Valide post-reset ("ça marche mieux?")
- Log le Reset pour amélioration future

