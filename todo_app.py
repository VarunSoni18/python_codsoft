import json
import os

# Define the filename for storing tasks
FILE_NAME = "todo_list.json"
# Global list to hold the tasks (each task is a dictionary)
tasks = []

def load_tasks():
    """Loads tasks from the JSON file into the global 'tasks' list."""
    global tasks
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, 'r') as file:
                tasks = json.load(file)
            print(f"Loaded {len(tasks)} tasks from {FILE_NAME}.")
        except json.JSONDecodeError:
            print("Warning: To-Do file is corrupted or empty. Starting with an empty list.")
            tasks = []
    else:
        print("No existing To-Do file found. Starting with a new list.")

def save_tasks():
    """Saves the current state of the global 'tasks' list to the JSON file."""
    try:
        with open(FILE_NAME, 'w') as file:
            json.dump(tasks, file, indent=4)
    except Exception as e:
        print(f"Error saving tasks: {e}")

def display_tasks():
    """Displays all tasks with their index, status, and description."""
    if not tasks:
        print("\nYour To-Do list is empty! Time to add a task.")
        return

    print("\n--- TO-DO LIST ---")
    print("{:<5} | {:<10} | {}".format("No.", "Status", "Description"))
    print("-" * 40)

    for index, task in enumerate(tasks, 1):
        status = "✅ DONE" if task['done'] else "⏳ PENDING"
        print("{:<5} | {:<10} | {}".format(index, status, task['description']))
    print("-" * 40)

def add_task():
    """Prompts the user for a task description and adds it to the list."""
    description = input("Enter the task description: ").strip()
    if description:
        new_task = {
            'description': description,
            'done': False
        }
        tasks.append(new_task)
        print(f"Task '{description}' added.")
        save_tasks()
    else:
        print("Task description cannot be empty.")

def update_task_status(index, status):
    """Marks a task as done or pending based on its index."""
    try:
        task_index = int(index) - 1
        if 0 <= task_index < len(tasks):
            action = "Marked" if status else "Unmarked"
            tasks[task_index]['done'] = status
            print(f"{action} task {index}: '{tasks[task_index]['description']}' as {'DONE' if status else 'PENDING'}.")
            save_tasks()
        else:
            print(f"Error: Invalid task number {index}.")
    except ValueError:
        print("Error: Please enter a valid number for the task.")

def delete_task():
    """Removes a task from the list based on its index."""
    display_tasks()
    if not tasks:
        return

    try:
        index_to_delete = input("Enter the number of the task to DELETE: ")
        task_index = int(index_to_delete) - 1

        if 0 <= task_index < len(tasks):
            removed_task = tasks.pop(task_index)
            print(f"Deleted task {index_to_delete}: '{removed_task['description']}'.")
            save_tasks()
        else:
            print(f"Error: Invalid task number {index_to_delete}.")
    except ValueError:
        print("Error: Please enter a valid number for the task.")

def main_menu():
    """Displays the main menu and handles user selection."""

    # Load tasks on startup
    load_tasks()

    while True:
        print("\n========== TO-DO LIST MENU ==========")
        print("1. View To-Do List")
        print("2. Add New Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit and Save")
        print("=====================================")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            display_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            display_tasks()
            if tasks:
                task_num = input("Enter the number of the task to mark as DONE: ")
                upd
