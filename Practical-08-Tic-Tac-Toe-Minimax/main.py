board = [" "] * 9

wins = [(0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)]

# Check winner
def winner():
    for a, b, c in wins:
        if board[a] == board[b] == board[c] != " ":
            return board[a]

# Minimax algorithm
def minimax(p):
    w = winner()
    if w == "O": return 1
    if w == "X": return -1
    if " " not in board: return 0

    scores = []
    for i in range(9):
        if board[i] == " ":
            board[i] = p
            next_p = "X" if p == "O" else "O"
            scores.append(minimax(next_p))
            board[i] = " "  # Undo move

    return max(scores) if p == "O" else min(scores)


# Main game (X = Human, O = AI)
while " " in board and not winner():
    for i in range(0, 9, 3):
        print("|".join(board[i:i+3]))

    move = int(input("Enter position (1-9): ")) - 1

    if move < 0 or move > 8 or board[move] != " ":
        print("Invalid move!")
        continue

    board[move] = "X"

    if " " in board and not winner():
        best = -2

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax("X")
                board[i] = " "

                if score > best:
                    best = score
                    ai_move = i

        board[ai_move] = "O"


# Final result
for i in range(0, 9, 3):
    print("|".join(board[i:i+3]))

print("Winner:", winner() or "Draw")
