from collections import deque

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def display(state):
    print("+---+---+---+")
    for i in range(0, 9, 3):
        row = state[i:i + 3]
        print("| " + " | ".join(str(x) if x != 0 else " " for x in row) + " |")
        print("+---+---+---+")

def get_neighbors(state):
    neighbors = []
    zero_position = state.index(0)
    row = zero_position // 3
    col = zero_position % 3
    moves = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]
    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_position = new_row * 3 + new_col
            new_state = list(state)
            new_state[zero_position], new_state[new_position] = (
                new_state[new_position], new_state[zero_position]
            )
            neighbors.append(tuple(new_state))
    return neighbors

def bfs(start):
    queue = deque([start])
    visited = {start}
    parent = {start: None}

    while queue:
        current = queue.popleft()
        if current == GOAL:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)
    return None

print("===================================")
print(" 8-PUZZLE USING BFS")
print("===================================")
print("\nEnter the initial puzzle state.")
print("Use 0 for the blank space.")
print("Enter 9 numbers separated by spaces.")

while True:
    try:
        numbers = list(map(int, input("\nEnter initial state: ").split()))
        if len(numbers) != 9:
            print("Error: Please enter exactly 9 numbers.")
            continue
        if sorted(numbers) != list(range(9)):
            print("Error: Enter numbers from 0 to 8 without repetition.")
            continue
        start = tuple(numbers)
        break
    except ValueError:
        print("Error: Please enter numbers only.")

print("\nInitial State:")
display(start)
print("\nGoal State:")
display(GOAL)
print("\nSearching solution using BFS...")
print("Please wait...")

solution = bfs(start)

if solution is None:
    print("\nNo solution found.")
else:
    print("\nSolution Found!")
    print("Number of moves:", len(solution) - 1)
    print("\nPath from Initial State to Goal State:")
    for step, state in enumerate(solution):
        print("\nStep", step)
        display(state)