# --------------------------- HANGMAN GAME -------------------------------------
# Hangman is a word guessing game where one player thinks of a word,            |
# and the other player tries to guess the word by suggesting letters            |
# one at a time. If the guessing player suggests a letter that appears          |
# in the word, the other player writes the letter in all its correct positions. |
# If the suggested letter does not appear in the word, the other player draws   |
# one part of a hanging man stick figure as a tally mark. The game continues    |
# until the guessing player either correctly guesses the word or the hanging    |
# man is completed. In this game the player will be playing against the         |
# CPU. Good Luck!                                                               |          
#-------------------------------------------------------------------------------

# Import necessary modules, in this case is random to give the player a random word to play with.
import random


# Set up the hangman stages as a list of strings
HANGMAN_STAGES = [
    """
     ________
    |        |
    |        O
    |        
    |        
    |       
 ___|___
""",
    """
     ________
    |        |
    |        O
    |        |
    |        
    |       
 ___|___
""",
    """
     ________
    |        |
    |        O
    |       \|
    |        
    |       
 ___|___
""",
    """
     ________
    |        |
    |        O
    |       \|/
    |        
    |       
 ___|___
""",
    """
     ________
    |        |
    |        O
    |       \|/
    |        |
    |       
 ___|___
""",
    """
     ________
    |        |
    |        O
    |       \|/
    |        |
    |       / 
 ___|___
""",
    """
     ________
    |        |
    |        O
    |       \|/
    |        |
    |       / \\
 ___|___
"""
]
# Set a list of programming languages to choose from inside a tuple
LANGUAGES = ("PYTHON", "JAVA", "RUBY", "SWIFT", "CPLUSPLUS", "JAVASCRIPT", "TYPESCRIPT", "KOTLIN")

# Set the maximum number of wrong guesses before the game is over
MAX_WRONG_GUESSES = len(HANGMAN_STAGES) - 1

# Choose a language from LANGUAGES at random
selected_language = random.choice(LANGUAGES)

# Set up the initial game state
guessed_so_far = "-" * len(selected_language)
wrong_guesses = 0
used_letters = []

# Print a welcome message
print("Welcome to Hangman. Guess the name of the programming language. Good luck!\n")

# Loop until the player has won or lost
while wrong_guesses < MAX_WRONG_GUESSES and guessed_so_far != selected_language:
    # Print the current state of the game
    print(HANGMAN_STAGES[wrong_guesses])
    print("\nYou've used the following letters:\n", used_letters)
    print("\nSo far, the word is:\n", guessed_so_far)

    # Ask the player for a guess
    guess = input("\n\nEnter your guess (a letter or the entire word): ")
    guess = guess.upper()

    # Check if the guess has already been made
    while guess in used_letters:
        print("The letter already have been used, take another guess ", guess)
        guess = input("Enter your guess: ")
        guess = guess.upper()

    # Add the guess to the list of used letters
    used_letters.append(guess)

    # Check if the guess is in the language
    if guess == selected_language:
        guessed_so_far = guess
    elif guess in selected_language:
        print("\nYes!", guess, "is in the language!")

        # Create a new `guessed_so_far` string with the guess in the correct position
        new = ""
        for i in range(len(selected_language)):
            if guess == selected_language[i]:
                new += guess
            else:
                new += guessed_so_far[i]
        guessed_so_far = new

    # If the guess is not in the language, increment the number of wrong guesses
    else:
        print("\nSorry,", guess, "isn't in the language.")
        wrong_guesses += 1
    if guessed_so_far == selected_language:
        print("\nCongratulations! You guessed the word", selected_language)
    else:
        print(HANGMAN_STAGES[MAX_WRONG_GUESSES])
        print("\nSorry, you ran out of guesses. The word was", selected_language)



