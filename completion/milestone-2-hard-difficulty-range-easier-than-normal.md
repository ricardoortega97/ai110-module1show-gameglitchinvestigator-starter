## Milestone 2: Hard Difficulty Range Easier Than Normal
**Status:** Completed  
**Bug fixed:** Hard mode used range 1–50 while Normal used 1–100, making Hard paradoxically easier.  
**Change made:** `logic_utils.py:6-9` — swapped ranges so Normal returns `(1, 50)` and Hard returns `(1, 100)`.  
**Tests added:**
- `test_normal_range`
- `test_hard_range`
- `test_easy_range`
- `test_hard_range_wider_than_normal`
- `test_normal_range_wider_than_easy`
- `test_unknown_difficulty_fallback`

**AI Collaboration:** Claude confirmed the fix was already applied during the refactor phase and verified correctness by reviewing the inline comment and running all 6 generated tests.
