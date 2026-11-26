
# Vacuum Cleaner Problem

def vacuum_cleaner():
    rooms = {
        'A': 'Dirty',
        'B': 'Dirty'
    }

    current_location = 'A'

    while 'Dirty' in rooms.values():

        print("\nVacuum Cleaner is in Room", current_location)

        if rooms[current_location] == 'Dirty':
            print("Room", current_location, "is Dirty. Cleaning...")
            rooms[current_location] = 'Clean'
            print("Room", current_location, "is now Clean.")

        if current_location == 'A':
            current_location = 'B'
            print("Moving Right to Room B")
        else:
            current_location = 'A'
            print("Moving Left to Room A")

    print("\nAll rooms are clean!")
    print("Final State:", rooms)


vacuum_cleaner()
