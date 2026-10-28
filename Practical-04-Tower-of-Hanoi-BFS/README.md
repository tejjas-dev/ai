# Practical 04 - Tower of Hanoi BFS

## Aim
Solve the Tower of Hanoi puzzle using Breadth-First Search to find the shortest sequence of moves.

## Algorithm Description
- **State representation:** Tuple of 3 tuples, each representing a peg's disks (bottom to top).
- **Initial state:** All n disks on Peg 1 (largest at bottom).
- **Goal state:** All n disks on Peg 3.
- **Valid moves:** Move top disk from one peg to another if the destination is empty or its top disk is larger.
- **BFS:** Explores all states level-by-level, guaranteeing minimum moves (2^n - 1).
- **Visited set:** Prevents cycles using hashable tuple-of-tuples state.

## How to Execute
```bash
cd Practical-04-Tower-of-Hanoi-BFS
python3 main.py
```
**Sample input:** `3` (for 3 disks)

## Corrections Made
None. The supplied code was syntactically correct and executed without modification.

## Sample Output
See `output.txt` — 7 moves for 3 disks (optimal).

## Known Limitations
- BFS state space grows exponentially; practical only for small n (n ≤ 5–6 on typical hardware).
- Memory usage is O(3^n) due to visited set storing all explored states.
- No iterative deepening or heuristic guidance — pure BFS.