# Verification checklist:
## [ ] Normal case passes
## [ ] Edge case 1: guess is exactly 1 below the secret (boundary too low)
## [ ] Edge case 2: guess is exactly 1 above the secret (boundary too high)
## [ ] Edge case 3: guess equals secret (exact match wins)

from logic_utils import check_guess


def test_too_high_returns_go_lower():
    """When guess > secret, outcome is 'Too High' and message directs player LOWER."""
    outcome, message = check_guess(50, 30)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_too_low_returns_go_higher():
    """When guess < secret, outcome is 'Too Low' and message directs player HIGHER."""
    outcome, message = check_guess(10, 30)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_exact_match_returns_win():
    """When guess == secret, outcome is 'Win'."""
    outcome, message = check_guess(30, 30)
    assert outcome == "Win"


# Edge case: guess is exactly 1 below the secret (boundary too low)
def test_one_below_secret_is_too_low():
    outcome, message = check_guess(29, 30)
    assert outcome == "Too Low"
    assert "HIGHER" in message


# Edge case: guess is exactly 1 above the secret (boundary too high)
def test_one_above_secret_is_too_high():
    outcome, message = check_guess(31, 30)
    assert outcome == "Too High"
    assert "LOWER" in message


# Edge case: guess and secret are both 1 (minimum boundary exact match)
def test_minimum_boundary_exact_match():
    outcome, message = check_guess(1, 1)
    assert outcome == "Win"
