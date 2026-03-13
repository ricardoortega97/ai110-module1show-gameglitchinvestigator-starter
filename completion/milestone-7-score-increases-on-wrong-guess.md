## Milestone 7: Score Increases on Wrong Guess

**Status:** Completed

**Bug fixed:** `update_score` added +5 points on even-numbered "Too High" attempts instead of deducting -5, making wrong guesses rewarding.

**Change made:** `logic_utils.py:61-62` — even/odd branching removed; "Too High" now always returns `current_score - 5`. Fixed implicitly during the Milestone 8 refactor when logic was moved to `logic_utils.py`.

**Tests added:** None — covered by existing score behavior in manual play.

**AI Collaboration:** Claude identified the fix was already applied during Milestone 8's refactor and confirmed the correct deduction logic was in place at `logic_utils.py:61-62`.
