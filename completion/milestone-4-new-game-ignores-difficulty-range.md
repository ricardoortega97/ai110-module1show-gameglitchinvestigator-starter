## Milestone 4: New Game Ignores Difficulty Range

**Status:** Completed

**Bug fixed:** Clicking "New Game" always generated a secret number between 1 and 100 regardless of the selected difficulty, making Easy and Hard modes behave identically on reset.

**Change made:** `app.py:73` — replaced `random.randint(1, 100)` with `random.randint(low, high)` inside the `if new_game:` block so the new secret respects the current difficulty's computed range.

**Tests added:**
- `test_new_game_uses_difficulty_range_normal`
- `test_new_game_easy_range`
- `test_new_game_hard_range`
- `test_new_game_unknown_difficulty_fallback`

**AI Collaboration:** Claude identified the hardcoded `random.randint(1, 100)` on the New Game path by tracing the `low`/`high` variables already in scope from `get_range_for_difficulty`, and worked with the user to substitute them so all difficulty ranges are honored on reset.
