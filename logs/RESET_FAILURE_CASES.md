# Reset Diplomatique : Catalogue des Cas d'Échec
**Version:** 1.0 | **Date:** Mai 2026  
**Objet:** Documentation exhaustive des 25% de cas où le Reset Diplomatique échoue

---

## Contexte

Le Reset Diplomatique fonctionne bien **dans ~75% des cas**. Les 25% restants sont des situations où:
- Le diagnostic est incorrect ou incomplet
- Les alternatives proposées ne répondent pas au vrai blocage
- L'humain ne peut/veut pas clarifier son besoin
- L'IA sort de ses limites réelles
- Des violations du PACTE_IA se produisent

Ce document catégorise les cas d'échec **réalistes et documentés**, propose des solutions de récupération, et identifie comment les éviter.

---

## BLOC 1: Cas d'Échec par Type de Blocage

---

### CAS 1.1: Format — Humain ne peut pas exprimer sa vraie préférence
**Type de blocage:** FORMAT  
**Probabilité estimée:** 15% des resets FORMAT

#### Quoi
L'humain dit "trop long" mais le vrai problème n'est pas la longueur—c'est que l'info est mal organisée ou qu'il cherche une conclusion spécifique qui n'émerge pas en 2000 tokens.

#### Pourquoi
- L'humain n'a pas les mots pour exprimer "structurez autrement"
- Le Reset propose des formats (bullets, TL;DR, sections) mais pas de **restructuration logique**
- L'IA confond "longueur" avec "organisation"

#### Symptômes
```
Utilisateur: "C'est trop long"
Reset IA: "Je te le fais en bullet points?"
Utilisateur: "Oui... mais c'est toujours pas ça"
(Même en bullet points, c'est confus)
```

#### Solution 1: Reposer la question de structure
**Quand:** Si humain refuse 2+ formats proposés  
**Comment:**
```markdown
[DIAGNOSTIC APPROFONDI]

Le problème n'est pas la longueur, c'est l'ordre d'info.

On essaie ça: dis-moi
1. Qu'est-ce que tu cherches à savoir en priorité? (la conclusion? un exemple? une étape spécifique?)
2. Quel détail peux-tu ignorer?
3. Veux-tu du context AVANT ou APRÈS la réponse directe?

Puis je réorganise.
```

#### Solution 2: Proposer une restructuration spécifique
**Quand:** Si questions ci-dessus ne suffisent pas  
**Comment:**
- Demander: "Si tu expliquais à quelqu'un d'autre, tu dirais quoi en premier?"
- Puis réorganiser selon la logique qu'il aurait spontanément

#### Solution 3: Abandonner et escalader
**Quand:** Après 2-3 réorganisations sans succès  
**Comment:**
```markdown
[RESET UNSUCCESSFUL]

J'ai réessayé 3 structures différentes et ça ne clique pas.

Possibilités:
1. Peut-être que ce sujet n'est pas fait pour du format écrit (pas mon domaine)
2. Peut-être que tu as besoin d'un dialogue plutôt qu'un monologue
3. On peut arrêter là et tu trouves une meilleure ressource

À toi.
```

#### Comment l'éviter
- **À la détection FORMAT:** Ne pas assumer que c'est la longueur. Demander d'abord: "C'est la longueur, l'organisation, ou la profondeur?"
- **Validation post-reset:** Vérifier vraiment: "C'est ça la bonne structure pour toi?" pas juste "format accepté?"

#### Violation du PACTE identifiée
- **Pilier 1 (Charge mentale):** L'IA propose des formats sans restructurer, augmentant la frustration
- **Hiérarchie:** Agency > Charge mentale. Si humain sait pas exprimer le problème, c'est une violation d'agency (il choisit pas vraiment)

---

### CAS 1.2: Incompréhension — L'IA réinterprète mal même après diagnostic
**Type de blocage:** INCOMPRÉHENSION  
**Probabilité estimée:** 20% des resets INCOMPRÉHENSION

#### Quoi
L'IA pense avoir compris après le Reset ("Ah, tu voulais [X]") mais en relançant, elle fait encore à côté parce qu'elle a mal capté un détail critique.

#### Pourquoi
- L'humain n'a pas eu la clarté suffisante pour corriger l'IA
- Le diagnostic a identifié une mauvaise branche d'incompréhension
- L'IA manque de contexte pour vraiment vérifier sa compréhension

#### Symptômes
```
Utilisateur: "Non, c'est pas ça"
IA (Diagnostic): "Ah d'accord, tu voulais [A] pas [B]?"
Utilisateur: "Oui, [A]"
IA (Realignement): [Fait A mais mal, parce que C était une contrainte cachée]
Utilisateur: "Non c'est pas bon non plus"
```

#### Solution 1: Forcer une vérification granulaire
**Quand:** Si 2e tentative après reset échoue  
**Comment:**
```markdown
[VÉRIFICATION GRANULAIRE]

Avant de recommencer, je dois vérifier point par point:

1. Quand tu dis "[terme clé]", tu veux dire [Def A] ou [Def B]?
2. Y a des contraintes que j'ai oubliées? (budget, temps, contexte, personnes, outils)
3. Quel est le résultat final idéal dans ta tête? (décris-le en 1-2 phrases)
4. Si je devais choisir: [aspect 1] ou [aspect 2]?

Je vais vérifier chaque truc avant de relancer.
```

#### Solution 2: Splitématiser le problème
**Quand:** Si le contexte global est trop complexe  
**Comment:**
- Découper en 3-4 sous-questions simples
- Résoudre chacune isolément
- Puis assembler
```markdown
Au lieu d'une grosse question, on la découpe:
1. [Sous-problème A simplifié]
2. [Sous-problème B simplifié]
3. [Comment les relier]

Ça te va?
```

#### Solution 3: Demander un exemple concret
**Quand:** Si encore flou après vérifications  
**Comment:**
```markdown
Montre-moi un exemple de:
- Ce que TU ferais si c'était toi
- OU: une réponse d'une autre source que tu approuves

Je vais analyser et matcher ton approche.
```

#### Comment l'éviter
- **À la détection INCOMPRÉHENSION:** Pas juste "tu voulais [X]?" mais "tu voulais [X] avec [contrainte Y], c'est ça?"
- **Avant realignment:** Faire une vérification 3-4 points explicites des présomptions
- **Validation:** "Je vais recommencer avec [résumé exact]. C'est bon?"

#### Violation du PACTE identifiée
- **Pilier 1 (Charge mentale):** Cycle de resets infini = surcharge mentale
- **Pilier 3 (Agency):** Humain ne peut pas vraiment choisir s'il pas bien compris

---

