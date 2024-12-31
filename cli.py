import chore_manager

def run_cli():
    while True:
        print("\nRoommate Chore Manager")
        print("1. Add Roommate")
        print("2. Add Chore")
        print("3. Assign Chores")
        print("4. View Assignments")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter roommate's name: ")
            chore_manager.add_roommate(name)
        elif choice == "2":
            chore = input("Enter chore description: ")
            chore_manager.add_chore(chore)
        elif choice == "3":
            chore_manager.assign_chores()
        elif choice == "4":
            chore_manager.view_assignments()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")
