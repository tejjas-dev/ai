# Practical 06 - 8-Queens Backtracking

## Aim
Place 8 queens on an 8×8 chessboard so that no two queens attack each other, using recursive backtracking.

## Algorithm Description
- **Board representation:** 8×8 matrix of 0/1 (1 = queen).
- **Safety check:** For each row, try columns left-to-right; check column, upper-left diagonal, upper-right diagonal for conflicts.
- **Recursion:** Place queen in safe column, recurse to next row. If no safe column, backtrack (remove queen, try next column).
- **Termination:** When row == 8, a solution is found (first solution only).

## How to Execute
```bash
cd Practical-06-8-Queens
python3 main.py
```
No input required — finds and prints the first valid configuration.

## Corrections Made
None. The supplied code was syntactically correct and executed without modification.

## Sample Output
See `output.txt` — one valid 8-queens solution (queens at columns: 0, 2, 4, 6, 1, 3, 5, 7 for rows 0–7).

## Known Limitations
- Only finds the **first** solution (stops after one). There are 92 distinct solutions for 8-queens.
- Column order is fixed (0→7); different ordering would yield different first solution.
- No symmetry breaking or optimization — standard textbook backtracking.