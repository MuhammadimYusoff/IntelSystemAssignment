# INTELLIGENCE SYSTEM ASSIGNMENT 1
This repo created for Intelligence System Assignment for State Space Search
- [INTELLIGENCE SYSTEM ASSIGNMENT 1](#intelligence-system-assignment-1)
- [LECTURER AND TEAM MEMBERRS](#lecturer-and-team-memberrs)
- [SYSTEM REQUIREMENT](#system-requirement)
	- [Troubleshooting](#troubleshooting)
- [GAME FLOW](#game-flow)
- [FLOWCHART LOGIC FROM THE CODE](#flowchart-logic-from-the-code)
- [SHORT EXPLANATION](#short-explanation)


# LECTURER AND TEAM MEMBERRS
LECTURER: ASSOC. PROF. TS. DR. AMELIA RITAHANI BINTI ISMAIL

|                NAME				  |   MATRIC NUMBER    |
|                ---				  |  	  ---		   |
|   MUHAMMAD YUSOFF BIN JAMALUDDIN    |     2016799    	   |
|   FADWA RAMADAN ALI HASSAN    	  |     2024334    	   |
|   LAZEENA TARNIM RANAK    		  |     2027718    	   |


# SYSTEM REQUIREMENT
Python 3.9 (usually bundled with tkinter, UI framework for Python)
VSCode Extensions (and Extension Pack):
- Python
  - Pylance
  - isort
- Jupyter
  - Jupyter Cell Tags
  - Jupyter Keymap
  - Jupyter Notebook Renderer
  - Jupyter Slide Show


## Troubleshooting
Since Python was build on top of C++, some errors are NOT related to Python but lack of C++ compiler which can be found in the error message while compiling this program. Search the error "path not found" properly.
Thank you.


# GAME FLOW
Arrange the letters to Allah's Almighty Name
	⁃	The user will be given a clue about Allah’s name
	⁃	They also will be provided with a few letters for them to arrange it [Pronunciation in English]
	⁃	No Timer, 3 tries
	⁃	The user have to reorder 5 names before they can win the game


# FLOWCHART LOGIC FROM THE CODE
1. When they open the application, shuffler() will run and display the jumbled word for the player to guess
2. The player will input their guess in the input field and press "Answer" button to check for correct guess
3. If the player input is correct, "Correct Answer" will be displayed
4. If the player input is incorrect, the input will be taken and the string will be evaluate with the correct answer (The Goal)
5. The logic will tell the player how many characters/letters are in wrong position (A* Algorithm)
6. The player can also use "Hint" button to display hint for clue and the correct answer, one letter per click
7. They can also change the word they have to guess by clicking on "Pick other word" button


# SHORT EXPLANATION
In this game, we demonstrate how A* Algorithm works, one of State Space Search Algorithm branch. The user input (the state) is compared with the word (the goal). The incorrect letter position will be printout to tell the player how many letters in wrong position.