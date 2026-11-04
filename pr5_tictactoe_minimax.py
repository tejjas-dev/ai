# Tic-Tac-Toe using Minimax Algorithm
# System = MAX (X), User = MIN (O)

import math

board = [" "] * 9

def check_win(p):
    wins = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    return any(all(board[i] == p for i in line) for line in wins)

def minimax(is_max):
    if check_win("X"):
        return 1
    if check_win("O"):
        return -1
    if " " not in board:
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                best = max(best, minimax(False))
                board[i] = " "
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                best = min(best, minimax(True))
                board[i] = " "
        return best

def show_board():
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("--+---+--")

print("Tic-Tac-Toe: System = X, You = O")
print("Choose positions from 1 to 9:")
print("1 | 2 | 3")
print("--+---+--")
print("4 | 5 | 6")
print("--+---+--")
print("7 | 8 | 9")

while True:
    # System (MAX player)
    best_score = -math.inf
    best_move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = "X"
    print("\nSystem's move:")
    show_board()

    if check_win("X"):
        print("System wins!")
        break
    if " " not in board:
        print("It's a draw!")
        break

    # User (MIN player)
    while True:
        try:
            move = int(input("\nEnter your position (1-9): ")) - 1
            if 0 <= move < 9 and board[move] == " ":
                board[move] = "O"
                break
            print("Invalid position! Choose an empty position.")
        except ValueError:
            print("Please enter a number from 1 to 9.")

    show_board()

    if check_win("O"):
        print("You win!")
        break
    if " " not in board:
        print("It's a draw!")
        break
