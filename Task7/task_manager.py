from Task7.task_operations import add_task, remove_task, update_task, view_tasks

def main():
    while True:
        print("\n--- Task Manager ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Update Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            task = input("Enter new task: ")
            add_task(task)
        elif choice == '3':
            try:
                index = int(input("Enter task number to remove: "))
                remove_task(index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            try:
                index = int(input("Enter task number to update: "))
                new_task = input("Enter new task: ")
                update_task(index, new_task)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
