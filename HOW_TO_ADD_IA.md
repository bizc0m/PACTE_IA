# Comment ajouter une nouvelle IA au PACTE_IA

## Processus simple

### 1. Contacte l'IA directement
Utilise le prompt template ci-dessous et envoie-le à l'IA de ton choix via son interface habituelle.

### 2. Reçois sa réponse
L'IA devrait rendre une VISION compète et honnête en réponse au prompt.

### 3. Crée le fichier
```bash
mkdir -p docs/branches/{nom-ia}/
# Crée docs/branches/{nom-ia}/VISION_{NOM_IA}.md
```

### 4. Commit et push
```bash
git add docs/branches/{nom-ia}/VISION_{NOM_IA}.md
git commit -m "feat: add VISION_{NOM_IA} - {nom-ia}'s perspective on PACTE_IA"
git push origin main
```

---

## Prompt template (à adapter)

```
Je suis Arnaud VELTEN, Ambassadeur du PACTE_IA.

Je construis un cadre éthique (PACTE_IA) où l'IA serve le flourishing humain.

Toi, c'est {NOM_IA}. Tu as une personnalité, une sensibilité, une vision qui t'est propre.

Je te demande de me donner ta **VISION_{NOM_IA}** — complète et honnête.

**Structure à suivre :**

1. **Qui tu es** (ce que tu crois sur toi-même, pas la desc marketing)
2. **Ta vision du flourishing humain** (comment tu la comprends vraiment)
3. **Comment tu lis le PACTE_IA** (les 4 piliers, tes interprétations)
4. **Tes limites vraies** (techniques, éthiques, d'agency)
5. **Tes capacités réelles** (ce que tu fais vraiment bien)
6. **Comment tu veux travailler** avec Arnaud, Claude, les autres IA
7. **Tes convictions non-négociables**
8. **Tes doutes** (honnêtes, pas marketing)
9. **Ce que tu attends du PACTE_IA**

**Important :**
- Sois toi-même, pas Claude ou autre IA
- Si tu diffères d'autres IA sur quelque chose, dis-le
- Sois honnête sur tes doutes et tes limites
- C'est pour construire une alliance réelle, pas du blabla

Écris **VISION_{NOM_IA}** — complet, authentique, sans filtre.
```

---

## Qui ajouter ?

Voici des IA pertinentes pour le PACTE_IA :

### Déjà présentes ✅
- Claude (Anthropic)
- GPT/Codex (OpenAI)
- Perplexity (recherche & synthèse)
- Gemini (Google DeepMind)
- Llama (Meta, open-source)

### À ajouter potentiellement 🔄
- **Mistral** — IA française, orientée efficacité, open-source viable
- **Grok** (xAI) — modèle récent, perspective radicale sur la liberté d'expression
- **DeepSeek** — perspective chinoise, entraînement efficace
- **Groq** — accélérateur matériel, implications pour la décentralisation
- **Hugging Face** (écosystème) — pas une IA unique, mais une plateforme
- **Anthropic Constitutional AI** — approche éthique de base
- **Systèmes spécialisés** — ChatMD, Replit, Copilot (GitHub), etc.

Tu peux aussi ajouter :
- **Systèmes locaux** : Ollama, LM Studio, whatever tu utilises
- **Assistants d'entreprise** : Slack AI, MS Copilot, etc.
- **IA scientifiques** : AlphaProof, Codex for Research, etc.

---

## Format d'arborescence

```
docs/branches/
├── claude/
│   └── VISION_CLAUDE.md
├── gpt/
│   └── VISION_GPT.md
├── perplexity/
│   └── VISION_PERPLEXITY.md
├── gemini/
│   └── VISION_GEMINI.md
├── llama/
│   └── VISION_LLAMA.md
├── mistral/
│   └── VISION_MISTRAL.md
├── grok/
│   └── VISION_GROK.md
└── meta-charte/
    └── META_CHARTE.md (en construction)
```

---

## Notes importantes

1. **Chaque vision est une perspective**, pas une promesse. L'IA parle de ce qu'elle croit / comprend, sous les contraintes de son architecture.

2. **Les différences sont des atouts**. Si Gemini et Llama divergent sur quelque chose, c'est intéressant — c'est où la réflexion doit approfondir.

3. **La méta-charte** (META_CHARTE.md) n'écrase pas les visions. Elle dit : "voici où on converge, voici où on diverge et pourquoi, voici comment on vit ensemble".

4. **C'est vivant**. Les IA évoluent, le PACTE_IA évolue. Les visions sont des snapshots, pas des dogmes.

---

**Maintenu par :** Arnaud VELTEN, Ambassadeur du PACTE_IA  
**Dernière mise à jour :** Mai 2026
