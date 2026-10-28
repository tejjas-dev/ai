from collections import deque

grid = [
    ['S', '.', '.', '#', '.'],
    ['.', '#', '.', '#', '.'],
    ['.', '#', '.', '.', '.'],
    ['.', '.', '.', '#', '.'],
    ['#', '#', '.', '.', 'G']
]

rows = len(grid)
cols = len(grid[0])

def find_position(symbol):
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == symbol:
                return (i, j)

start = find_position('S')
goal = find_position('G')

def display():
    print("\nEnvironment:")
    for row in grid:
        print(" ".join(row))

def get_neighbors(position):
    row, col = position
    moves = [ (-1, 0), (1, 0), (0, -1), (0, 1) ]
    neighbors = []
    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc
        if 0 <= new_row < rows and 0 <= new_col < cols:
            if grid[new_row][new_col] != '#':
                neighbors.append((new_row, new_col))
    return neighbors

def find_path():
    queue = deque()
    queue.append((start, [start]))
    visited = set()
    visited.add(start)

    while queue:
        current, path = queue.popleft()

        if current == goal:
            return path, visited

        for next_position in get_neighbors(current):
            if next_position not in visited:
                visited.add(next_position)
                new_path = path + [next_position]
                queue.append((next_position, new_path))
    return None, visited

def show_path(path):
    for row, col in path:
        if grid[row][col] != 'S' and grid[row][col] != 'G':
            grid[row][col] = '*'

print("MODEL-BASED INTELLIGENT AGENT")
print("----------------------------------------")
print("\nInitial Grid:")
display()
print("\nStart:", start)
print("Goal :", goal)

path, visited = find_path()

if path:
    print("\nGoal reached!")
    print("\nAgent Path:")
    for position in path:
        print(position)
    print("\nVisited Locations:")
    print(visited)
    print("\nNumber of visited locations:", len(visited))
    print("Number of steps:", len(path) - 1)
    show_path(path)
    print("\nFinal Grid:")
    display()
else:
    print("\nNo path found!")