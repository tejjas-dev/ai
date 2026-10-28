# Practical 01 - Vacuum Cleaner Agent

## Aim
Implement a simple reflex agent for a vacuum cleaner operating in a two-room environment (Room A and Room B).

## Algorithm Description
The agent uses a simple reflex strategy:
- If the current room is **Dirty**, perform **Suck** action to clean it.
- If in **Room A** and clean, move **Right** to Room B.
- If in **Room B** and clean, move **Left** to Room A.

The simulation runs for 4 steps, demonstrating the agent cleaning Room A and then oscillating between rooms.

## How to Execute
```bash
cd Practical-01-Vacuum-Cleaner-Agent
python3 main.py
```
No input required — runs automatically for 4 iterations.

## Corrections Made
None. The supplied code was syntactically correct and executed without modification.

## Sample Output
See `output.txt` for the exact console output matching the provided screenshot.