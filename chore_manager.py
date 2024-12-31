import random
import database

def add_roommate(name):
    database.add_roommate(name)
    print(f"Roommate '{name}' added.")

def add_chore(chore):
    database.add_chore(chore)
    print(f"Chore '{chore}' added.")

def assign_chores():
    roommates = database.get_roommates()
    chores = database.get_chores()

    if not roommates:
        print("No roommates added yet.")
        return
    if not chores:
        print("No chores added yet.")
        return

    assignments = {roommate: [] for roommate in roommates}
    random.shuffle(chores)

    for i, chore in enumerate(chores):
        roommate = roommates[i % len(roommates)]
        assignments[roommate].append(chore)

    database.save_assignments(assignments)
    print("Chores assigned successfully!")

def view_assignments():
    assignments = database.get_assignments()
    if not assignments:
        print("No assignments found. Assign chores first.")
        return

    for roommate, chores in assignments.items():
        print(f"\n{roommate}'s chores:")
        for chore in chores:
            print(f"- {chore}")
