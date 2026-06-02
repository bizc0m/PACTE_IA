"""
L0RE IS GO — v0.1
RÈGLE #001 : uid / hash / addr

UID  = qui suis-je ?
HASH = suis-je intact ?
ADDR = où suis-je ?
"""

import hashlib
import json
import os
import time


# ---------------------------------------------------------------------------
# UID — UUIDv7 préfixé lore:
# ---------------------------------------------------------------------------

def generate_uid() -> str:
    """Génère lore:<uuidv7> — identité logique stable."""
    return f"lore:{_uuid7()}"


def _uuid7() -> str:
    """UUIDv7 : timestamp milliseconde + aléatoire, version=7, variant=10."""
    ts_ms = int(time.time() * 1000)

    # 48 bits timestamp | 4 bits version=7 | 12 bits rand_a
    time_high = (ts_ms >> 16) & 0xFFFFFFFF
    time_mid  = ts_ms & 0xFFFF
    rand_a    = int.from_bytes(os.urandom(2), 'big') & 0x0FFF
    ver_rand  = 0x7000 | rand_a

    # 2 bits variant=10 | 62 bits rand_b
    rand_b_raw  = int.from_bytes(os.urandom(8), 'big') & 0x3FFFFFFFFFFFFFFF
    var_high    = 0x8000 | ((rand_b_raw >> 48) & 0x3FFF)
    rand_b_low  = rand_b_raw & 0xFFFFFFFFFFFF

    return (
        f"{time_high:08x}-"
        f"{time_mid:04x}-"
        f"{ver_rand:04x}-"
        f"{var_high:04x}-"
        f"{rand_b_low:012x}"
    )


# ---------------------------------------------------------------------------
# HASH — SHA-256 de la forme canonique
# ---------------------------------------------------------------------------

# Champs exclus du calcul de hash
_EXCLUDED = frozenset({"hash", "signature"})


def canonicalize_loregram(loregram: dict) -> bytes:
    """
    Forme canonique : JSON UTF-8, clés triées, séparateurs compacts,
    sans hash ni signature.
    """
    filtered = {k: v for k, v in loregram.items() if k not in _EXCLUDED}
    return json.dumps(
        filtered,
        sort_keys=True,
        separators=(',', ':'),
        ensure_ascii=False,
    ).encode('utf-8')


def compute_hash(loregram: dict) -> str:
    """sha256:<hexdigest> de la forme canonique."""
    digest = hashlib.sha256(canonicalize_loregram(loregram)).hexdigest()
    return f"sha256:{digest}"


def verify_hash(loregram: dict) -> bool:
    """True si le hash stocké correspond au contenu actuel."""
    stored = loregram.get("hash")
    if not stored:
        return False
    return stored == compute_hash(loregram)


def update_hash(loregram: dict) -> dict:
    """Recalcule et met à jour le champ hash. Retourne le loregram modifié."""
    loregram["hash"] = compute_hash(loregram)
    return loregram
