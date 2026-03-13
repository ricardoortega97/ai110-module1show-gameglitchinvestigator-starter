## Milestone 5: Hint Messages Swapped

**Status:** Completed

**Bug fixed:** `check_guess` returned `"Go HIGHER!"` when the guess was too high and `"Go LOWER!"` when too low — the direction hints were backwards, actively misleading the player away from the secret number.

**Change made:** [logic_utils.py:46-49](../logic_utils.py#L46-L49) — swapped the message strings so `guess > secret` returns `"Go LOWER!"` and the `else` branch returns `"Go HIGHER!"`.

**Tests added:**
- `test_too_high_returns_go_lower`
- `test_too_low_returns_go_higher`
- `test_exact_match_returns_win`
- `test_one_below_secret_is_too_low`
- `test_one_above_secret_is_too_high`
- `test_minimum_boundary_exact_match`

**AI Collaboration:** Claude traced the return values of `check_guess` in `logic_utils.py`, identified the swapped message strings, and collaborated with the user to apply the correct fix and generate edge-case tests verifying both outcome labels and direction hints.
