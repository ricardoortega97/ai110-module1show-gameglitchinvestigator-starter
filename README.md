# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Game: This is a guessing game with three levels - Normal, Easy, and Hard.
- [x] How many Bugs?: Found a total of ten bugs with the assistance of AI. Some were found while playing the game and provided the context to the AI. 
- [x] Fixes: I have a completion folder with details how they were fixed with some of them providing with test cases.

## 📸 Demo

   ![game_glitch](/images/game_glitch.gif)

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]

 - [x] **Pytest (Advance Edge-Case Testing):**

   - **Off by One Tests:**
   ![image1](./images/off_one_tests.png)

   -  **Even Strings Attempts:**
      ![image6](./images/even_stings.png)
   
   - **Get Difficulties:**
      ![image2](/images/levels.png)