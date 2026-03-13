# Verification checklist:
# [ ] Normal case passes — all four functions importable and return correct values
# [ ] Edge case 1: Hard difficulty returns wider range than Normal (M2 fix)
# [ ] Edge case 2: check_guess too-high returns "Go LOWER!" not "Go HIGHER!" (M5 fix)
# [ ] Edge case 3: update_score deducts on "Too High" at even attempt number (M7 fix)

from logic_utils import get_range_for_difficulty, parse_guess, check_guess, update_score


# --- Normal case: all four functions are callable and return expected types ---

def test_all_functions_importable_and_callable():
    """Milestone 8: logic_utils stubs are replaced with real implementations."""
    low, high = get_range_for_difficulty("Normal")
    assert isinstance(low, int) and isinstance(high, int)

    ok, val, err = parse_guess("42")
    assert ok is True and val == 42

    outcome, message = check_guess(42, 42)
    assert outcome == "Win"

    new_score = update_score(100, "Win", 1)
    assert isinstance(new_score, int)


# --- Edge case 1: Hard difficulty range is wider than Normal (M2 fix) ---

def test_hard_range_wider_than_normal():
    # Edge case: Hard should be 1–100, not the bugged 1–50
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert hard_high > normal_high, (
        f"Hard high ({hard_high}) should exceed Normal high ({normal_high})"
    )


# --- Edge case 2: Too-high guess directs player LOWER (M5 fix) ---

def test_check_guess_too_high_message_says_lower():
    # Edge case: guessing above the secret should tell the player to go LOWER
    outcome, message = check_guess(99, 1)
    assert outcome == "Too High"
    assert "LOWER" in message, f"Expected 'LOWER' in message, got: {message!r}"


# --- Edge case 3: update_score deducts on "Too High" at even attempt (M7 fix) ---

def test_update_score_too_high_even_attempt_deducts():
    # Edge case: even attempt numbers must NOT add points for a wrong "Too High" guess
    score_before = 100
    score_after = update_score(score_before, "Too High", attempt_number=2)
    assert score_after < score_before, (
        f"Score should decrease on 'Too High', got {score_after} (was {score_before})"
    )
