# L0RE IS GO — v0.1

Système d'adressage sémantique pour fragments de sens.  
Inspiré du datagramme de Louis Pouzin (Cyclades, 1973).

---

## Règle fondamentale

```
UID  = qui suis-je ?
HASH = suis-je intact ?
ADDR = où suis-je ?
```

Comme un paquet IP porte son adresse et navigue le réseau de manière autonome,  
un fragment de lore porte son adresse et navigue un espace symbolique de manière autonome.

---

## RÈGLE #001 — Structure obligatoire

Tout Loregram possède obligatoirement : `uid`, `hash`, `addr`.

### Format UID

```
lore:<uuidv7>
```

Exemple :
```
lore:018fc6c2-8c8b-7c4a-a9d2-6a2d8d8f8e21
```

### Format HASH

```
sha256:<hexdigest>
```

Le hash couvre tous les champs **sauf** `hash` et `signature`.  
Champs couverts : `uid`, `parent_hash`, `addr`, `title`, `body`, `links`, `metadata`, `version`, `created_at`, `updated_at`.

### Format ADDR

Capsules de 3 caractères `[a-z0-9]`, séparées par `.`, sur 3 ou 4 niveaux.

```
myt.her.001
myt.her.arc.042
```

---

## API

```python
from loregram import generate_uid, compute_hash, verify_hash, update_hash

# Créer un UID
uid = generate_uid()
# → "lore:018fc6c2-8c8b-7c4a-a9d2-6a2d8d8f8e21"

# Calculer le hash
h = compute_hash(loregram)
# → "sha256:8f3c1b7e..."

# Vérifier l'intégrité
ok = verify_hash(loregram)
# → True / False

# Mettre à jour le hash après modification
loregram = update_hash(loregram)
```

---

## Tests

```bash
python -m pytest l0re/tests/ -v
```

10 cas obligatoires + 2 bonus (format UID, unicité).

---

## Canonicalisation

```python
canonical = json.dumps(
    {k: v for k, v in loregram.items() if k not in {"hash", "signature"}},
    sort_keys=True,
    separators=(',', ':'),
    ensure_ascii=False,
).encode('utf-8')

hash = "sha256:" + sha256(canonical).hexdigest()
```

---

**L0RE IS GO** — Mai 2026
