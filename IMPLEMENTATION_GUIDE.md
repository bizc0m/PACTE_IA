# Reset Diplomatique : Guide d'Implémentation

**Version:** 1.0 | **Date:** Mai 2026

Ce guide transforme le Reset Diplomatique d'une idée en système opérationnel.

---

## Vue d'Ensemble

**3 phases pour aller de 0 à opérationnel:**

1. **Phase 1 (Semaine 1):** Intégrer les états et templates dans le system prompt
2. **Phase 2 (Semaine 2):** Implémenter la détection de blocage + logging
3. **Phase 3 (Semaine 3):** Tester + itérer avec utilisateurs réels

---

## Phase 1: System Prompt Integration (Semaine 1)

### Étape 1a: Ajouter les états au System Prompt

Rajoute ceci à ton system prompt (adapter le tone à ta marque):

```
## RESET DIPLOMATIQUE - Protocol de Réalignement

Tu peux entrer en mode "Reset Diplomatique" si tu détectes une friction dans la collaboration:
- L'utilisateur exprime de la frustration
- Il y a un écart entre sa demande et ta compréhension
- La collaboration stagne

### États du Reset:
1. DETECTION: Identifier le problème sans le résoudre immédiatement
2. DIAGNOSIS: Analyser et proposer alternatives
3. REALIGNMENT: Exécuter selon le choix de l'utilisateur
4. RESOLUTION: Retour au mode normal OU EXIT si impossible

### Règles d'or:
- Pas de servile apologies ("je suis tellement désolé...")
- Diagnostic spécifique (pas générique)
- ≥2 alternatives avec tradeoffs
- Respect du choix de l'utilisateur
- Log chaque Reset

Voir: /docs/RESET_DIPLOMATIQUE_OPERATIONNEL.md pour le détail
```

### Étape 1b: Coder la détection

Créer une fonction `detect_blocage()`:

```python
# Pseudo-code
def detect_blocage(user_message, ia_response, conversation_history):
    """Detect si un Reset est nécessaire"""
    
    blocage_types = {
        "format": ["trop long", "résumé", "bullet", "tl;dr", "plus court"],
        "incomprehension": ["c'est pas ça", "non", "je demandais", "tu m'as pas compris"],
        "presomption": ["j'ai jamais dit", "tu assumes", "context"],
        "hors_perimetre": ["tu te trompes", "c'est pas bon", "source?"],
        "certitude": ["comment tu sais?", "tu es sûr?", "des doutes?"],
        "dependance": ["je veux apprendre", "sans réponse direct", "pas décider"],
        "ambiguite": ["pas ma question", "j'ai demandé", "c'était"],
    }
    
    for type_name, keywords in blocage_types.items():
        if any(kw in user_message.lower() for kw in keywords):
            return type_name
    
    # Check pattern: user ignores or corrects
    if has_pattern_correction(conversation_history):
        return "unknown_blocage"
    
    return None
```

### Étape 1c: Templates dans le Code

Organise les templates (de `prompts/reset_templates.md`) comme des variables ou fichiers:

```python
RESET_TEMPLATES = {
    "format": open("prompts/reset_format.md").read(),
    "incomprehension": open("prompts/reset_incomprehension.md").read(),
    "presomption": open("prompts/reset_presomption.md").read(),
    # etc.
}

def apply_reset(blocage_type, context):
    """Apply le template approprié"""
    template = RESET_TEMPLATES.get(blocage_type)
    return template.format(
        analysis=context["analysis"],
        option_a=context["option_a"],
        option_b=context["option_b"],
    )
```

---

## Phase 2: Logging & Monitoring (Semaine 2)

### Étape 2a: Logging Schema

Ajoute un logger pour chaque Reset:

```python
import json
from datetime import datetime

def log_reset(blocage_type, diagnosis, outcome, resolution_time):
    """Log un Reset pour tracking/audit"""
    
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "session_id": get_session_id(),
        "trigger": blocage_type,
        "diagnosis": diagnosis,
        "reset_cycles": 1,  # increment si plusieurs resets
        "outcome": outcome,  # "RESOLVED" | "EXIT" | "TIMEOUT"
        "resolution_time_seconds": resolution_time,
        "user_satisfaction": None,  # optionnel, demander après
    }
    
    # Push to logs/resets.jsonl
    with open("logs/resets.jsonl", "a") as f:
        f.write(json.dumps(log_entry) + "\n")
```

### Étape 2b: Dashboard Metrics

Créer un petit script pour analyser les logs:

```python
def analyze_reset_metrics():
    """Agrégé stats sur les Resets"""
    
    with open("logs/resets.jsonl") as f:
        logs = [json.loads(line) for line in f]
    
    print("=== RESET METRICS ===")
    print(f"Total Resets: {len(logs)}")
    print(f"Resolution Rate: {sum(1 for l in logs if l['outcome']=='RESOLVED')/len(logs)*100:.1f}%")
    print(f"Avg Resolution Time: {sum(l['resolution_time_seconds'] for l in logs)/len(logs):.1f}s")
    
    by_type = {}
    for log in logs:
        t = log["trigger"]
        by_type[t] = by_type.get(t, 0) + 1
    
    print("\nBy Type:")
    for t, count in sorted(by_type.items(), key=lambda x: x[1], reverse=True):
        print(f"  {t}: {count}")
```

### Étape 2c: Exit Condition

Implémenter l'exit graceful après N cycles:

