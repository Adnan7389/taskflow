import json
from task import Task


class TaskManager:
    def __init__(self, file_path="tasks.json"):
        """Initialize the TaskManager and load existing tasks."""
        self.file_path = file_path
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """Load tasks from a JSON file, or return an empty list if file not found."""
        try:
            with open(self.file_path, "r") as f:
                data = json.load(f)
                return [Task.from_dict(item) for item in data]
        except FileNotFoundError:
            return []

    def save_tasks(self):
        """Save current tasks to a JSON file."""
        with open(self.file_path, "w") as f:
            json.dump([t.to_dict() for t in self.tasks], f, indent=4)

    def add_task(self, title, category):
        """Add a new task and save."""
        new_task = Task(title, category)
        self.tasks.append(new_task)
        self.save_tasks()
        print(f"✅ Added: {title}")

    def list_tasks(self):
        """Print all tasks."""
        if not self.tasks:
            print("No tasks available.")
            return
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    def mark_done(self, index):
        """Mark a task as completed by its index."""
        try:
            task = self.tasks[index - 1]
            task.mark_done()
            self.save_tasks()
            print(f"✅ '{task.title}' marked as done.")
        except IndexError:
            print("❌ Invalid task number.")

    def delete_task(self, index):
        """Delete a task by its index."""
        try:
            removed = self.tasks.pop(index - 1)
            self.save_tasks()
            print(f"🗑️ Deleted: {removed.title}")
        except IndexError:
            print("❌ Invalid task number.")
