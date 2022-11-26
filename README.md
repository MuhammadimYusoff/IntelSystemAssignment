# IntelSystemAssignment
This repo created for Intelligence System Assignment for State Space Search

# Game Flow
Arrange the letters to Allah's Almighty Name
	⁃	The user will be given a clue about Allah’s name
	⁃	They also will be provided with a few letters for them to arrange it [Pronunciation in English]
	⁃	No Timer, 3 tries
	⁃	The user have to reorder 5 names before they can win the game


# Flowchart logic from the code
1. When they open the application, shuffler() will run and display the jumbled word for the player to guess
2. The player will input their guess in the input field and press "Answer" button to check for correct guess
3. If the player input is correct, "Correct Answer" will be displayed
4. If the player input is incorrect, the input will be taken and the string will be evaluate with the correct answer (The Goal)
5. The logic will tell the player how many characters/letters are in wrong position (A* Algorithm)
6. The player can also use "Hint" button to display hint for clue and the correct answer, one letter per click
7. They can also change the word they have to guess by clicking on "Pick other word" button

# Short explanation
In this game, we demonstrate how A* Algorithm works, one of State Space Search Algorithm branch. The user input (the state) is compared with the word (the goal). The incorrect letter position will be printout to tell the player how many letters in wrong position.