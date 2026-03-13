## Milestone 8: Refactor Logic into logic_utils.py

**Status:** Completed

**Bug fixed:** All four functions in `logic_utils.py` raised `NotImplementedError` — they were never implemented. Working logic lived only in `app.py` as inline definitions, causing every `pytest` test that imported from `logic_utils` to fail immediately.

**Change made:**
- `logic_utils.py` (lines 1–63): Replaced all four `raise NotImplementedError(...)` stubs with corrected implementations — including the M2 fix (Hard range `1,100`), M5 fix (hint messages swapped to correct direction), and M7 fix (Too High always deducts score).
- `app.py` (line 3): Added `from logic_utils import get_range_for_difficulty, parse_guess, check_guess, update_score`.
- `app.py` (lines 4–65 removed): Deleted the four inline function definitions, leaving `app.py` as UI-only.

**Tests added:**
- `test_all_functions_importable_and_callable`
- `test_hard_range_wider_than_normal`
- `test_check_guess_too_high_message_says_lower`
- `test_update_score_too_high_even_attempt_deducts`

**AI Collaboration:** Claude identified that all four `logic_utils.py` stubs were unimplemented, moved the corrected function bodies from `app.py` into `logic_utils.py`, and removed the inline definitions to enforce a clean UI/logic separation.
