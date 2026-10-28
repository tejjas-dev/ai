# Practical 05 - 8-Puzzle BFS

## Aim
Solve the 8-puzzle using Breadth-First Search to find the shortest solution path.

## Algorithm Description
- **State representation:** Flat tuple of 9 integers (0 = blank, 1–8 = tiles).
- **Goal state:** `(1, 2, 3, 4, 5, 6, 7, 8, 0)`
- **Actions:** Move blank Up, Down, Left, Right (swapping with adjacent tile).
- **BFS:** Guarantees optimal (minimum moves) solution by exploring level-by-level.
- **Parent tracking:** Reconstructs path from goal back to start.
- **Visited set:** Prevents revisiting states.

## How to Execute
```bash
cd Practical-05-8-Puzzle-BFS
python3 main.py
```
**Sample input (from screenshot):** `1 2 3 4 0 6 7 5 8`

## Corrections Made
None. The supplied code was syntactically correct and executed without modification.

## Sample Output
See `output.txt` — solves in 2 moves (3 steps including initial).

## Known Limitations
- BFS explores all states up to solution depth; for 8-puzzle worst-case (31 moves) this is ~180k states — feasible but slow.
- Memory usage grows with visited states; not suitable for 15-puzzle or larger.
- No heuristic guidance — pure BFS. A* (Practical 03) is more efficient for this problem.