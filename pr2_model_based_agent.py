# Model-Based Intelligent Agent

grid = [
    ['S', '.', '#', '.'],
    ['.', '.', '#', '.'],
    ['#', '.', '.', 'G']
]

# S = Start, G = Goal, # = Obstacle, . = Empty cell

position = (0, 0)
internal_state = set()

while True:
    row, col = position
    internal_state.add(position)

    print("Current Position:", position)

    if grid[row][col] == 'G':
        print("Goal reached!")
        break

    # Possible movements: Down, Right, Up, Left
    moves = [
        (row + 1, col),
        (row, col + 1),
        (row - 1, col),
        (row, col - 1)
    ]

    moved = False

    for r, c in moves:
        if (0 <= r < len(grid) and
            0 <= c < len(grid[0]) and
            grid[r][c] != '#' and
            (r, c) not in internal_state):

            position = (r, c)
            moved = True
            break

    if not moved:
        print("No path found!")
        break

print("Visited cells:", internal_state)
