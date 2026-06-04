"""Tests RÈGLE L0RE #002 — ADDR"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import pytest
from addr import validate_addr, is_valid_addr, parse_addr, addr_depth, addr_parent, AddrError


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def test_valid_3_levels():
    assert validate_addr("myt.her.001") is True

def test_valid_4_levels():
    assert validate_addr("myt.her.arc.042") is True

def test_all_digits_valid():
    assert validate_addr("000.111.999") is True

def test_mixed_alphanum_valid():
    assert validate_addr("a1b.2c3.d4e") is True

def test_invalid_too_short():
    with pytest.raises(AddrError):
        validate_addr("myt.her")

def test_invalid_too_long():
    with pytest.raises(AddrError):
        validate_addr("myt.her.arc.042.xyz")

def test_invalid_capsule_too_long():
    with pytest.raises(AddrError):
        validate_addr("myth.her.001")

def test_invalid_capsule_too_short():
    with pytest.raises(AddrError):
        validate_addr("my.her.001")

def test_invalid_uppercase():
    with pytest.raises(AddrError):
        validate_addr("MYT.her.001")

def test_invalid_special_char():
    with pytest.raises(AddrError):
        validate_addr("my-.her.001")

def test_invalid_empty_string():
    with pytest.raises(AddrError):
        validate_addr("")

def test_is_valid_addr_true():
    assert is_valid_addr("myt.her.001") is True

def test_is_valid_addr_false():
    assert is_valid_addr("bad") is False


# ---------------------------------------------------------------------------
# Parse
# ---------------------------------------------------------------------------

def test_parse_3_levels():
    result = parse_addr("myt.her.001")
    assert result == {"domain": "myt", "subdomain": "her", "index": "001"}

def test_parse_4_levels():
    result = parse_addr("myt.her.arc.042")
    assert result == {
        "domain":    "myt",
        "subdomain": "her",
        "section":   "arc",
        "index":     "042",
    }

def test_parse_invalid_raises():
    with pytest.raises(AddrError):
        parse_addr("bad.addr")


# ---------------------------------------------------------------------------
# Depth & Parent
# ---------------------------------------------------------------------------

def test_depth_3():
    assert addr_depth("myt.her.001") == 3

def test_depth_4():
    assert addr_depth("myt.her.arc.042") == 4

def test_parent_of_4():
    assert addr_parent("myt.her.arc.042") == "myt.her.arc"

def test_parent_of_3_is_none():
    assert addr_parent("myt.her.001") is None
