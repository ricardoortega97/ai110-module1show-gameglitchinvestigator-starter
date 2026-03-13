## Milestone 1: Attempt Counter Off-by-One
**Status:** Completed.  

**Bug fixed:** `st.session_state.attempts` was initialized to `1` instead of `0`, causing the first submitted guess to be treated as attempt #2 and costing the player one attempt before they even started.  

**Change made:** `app.py:33` — changed `st.session_state.attempts = 1` to `st.session_state.attempts = 0`; stale `# FIXME` comment on the preceding line also removed.

**Tests added:** 
- `test_score_win_on_corrected_first_attempt`
- `test_parse_guess_string_input`, `test_parse_guess_negative_number`
- `test_parse_guess_empty_input` (in `tests/test_milestone1.py`)

**Test update:** Edge cases were revised from scoring-math assertions to input-boundary tests using `parse_guess`. The three edge cases now confirm that invalid inputs (`"abc"`, `""`) are rejected before the attempt counter increments, and that negative numbers (`"-5"`) are accepted as valid integers so the counter increments correctly. All 4 tests pass.

**AI Collaboration:** Claude identified the off-by-one by tracing the session state initialization in `app.py`, confirmed the downstream scoring impact, and later extended the edge cases to cover `parse_guess` input boundaries that guard the attempt counter from incrementing on invalid input.
