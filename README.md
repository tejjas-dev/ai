# AI Practicals

Simple Python programs for the Artificial Intelligence Laboratory practicals.

- **Course:** PCC304COM - Artificial Intelligence Laboratory
- **University / Pattern:** SPPU, TE Computer Engineering, 2024 Pattern (Semester V)
- **Software requirement:** Python 3 (no extra libraries)

All files are in the root folder. Run any one with:

```
python pr1_vacuum_cleaner.py
```


| No. | File | Topic | Syllabus reference |
|-----|------|-------|--------------------|
| 1 | `pr1_vacuum_cleaner.py` | Simple Reflex Agent (Vacuum Cleaner World) | Part A, Assignment 1 |
| 2 | `pr2_model_based_agent.py` | Model-Based Intelligent Agent | Part A, Assignment 2 |
| 3 | `pr3_astar_8puzzle.py` | A* Search for 8 Puzzle | Part A, Assignment 3 |
| 4 | `pr4_tower_of_hanoi.py` | Tower of Hanoi (State Space Search) | Part A, Assignment 5 |
| 5 | `pr5_tictactoe_minimax.py` | Tic-Tac-Toe using Minimax | Part B, Assignment 7 |
| 6 | `pr6_8queens.py` | 8-Queens using Backtracking | Part B, Assignment 3 |
| 7 | `pr7_robot_bfs.py` | Robot Path Planning using BFS | Part B, Assignment 1 |
| 8 | `pr8_chatbot.py` | Simple Rule-Based Chatbot | Part B, Assignment 4 |

Syllabus requirement: Part A - any four and Part B - any four. These 8 practicals cover 4 from Part A and 4 from Part B.

---

## Practical 1: Simple Reflex Agent (Vacuum Cleaner World)
**File:** `pr1_vacuum_cleaner.py`
**Syllabus problem statement:** Part A, No. 1 - To design and implement a simple reflex agent for the Vacuum Cleaner world and analyze its rational behavior in a given environment.

- **Aim:** Build a simple reflex agent that cleans a two-room world (A and B).
- **Concept:** A simple reflex agent decides only from the *current percept* (location + dirt status), using condition-action rules. It has no memory.
- **Rules used:**
  - If the current room is Dirty -> Suck
  - Else if at A -> Move Right
  - Else if at B -> Move Left
- **How it works:** The environment is a dictionary `{'A': 'Dirty', 'B': 'Dirty'}`. The loop perceives, acts, and stops when both rooms are Clean.
- **Output:** Prints location, environment and action each step, then "Both rooms are clean!".
- **Conclusion:** The agent cleans both rooms using simple rules.

## Practical 2: Model-Based Intelligent Agent
**File:** `pr2_model_based_agent.py`
**Syllabus problem statement:** Part A, No. 2 - To implement a model-based intelligent agent capable of navigating a grid environment with obstacles using internal state representation.

- **Aim:** Implement an agent that keeps an internal model (memory) of the world and uses it to reach a goal.
- **Concept:** A model-based agent stores an *internal state* (here, the set of visited cells) so it does not depend only on the current percept.
- **Grid:** `S` = Start, `G` = Goal, `#` = Obstacle, `.` = Empty cell.
- **How it works:**
  1. Start at (0, 0) and add the position to `internal_state`.
  2. Try moves in the order Down, Right, Up, Left.
  3. Move to the first cell that is inside the grid, not an obstacle, and not visited.
  4. Stop at `G`, or print "No path found!" if no move is possible.
- **Output:** Each position visited, "Goal reached!", and the visited cells.
- **Note:** The agent never backtracks, so on some grids it can get stuck.

## Practical 3: A* Search for 8 Puzzle
**File:** `pr3_astar_8puzzle.py`
**Syllabus problem statement:** Part A, No. 3 - Implement A* Search for 8 puzzle problem.

- **Aim:** Solve the 8 puzzle using A* search.
- **Concept:** A* picks the state with the lowest `f(n) = g(n) + h(n)`.
  - `g(n)` = moves made so far (cost)
  - `h(n)` = heuristic = number of misplaced tiles (blank not counted)
