# Verification checklist:
## [ ] Normal case passes
## [ ] Edge case 1: Easy difficulty — secret always within 1–20
## [ ] Edge case 2: Hard difficulty — secret always within 1–100
## [ ] Edge case 3: Unknown difficulty — fallback range 1–100

import random
from logic_utils import get_range_for_difficulty


def test_new_game_uses_difficulty_range_normal():
    """Normal case: Normal difficulty range is 1–50."""
    low, high = get_range_for_difficulty("Normal")
    for _ in range(50):
        secret = random.randint(low, high)
        assert low <= secret <= high, f"Secret {secret} outside Normal range [{low}, {high}]"


def test_new_game_easy_range():
    # Edge case: Easy difficulty — secret always within 1–20
    low, high = get_range_for_difficulty("Easy")
    assert low == 1 and high == 20
    for _ in range(50):
        secret = random.randint(low, high)
        assert 1 <= secret <= 20, f"Secret {secret} outside Easy range [1, 20]"


def test_new_game_hard_range():
    # Edge case: Hard difficulty — secret always within 1–100
    low, high = get_range_for_difficulty("Hard")
    assert low == 1 and high == 100
    for _ in range(50):
        secret = random.randint(low, high)
        assert 1 <= secret <= 100, f"Secret {secret} outside Hard range [1, 100]"


def test_new_game_unknown_difficulty_fallback():
    # Edge case: Unknown difficulty — fallback range 1–100
    low, high = get_range_for_difficulty("Legendary")
    assert low == 1 and high == 100
