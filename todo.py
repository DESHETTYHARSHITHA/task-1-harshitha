tasks =[]
while True:
    print("\n===== TO DO LIST ====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")
    choice = input("Ent1er your choice: ")
    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task Added Succesfully!")

    elif choice == "2":
        print("\nYour Tasks:")

        for task in tasks:
            print("-",task)

    elif choice == "3":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice")