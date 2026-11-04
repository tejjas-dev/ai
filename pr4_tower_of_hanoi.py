# Tower of Hanoi using State Space Search

def hanoi(n, source, auxiliary, destination):
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return

    hanoi(n - 1, source, destination, auxiliary)

    print("Move disk", n, "from", source, "to", destination)

    hanoi(n - 1, auxiliary, source, destination)


n = 3

print("Tower of Hanoi Solution:")
hanoi(n, 'A', 'B', 'C')