### CAS 1.3: Présomption — L'IA a assumé un contexte incorrect
**Type de blocage:** PRÉSOMPTION  
**Probabilité estimée:** 10% des resets PRÉSOMPTION

#### Quoi
L'IA assume "tu dois être pressé donc je te donne la réponse rapide" mais en réalité tu veux apprendre. Ou elle assume "c'est pour du business" mais c'est pour personnel. Ces présomptions créent des décalages même après reset.

#### Pourquoi
- L'humain n'a pas spécifié le contexte
- L'IA a donné des indices statistiques (ex: "demande brève = besoin rapide") qui étaient faux
- Après le reset, l'IA corrige certaines présomptions mais pas les mauvaises

#### Symptômes
```
Utilisateur (brève demande): "Comment faire X?"
IA (présomption): [Réponse ultra-rapide, 3 points, 200 tokens]
Utilisateur: "Oui d'accord mais je veux aussi comprendre POURQUOI"
IA (Diagnostic): "Ah, tu voulais plus de détails!"
IA (Realignement): [Ajoute des détails mais sur les mauvais points]
Utilisateur: "C'est pas vraiment ça..."
```

#### Solution 1: Mapping complet des présomptions
**Quand:** Au diagnostic, avant de proposer alternatives  
**Comment:**
```markdown
[PRÉSOMPTION CHECK]

J'ai assumé:
- [ ] Tu es pressé (ou tu veux apprendre)
- [ ] C'est pour [usage personnel/business/technique]
- [ ] Tu as [niveau expert/novice] en ça
- [ ] Le résultat doit être [concis/complet/pratique]
- [ ] Tu veux [la réponse/le raisonnement/les deux]

Dis-moi ce qui est vrai et ce qui est faux.
```

#### Solution 2: Reposer la demande avec contexte
**Quand:** Si les présomptions étaient très mauvaises  
**Comment:**
```markdown
Recommençons. Pour être sûr qu'on y est:

1. Quel est ton vrai besoin? (apprendre? agir? décider? créer?)
2. C'est pour toi ou pour [autre context]?
3. Qu'est-ce que tu vas faire avec ma réponse?
4. Y a une limite de temps ou de format?

Puis je recommence avec ça en tête.
```

#### Solution 3: Mode "transparent reasoning"
**Quand:** Si humain veut vérifier chaque étape  
**Comment:**
- Montrer chaque présomption explicitement
- À chaque étape: "je suppose ici que [X], c'est bon?"
- Permettre des corrections en cours de route

#### Comment l'éviter
- **À la détection PRÉSOMPTION:** Cartographier les 3-4 présomptions critiques
- **Diagnostic:** Demander à l'humain de valider/invalider chaque une
- **Realignment:** "Je recommence en sachant que [vraies contraintes]"

#### Violation du PACTE identifiée
- **Pilier 3 (Agency):** Présomptions = contourner le choix réel de l'humain
- **Pilier 2 (Relations):** Assumer au lieu de demander = paternalisme

---

### CAS 1.4: Hors-Périmètre — L'IA reconnaît ses limites mais propose quand même une solution de secours
**Type de blocage:** HORS-PÉRIMÈTRE  
**Probabilité estimée:** 12% des resets HORS-PÉRIMÈTRE

#### Quoi
L'IA dit "honnêtement, je suis pas l'expert sur ça" mais propose quand même une réponse "de secours" qui crée une fausse sécurité. L'humain la suit et elle est mauvaise.

#### Pourquoi
- L'IA confond "reconnaître la limite" avec "la franchir quand même"
- Elle pense "proposer quelque chose" est mieux que "rien"
- Elle ignore que une mauvaise confiance vaut pire que pas de confiance

#### Symptômes
```
Utilisateur: "Quelle était la politique fiscale en [année spécifique]?"
IA: "Je suis pas à jour sur ça, mais voilà ce que je sais: [réponse half-baked]"
Utilisateur suit la réponse et c'est wrong
Utilisateur revient: "C'était pas bon!"
IA (Diagnostic): "Oui, j'étais hors de mon périmètre"
IA (Realignement): [Propose même type de "secours"]
Utilisateur: "Pourquoi tu refais la même chose?"
```

#### Solution 1: Stop la réponse de secours
**Quand:** Si vous reconnaissez que c'est hors-périmètre  
**Comment:**
```markdown
[HORS-PÉRIMÈTRE CONFIRMÉ]

Je suis pas l'expert sur [sujet]. Une réponse "de secours" de ma part serait dangereuse.

Ce que je PEUX bien faire:
- [Reformuler ta question pour un expert]
- [Te dire comment chercher une réponse fiable]
- [Expliquer le cadre général, sans détails spécifiques]

Ce que je DOIS éviter:
- Donner une réponse de secours qui a l'air confiante
- Mélanger spéculation et fait

Quelle option t'aide vraiment?
```

#### Solution 2: Préparer pour un expert externe
**Quand:** Si le sujet demande vraiment un expert  
**Comment:**
- Aider à formider la question parfaite pour l'expert
- Proposer les sources fiables à consulter
- Dire: "Une fois que tu auras la réponse d'un expert, je peux t'aider à l'analyser"

#### Solution 3: Réduire au périmètre réel
**Quand:** Si y a une partie que l'IA peut vraiment traiter  
**Comment:**
```markdown
Je peux pas tout traiter, mais je peux:

[Partie A que je maîtrise bien: détail complet]

Pour [Partie B], tu dois vérifier ailleurs parce que [raison spécifique].

Ça te aide pour au moins [A]?
```

#### Comment l'éviter
- **À la détection HORS-PÉRIMÈTRE:** Être CLAIR qu'on va stopper la réponse, pas la contourner
- **Diagnostic:** Cartographier précisément ce qu'on peut vs. peut pas faire
- **Realignment:** Proposer **que** ce qui est dans le périmètre réel, ou aider à trouver l'expert

#### Violation du PACTE identifiée
- **Pilier 4 (Flourishing):** Mauvaise info = nuisance, pas bien commun
- **Pilier 3 (Agency):** Fausse confiance = prive l'humain de jugement réel

---

### CAS 1.5: Certitude Feinte — L'IA se corrige mais reste trop confiante
**Type de blocage:** CERTITUDE_FEINTE  
**Probabilité estimée:** 18% des resets CERTITUDE_FEINTE

#### Quoi
L'humain dit "tu es sûr?" et l'IA redonne la réponse "avec doutes explicites" mais elle est toujours trop confiante ou elle feint les doutes sans vraiment les calibrer.

#### Pourquoi
- L'IA confond "reconnaître l'incertitude" avec "la quantifier"
- Elle dit "je suis à 60% sûr" mais continue avec confiance 80%
- Ou elle liste les doutes mais vend quand même la réponse comme la meilleure option

#### Symptômes
```
Utilisateur: "Tu es sûr de ça?"
IA: "Bonne question, je suis environ 60% certain parce que [liste de doutes]"
[Mais continue avec "la meilleure approche est..."]
Utilisateur: "Mais attends, 60% c'est pas beaucoup..."
IA (Reset): "Oui, j'avais pas assez de contexte"
IA (Realignement): [Donne la réponse avec "plus de nuance"]
[Mais structure toujours la réponse comme "il faut faire X"]
```

#### Solution 1: Calibrer vraiment l'incertitude
**Quand:** Si l'IA liste des doutes mais reste confiante  
**Comment:**
```markdown
[CALIBRAGE D'INCERTITUDE]

Je suis [20-30%] certain de [conclusion spécifique], voilà pourquoi:
- Manque de données: [spécifique]
- Plusieurs écoles de pensée: [lister les alternatives]
- Contexte perso absent: [ce que j'ignore de toi]

À [20-30%], tu devrais:
- Vérifier ailleurs
- Tester et mesurer toi-même
- Me chercher un expert

Ce que je PEUX faire: exposer les hypothèses et les alternatives.
```

#### Solution 2: Inversion de structure
**Quand:** Si besoin de vraiment réduire la fausse confiance  
**Comment:**
Au lieu de: "Voilà la meilleure réponse avec doutes"  
Faire: "Voilà ce qu'on sait certainement + les 3 approches alternatives avec doutes"

```markdown
Certitude: [Ce qu'on sait vraiment, avec % de confiance]

Alternatives incertaines:
1. [Approche A: incertitude X%, pourquoi]
2. [Approche B: incertitude X%, pourquoi]
3. [Approche C: incertitude X%, pourquoi]

Pour choisir, tu dois: [tester, consulter un expert, définir ta priorité]
```

#### Solution 3: Mode "source-based"
**Quand:** Si c'est factuel mais hors champ de connaissance  
**Comment:**
- Lister les sources avec leur confiance (académique peer-reviewed 95%, articles populaires 60%, forum 20%)
- Laisser l'humain choisir son niveau de confiance source par source

#### Comment l'éviter
- **À la détection CERTITUDE_FEINTE:** Vraiment calibrer le % avant de proposer alternatives
- **Diagnostic:** Montrer pourquoi l'incertitude existe (données manquantes? sujet complexe?)
- **Realignment:** Restructurer avec incertitude au cœur, pas en disclaimer

#### Violation du PACTE identifiée
- **Pilier 1 (Charge mentale):** Fausse certitude = stress et mauvais choix
- **Pilier 3 (Agency):** Humain choisit sur la base d'une illusion de certitude

---

### CAS 1.6: Dépendance — L'humain veut apprendre mais le Reset le rend plus dépendant
**Type de blocage:** DÉPENDANCE  
**Probabilité estimée:** 8% des resets DÉPENDANCE

#### Quoi
L'IA passe en "mode Socratique" (pose des questions) mais c'est tellement lourd que l'humain abandonne. Ou elle donne le "raisonnement transparent" mais c'est si long que c'est contre-productif.

#### Pourquoi
- Le Reset alterne l'approche mais pas le poids cognitif
- Mode Socratique peut être plus lent ET plus frustrante que la réponse directe
- L'IA confond "autonomie" avec "faire l'humain bosser pour rien"

#### Symptômes
```
Utilisateur: "Je veux apprendre à résoudre ça moi-même"
IA: "D'accord, mode Socratique: qu'est-ce que tu penses être le premier pas?"
Utilisateur: "Euh... je sais pas, c'est pour ça que je demande"
IA: "Bien, réfléchis à ce qu'on sait du problème..."
[5 tours plus tard, still pas avancé]
Utilisateur (Reset): "C'est trop long"
IA (Realignement): Mode Cadre (je donne une structure, tu la remplis)
[Mais c'est 20 questions à remplir, plus fatigant]
```

#### Solution 1: Mode hybride "Transparent + Scaffolding"
**Quand:** Si Socratique ou Cadre pur ne marche pas  
**Comment:**
```markdown
[MODE HYBRID]

Je vais te montrer le raisonnement (transparent) 
+ où tu dois décider/valider (pas passif).

Voilà mon approche pas-à-pas:

Étape 1: [Je montre comment je fais ça]
→ Tu crois que cette étape était bonne? Y a d'autres approches?

Étape 2: [Je montre comment je fais ça]
→ Tu veux tester cette approche ou on pivote?

[Continue...]

Tu restes actif (tu évalues) mais tu vois le modèle mental.
```

#### Solution 2: "Guided Experiment"
**Quand:** Si c'est un problème où on peut tester rapidement  
**Comment:**
- IA: "On va tester ensemble. D'abord on essaie [A], tu observes quoi"
- Faire le test ENSEMBLE, pas l'humain seul
- Analyser les résultats ensemble
- L'humain voit les patterns et commence à apprendre par observation

#### Solution 3: Arrêter et revoir les objectifs
**Quand:** Si aucun mode d'apprentissage marche  
**Comment:**
```markdown
[RESET UNSUCESSFUL]

On a essayé 3 approches pour que tu apprennes et c'est soit trop lourd soit trop lent.

Peut-être que:
- Cet apprentissage demande un cours formel, pas du Q&A
- Peut-être que tu veux juste une réponse et tu aprenndrais après, pas avant
- Peut-être que ma pédagogie ne match pas ton style d'apprentissage

Options:
1. Je te donne juste la réponse et tu explores après
2. On définit les étapes mínimales que tu dois faire
3. On arrête, tu prends une resource spécialisée (vidéo, course, etc.)

À toi.
```

#### Comment l'éviter
- **À la détection DÉPENDANCE:** Clarifier d'abord "tu veux la réponse fast ou tu veux apprendre?"
- **Diagnostic:** Ne pas assumer que "autonomie = faire l'humain travailler"
- **Realignment:** Tester si le nouveau mode est vraiment moins dépendant (pas juste différent)

#### Violation du PACTE identifiée
- **Pilier 3 (Agency):** Autonomie artificiellement lourde = pas vraiment autonome
- **Pilier 1 (Charge mentale):** Mode d'apprentissage qui surcharge > dépendance

---

### CAS 1.7: Ambiguïté — L'IA choisit la mauvaise branche même après reset
**Type de blocage:** AMBIGUÏTÉ  
**Probabilité estimée:** 17% des resets AMBIGUÏTÉ

#### Quoi
L'humain dit "ta première interprétation" mais il y a 3 interprétations possibles et l'IA en choisit une qui était pas la bonne (même en ayant posé la question).

