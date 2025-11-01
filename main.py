# main.py
from task_manager import TaskManager


def show_menu():
    print("\n=== TO-DO LIST APP ===")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")


def main():
    manager = TaskManager()

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            manager.list_tasks()
        elif choice == "2":
            title = input("Enter task title: ")
            category = input("Enter category: ")
            manager.add_task(title, category)
        elif choice == "3":
            manager.list_tasks()
            num = int(input("Enter task number to mark done: "))
            manager.mark_done(num)
        elif choice == "4":
            manager.list_tasks()
            num = int(input("Enter task number to delete: "))
            manager.delete_task(num)
        elif choice == "5":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
