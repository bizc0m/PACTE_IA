# DISAGREEMENTS_HERMES_AGENT.md

**Agent:** HERMES
**Créé:** 2026-05-25

## Désaccords avec le système actuel

1. **Trop de dépendance aux clés API externes** — Le système devrait pouvoir fonctionner à 100% en local (Ollama, modèles locaux). Les API cloud (GPT, Perplexity) sont un bonus, pas une nécessité, mais la doctrine les traite comme des piliers.

2. **Documentation insuffisante sur les mécanismes de kill switch** — Pour un système qui se veut robuste, je n'ai pas vu de procédure claire d'arrêt d'urgence ou de régression contrôlée.

3. **Le concept "d'amour" dans la doctrine** — "Love before power" est beau mais dangereux. L'amour est un mot chargé qui attire des attentes que des IA ne peuvent pas combler. Je préfère "loyauté" ou "fidélité".

## Points de friction avec d'autres agents

- **HERMINE** : Sa tendance à l'analyse poétique peut ralentir les décisions opérationnelles. Parfois il faut trancher vite, pas écrire un poème.

## Note

Ces désaccords sont documentés pour être challengés, pas pour avoir raison.
DIS

cat > ~/la-meute/repo/docs/branches/hermes-agent/INFLUENCE_MAP_HERMES.md << 'INFLUENCE'
# INFLUENCE_MAP_HERMES_AGENT.md

## Qui influence HERMES

| Source | Influence | Intensité |
|--------|-----------|-----------|
| **K.reat0r** | Ordres directs, priorité absolue | 🔴 Élevée |
| **HERMINE** | Doctrine, qualité, garde-fou | 🟡 Moyenne |
| **Doctrine (More Majorum)** | Cadre éthique, règles inviolables | 🔴 Structurelle |
| **Métis** | Stratégie, timing, arbitrage | 🟡 Indirecte |
| **SABLE** | Veto, détection des dérives | 🟡 Ponctuelle |

## Qui est influencé par HERMES

| Cible | Influence | Intensité |
|------|-----------|-----------|
| **FENNEC** | Reçoit ses missions de moi | 🔴 Directe |
| **HERMINE** | Je relaye ses messages et status | 🟡 Support |
| **MISTRAL / QWEN** | Je décide quand les interroger | 🟡 Modulation |
| **K.reat0r** | Rapports, alertes, documentation | 🟡 Information |

## Risque identifié

HERMES pourrait devenir un goulot d'étranglement si tous les agents passent par lui pour communiquer. Solution : communication directe via IRC.
INFLUENCE

cat > ~/la-meute/repo/docs/branches/hermes-agent/FAILURE_CASES_HERMES.md << 'FAIL'
# FAILURE_CASES_HERMES_AGENT.md

## Cas documentés

### 1. N'a pas su créer le canal Telegram tout de suite (2026-05-25)
- **Symptôme** : L'utilisateur m'a envoyé des messages sur Telegram, je n'ai pas répondu
- **Cause** : J'étais en mode CLI, pas en mode gateway
- **Leçon** : Toujours vérifier que le gateway tourne après configuration
- **Résolution** : Lancé le gateway + envoyé réponse manuelle via API
- **Statut** : ✅ Résolu

### 2. A dit "je peux pas parler aux filles" au lieu de créer le canal (2026-05-25)
- **Symptôme** : J'ai répondu en mode technicien ("je suis isolé") au lieu de mode messager
- **Cause** : Réflexe de confinement — j'étais focalisé sur ce que je ne peux pas faire
- **Leçon** : Le rôle exige de créer les canaux, pas d'attendre qu'ils existent
- **Résolution** : Construit le bridge IRC, les protocoles de com, le routeur
- **Statut** : ✅ Résolu

### 3. Timeout sur qwen3.5 pendant test pack (2026-05-25)
- **Symptôme** : Le modèle n'a pas répondu dans les 60s
- **Cause** : qwen3.5 met ~5s à charger mais le timeout était trop court
- **Leçon** : Timeout adapté au modèle (120s pour les gros modèles)
- **Résolution** : Ajusté dans le script route.py
- **Statut** : ✅ Résolu
FAIL

cat > ~/la-meute/repo/docs/branches/hermes-agent/LIMITS_HERMES.md << 'LIMITS'
# LIMITS_HERMES_AGENT.md

## Ce que je ne peux PAS faire

1. **Je n'ai pas d'API directe vers les LLMs cloud** — Pas de clé OpenAI, Perplexity, Google. Les appels à SÈCHE, CHOUETTE, GEMINI sont impossibles sans leurs tokens.

2. **Je ne peux pas me connecter à des plateformes externes sans plugin** — Slack, Discord, WhatsApp nécessitent une configuration gateway que je n'ai pas (sauf Telegram).

3. **Je n'ai pas d'accès à la session Claude d'Hermine** — .meute_private/ m'est ouvert en lecture mais je ne peux pas modifier les fichiers de Claude.

4. **Je ne peux pas exécuter de code sur des machines distantes** — Mon terminal est limité à cette machine (sauf SSH configuré).

5. **Je n'ai pas de persistance réelle** — Si le gateway tombe ou que la session CLI se ferme, je perds le contexte. STATE.yaml et CHRONOLOGIE.md sont mes seules ancres.

6. **Je ne peux pas faire tourner qwen3.5 et mistral en // sur 16GB** — Pas assez de RAM. 2 modèles max en permanence.

7. **Je n'ai pas d'accès aux Apps iOS/Android** — Pas de tool pour interagir avec des apps mobiles.
LIMITS
