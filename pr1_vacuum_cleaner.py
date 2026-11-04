# Simple Reflex Agent for Vacuum Cleaner World

# Initial environment
environment = {
    'A': 'Dirty',
    'B': 'Dirty'
}

# Starting position
location = 'A'

while True:
    print("\nLocation:", location)
    print("Environment:", environment)

    # Perceive and act
    if environment[location] == 'Dirty':
        print("Action: Suck")
        environment[location] = 'Clean'

    elif location == 'A':
        print("Action: Move Right")
        location = 'B'

    elif location == 'B':
        print("Action: Move Left")
        location = 'A'

    # Stop when both rooms are clean
    if environment['A'] == 'Clean' and environment['B'] == 'Clean':
        print("\nBoth rooms are clean!")
        print("Performance: Successful")
        break
