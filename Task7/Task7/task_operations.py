from Task7.file_handler import save_tasks, load_tasks

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("Task added.")

def remove_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"Task '{removed}' removed.")
    else:
        print("Invalid task number.")

def update_task(index, new_task):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        old = tasks[index]
        tasks[index] = new_task
        save_tasks(tasks)
        print(f"Task updated from '{old}' to '{new_task}'.")
    else:
        print("Invalid task number.")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i}. {task}")
