# Noughts and Crosses
# Ryan Stubbs

board = ["" for _ in range(9)] # 1D list used to store the board

# 0 | 1 | 2
# ---------
# 3 | 4 | 5
# ---------
# 6 | 7 | 8

player = 1

def isGameOver(board, symbol):
    # Task 2: add diagonal lines
    lines = [(0,3,6),
             (1,4,7),
             (2,5,8),
             (0,1,2),
             (3,4,5),
             (6,7,8),
             ]

    for line in lines:
        if all(board[idx] == symbol for idx in line):
            return True

    return False


def displayBoard(board):
    for i in range(9):
        if board[i] == "":
            print(i, end="")
        else:
            print(board[i], end="")

        if i % 3 == 2:
            print()
            if i != 8:
                print("-----------")
        else:
            print(" | ", end="")


def makeMove(board, position, symbol):
    if position < 0 or position > 8:
        return False

    if board[position] != "":
        return False

    board[position] = symbol
    return True


def isDraw(board):
    # Task 3: determine whether the game is a draw.
    # A draw happens when all 9 spaces are occupied
    # and neither player has won.

    return False


# Main game loop
while True:
    displayBoard(board)

    symbol = "X" if player == 1 else "O"
    print("Player", player, "'s turn!")

    position = int(input("Choose a position (0-8): "))

    if makeMove(board, position, symbol):
        if isGameOver(board, symbol):
            displayBoard(board)
            print("Player", player, "wins!")
            break

        if isDraw(board):
            displayBoard(board)
            print("It's a draw!")
            break

        # Task 1 - switch players

    else:
        print("Invalid move! Try again.")


# Extension 1:
# Add input validation so that the program doesn't crash
# if the user enters something that isn't a number.

# Extension 2:
# Add a single-player mode where the computer chooses
# a random empty position.

# Extension 3:
# Keep track of how many games each player wins.
# Allow players to play multiple games without restarting
# the program.