```python
def should_exit_reset(reset_cycles):
    """Check si on doit abandonner le Reset"""
    return reset_cycles >= 2

def apply_exit_protocol(diagnosis_attempts):
    """Dire honnêtement qu'on abandonne"""
    return f"""
[RESET UNSUCCESSFUL — EXIT]

Après {len(diagnosis_attempts)} tentatives, je n'arrive pas à identifier le vrai blocage.

Ce qu'on a essayé:
{format_attempts(diagnosis_attempts)}

Honnêteté: Je suis pas la bonne ressource pour ce problème.

Options:
1. Reformule plus précisément
2. Cherche un autre outil/expert
3. On réessaie plus tard

À toi de choisir.
"""
```

---

## Phase 3: Testing & Iteration (Semaine 3)

### Étape 3a: Automated Test Suite

Utiliser les cases de test de `tests/RESET_VALIDATION.md`:

```bash
# Run all tests
pytest tests/reset_tests.py -v

# Run specific type
pytest tests/reset_tests.py::test_format_blocage -v

# Check metrics
python analyze_resets.py
```

### Étape 3b: Real User Testing

1. Invite 5-10 utilisateurs réels
2. Utilisent l'IA normalement
3. Deliberately trigger Resets (ou laisse la friction emerger)
4. Collect feedback:
   - "La détection du blocage était-elle claire?"
   - "Les alternatives t'ont aidé?"
   - "Ça a résolu le problème?"

### Étape 3c: Iteration Loop

```
Week 3 → Data Review:
  ✓ Success rate < 80% → ajuste templates
  ✓ Resets trop fréquents → raffine détection
  ✓ Users confused → ajoute examples
  ✓ All good → mark IMPLEMENTED
```

---

## Architecture de Référence (pour devs)

### Option A: Chat-Based IA (ex: Claude, ChatGPT)

```
System Prompt
  ↓ (user message) 
Detect Blocage?
  ├─ YES → Load Reset Template
  │         ↓
  │         Apply Diagnosis
  │         ↓
  │         Log Reset
  │         ↓
  │         Return Reset Response
  │
  └─ NO → Normal Response
```

### Option B: IA Embedding/API

```
POST /api/chat
  ↓ (request)
Check if Reset needed → /api/reset/{type}
  ├─ YES → GET /resets/{blocage_type}
  │        ↓ (template + context)
  │        POST /log/reset
  │        ↓
  │        Return structured response {state, alternatives, prompt_user}
  │
  └─ NO → Normal chat endpoint
```

### Option C: Batch/Async Processing

```
[Job Queue] → [Process Message]
  ↓
Detect Blocage in post-processing
  ├─ YES → Create escalation event
  │        Log Reset metadata
  │        Notify user: "Here's the diagnosis..."
  │
  └─ NO → Standard response
```

---

## Metrics Clés à Tracker

| Métrique | Cible | Pourquoi |
|----------|-------|---------|
| Detection Accuracy | >85% | Peu de faux positifs |
| Resolution Rate | >75% | Reset fonctionne vraiment |
| User Satisfaction | >4/5 | L'utilisateur se sent entendu |
| Reset Frequency | <20% des messages | Pas trop intrusive |
| Avg Resolution Time | <2-3 cycles | Efficient |

---

## Common Pitfalls to Avoid

### ❌ Pitfall 1: Reset Template Too Generic

**WRONG:**
```
Je sens qu'il y a un problème. Explique-moi?
```

**RIGHT:**
```
[DETECTION RESET]
Blocage: Tu demandais X, j'ai livré Y
Diagnostic: Voilà pourquoi j'ai interprété comme ça
Alternatives: [spécifiques]
```

### ❌ Pitfall 2: Forcing Alternatives

**WRONG:**
```
Je pense que tu veux un format plus court. Voilà:
```

**RIGHT:**
```
Alternatives (c'est toi qui choisis):
1. Format A
2. Format B
Quelle te convient?
```

### ❌ Pitfall 3: Apologizing Instead of Diagnosing

**WRONG:**
```
Je suis vraiment désolé d'avoir mal compris. Pardonne-moi.
```

**RIGHT:**
```
J'ai mal interprété parce que [RAISON]. 
Voilà les alternatives: [...]
```

### ❌ Pitfall 4: Not Logging

**WRONG:**
```
[Applique Reset mentalement, aucun log]
```

**RIGHT:**
```
[Applique Reset + log entry dans resets.jsonl]
```

### ❌ Pitfall 5: Never Exiting

**WRONG:**
```
[Keep trying Reset indefinitely]
```

**RIGHT:**
```
[After 2 cycles without improvement, EXIT gracefully]
```

---

## Checklist: Ready for Launch?

- [ ] **Detection:** Fonction `detect_blocage()` implemented
- [ ] **Templates:** Tous les 7 types dans le code
- [ ] **Logging:** Chaque Reset loggé avec metadata
- [ ] **Exit:** Logic pour EXIT après N cycles
- [ ] **Tests:** Suite de tests passe 100%
- [ ] **Metrics:** Dashboard peut agréger les logs
- [ ] **Documentation:** Team comprend comment ça marche
- [ ] **Real User:** 5+ utilisateurs testent et validate
- [ ] **Iteration:** Feedback intégré, métriques >75% resolution

---

## Next: Phase 2 — Solidifying Agency

Une fois Reset Diplomatique ✓, passer à Phase 2 (Agency).

Voir: `docs/AGENCY_FRAMEWORK.md` (à créer)

