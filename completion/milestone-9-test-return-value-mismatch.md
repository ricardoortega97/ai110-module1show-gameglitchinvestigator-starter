## Milestone 9: Test Return Value Mismatch

**Status:** Completed

**Bug fixed:** `check_guess` returned a tuple `(outcome, message)`, but the tests in `tests/test_game_logic.py` asserted against plain strings (`"Win"`, `"Too High"`, `"Too Low"`), causing all three tests to fail with `AssertionError: assert ('Win', '...') == 'Win'`.

**Change made:**
- `logic_utils.py:44-49` — Refactored `check_guess` to return only the outcome string, dropping the message from each return value.
- `app.py:97-99` — Replaced tuple unpacking `outcome, message = check_guess(...)` with `outcome = check_guess(...)` and added a `messages` dict to derive the display string from the outcome.

**Tests added:**
- `test_winning_guess`
- `test_guess_too_high`
- `test_guess_too_low`

**AI Collaboration:** Claude identified the contract mismatch between `check_guess`'s tuple return and the test assertions, proposed separating the outcome string from the display message, and collaborated with the user to update both `logic_utils.py` and `app.py` so the logic and UI responsibilities are cleanly separated.
