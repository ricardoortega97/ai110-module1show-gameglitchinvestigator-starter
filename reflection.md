# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

  **Response:** The game looks normal, with all the features to understand how it works. There are levels to play from. There are levels to play, as each time I play the game, the hint felt off as I noticed that the secret number was way off (It kept telling me go lower, but the number was higher). 

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  
  **Response:** Playing the game, seems that the amount of attempts is incorrect by one. Once I finish one game, the `New Game` button is not working. Looking into the debug info, on a new game, the hints were off and were backwards. I also noticed the levels were not correct as the easy had a wider range of numbers to pick from while the hard level number range is lower. 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

  **Response:** Will being using Claude Code (VSCode Extension) to assist me with this work, provided the context of the file and what it does, and implement a plan. I plan to create a milestone for each bug I found, pass it to the AI to plan with me what to work on and how we can test it. I also created commands to assist with me per each milestone. 
    - `/planTarget` - analyze the milestone. 
    - `/refactor` - implement the changes made from me or the AI Assistant.
    - `/generateTests` - creates three edge cases.
    - `/document` - create a shot readme per each milestone of the chat progress. 

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result). 

  **Response:** The AI did provide helpful information once we created this milestone plan. The first milestone was a simple change, which was to update the counter, to ensure it was working before generating testes, I would test it in the UI. One thing I missed was to ensure the `New Game` button resets to 0. 

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).  

  **Response:** When creating the commands, I provided some context how to structure it, but it failed to understand the outcome of the commands. I had to revise it from time to time as each milestone passes by. I also noticed that it created another pytest folder. Once I updated the context, I was able to get it back on track. On the first milestone tests, I noticed the edge cases are a bit similar and will pass. I had to add a few more test to with string input, invalid number (-1, empty). 

  Did noticed that it missed a few bugs while planning the AI to review the code. Since It does not understand the whole structure how Streamlit works, I had to provide the context of the bugs I had to find manually. 
 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?  

  **Response:** I would look at the logic of the code and compare the changes made with the AI and I. Run pytest with the edge cases for it. Once the test pass, I refresh the page and do final confirmations in the streamlit application. 

- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.

  **Response:** From what I understand running the test case helps with ensuring the player will not experience with running into the same issue the edge case was provided in. I looked into the test cases that was created and sounds reasonable that it will pass within that case. 
  

- Did AI help you design or understand any tests? How?  

  **Response:** I am very new to designing tests and have minimal understanding how to structure one. With the command created to generate test, the context informs the AI to create three edge case that it can think of. If needed, I can also provide another edge case along with the command. Though it will need to be revised to ensure the AI is creating reasonable tests. 
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

  **Response:** From what I understand with reruns, every button clicked causes Python to run the script from scratch, so without session state, variables reset each time. Learned something new: Vanilla JS + DOM on interaction, only the specific element/handler runs, while the entire Python script re-runs **top** to **bottom**.
  
   As for session states, these store and persist variables like **state components** in front-end development while running the application. 

- What change did you make that finally gave the game a stable secret number?

  **Response:** We added a check so that if st.session_state.secret_number already exists and is within the current difficulty's range, it keeps it. Otherwise, it generates a new one. This also resets on difficulty change.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

**Response:** A strategy I can do is create a milestone that I can work with along with the agent. This will help out reducing some tokens usage and ensure neither I nor the agent will be looping around to the same context. 

I can create a milestone plan that provides a small context of the app and only document the ones that the agent found bugs. 
AI does help adapt faster but there is also pros/cons using it. If one knows the context of the code, there is an advantage and can ship the product faster/fix bugs/update.  The disadvantage I can see is to blindly just use the AI to apply changes without a human checking. 

How I will be using AI is to assist me were I lack, educate me how I can improve with feedback, apply testing, and documentation to better understand the code. 
