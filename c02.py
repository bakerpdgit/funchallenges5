# The Animal Guess-O-Matic
# Starter code for Tasks 1–4
# Run this working game first, then follow the challenges in c02.md.

# --- Functions ---

# ==> Task 2 - Make the questions friendlier
def ask_yes_no(question):
    answer = input(question + " (yes/no) ")
    return answer == "yes"


# ==> Task 3 - Follow the animal trail
# This version only follows one question. Make it follow any number!
def play_round(tree):
    node = tree

    if len(node) == 3:
        if ask_yes_no(node[0]):
            node = node[1]
        else:
            node = node[2]

    if ask_yes_no("Is your animal a " + node[0] + "?"):
        print("I guessed it! My animal knowledge is legendary!")
    else:
        print("You win! I don't know that animal yet.")
        # ==> Task 4 - Teach an old program new tricks
        # Ask for the animal and a question that separates it from my guess.
        # Then turn this animal node into a question with two animal branches.


# --- Main Code ---

# An animal is a one-item list: [animal_name].
# A question is a three-item list: [question, yes_branch, no_branch].
knowledge = [
    "Does it live in water?",
    ["dolphin"],
    ["cat"],
]

# ==> Task 1 - Give your animal expert some personality
print("Welcome to the Animal Guess-O-Matic!")
print("Think of an animal and I will try to guess it.")

while True:
    play_round(knowledge)
    if not ask_yes_no("Would you like to play again?"):
        break
    print("Think of another animal!")

print("Thanks for playing!")
