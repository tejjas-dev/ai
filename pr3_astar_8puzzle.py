# A* Search for 8 Puzzle Problem

from heapq import heappush, heappop

start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

def heuristic(state):
    # Number of misplaced tiles (excluding blank 0)
    return sum(state[i] != goal[i] and state[i] != 0
               for i in range(9))

def astar(start):
    pq = []
    heappush(pq, (heuristic(start), 0, start, []))
    visited = set()

    while pq:
        f, cost, state, path = heappop(pq)

        if state == goal:
            return path + [state]

        if state in visited:
            continue
        visited.add(state)

        zero = state.index(0)
        row, col = divmod(zero, 3)

        moves = []
        if row > 0:
            moves.append(zero - 3)
        if row < 2:
            moves.append(zero + 3)
        if col > 0:
            moves.append(zero - 1)
        if col < 2:
            moves.append(zero + 1)

        for move in moves:
            new_state = list(state)
            new_state[zero], new_state[move] = (
                new_state[move], new_state[zero])
            new_state = tuple(new_state)

            if new_state not in visited:
                g = cost + 1
                h = heuristic(new_state)
                heappush(pq, (g + h, g, new_state,
                              path + [state]))

    return None

solution = astar(start)

if solution:
    print("Solution found:")
    for state in solution:
        print(state[0:3])
        print(state[3:6])
        print(state[6:9])
        print()
else:
    print("No solution found")
