# Practical 02 - BFS Grid Pathfinding

## Aim
Implement a model-based intelligent agent that finds a path from start (S) to goal (G) on a 5×5 grid with obstacles (#) using Breadth-First Search (BFS).

## Algorithm Description
- **State space:** Grid positions (row, col) on a 5×5 grid.
- **Actions:** Move Up, Down, Left, Right (no diagonals).
- **Obstacles:** Cells marked `#` are walls and cannot be entered.
- **BFS exploration:** Uses a queue to explore level-by-level, guaranteeing the shortest path (in steps) from start to goal.
- **Visited tracking:** A set prevents revisiting cells.

## How to Execute
```bash
cd Practical-02-BFS-Grid-Pathfinding
python3 main.py
```
No input required — the grid is hardcoded.

## Corrections Made
- **Line 29 (original):** `new_path = path + [next_position` → **Fixed:** added missing closing bracket `]` → `new_path = path + [next_position]`
- This was the only syntax error; the algorithm logic was preserved as-is.

## Sample Output
See `output.txt` for the exact console output matching the provided screenshot. The agent finds an 8-step path visiting 18 unique cells.