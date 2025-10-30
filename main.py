# main.py

from task_manager import TaskManager
from models import Task


def show_menu() -> None:
    print("\n=== TaskFlow Menu ===")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")


def add_task_flow(manager: TaskManager) -> None:
    title = input("Enter task title: ").strip()
    category = input("Enter category (Work/Study/Personal): ").strip()
    if title:
        manager.add_task(title, category)
        print("Task added successfully.")
    else:
        print("Title cannot be empty.")


def view_tasks_flow(manager: TaskManager) -> None:
    tasks = manager.view_tasks()
    if not tasks:
        print("No tasks available.")
        return

    print("\nCurrent tasks:")
    for idx, task in enumerate(tasks):
        status = "✓" if task["done"] else " "
        print(
            f"{idx}. [{status}] {task['title']} (Category: {task['category']})")


def delete_task_flow(manager: TaskManager) -> None:
    tasks = manager.view_tasks()
    if not tasks:
        print("No tasks to delete.")
        return

    try:
        index_str = input("Enter task index to delete: ").strip()
        index = int(index_str)
        if manager.delete_task(index):
            print("Task deleted successfully.")
        else:
            print("Invalid index; no task deleted.")
    except ValueError:
        print("Please enter a valid integer index.")


def main() -> None:
    manager = TaskManager()

    while True:
        show_menu()
        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            add_task_flow(manager)
        elif choice == "2":
            view_tasks_flow(manager)
        elif choice == "3":
            delete_task_flow(manager)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice; please choose 1-4.")


if __name__ == "__main__":
    main()
