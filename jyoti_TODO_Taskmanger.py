import json

TASKS_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Display tasks
def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks available!")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, 1):
            status = "✅" if task["done"] else "❌"
            print(f"{i}. {task['task']} [{status}]")

# Add a task
def add_task(tasks):
    task_name = input("\nEnter task: ")
    tasks.append({"task": task_name, "done": False})
    save_tasks(tasks)
    print("Task added!")

# Mark task as done
def complete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("\nEnter task number to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            save_tasks(tasks)
            print("Task marked as done!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Remove a task
def remove_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("\nEnter task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            save_tasks(tasks)
            print(f"Removed task: {removed_task['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main function
def main():
    tasks = load_tasks()
    while True:
        print("\nOptions:")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Remove Task")
        print("5. Exit")
        
        choice = input("\nEnter choice: ")
        
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
