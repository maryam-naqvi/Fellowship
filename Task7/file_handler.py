def load_tasks():
    try:
        with open("Task7/tasks.txt", "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("Task7/tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