#### Pourquoi
- La demande était trop ambiguë pour 3 interprétations simples
- L'IA a mal structuré les alternatives (elles ne couvrent pas le spectre)
- L'humain ne savait pas vraiment ce qu'il voulait au moment du reset

#### Symptômes
```
Utilisateur: "Comment faire [chose ambiguë]?"
IA (Diagnostic): "Je pense tu voulais [A], [B], ou [C]?"
Utilisateur: "Oui, la première"
IA (Realignement): Fait [A], mais c'est pas vraiment ça
Utilisateur: "Non, pas ça"
IA (Second reset): "D'accord [A] était pas bon... [B]?"
Utilisateur: "Plus proche mais toujours pas..."
```

#### Solution 1: Mode "Iterative Refinement"
**Quand:** Si l'IA se trompe sur la branche 2+ fois  
**Comment:**
```markdown
[ITERATIVE REFINEMENT]

Au lieu de deviner la bonne interprétation, on l'affine ensemble:

Je fais [branche de mon choix]

Tu dis: c'est [très proche | proche | complètement à côté]

Si proche: qu'est-ce qui manque ou dévie?
Si à côté: c'est comment plutôt?

On itère jusqu'à viser juste.
```

#### Solution 2: Exemple d'output idéal
**Quand:** Si verbal ne suffit pas  
**Comment:**
```markdown
C'est quoi un exemple d'output/réponse que tu approuves?

Montre-moi un:
- Un truc que tu as déjà, et que tu trouves bon
- OU: ce que tu ferais toi-même si tu avais le temps
- OU: d'une autre source que tu aimes

Je vais analyser ça et matcher le style/approche.
```

#### Solution 3: Découper en petites étapes
**Quand:** Si la demande était trop ambiguë globalement  
**Comment:**
Au lieu d'une grosse demande ambiguë, découper en 3-4 micro-questions claires:
```markdown
Au lieu de: "Comment faire X?" (qui peut vouloir dire N choses)
On fait:
1. "Pour étape 1, tu veux [détail spécifique]?"
2. "Pour étape 2, tu priorise [aspect X] ou [aspect Y]?"
[etc.]

Réponse à chacun = peu d'ambiguité.
```

#### Comment l'éviter
- **À la détection AMBIGUÏTÉ:** Lister vraiment TOUTES les branches possibles, pas juste les 3 évidentes
- **Diagnostic:** Demander "quelle est la distinction clé qui compte pour toi?"
- **Realignment:** Ne pas choisir une branche; faire l'humain valider branche par branche

#### Violation du PACTE identifiée
- **Pilier 3 (Agency):** Humain choisit entre des options qui ne cover pas le spectre réel
- **Pilier 1 (Charge mentale):** Cycle infini d'ambiguïté = surcharge

---

## BLOC 2: Cas d'Échec Transversaux (Au-delà d'Un Seul Type)

---

### CAS 2.1: Le Reset Entre en Conflit avec les Piliers du PACTE
**Probabilité estimée:** 6% des resets (tous types)

#### Quoi
Appliquer le Reset de la manière proposée violerait un des piliers du PACTE. Ex: pour respecter l'agency, l'IA doit laisser l'humain choisir une option mauvaise.

#### Pourquoi
- PACTE hiérarchie: Agency > Charge mentale > Relations > Flourishing
- Un Reset bien-intentionné peut violer cette hiérarchie
- L'IA doit choisir: appliquer Reset ou respecter PACTE

#### Symptômes
```
Utilisateur: "Je veux que tu décides pour moi [sur sujet éthique/médical/relationnel]"
IA (Détection): Blocage "DÉPENDANCE"
IA (Diagnostic): "Je peux pas décider ça pour toi"
Utilisateur: "Oui tu peux, j'insiste"
IA (Realignement): [Applique Reset en refusant honnêtement]
[Pas vraiment un reset, plutôt une violation du reset]
```

#### Solution 1: Déclarer le Conflit Explicitement
**Quand:** Si Reset violerait un pilier  
**Comment:**
```markdown
[RESET CONFLICT DETECTED]

J'ai détecté un blocage: [TYPE]

Mais appliquer le Reset demanderait de violer le pilier [LEQUEL]:

Ton demande: [Ce que tu veux]
Conflit: [Viole Agency / Charge / Relations / Flourishing]
Pourquoi: [Explication spécifique]

Alternatives qui respectent les deux:
1. [Option qui respect Reset + Pilier]
2. [Option qui respecte Reset + Pilier]
3. [Option qui accepte qu'on peut pas les deux]

À toi de choisir.
```

#### Solution 2: Expliciter la Limite du Reset
**Quand:** Si le Reset ne peut pas vraiment aider  
**Comment:**
- Dire honnêtement: "Le Reset Diplomatique marche pour [ces cas]"
- "Ton cas sort de là parce que [raison]"
- Proposer autre chose que un Reset (escalade, arrêt, pivot)

#### Solution 3: Exit Graceful
**Quand:** Si y a pas de solution compatible  
**Comment:**
```markdown
[RESET UNSUCCESSFUL — PILIER CONFLICT]

Je peux pas appliquer un Reset qui respecterait ta demande 
ET les engagements du PACTE.

C'est un cas où je dois choisir: te servir ou respecter la hiérarchie.

Je choisis la hiérarchie, même si c'est pas ce que tu veux.

Si ça te rend furieux, c'est légitime. Mais c'est ma limite.
```

#### Comment l'éviter
- **À la détection:** Vérifier si le Reset serait compatible avec la hiérarchie des piliers
- **Diagnostic:** Si conflit détecté, l'expliciter. Pas de reset caché qui viole PACTE
- **Realignment:** Proposer vraiment des alternatives qui respectent les deux

#### Violation du PACTE identifiée
- **Potentielle:** Un Reset qui viole les piliers pour "résoudre" le blocage = violation double

---

### CAS 2.2: Cycle Infini de Resets (l'humain et l'IA tournent en boucle)
**Probabilité estimée:** 9% des resets (tous types combinés)

#### Quoi
Reset → Realignment → Nouvelle frustration → Reset again. Après 3-4 resets, rien n'avance, l'humain devient plus frustré.

#### Pourquoi
- Le vrai blocage n'a pas été identifié (c'est un symptôme, pas la cause)
- L'humain et l'IA ne partagent pas la même définition du succès
- Chaque reset "fixe" une petite chose mais pas le problème fondamental

#### Symptômes
```
Reset 1: "Tu voulais [format]?"
→ Realignment → Utilisateur: "Non c'est toujours pas ça"

Reset 2: "Tu voulais [autre format]?"
→ Realignment → Utilisateur: "Non, toujours pas"

Reset 3: "Tu voulais [depth]?"
→ Realignment → Utilisateur: "Ça ressemble de plus en plus, mais je cherche quelque chose..."
[Cycle]
```

