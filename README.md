 To-Do List CLI App

A simple **Command-Line To-Do List Application** built with Python.  
It allows users to **add, view, complete, and remove tasks**, while saving progress automatically using a JSON file.

 Features
✅ Add new tasks  
✅ View all tasks with status  
✅ Mark tasks as **completed**  
✅ Remove tasks from the list  
✅ Save tasks in a file (`tasks.json`) for persistence  

 How It Works
This program uses **Python and JSON** to manage tasks.  
Each task has:
- A **task name**
- A **status** (`✅` for done, `❌` for pending)
- A **JSON file (`tasks.json`)** to store tasks persistently  

When a user **adds**, **completes**, or **removes** a task, the changes are saved in `tasks.json`.

---

Installation & Setup
**1. Clone the Repository**
```bash
git clone https://github.com/your-username/to-do-list.git
cd to-do-list
```
**2. Run the Script**
Make sure you have **Python 3** installed, then run:
```bash
python todo.py
```

---

**Menu Options**
When you run the script, you will see:
```
Options:
1. Show Tasks
2. Add Task
3. Complete Task
4. Remove Task
5. Exit
Enter choice:
```
**Enter the corresponding number to perform an action.**

**Example Usage**
 **1️⃣ Add a Task**
```
Enter task: Buy groceries
Task added!
```
 **2️⃣ View Tasks**
```
To-Do List:
1. Buy groceries [❌]
```
 **3️⃣ Complete a Task**
```
Enter task number to mark as done: 1
Task marked as done!
```
 **4️⃣ Remove a Task**
```
Enter task number to remove: 1
Removed task: Buy groceries
```

---

 **Code Explanation**

**1. Load and Save Tasks**
```python
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
```
- The function `load_tasks()` reads `tasks.json` and loads existing tasks.
- If the file **doesn't exist** or is **corrupt**, it returns an empty list.

```python
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)
```
- The function `save_tasks(tasks)` writes tasks into `tasks.json` so that tasks **persist after the program closes**.

---

**2. Add a Task**
```python
def add_task(tasks):
    task_name = input("\nEnter task: ")
    tasks.append({"task": task_name, "done": False})
    save_tasks(tasks)
    print("Task added!")
```
- Prompts the user for a **task name**.
- Adds it to the **tasks list**.
- Saves the task to **`tasks.json`**.

---

**3. Mark Task as Completed**
```python
def complete_task(tasks):
    show_tasks(tasks)
    index = int(input("\nEnter task number to mark as done: ")) - 1
    tasks[index]["done"] = True
    save_tasks(tasks)
    print("Task marked as done!")
```
- Displays current tasks.
- Asks the user **which task to mark as done**.
- Updates the task’s status from `❌` to `✅`.

---

**4. Remove a Task**
```python
def remove_task(tasks):
    show_tasks(tasks)
    index = int(input("\nEnter task number to remove: ")) - 1
    removed_task = tasks.pop(index)
    save_tasks(tasks)
    print(f"Removed task: {removed_task['task']}")
```
- Displays tasks.
- Prompts for the **task number to remove**.
- Removes the selected task.

---

 **Future Improvements**
✅ Add a **due date** for tasks  
✅ Implement a **GUI version** using Tkinter  
✅ Add **categories** for tasks  




🚀 **Happy Coding!** 😊

