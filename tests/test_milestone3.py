# Verification checklist:
## [ ] Normal case passes — Easy returns (1, 20), Normal returns (1, 50), Hard returns (1, 100)
## [ ] Edge case 1: Unknown difficulty falls back to (1, 100)
## [ ] Edge case 2: Case-sensitive input ("easy" lowercase) does not match Easy
## [ ] Edge case 3: Empty string difficulty falls back to (1, 100)

import pytest
from logic_utils import get_range_for_difficulty


def test_easy_range():
    assert get_range_for_difficulty("Easy") == (1, 20)


def test_normal_range():
    assert get_range_for_difficulty("Normal") == (1, 50)


def test_hard_range():
    assert get_range_for_difficulty("Hard") == (1, 100)


def test_hard_range_is_wider_than_normal():
    _, hard_high = get_range_for_difficulty("Hard")
    _, normal_high = get_range_for_difficulty("Normal")
    assert hard_high > normal_high, "Hard should have a wider range than Normal"


# Edge case: unknown difficulty string falls back to default (1, 100)
def test_unknown_difficulty_fallback():
    assert get_range_for_difficulty("Impossible") == (1, 100)


# Edge case: lowercase difficulty does not match named difficulties
def test_lowercase_difficulty_fallback():
    assert get_range_for_difficulty("easy") == (1, 100)


# Edge case: empty string difficulty falls back to default (1, 100)
def test_empty_string_difficulty_fallback():
    assert get_range_for_difficulty("") == (1, 100)
