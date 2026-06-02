"""
Tests RÈGLE L0RE #001 — uid / hash / addr
10 cas obligatoires.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from loregram import compute_hash, verify_hash, update_hash, generate_uid


# ---------------------------------------------------------------------------
# Fixture
# ---------------------------------------------------------------------------

def make_loregram(**overrides) -> dict:
    """Loregram de base valide avec hash calculé."""
    lg = {
        "uid":         "lore:018fc6c2-8c8b-7c4a-a9d2-6a2d8d8f8e21",
        "parent_hash": None,
        "addr":        "myt.her.001",
        "title":       "Fragment test",
        "body":        "Ceci est un fragment de lore.",
        "links":       [],
        "metadata":    {},
        "version":     "0.1",
        "created_at":  "2026-05-24T00:00:00Z",
        "updated_at":  "2026-05-24T00:00:00Z",
    }
    lg.update(overrides)
    lg["hash"] = compute_hash(lg)
    return lg


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

def test_1_identical_loregrams_same_hash():
    """Deux loregrams identiques (sauf hash/signature) → même hash."""
    lg1 = make_loregram()
    lg2 = make_loregram()
    lg1["hash"]      = "hash_different"
    lg2["signature"] = "sig_quelconque"
    assert compute_hash(lg1) == compute_hash(lg2)


def test_2_body_change_changes_hash():
    """Modifier body → hash différent."""
    lg = make_loregram()
    h  = lg["hash"]
    lg["body"] = "Contenu modifié."
    assert compute_hash(lg) != h


def test_3_title_change_changes_hash():
    """Modifier title → hash différent."""
    lg = make_loregram()
    h  = lg["hash"]
    lg["title"] = "Titre modifié"
    assert compute_hash(lg) != h


def test_4_addr_change_changes_hash():
    """Modifier addr → hash différent."""
    lg = make_loregram()
    h  = lg["hash"]
    lg["addr"] = "oth.er.999"
    assert compute_hash(lg) != h


def test_5_links_change_changes_hash():
    """Modifier links → hash différent."""
    lg = make_loregram()
    h  = lg["hash"]
    lg["links"] = ["myt.her.002"]
    assert compute_hash(lg) != h


def test_6_metadata_change_changes_hash():
    """Modifier metadata → hash différent."""
    lg = make_loregram()
    h  = lg["hash"]
    lg["metadata"] = {"author": "Arnaud"}
    assert compute_hash(lg) != h


def test_7_signature_does_not_change_hash():
    """Modifier signature → hash inchangé."""
    lg = make_loregram()
    h  = compute_hash(lg)
    lg["signature"] = "nouvelle_signature"
    assert compute_hash(lg) == h


def test_8_hash_field_does_not_change_computed_hash():
    """Modifier le champ hash → hash calculé inchangé (pas de récursion)."""
    lg = make_loregram()
    h  = compute_hash(lg)
    lg["hash"] = "sha256:" + "0" * 64
    assert compute_hash(lg) == h


def test_9_verify_hash_intact():
    """verify_hash → True sur loregram intact."""
    lg = make_loregram()
    assert verify_hash(lg) is True


def test_10_verify_hash_altered():
    """verify_hash → False sur loregram altéré."""
    lg = make_loregram()
    lg["body"] = "Altération silencieuse."
    assert verify_hash(lg) is False


# ---------------------------------------------------------------------------
# Bonus : generate_uid
# ---------------------------------------------------------------------------

def test_uid_format():
    uid = generate_uid()
    assert uid.startswith("lore:")
    parts = uid[5:].split("-")
    assert len(parts) == 5
    assert parts[2][0] == "7"        # version 7
    assert parts[3][0] in "89ab"     # variant 10xx


def test_uid_unique():
    uids = {generate_uid() for _ in range(100)}
    assert len(uids) == 100
