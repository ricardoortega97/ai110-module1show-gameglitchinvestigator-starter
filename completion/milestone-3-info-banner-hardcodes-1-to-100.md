## Milestone 3: Info Banner Hardcodes "1 to 100"

**Status:** Completed

**Bug fixed:** The `st.info()` banner always displayed "Guess a number between 1 and 100" regardless of difficulty, because the range was hardcoded instead of using the already-computed `low` and `high` variables.

**Change made:** `app.py:47` — replaced `f"Guess a number between 1 and 100. "` with `f"Guess a number between {low} and {high}. "` (fix was already applied prior to this session).

**Tests added:**
- `test_easy_range`
- `test_normal_range`
- `test_hard_range`
- `test_hard_range_is_wider_than_normal`
- `test_unknown_difficulty_fallback`
- `test_lowercase_difficulty_fallback`
- `test_empty_string_difficulty_fallback`

**AI Collaboration:** Claude identified that the banner used hardcoded range values instead of the `low`/`high` variables from `get_range_for_difficulty`, confirmed the fix was already in place, and generated tests covering all three difficulties plus three edge cases for unknown, lowercase, and empty string inputs.
