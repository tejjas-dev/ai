room = { 'A': 'Dirty', 'B': 'Clean' }
position = 'A'

def vacuum_agent(location, status):
    if status == 'Dirty':
        return 'Suck'
    elif location == 'A':
        return 'Right'
    else:
        return 'Left'

for i in range(4):
    status = room[position]
    print("\nPosition:", position)
    print("Room Status:", status)
    action = vacuum_agent(position, status)
    print("Action:", action)
    if action == 'Suck':
        room[position] = 'Clean'
    elif action == 'Right':
        position = 'B'
    elif action == 'Left':
        position = 'A'
    print("Updated Room:", room)