from logic_utils import update_score, parse_guess

# Milestone 1 — Attempt Counter Off-by-One
# Before fix: attempts init to 1, first submission yields attempt_number=2.
# After fix:  attempts init to 0, first submission yields attempt_number=1.
# update_score(attempt_number) is the downstream consumer that reveals the difference.
# parse_guess validates the input before attempt_number is ever incremented.
#
# Verification checklist:
# [ ] Normal case passes
# [ ] Edge case 1: string input is rejected before attempt counter increments
# [ ] Edge case 2: negative number is parsed as a valid (losing) guess
# [ ] Edge case 3: empty input is rejected before attempt counter increments

def test_score_win_on_corrected_first_attempt():
    # Normal case: after fix, first guess is attempt_number=1.
    # Win score: 100 - 10*(1+1) = 80. Before fix it was attempt_number=2 → 70.
    result = update_score(0, "Win", 1)
    assert result == 80

def test_parse_guess_string_input():
    # Edge case: string input ("abc") is rejected — parse_guess returns ok=False.
    # A rejected guess must not increment attempts, so the counter stays correct.
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert value is None
    assert err is not None

def test_parse_guess_negative_number():
    # Edge case: negative number is a valid integer — parse_guess returns ok=True.
    # The attempt counter will increment and update_score will run with attempt_number=1.
    ok, value, err = parse_guess("-5")
    assert ok is True
    assert value == -5
    assert err is None

def test_parse_guess_empty_input():
    # Edge case: empty string is rejected — parse_guess returns ok=False.
    # A rejected guess must not increment attempts, keeping the counter correct.
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None
    assert err is not None
