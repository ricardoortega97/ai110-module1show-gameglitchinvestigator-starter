from logic_utils import check_guess, get_high_score, record_completed_score


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


def test_record_completed_score_keeps_last_five_games():
    scores = [10, 20, 30, 40, 50]

    updated_scores = record_completed_score(scores, 60)

    assert updated_scores == [20, 30, 40, 50, 60]


def test_get_high_score_returns_max_from_recent_games():
    result = get_high_score([15, 45, 25, 40, 35])

    assert result == 45


def test_get_high_score_returns_none_for_empty_history():
    result = get_high_score([])

    assert result is None
