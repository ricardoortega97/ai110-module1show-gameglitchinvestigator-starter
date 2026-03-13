## Milestone 6: Secret Cast to String on Even Attempts (Wins Impossible)
**Status:** Completed.

**Bug fixed:** On every even-numbered attempt, `secret` was cast to a string via `str(st.session_state.secret)`. This caused a `TypeError: '>' not supported between instances of 'int' and 'str'` when `check_guess` tried to compare the integer guess against the string secret, making winning impossible on those turns.

**Change made:** `app.py:94` — removed the `if/else` even/odd branching block that cast `secret` to `str`; replaced with `secret = st.session_state.secret`, ensuring the secret is always passed as an `int` to `check_guess`.

**Tests added:**
- `test_win_on_even_simulated_attempt`
- `test_too_high_on_even_attempt`, `test_too_low_on_even_attempt`
- `test_win_at_high_boundary`, `test_win_at_low_boundary`
- `test_no_type_error_int_vs_int` (in `tests/test_milestone6.py`)

**AI Collaboration:** Claude identified the even/odd string-cast block in `app.py` as the root cause of the `TypeError` and the impossible-win bug, and confirmed the fix by tracing the type flowing into `check_guess` across all attempt numbers.
