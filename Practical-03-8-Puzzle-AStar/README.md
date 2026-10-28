# Practical 03 - 8-Puzzle A* Search

## Aim
Solve the 8-puzzle (3×3 sliding puzzle) using the A* search algorithm with the misplaced-tile heuristic.

## Algorithm Description
- **State representation:** 3×3 matrix with tiles 1–8 and `_` (blank).
- **Heuristic h(n):** Number of misplaced tiles (excluding the blank).
- **Cost g(n):** Depth of the node (number of moves from start).
- **Evaluation f(n) = g(n) + h(n):** A* prioritizes nodes with lowest f(n).
- **Open/Closed lists:** Standard A* bookkeeping with sorting of open list by f-value.

## How to Execute
```bash
cd Practical-03-8-Puzzle-AStar
python3 main.py
```
**Sample input (from screenshot):**
```
Start State Matrix:
1 2 3
4 _ 6
7 5 8

Goal State Matrix:
1 2 3
4 5 6
7 8 _
```
Enter each row on a new line with space-separated values.

## Corrections Made
- **Indentation fix:** The `accept(self)` method was incorrectly placed outside the `Puzzle` class in the source. Moved it inside the class with proper indentation (4 spaces).
- No other changes to algorithm logic.

## Sample Output
See `output.txt` — reaches goal in 2 moves with f(x)=2 at each step.

## Known Limitations
- The heuristic (misplaced tiles) is admissible but not very informed; A* will still find optimal solution but may expand more nodes than with Manhattan distance.
- No duplicate state detection in open list beyond closed list check; could be optimized.
- Input validation is minimal (assumes valid 3×3 matrices with `_` as blank).