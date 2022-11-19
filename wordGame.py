# Testing UI Framework
from tkinter import *
root = Tk()
root.title("What's The Word? The Almighty Name")

# All Variables
marks = 0 # Player's Marks

# Function chooseQuestions
def chooseQuestions():
    return
    # for i in range(len()):
        # myLabel = Label(root, text="Button Number " + i)

# Function checkGuess
def checkGuess():
    return
#     playerGuess = Label(root, text="Player's Guess Number").grid(row=1, column=0,)
#     playerGuessCount = Label(root, text="Playes's Guess Count").grid(row=1, column=5)

# Function checkMarks
def checkMarks():
    return
    # playerMarks = Label(root, text="Your Marks is " + marks)

# Player options to choose which word to guess (Button Widgets)
buttonOne = Button(root, text="Guess Me 1!", width=10, command=chooseQuestions).grid(row=0, column=0, columnspan=1)
buttonTwo = Button(root, text="Guess Me 2!", width=10, command=chooseQuestions).grid(row=0, column=1, columnspan=1)
buttonThree = Button(root, text="Guess Me 3!", width=10, command=chooseQuestions).grid(row=0, column=2, columnspan=1)
buttonFour = Button(root, text="Guess Me 4!", width=10, command=chooseQuestions).grid(row=0, column=3, columnspan=1)
buttonFive = Button(root, text="Guess Me 5!", width=10, command=chooseQuestions).grid(row=0, column=4, columnspan=1)
buttonMarks = Button(root, text="My Marks!", width=10,  command=checkMarks).grid(row=0, column=5, columnspan=1)

# Hint for Player (Label Widgets)
hint = Label(root, text="Hint for the word here").grid(row=1, column=2)

# Words to Guess
words = Label(root, text="Word to Guess here").grid(row=2, column=2)

# Players previous Input display (Label Widget)


# Input for players to guess the word (Input Widget)
playerGuess = Entry(root, width=100, bg="white").grid(row=3, column=0, columnspan=4)

# Guess Button for Player Guess
guessButton = Button(root, text="Be My Guess!", width=10, command=checkGuess).grid(row=3, column=4)

# Quit Button
guessButton = Button(root, text="I Quit!", width=10,  command=root.quit).grid(row=3, column=5)

root.mainloop()