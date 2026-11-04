# Robot Path Planning using BFS

from collections import deque

grid = [
    ['S', '.', '.', '#'],
    ['#', '#', '.', '#'],
    ['.', '.', '.', 'G']
]

start = (0, 0)
goal = (2, 3)

queue = deque([[start]])
visited = {start}

while queue:
    path = queue.popleft()
    row, col = path[-1]

    if (row, col) == goal:
        print("Path found:")
        print(path)
        break

    # Up, Down, Left, Right
    moves = [
        (row-1, col),
        (row+1, col),
        (row, col-1),
        (row, col+1)
    ]

    for r, c in moves:
        if (0 <= r < 3 and 0 <= c < 4 and
            grid[r][c] != '#' and (r, c) not in visited):

            visited.add((r, c))
            queue.append(path + [(r, c)])
else:
    print("No path found!")
