def get_range_for_difficulty(difficulty: str):
    """Resolve the inclusive guessing range for a difficulty level.

    Args:
        difficulty: Difficulty label selected by the player.
            Expected values are ``"Easy"``, ``"Normal"``, and ``"Hard"``.

    Returns:
        A 2-tuple ``(low, high)`` representing the inclusive numeric range used
        to generate the secret number. Unknown values fall back to
        ``(1, 100)``.
    """
    # FIX: Refactored from app.py stub into logic_utils.py using
    # Claude Agent mode; Hard range corrected to 1-100 (was 1-50).
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 100
    return 1, 100


def parse_guess(raw: str):
    """Parse raw user input into an integer guess.

    The parser accepts integer text and also decimal text by truncating toward
    zero via ``int(float(raw))`` for compatibility with existing game behavior.

    Args:
        raw: Raw input string from the UI.

    Returns:
        A tuple ``(ok, guess_int, error_message)`` where:
        - ``ok`` is ``True`` when parsing succeeds, otherwise ``False``.
        - ``guess_int`` is the parsed integer on success, otherwise ``None``.
        - ``error_message`` is a user-facing validation message on failure.
        - ``None`` is returned for ``error_message`` when parsing succeeds.
    """
    # FIX: Refactored from app.py stub into logic_utils.py using
    # Claude Agent mode.
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """Evaluate a player's guess against the secret number.

    Args:
        guess: Player's numeric guess.
        secret: Target number to compare against.

    Returns:
        Outcome string describing the result of the comparison:
        ``"Win"``, ``"Too High"``, or ``"Too Low"``.
    """
    # FIX: Refactored from app.py stub into logic_utils.py; hint messages
    # corrected (Too High -> LOWER, Too Low -> HIGHER) using Claude Agent mode.
    # FIX: Milestone 9 - returns plain outcome string (not tuple) so tests
    # assert == "Win" / "Too High" / "Too Low" (Claude Agent).
    if guess == secret:
        return "Win"
    if guess > secret:
        return "Too High"
    else:
        return "Too Low"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Compute the next score after a guess outcome.

    Scoring rules:
    - ``"Win"`` awards ``100 - 10 * (attempt_number + 1)`` points with a
        minimum award of 10 points.
    - ``"Too High"`` and ``"Too Low"`` each deduct 5 points.
    - Any unknown outcome leaves the score unchanged.

    Args:
        current_score: Score before applying this guess result.
        outcome: Outcome label from guess evaluation.
        attempt_number: Zero-based attempt index for the current round.

    Returns:
        Updated score after applying the scoring rule.
    """
    # FIX: Refactored from app.py stub into logic_utils.py; removed even/odd
    # branch so Too High always deducts using Claude Agent mode.
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
