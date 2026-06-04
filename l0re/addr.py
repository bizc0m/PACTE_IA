"""
L0RE IS GO — v0.1
RÈGLE #002 : ADDR — adressage sémantique

Format : capsules [a-z0-9]{3}, séparées par '.', 3 ou 4 niveaux.

Exemples valides :
    myt.her.001
    myt.her.arc.042

Niveaux :
    niveau 1 — domaine     (ex: myt)
    niveau 2 — sous-domaine (ex: her)
    niveau 3 — section      (ex: arc)   [optionnel si 4 niveaux]
    dernier   — index       (ex: 001)
"""

import re

_CAPSULE = re.compile(r'^[a-z0-9]{3}$')


class AddrError(ValueError):
    pass


def validate_addr(addr: str) -> bool:
    """
    Retourne True si l'adresse est valide.
    Lève AddrError avec message explicite sinon.
    """
    if not isinstance(addr, str):
        raise AddrError(f"addr doit être une chaîne, reçu {type(addr).__name__}")

    parts = addr.split('.')

    if len(parts) not in (3, 4):
        raise AddrError(
            f"addr doit avoir 3 ou 4 niveaux, reçu {len(parts)} : '{addr}'"
        )

    for i, part in enumerate(parts):
        if not _CAPSULE.match(part):
            raise AddrError(
                f"capsule[{i}] invalide '{part}' — "
                f"attendu exactement 3 chars [a-z0-9]"
            )

    return True


def is_valid_addr(addr: str) -> bool:
    """Version booléenne sans exception."""
    try:
        return validate_addr(addr)
    except AddrError:
        return False


def parse_addr(addr: str) -> dict:
    """
    Parse une adresse valide en composants nommés.

    3 niveaux → {domain, subdomain, index}
    4 niveaux → {domain, subdomain, section, index}
    """
    validate_addr(addr)
    parts = addr.split('.')

    if len(parts) == 3:
        return {
            "domain":    parts[0],
            "subdomain": parts[1],
            "index":     parts[2],
        }
    return {
        "domain":    parts[0],
        "subdomain": parts[1],
        "section":   parts[2],
        "index":     parts[3],
    }


def addr_depth(addr: str) -> int:
    """Retourne le nombre de niveaux (3 ou 4)."""
    validate_addr(addr)
    return len(addr.split('.'))


def addr_parent(addr: str) -> str | None:
    """
    Retourne l'adresse parente (un niveau au-dessus).
    Retourne None si déjà au niveau minimal (3 niveaux).
    """
    validate_addr(addr)
    parts = addr.split('.')
    if len(parts) == 3:
        return None
    return '.'.join(parts[:-1])
