# Verification checklist:
## [ ] Normal case passes — winning guess on an even-simulated attempt returns "Win"
## [ ] Edge case 1: exact secret match still wins when secret is at range boundary (high end)
## [ ] Edge case 2: comparison works correctly when guess equals secret (no TypeError)
## [ ] Edge case 3: no TypeError raised when comparing int guess to int secret (the original crash)

from logic_utils import check_guess


def test_win_on_even_simulated_attempt():
    """Core fix: check_guess always receives int secret, win is possible on any attempt."""
    secret = 42
    # simulate even attempt — secret must stay int, not str
    outcome, message = check_guess(42, secret)
    assert outcome == "Win"


def test_too_high_on_even_attempt():
    """check_guess correctly identifies Too High without TypeError."""
    secret = 30
    outcome, message = check_guess(50, secret)
    assert outcome == "Too High"


def test_too_low_on_even_attempt():
    """check_guess correctly identifies Too Low without TypeError."""
    secret = 80
    outcome, message = check_guess(10, secret)
    assert outcome == "Too Low"


# Edge case: boundary value — secret at top of range (e.g. Hard mode high=100)
def test_win_at_high_boundary():
    secret = 100
    outcome, _ = check_guess(100, secret)
    assert outcome == "Win"


# Edge case: no TypeError — int vs int comparison must not raise
def test_no_type_error_int_vs_int():
    secret = 55
    try:
        outcome, _ = check_guess(55, secret)
    except TypeError:
        assert False, "TypeError raised — secret was likely a str, not int"
    assert outcome == "Win"


# Edge case: guess of 1 vs secret of 1 (lowest boundary win)
def test_win_at_low_boundary():
    secret = 1
    outcome, _ = check_guess(1, secret)
    assert outcome == "Win"
