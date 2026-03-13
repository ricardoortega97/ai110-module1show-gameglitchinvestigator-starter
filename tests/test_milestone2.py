from logic_utils import get_range_for_difficulty

# Verification checklist:
## [ ] Normal case passes
## [ ] Edge case 1: Hard range is wider than Normal (Hard > Normal)
## [ ] Edge case 2: Easy range is narrower than Normal
## [ ] Edge case 3: Unknown difficulty falls back to default (1, 100)


def test_normal_range():
    """Normal difficulty should return (1, 50)."""
    assert get_range_for_difficulty("Normal") == (1, 50)


def test_hard_range():
    """Hard difficulty should return (1, 100)."""
    assert get_range_for_difficulty("Hard") == (1, 100)


def test_easy_range():
    """Easy difficulty should return (1, 20)."""
    assert get_range_for_difficulty("Easy") == (1, 20)


def test_hard_range_wider_than_normal():
    # Edge case: Hard range is wider than Normal (Hard > Normal)
    _, hard_high = get_range_for_difficulty("Hard")
    _, normal_high = get_range_for_difficulty("Normal")
    assert hard_high > normal_high, "Hard should have a wider range than Normal"


def test_normal_range_wider_than_easy():
    # Edge case: Easy range is narrower than Normal
    _, normal_high = get_range_for_difficulty("Normal")
    _, easy_high = get_range_for_difficulty("Easy")
    assert normal_high > easy_high, "Normal should have a wider range than Easy"


def test_unknown_difficulty_fallback():
    # Edge case: Unknown difficulty falls back to default (1, 100)
    assert get_range_for_difficulty("Impossible") == (1, 100)
