# Hangman
# Made by Leo

import random

words = ["python", "banana", "glider", "keyboard", "rocket", "giraffe", "pizza", "castle"]
word = random.choice(words)   # picks a random word from the list

guessed = ""   # every letter the player has guessed so far, all stuck together in one string
lives = 6

print("Welcome to Hangman!")
print(f"The word has {len(word)} letters.")

while lives > 0:

    # build up the display one letter at a time - guessed letters show, the rest are blanks
    display = ""
    i = 0
    while i < len(word):
        if word[i] in guessed:
            display += word[i] + " "
        else:
            display += "_ "
        i += 1

    # Task 1 - if there are no blanks left in display, the player has won

    print()
    print(display)
    print(f"Lives left: {lives}")
    # Task 2 - show the player which wrong letters they've already tried

    guess = input("Guess a letter: ").lower()
    # Task 3 - don't take a life for a letter they've already guessed, or for anything that isn't one letter

    guessed += guess

    if guess in word:
        print("Nice one!")
    else:
        print("Unlucky, you lose a life!")
        lives -= 1

if lives == 0:
    print(f"Game over! The word was {word}.")
