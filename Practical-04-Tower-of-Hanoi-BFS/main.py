from collections import deque

def hanoi(n):
    start = (tuple(range(n, 0, -1)), ( ), ( ))
    goal = (( ), ( ), tuple(range(n, 0, -1)))
    queue = deque([(start, [])])
    visited = {start}
    while queue:
        state, path = queue.popleft()

        if state == goal:
            print("\nSolution:")
            for move in path:
                print(move)
            return

        for i in range(3):
            if not state[i]:
                continue
            disk = state[i][-1]
            for j in range(3):
                if i == j:
                    continue
                if not state[j] or state[j][-1] > disk:
                    new_state = [list(peg) for peg in state]
                    new_state[i].pop()
                    new_state[j].append(disk)

                    new_state = tuple(tuple(peg) for peg in new_state)
                    if new_state not in visited:
                        visited.add(new_state)
                        move = f"Move disk {disk}: Peg {i+1} -> Peg {j+1}"
                        queue.append((new_state, path + [move]))

n = int(input("Enter Number of Disk: "))
if n > 0:
    hanoi(n)
else:
    print("Enter a Positive Number !")