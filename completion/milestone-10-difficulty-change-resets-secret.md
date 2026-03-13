## Milestone 10: Difficulty Change Resets Secret

**Status:** Completed

**Bug fixed:** Changing the difficulty selector did not regenerate the secret number. The secret was only created once on first load (`if "secret" not in st.session_state`), so switching from Easy to Hard (or any difficulty) left the old secret in place — potentially outside the new range.

**Change made:** `app.py:31-36` — replaced the one-time `if "secret" not in st.session_state` guard with a compound condition that also checks whether the stored difficulty differs from the current selection. When a mismatch is detected, the secret, attempts, status, and history are all reset to match the new difficulty.

**Tests added:**
- No new test function added (behavior is Streamlit session-state driven; covered by manual verification)

**AI Collaboration:** Claude identified that the session state guard never re-evaluated on difficulty change and added a `st.session_state.get("difficulty") != difficulty` comparison to trigger a full game reset whenever the player switches difficulty.
