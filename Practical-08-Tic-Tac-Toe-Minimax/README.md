# Practical 08 - Tic-Tac-Toe Minimax AI

## Aim
Implement a Tic-Tac-Toe game where the AI plays optimally using the Minimax algorithm with depth penalty.

## Algorithm Description
- **Board:** 3×3 grid with "X" (human), "O" (AI), or " " (empty).
- **Minimax:** Recursive search of all possible game states.
  - AI (O) = maximizing player, score = 10 - depth (prefers faster wins).
  - Human (X) = minimizing player, score = depth - 10 (prefers delayed losses).
  - Draw = 0.
- **Depth penalty:** Encourages AI to win quickly and delay losses.
- **Best move:** AI evaluates all empty cells, picks move with highest minimax score.
- **Win detection:** Checks rows, columns, diagonals for 3-in-a-row.

## How to Execute
```bash
cd Practical-08-Tic-Tac-Toe-Minimax
python3 main.py
```
**Sample game (from screenshot):**
```
Enter row (1-3): 1
Enter column (1-3): 1
Enter row (1-3): 1
Enter column (1-3): 2
Enter row (1-3): 3
Enter column (1-3): 1
Enter row (1-3): 2
Enter column (1-3): 3
Enter row (1-3): 3
Enter column (1-3): 3
```

## Corrections Made
- **Line 138 (original):** `def check_winner(board)` → **Fixed:** added missing colon `:` → `def check_winner(board):`
- No other changes to algorithm logic.

## Sample Output
See `output.txt` — game ends in a draw with optimal play from both sides.

## Known Limitations
- Minimax explores the full game tree (max 9! = 362,880 leaf nodes); instantaneous for 3×3 but doesn't scale.
- No alpha-beta pruning (would be a simple optimization).
- AI is unbeatable with perfect play; best human outcome is a draw.
- No difficulty setting or "mistake" injection for weaker play.
- Input validation is basic (range check, occupancy check).