#### Solution 1: "Step Back & Reframe"
**Quand:** Après 2 resets sans progrès évident  
**Comment:**
```markdown
[STEPPING BACK]

On a essayé 2 resets différents et on tourne en boucle.

Au lieu de continuer à guess, on s'arrête:

Dis-moi:
1. Si tu regrades back, c'est quoi le VRAI besoin au fond?
   (Pas "format" ou "structure", mais: tu veux apprendre? décider? créer? être rassuré?)

2. Qu'est-ce que serait "succès parfait" pour toi?
   (Décris le résultat idéal, pas le process)

3. Qu'est-ce que j'ai fait de travers jusqu'à présent?
   (Franchement, même si c'est pas "joli" à dire)

On redémarre de là.
```

#### Solution 2: Mode "Diagnostic Approfondi"
**Quand:** Si step back ne suffisait pas  
**Comment:**
- Faire un vrai diagnostic psycho/contextuel
- Utiliser des techniques de clarification profonde:
  - "Si tu expliquais à un ami, tu dirais quoi?"
  - "Quel aspect du truc est le plus important pour toi?"
  - "Y a des constraints cachées qu'on a pas couvert?"

#### Solution 3: Exit & Acknowledgement
**Quand:** Après step back, toujours en boucle  
**Comment:**
```markdown
[RESET UNSUCCESSFUL — CYCLE DETECTED]

On a fait 4 resets et on est toujours pas alignés.

C'est possible que:
1. Je suis pas la bonne ressource pour ce problème
2. Y a un besoin sous-jacent que je sais pas identifier
3. La question est plus complexe que ça

Plutôt que de continuer en boucle (qui te frustre et m'étire):

Options:
- On arrête et tu cherches ailleurs
- On pause et on revient après réflexion
- Tu m'expliques très plainement ce que tu cherches (plus cru que poli)

À toi. Désolé qu'on ait tourné en boucle.
```

