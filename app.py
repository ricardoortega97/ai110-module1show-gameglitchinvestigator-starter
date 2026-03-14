import random
import streamlit as st
from logic_utils import (
    check_guess,
    get_high_score,
    get_range_for_difficulty,
    parse_guess,
    record_completed_score,
    update_score,
)

st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Something is off.")

st.sidebar.header("Settings")

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)

attempt_limit_map = {
    "Easy": 6,
    "Normal": 8,
    "Hard": 5,
}

attempt_limit = attempt_limit_map[difficulty]

low, high = get_range_for_difficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

if (
    "secret" not in st.session_state
    or st.session_state.get("difficulty") != difficulty
):
    # FIX: Milestone 10 - changing difficulty regenerates the secret within
    # the selected range and resets the active round.
    st.session_state.secret = random.randint(low, high)
    st.session_state.difficulty = difficulty
    st.session_state.attempts = 0
    st.session_state.score = 0
    st.session_state.status = "playing"
    st.session_state.history = []
    st.session_state.score_recorded = False
if "attempts" not in st.session_state:
    # FIX: Changed from 1 to 0; first submission now correctly registers as
    # attempt #1.
    st.session_state.attempts = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "status" not in st.session_state:
    st.session_state.status = "playing"

if "history" not in st.session_state:
    st.session_state.history = []

if "completed_scores" not in st.session_state:
    st.session_state.completed_scores = []

if "score_recorded" not in st.session_state:
    st.session_state.score_recorded = False

st.subheader("Make a guess")

st.info(
    # FIX: Milestone 3 - banner now reflects the selected difficulty range.
    f"Guess a number between {low} and {high}. "
    f"Attempts left: {attempt_limit - st.session_state.attempts}"
)

with st.expander("Developer Debug Info"):
    st.write("Secret:", st.session_state.secret)
    st.write("Attempts:", st.session_state.attempts)
    st.write("Score:", st.session_state.score)
    st.write("Difficulty:", difficulty)
    st.write("History:", st.session_state.history)
    st.write("Completed scores:", st.session_state.completed_scores)
    st.write("Score recorded:", st.session_state.score_recorded)

raw_guess = st.text_input(
    "Enter your guess:",
    key=f"guess_input_{difficulty}"
)

col1, col2, col3 = st.columns(3)
with col1:
    submit = st.button("Submit Guess 🚀")
with col2:
    new_game = st.button("New Game 🔁")
with col3:
    show_hint = st.checkbox("Show hint", value=True)

if new_game:
    st.session_state.attempts = 0
    st.session_state.score = 0
    st.session_state.status = "playing"
    st.session_state.history = []
    st.session_state.score_recorded = False
    # FIX: Milestone 4 - New Game respects the selected difficulty range.
    st.session_state.secret = random.randint(low, high)
    st.success("New game started.")
    st.rerun()

if st.session_state.status != "playing":
    if st.session_state.status == "won":
        st.success("You already won. Start a new game to play again.")
    else:
        st.error("Game over. Start a new game to try again.")
    st.stop()

if submit:
    st.session_state.attempts += 1

    ok, guess_int, err = parse_guess(raw_guess)

    if not ok:
        st.session_state.history.append(raw_guess)
        st.error(err)
    else:
        st.session_state.history.append(guess_int)
        # FIX: Milestone 6 - secret always stays an int, preventing impossible
        # wins on even attempts.
        secret = st.session_state.secret

        # FIX: Milestone 9 - check_guess now returns a plain string.
        outcome = check_guess(guess_int, secret)
        messages = {
            "Win": "🎉 Correct!",
            "Too High": "📉 Go LOWER!",
            "Too Low": "📈 Go HIGHER!",
        }
        message = messages[outcome]

        if show_hint:
            st.warning(message)

        st.session_state.score = update_score(
            current_score=st.session_state.score,
            outcome=outcome,
            attempt_number=st.session_state.attempts,
        )

        if outcome == "Win":
            st.balloons()
            st.session_state.status = "won"
            if not st.session_state.score_recorded:
                st.session_state.completed_scores = record_completed_score(
                    st.session_state.completed_scores,
                    st.session_state.score,
                )
                st.session_state.score_recorded = True
            st.success(
                f"You won! The secret was {st.session_state.secret}. "
                f"Final score: {st.session_state.score}"
            )
        else:
            if st.session_state.attempts >= attempt_limit:
                st.session_state.status = "lost"
                if not st.session_state.score_recorded:
                    st.session_state.completed_scores = record_completed_score(
                        st.session_state.completed_scores,
                        st.session_state.score,
                    )
                    st.session_state.score_recorded = True
                st.error(
                    f"Out of attempts! "
                    f"The secret was {st.session_state.secret}. "
                    f"Score: {st.session_state.score}"
                )

current_high_score = get_high_score(st.session_state.completed_scores)
score_col, high_score_col = st.columns(2)
with score_col:
    st.metric("Current score", st.session_state.score)
with high_score_col:
    if current_high_score is None:
        st.metric("High score (last 5 games)", "No games yet")
    else:
        st.metric("High score (last 5 games)", current_high_score)

if st.session_state.completed_scores:
    recent_scores = ", ".join(
        str(score) for score in st.session_state.completed_scores
    )
    st.caption(f"Recent completed game scores: {recent_scores}")
else:
    st.caption("Complete a game to start tracking high scores.")

st.divider()
st.caption("Built by an AI that claims this code is production-ready.")