- **How it works:**
  1. Put the start state in a priority queue (`heapq`).
  2. Pop the lowest `f` state; if it is the goal, return the path.
  3. Otherwise find the blank (0), generate moves Up/Down/Left/Right, and push the new states.
  4. A `visited` set avoids repeating states.
- **Output:** The sequence of board states from start to goal.
- **Conclusion:** A* finds the solution using the heuristic to guide the search.

## Practical 4: Tower of Hanoi (State Space Search)
**File:** `pr4_tower_of_hanoi.py`
**Syllabus problem statement:** Part A, No. 5 - Implement Tower of Hanoi by State Space Search.

- **Aim:** Solve Tower of Hanoi for `n` disks using recursion.
- **Rules:** Move one disk at a time, and never place a bigger disk on a smaller one.
- **Idea:**
  1. Move `n-1` disks from Source to Auxiliary.
  2. Move the largest disk from Source to Destination.
  3. Move `n-1` disks from Auxiliary to Destination.
- **Pegs:** A = source, B = auxiliary, C = destination. Here `n = 3`.
- **Output:** List of moves. Total moves = 2^n - 1 (7 for 3 disks).

## Practical 5: Tic-Tac-Toe using Minimax
**File:** `pr5_tictactoe_minimax.py`
**Syllabus problem statement:** Part B, No. 7 - To develop a game-playing agent using the Minimax algorithm for optimal decision-making.

- **Aim:** Play Tic-Tac-Toe against the computer using the Minimax algorithm.
- **Concept:** Minimax is used in two-player games.
  - System = MAX (X), tries to maximise the score
  - User = MIN (O), tries to minimise the score
  - Scores: X wins = +1, O wins = -1, Draw = 0
- **How it works:** `minimax()` tries every possible move recursively until the game ends, then returns the best score. The system plays the move with the highest score.
- **How to play:** The system (X) moves first. Enter a position 1 to 9:

```
1 | 2 | 3
4 | 5 | 6
7 | 8 | 9
```

- **Result:** The system plays perfectly, so you can draw at best.

## Practical 6: 8-Queens using Backtracking
**File:** `pr6_8queens.py`
**Syllabus problem statement:** Part B, No. 3 - To implement Backtracking search to solve the 8-Queens constraint satisfaction problem.

- **Aim:** Place 8 queens on an 8x8 board so that no two attack each other.
- **Concept:** Backtracking: place a queen row by row. If a row has no safe column, go back to the previous row and try another column.
- **How it works:**
  - `board[row] = col` stores the queen position of each row.
  - `is_safe()` checks the same column and the diagonals.
  - `solve(row)` places a queen and calls itself for the next row; resets to -1 when backtracking.
- **Output:** The board printed with `Q` for queens and `.` for empty cells (first solution found).

## Practical 7: Robot Path Planning using BFS
**File:** `pr7_robot_bfs.py`
**Syllabus problem statement:** Part B, No. 1 - Use BFS to solve a planning problem (example: Robot path planning).

- **Aim:** Find the shortest path for a robot from Start to Goal in a grid.
- **Concept:** BFS explores level by level using a queue, so the first path to reach the goal is the shortest.
- **Grid:** `S` = Start, `G` = Goal, `#` = Obstacle, `.` = Free cell.
- **How it works:**
  1. Put the start path in a queue and mark the start as visited.
  2. Take a path from the queue and look at its last cell.
  3. If it is the goal, print the path.
  4. Otherwise add paths for the valid Up/Down/Left/Right neighbours that are not obstacles or visited.
- **Output:** `[(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 3)]` or "No path found!".

## Practical 8: Simple Rule-Based Chatbot
**File:** `pr8_chatbot.py`
**Syllabus problem statement:** Part B, No. 4 - To develop a simple chatbot using predefined rules and pattern matching.

- **Aim:** Create a chatbot that replies using fixed rules.
- **Concept:** A rule-based chatbot matches keywords in the user's input and gives a predefined reply (if-elif rules).
- **Keywords handled:** hello/hi, your name, how are you, help, thank, bye.
- **How it works:** The input is converted to lowercase and split into words. Matching is done on whole words, so "which" does not trigger "hi". Unknown input gives "Sorry, I don't understand that." Typing `bye` ends the chat.