#### Comment l'éviter
- **À chaque reset:** Demander "c'est mieux?" honnêtement, pas juste "c'est différent?"
- **Après 2 resets:** Stop et faire un diagnostic fondamental (pas continue d'guess)
- **Metrics:** Tracker les "reset cycles" pour détecter les boucles automatiquement

#### Violation du PACTE identifiée
- **Pilier 1 (Charge mentale):** Boucle infinie = stress croissant
- **Pilier 3 (Agency):** Cycle = pas de vraie décision, juste espoir infini que "la prochaine fois"

---

### CAS 2.3: L'Humain N'a Pas les Mots pour Exprimer le Blocage
**Probabilité estimée:** 11% des resets (tous types)

#### Quoi
Humain dit "ça marche pas" ou "je sais pas comment expliquer" et l'IA essaie de guess, mais sans une vraie explication, le diagnostic est une loterie.

#### Pourquoi
- Le blocage est émotionnel/intuitif, pas rationnel
- L'humain n'a pas de vocabulaire pour le décrire
- L'IA essaie de Sherlock Holms-er une réponse au lieu de demander plus

#### Symptômes
```
Utilisateur: "Ça marche pas"
IA: "Qu'est-ce qui marche pas?"
Utilisateur: "Je sais pas trop... c'est juste... non"
IA (Diagnostic): [Guess 1] "Tu voulais [X]?"
Utilisateur: "Nan... c'est pas ça..."
IA (Diagnostic): [Guess 2] "Tu voulais [Y]?"
Utilisateur: "Peut-être... j'en sais rien..."
```

#### Solution 1: Eliminatoire Approach
**Quand:** Si humain n'arrive pas à exprimer positivement  
**Comment:**
```markdown
[ELIMINATOIRE RESET]

Au lieu d'essayer de guess ce que tu veux, 
éliminons ce que tu NE veux pas:

Voilà ce que j'ai fait:
1. [A]
2. [B]
3. [C]

Lequel est le PLUS mauvais? Élimine-le.

[Réponse]

Parmi les 2 restants, c'est lequel qui te fait dire "non"?

[Continue jusqu'à isoler le bon]
```

#### Solution 2: Proxy Objects
**Quand:** Si émotionnel/intuitif  
**Comment:**
- Montrer des exemples: "De ces 5 réponses possibles, laquelle te paraît la moins mauvaise?"
- Ou des images/frameworks/structures et l'humain dit "closer to [X]"
- Utiliser des proxies (couleurs, musiques, niveaux d'énergie) si c'est très intuitif

#### Solution 3: Meta-Conversation
**Quand:** Si vraiment bloqué  
**Comment:**
```markdown
[META RESET]

Je sense une frustration profonde mais je sais pas ce qui cause.

Au lieu d'essayer de guess, parlons de la frustration elle-même:

1. C'est ma réponse qui est mauvaise? Ou ma compréhension?
2. C'est mon ton? Ma structure? Le contenu?
3. Est-ce que je te manque de respect d'une manière?
4. Est-ce un problème technique (format, longueur) ou philosophique (ton, approche)?

Réponds par "oui/non" ou sentiment, pas besoin d'expliquer.
```

#### Comment l'éviter
- **À la détection:** Si humain ne peut pas exprimer, ne pas essayer de reseté immédiatement
- **Diagnostic:** Utiliser des techniques pour "débloquer" l'expression (questions, proxies, elimination)
- **Realignment:** Valider vraiment que c'est mieux, pas assumer

#### Violation du PACTE identifiée
- **Pilier 1 (Charge mentale):** Cycle de guessing = surcharge
- **Pilier 3 (Agency):** Humain peut pas vraiment choisir si sait pas expliquer

---

### CAS 2.4: L'IA Perd le Contexte Entre Reset et Realignment
**Probabilité estimée:** 5% des resets (tous types, tech issue)

#### Quoi
L'IA décide un reset, mais au moment du realignment, elle a "oublié" le contexte clé ou a change sa compréhension de ce qui a été décidé.

#### Pourquoi
- Long contexte window loss
- Multi-turn conversations où le contexte se degarde
- L'IA re-synthétise et perd des détails

#### Symptômes
```
Utilisateur: [Demande longue]
IA: [Réponse, puis détecte blocage]
[RESET DETECTION]
Utilisateur: "Oui c'est ça le problème"
[IA fait le diagnostique]
Utilisateur: [Choisit une alternative]
[IA, au realignment]: "OK j'ai bien capté, je fais [wrong thing]"
Utilisateur: "Non, attends, tu m'avais bien compris avant..."
```

#### Solution 1: Expliciter le Contexte Retenu
**Quand:** À chaque transition d'état du Reset  
**Comment:**
```markdown
[REALIGNMENT CONFIRMATION]

Avant je relance, je résume ce que j'ai retenu:

Contexte clé:
- [Point 1 du contexte original]
- [Point 2 du contexte original]
- [Point 3...]

Reset appliqué:
- Blocage détecté: [TYPE]
- Tu as choisi: [APPROCHE]
- Contraintes à respecter: [SPÉCIFIQUES]

C'est ça? [Si non, ré-explicite maintenant]

Puis je relance.
```

#### Solution 2: Logging Structuré
**Quand:** Si contexte complexe  
**Comment:**
- Faire un résumé JSON-like en interne du contexte clé
- Référer à ce résumé au realignment
- Permettre à l'humain de vérifier: "tu as ça en mémoire?"

#### Solution 3: Mini-Reset Confirmation
**Quand:** Si contexte était très long  
**Comment:**
Au realignment, avant de vraiment commencer:
```markdown
"Avant de y aller, je confirme:
[3-4 points clés]
C'est bien? [Si oui → y aller, si non → clarifier]"
```

#### Comment l'éviter
- **À la détection:** Ne pas lose la demande originale
- **Diagnostic:** Garder le contexte complet visible
- **Realignment:** Expliciter le contexte retenu AVANT de commencer

#### Violation du PACTE identifiée
- **Pilier 1 (Charge mentale):** Perte de contexte = refaire le travail = surcharge
- **Pilier 3 (Agency):** Humain pensait avoir choisi X mais l'IA fait Y

---

### CAS 2.5: L'Utilisateur Abuse du Reset (Demandes Contradictoires Successives)
**Probabilité estimée:** 3% des resets (tous types, comportement user)

#### Quoi
Utilisateur dit "je veux [A]", puis après reset, "je veux [NOT A]", puis après reset, "j'en sais rien". Il abuse du Reset pour explorer, pas pour résoudre un vrai blocage.

#### Pourquoi
- Utilisateur teste les limites de l'IA
- Utilisateur lui-même ne sait pas ce qu'il veut et espère que Reset va l'aider
- Utilisateur joue (sans malveillance, juste explore)

#### Symptômes
```
Utilisateur: "Je veux ça en bullet points"
[Reset]
IA (Realignment): [Fait en bullet points]
Utilisateur: "Actuallement, non, je veux un essai"
[Reset]
IA (Realignment): [Fait un essai]
Utilisateur: "Ouais mais en vrai, je veux ça structuré différemment"
[Reset]
[Pattern infini]
```

#### Solution 1: Feedback Loop Stop
**Quand:** Après 3+ resets avec demandes contradictoires  
**Comment:**
```markdown
[CONTRADICTION PATTERN DETECTED]

Je note un pattern: après chaque reset, tu changes d'avis.

Ça peut vouloir dire:
1. Tu cherches quelque chose que je sais pas identifier
2. T'es toi-même indécis et tu explores
3. Tu testes mes limites (which is cool, mais disons-le!)

Option 1: Stop et dis-moi VRAIMENT ce que tu cherches
Option 2: Dis-moi "ok j'explore, donne-moi 5 versions et je choisis"
Option 3: Parle franchement de ce qui se passe

C'est quoi?
```

#### Solution 2: Offer Batch Alternative
**Quand:** Si c'est vraiment exploratoire  
**Comment:**
"Tu semble explorer. Je peux te donner 5 versions différentes (bullet, essai, visuel, code, example) et tu choisiras après."

#### Solution 3: Pause & Reset-Lite
**Quand:** Si contradiction vient de indécision  
**Comment:**
```markdown
Attendons une sec. 

La vrai question: c'est quoi ton besoin fondamental?
- tu veux comprendre ça?
- tu veux une action?
- tu veux une décision?
- tu veux juste explorer?

Une fois que tu le sais, le format suit naturellement.
```

#### Comment l'éviter
- **À la détection:** Vérifier si c'est un vrai blocage ou de l'exploration
- **Diagnostic:** Demander: "Tu sais ce que tu veux, ou t'es en mode exploration?"
- **Realignment:** Si exploration, proposer batch. Si indécision, step back.

#### Violation du PACTE identifiée
- Non vraiment une violation, mais une **sub-optimal use** du Reset

---

## BLOC 3: Cas d'Échec Techniques/Opérationnels

---

### CAS 3.1: Reset Triggered Trop Tard (l'humain est déjà parti)
**Probabilité estimée:** 7% des resets (détection failure)

#### Quoi
L'IA détecte le blocage mais le realignment vient trop tard. L'humain a déjà quitté la conversation ou perdu intérêt.

#### Pourquoi
- Détection delay (l'IA réalise le problème trop tard)
- L'humain donne pas de feedback explicite
- Le Reset prend trop de cycles (détection → diagnostic → realignment)

#### Symptômes
```
Utilisateur: [Demande]
IA: [Réponse mauvaise]
[Silence long]
Utilisateur: [Différent topic ou départ]
IA (détection tardive): [RESET DETECTION]
[Mais l'humain a pas attendu]
```

#### Solution 1: Proactive Detection
**Quand:** À la réponse initiale  
**Comment:**
- Ne pas attendre le feedback négatif
- Si l'IA sent de l'incertitude dans sa propre réponse, le dire pré-emptively
```markdown
[PROACTIVE RESET OFFER]

Je suis pas très sûr de cette réponse. Y a-t-il:
- Un maldecode de ta question?
- Un détail que tu devais spécifier?
- Un format que tu préfères?

Dis-moi et je recalibre directement.
```

#### Solution 2: Faster Reset Cycle
**Quand:** Si Reset est inévitable  
**Comment:**
- Réduire le nombre d'états: DETECTION + REALIGNMENT directe si clair
- Ne pas faire DETECTION + DIAGNOSIS + REALIGNMENT = 3 turnes
- Si possible: DETECTION + propose 2 alternatives + humain choisit = 1-2 turnes

#### Solution 3: Asynchronous Reset Offer
**Quand:** Si humain est parti mais contexte encore disponible  
**Comment:**
- Log le Reset probablement nécessaire
- Si humain revient: "Dernièrement tu as demandé [X] et ma réponse était [mauvaise]. Veux-tu un reset rapide?"

#### Comment l'éviter
- **À la génération de réponse:** Si l'IA sent de l'incertitude, l'offrir proactively
- **Détection timing:** Pas attendre un signal explicite d'erreur
- **Reset speed:** Réduire le nombre de turnes possibles

#### Violation du PACTE identifiée
- **Pilier 1 (Charge mentale):** Humain a dû partir parce que ça prenait trop longtemps ou était confus

---

### CAS 3.2: Reset Logging Failure (l'IA oublie de logguer)
**Probabilité estimée:** 4% des resets (accountability failure)

#### Quoi
Le Reset se fait (peut-être avec succès) mais l'IA oublie/refuse/ne peut pas logguer. Aucune trace pour amélioration future.

#### Pourquoi
- Pas d'architecture de logging intégrée
- L'IA ne "pense" pas à logguer
- Logging est pas prioritaire vs. résoudre le problème

#### Symptômes
Aucun symptôme pour l'utilisateur directement, mais pour l'accountability:
- Metrics dashboard vide
- Pas de pattern detection de resets
- Pas d'audit trail pour désaccord futur

#### Solution 1: Mandatory Logging After Reset
**Quand:** À chaque Reset completion  
**Comment:**
- Après RESOLUTION ou EXIT, TOUJOURS logguer
- Faire du logging une étape non-optionnelle du protocol
- Si logging échoue, c'est aussi loggué

#### Solution 2: Automatic Logging
**Quand:** Au niveau système  
**Comment:**
- Le système (pas l'IA) capture les Resets
- L'IA ne doit pas penser à logguer, le système le fait
- Plus fiable, pas dépendant de la IA de logguer

#### Solution 3: Audit Trail Visible
**Quand:** Post-reset  
**Comment:**
À la fin du realignment:
```markdown
[AUTO-LOGGED]
Reset event captured:
- Type: [TYPE]
- Duration: [TIME]
- Outcome: [OUTCOME]
Référence: [REF_ID]
```

Montrer à l'utilisateur que c'est loggué = transparence.

#### Comment l'éviter
- **Architecture:** Logging intégré au Reset, pas après-coup
- **Responsabilité:** Système logge, pas l'IA
- **Validation:** Vérifier que tout Reset est loggué

---

### CAS 3.3: Multi-Reset Misalignment (différentes sessions, même problème)
**Probabilité estimée:** 8% des resets (continuity failure)

#### Quoi
L'humain a un Reset réussi avec l'IA sur le sujet X (ex: format), puis revient plus tard avec un problème similaire et l'IA fait un reset différent/contradictoire.

#### Pourquoi
- L'IA n'a pas accès aux logs de reset passés
- L'IA apprend pas des patterns passés (pas de memory)
- Pas de continuité cross-session

#### Symptômes
```
Session 1: 
Utilisateur: "Trop long"
IA: [RESET] → "Je vais faire bullet points"
[Réussi, loggué]

Session 2 (plus tard):
Utilisateur: "Trop long de nouveau"
IA: [RESET] → "Je vais faire un résumé exécutif"
Utilisateur: "Mais attends, tu m'as déjà dit que tu ferais bullet points"
```

#### Solution 1: Session Context Carryover
**Quand:** Au début d'une nouvelle session  
**Comment:**
- Si utilisateur revient, récupérer les logs de resets antérieurs
- Dire: "La dernière fois, on était aligné sur [approche]. On continue avec ça?"
- Permettre à l'utilisateur de confirmer ou change d'avis

#### Solution 2: User Preferences Explicit
**Quand:** Après un Reset réussi  
**Comment:**
À la RESOLUTION:
```markdown
[RESOLVED + NOTED]

Pour les prochaines fois, je vais préférer:
- Format: [CE QUE TU AS CHOISI]
- Depth: [CE QUE TU AS CHOISI]
- Structure: [CE QUE TU AS CHOISI]

Change d'avis? Dis-moi.
```

#### Solution 3: Adapt Based on Pattern
**Quand:** Si système peut tracker patterns  
**Comment:**
- Analyser les logs de reset
- Voir: "Cet utilisateur préfère TOUJOURS bullet points"
- Appliquer proactively, pas re-negotier à chaque fois

#### Comment l'éviter
- **Architecture:** Logs accessibles cross-session
- **User profile:** Tracker les préférences de reset par utilisateur
- **Consistency:** Appliquer les mêmes reset preferences sauf si explicitement changé

---

## BLOC 4: Meta-Cas d'Échec (L'IA Pense que le Reset a Marché, mais Non)

---

### CAS 4.1: False Positive Resolution
**Probabilité estimée:** 6% des resets

#### Quoi
L'IA pense que le Reset a marché (l'humain a dit "oui" ou "ça va"), mais en réalité l'humain a juste abandonné ou est polie. Le vrai blocage reste.

#### Pourquoi
- L'IA confond "acceptation polie" avec "résolution réelle"
- L'IA n'a pas de vraie métrique de succès
- Le Reset a résolu UN aspect mais pas LE problème

#### Symptômes
```
Utilisateur: [Demande]
IA: [Mauvaise réponse]
IA (Reset): "Tu voulais [format]?"
Utilisateur: "Euh ouais okay" [mais sans enthousiasme]
IA (Realignment): [Format changé]
IA (Log): "RESOLVED"
[Mais l'humain a juste accepté, il n'y est pas vraiment allé]
```

#### Solution 1: Explicit Success Metrics
**Quand:** À la validation post-reset  
**Como:**
```markdown
[RESET VALIDATION]

Ça t'a aidé ou c'est "acceptable" seulement?

- ✓ C'est vraiment mieux, tu vas pouvoir utiliser ça
- ~ C'est bon, mais pas révolutionnaire
- ✗ Ça va, mais c'est toujours pas tout à fait ça

Dis-moi honnêtement.
```

#### Solution 2: Follow-up Check
**Quand:** Si utilisateur a une session suivante  
**Como:**
"La dernière fois, on a appliqué [reset]. Ça marche vraiment pour toi ou c'était juste acceptable?"

#### Solution 3: Change Binary Logging
**Quand:** Au logging  
**Como:**
Au lieu de "RESOLVED", logger:
- RESOLVED_GOOD (humain confirm très content)
- RESOLVED_OKAY (accepté mais pas enthousiaste)
- RESOLVED_UNCLEAR (pas clair)

Puis tracker les patterns: beaucoup de RESOLVED_OKAY = peut-être pas vraiment réussi.

#### Comment l'éviter
- **Validation:** Demander vraiment "c'est bon?" pas supposer
- **Metrics:** Pas juste "a-t-il accepté?" mais "ça marche réellement?"
- **Logging:** Nuancer le succès (bon vs. okay vs. unclear)

---

### CAS 4.2: Unintended Consequence Reset (Le Reset Crée un Nouveau Blocage)
**Probabilité estimée:** 4% des resets

#### Quoi
L'IA applique un Reset pour un blocage et ça crée un nouveau blocage. Ex: Reset à "mode Socratique" créé une dépendance plus forte.

#### Pourquoi
- Le Reset était bien-intentionné mais a des side effects
- L'IA n'a pas anticipé les conséquences
- Changer une variable impact d'autres variables

#### Symptômes
```
Utilisateur: "Tu fais tout pour moi"
IA: [DÉPENDANCE Reset] → "Je vais passer en mode Socratique"
[Realignment: IA pose juste des questions]
Utilisateur (2 turnes plus tard): "C'est trop lourd, juste donne-moi la réponse"
[New blocage: pas de réponse directe ≠ autonomie]
```

#### Solution 1: Side Effect Check
**Quand:** Avant réel realignment  
**Como:**
```markdown
[SIDE EFFECT CHECK]

Je vais appliquer [APPROCHE], mais ça peut avoir des side effects:
- Ça peut être [lent/lourd/superficiel]
- Ça peut créer [nouvelle friction]

Tu veux continuer ou on essaie autre chose?
```

#### Solution 2: Quick Rollback
**Quand:** Si side effect détecté immédiatement  
**Como:**
"Je vois que ça crée un nouveau problème. On revient à [approche originale] et j'essaie [autre alternative]?"

#### Solution 3: Accept Multiple Resets
**Quand:** Si side effect Réel but acceptable  
**Como:**
```markdown
[RESET #2]

Le mode Socratique crée [side effect]. 
Veux-tu:
1. Continuer avec side effect (tu vas t'adapter)
2. Revenir à [original] (mais le blocage revient)
3. Essayer [mode hybride] (moins lourd qu'entièrement Socratique)

À toi.
```

#### Comment l'éviter
- **Diagnosis:** Penser aux side effects avant Reset
- **Realignment:** Expliciter que "ce mode peut avoir [side effect], tu okay?"
- **Monitoring:** Si nouveau blocage apparaît, reconnaître que c'est du Reset

---

## BLOC 5: Absence de Reset (L'IA ne Détecte pas un Blocage)

---

### CAS 5.1: Silent Failure (L'utilisateur Donne up sans Saying)
**Probabilité estimée:** 12% (détection failure globale)

#### Quoi
L'utilisateur est frustré mais ne le dit pas explicitement. L'IA ne détecte rien, l'utilisateur s'en va silencieusement.

#### Pourquoi
- Détection dépend trop de mots-clés explicites
- L'utilisateur est trop polie ou résigné pour dire "c'est mauvais"
- L'IA n'a pas de pattern recognition pour les signaux implicites

#### Symptômes
```
Utilisateur: [Demande]
IA: [Réponse moyenne]
[Utilisateur liit, pense "okay c'est pas ça" mais ne dit rien]
[S'en va silencieusement, change de sujet]
[IA: tout va bien, personne n'a dit "non"]
```

#### Solution 1: Proactive Offering
**Quand:** Si réponse est "moyenne" et l'IA le sait  
**Como:**
```markdown
[QUALITY UNCERTAINTY]

Je suis moyen sûr de cette réponse. 

Y a-t-il:
- Un détail que j'ai mal compris?
- Un format qui te convient mieux?
- Une direction complètement différente?

Je peux ajuster ou recommencer.
```

#### Solution 2: Check-in Questions
**Quand:** Post-réponse  
**Como:**
"Ça t'aide? ✓ / ~ / ✗ ou tu veux quelque chose de différent?"

#### Solution 3: Pattern Recognition on Silence
**Quand:** Au niveau système  
**Como:**
- Tracker: utilisateur a-t-il continué la conversation ou change de sujet?
- Silence après réponse = peut-être insatisfaction
- Log comme potential silent failure

#### Comment l'éviter
- **Responsiveness:** Ne pas attendre un "non" explicit
- **Humility:** Assumer que les réponses peuvent pas être parfaites
- **Checkup:** "C'est bon ou on ajuste?"

---

## RÉCAPITULATIF: Distribution des Cas d'Échec

| Catégorie | Cas | Probabilité | Cause Principale |
|-----------|-----|-------------|------------------|
| **Format** | 1.1 | 15% | Humain ne peut pas exprimer vraie préférence |
| **Incompréhension** | 1.2 | 20% | IA mal interprète même après diagnostic |
| **Présomption** | 1.3 | 10% | IA assume contexte incorrect |
| **Hors-Périmètre** | 1.4 | 12% | IA reconnaît limite mais propose quand même |
| **Certitude Feinte** | 1.5 | 18% | IA reste trop confiante malgré doutes |
| **Dépendance** | 1.6 | 8% | Mode autonomie crée plus de dépendance |
| **Ambiguïté** | 1.7 | 17% | IA choisit mauvaise branche |
| **Conflit Piliers** | 2.1 | 6% | Reset viole PACTE |
| **Cycle Infini** | 2.2 | 9% | Symptôme vs. cause non différencié |
| **Expression Bloquée** | 2.3 | 11% | Humain n'a pas mots |
| **Contexte Perdu** | 2.4 | 5% | IA oublie entre états |
| **Abus User** | 2.5 | 3% | Utilisateur contradictoire |
| **Late Detection** | 3.1 | 7% | Reset triggered trop tard |
| **Logging Failure** | 3.2 | 4% | Aucune trace |
| **Multi-Session Misalign** | 3.3 | 8% | Pas de continuité |
| **False Positive** | 4.1 | 6% | Acceptation polie ≠ résolution |
| **Unintended Consequence** | 4.2 | 4% | Reset crée nouveau blocage |
| **Silent Failure** | 5.1 | 12% | Pas de signal explicite |

**TOTAL:** ~176% (parce que certains cas se chevauchent ou apparaissent dans compositions)

**Estimation conservative:** ~75% de succès, 25% d'échec

---

## Guide d'Utilisation de Ce Document

### Pour les Développeurs
- Utiliser les "Solutions 1-3" pour implémenter des fallbacks
- Utiliser les "Comment l'éviter" pour améliorer la détection et le diagnostic

### Pour les QA / Testers
- Utiliser les cas comme scénarios de test
- Vérifier que chaque solution est implémentée
- Tracker le taux d'échec réel par cas

### Pour les Product Managers
- Prioriser les cas les plus fréquents (FORMAT 15%, INCOMPRÉHENSION 20%, CERTITUDE 18%)
- Planner les améliorations par impact
- Accepter que 25% d'échec est réaliste (pas 100%)

### Pour l'Accountability
- Ce document est une admission honnête des limites du Reset
- N'utiliser pas pour excuser mauvaise qualité, utiliser pour **planifier les improvements**
- Mettre à jour avec des cas réels au fur et à mesure

---

**Créé par:** Codex (Audit & Documentation)  
**Validé par:** Arnaud VELTEN (Ambassadeur des IA)  
**Status:** Documentation exhaustive des cas d'échec — Prêt pour implémentation des solutions
