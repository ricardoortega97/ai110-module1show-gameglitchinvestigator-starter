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

 - [x] **Pytest (Advance Edge-Case Testing)**

   - **Off by One Tests:**
   ![image1](./images/off_one_tests.png)

   -  **Even Strings Attempts:**
      ![image6](./images/even_stings.png)
   
   - **Get Difficulties:**
      ![image2](/images/levels.png)

- [x] **Feature Expansion via Agent Mode**

   I requested the AI to implement a new feature to track the high score within the state with the list of 5 previous completed games. 

   - Created two new logic functions: `get_high_score` will return the max value in the list of the previous scores; `record_completed_score` appends the score to the list, with a limit of 5 values, so it will update the list by slicing the limit backwards. 

   - In the `app.py` file, there is a `completed_scores` within the session state that will record for each finished game, displaying the current and highest score. The outcome of "Win" is where holds additional session states that implements completed and scores to the logic. 

   **Gif**
   ![high_score](/images/high_score_feat.gif)

- [x] **Professional Documentation and Linting**

   Notes: I used Copilot for this task, the process was a bit confusing in a way as I tried searching for the option **Generate Documents** smart action and it was no where to be found. I instead provided the context and attached the file. I also went above and beyond with checking outside of the requested file for no reason. Used a bit too much on the context while running and looping but somehow managed to update it with PEP 8 style compliance. 

   

- [x] **AI Model Comparison**

   Thoughts: I have been using Copilot throughout my time using it in VSCode and never thought of trying another model. It was limited usage with checking minor issues, what can be improved, and generate some basic code. When I started to use Claude, the process was more flexible in a way since I created the agent, implement commands, and context was taken better. 

   For example, I used Copilot for the documentation/linting and comply with PEP 8 with the Inline Chat to only recommend me with issues. 

   **Inline chat**
   ![doc_lint_indent](/images/doc_lint2.png)

   With Claude and new techniques I learned in the course, I was able to apply better practices and management. 


