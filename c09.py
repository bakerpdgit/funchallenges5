# Battleships
# Made by Leo

import random

SIZE = 5
NUM_SHIPS = 3
shots = 15

# "" = sea, "S" = ship, "X" = hit, "o" = miss
board = []
for row in range(SIZE):
    newRow = []
    for col in range(SIZE):
        newRow.append("")
    board.append(newRow)


def placeShips(board):
    placed = 0
    while placed < NUM_SHIPS:
        row = random.randint(0, SIZE - 1)
        col = random.randint(0, SIZE - 1)
        if board[row][col] == "":
            board[row][col] = "S"
            placed += 1


def displayBoard(board):
    header = "   "
    for col in range(SIZE):
        header += str(col) + " "
    print(header)

    for row in range(SIZE):
        line = str(row) + "  "
        for col in range(SIZE):
            square = board[row][col]
            if square == "X" or square == "o":
                line += square + " "
            else:
                line += "~ "  # hides the ships
        print(line)
    print()


def fireShot(board, row, col):
    if row < 0 or row >= SIZE or col < 0 or col >= SIZE:
        return "invalid"

    # Task 2: stop repeat shots

    if board[row][col] == "S":
        board[row][col] = "X"
        return "hit"

    board[row][col] = "o"
    return "miss"


def isGameOver(board):
    # Task 3: return True if no ships are left

    return False


# Main game loop
placeShips(board)
print(f"There are {NUM_SHIPS} ships hidden in the sea. Sink them all!")

while True:
    displayBoard(board)

    # Task 1: show shots left

    row = int(input(f"Row (0-{SIZE - 1}): "))
    col = int(input(f"Column (0-{SIZE - 1}): "))

    result = fireShot(board, row, col)

    if result == "invalid":
        print("Invalid shot! Try again.")
    else:
        shots -= 1

        if result == "hit":
            print("Hit!")
        else:
            print("Miss.")

        if isGameOver(board):
            displayBoard(board)
            print("You sank all the ships! You win!")
            break

        if shots == 0:
            displayBoard(board)
            print("Out of shots. Game over!")
            break