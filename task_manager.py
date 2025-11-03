import json
import os
import shutil
import logging
from task import Task

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


class TaskManager:
    def __init__(self, file_path="tasks.json"):
        self.file_path = file_path
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """Load tasks from a JSON file with error handling."""
        if not os.path.exists(self.file_path):
            logging.info("No existing task file found. Starting fresh.")
            return []

        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            return [Task.from_dict(item) for item in data]

        except json.JSONDecodeError:
            logging.error("Corrupted tasks file detected! Creating backup...")
            backup_path = self.file_path + ".bak"
            shutil.copy(self.file_path, backup_path)
            logging.info(f"Backup created at: {backup_path}")
            return []

        except Exception as e:
            logging.exception(f"Unexpected error while loading tasks: {e}")
            return []

    def save_tasks(self):
        """Save all current tasks to a JSON file safely."""
        try:
            with open(self.file_path, "w", encoding="utf-8") as f:
                json.dump([t.to_dict() for t in self.tasks], f, indent=4)
        except Exception as e:
            logging.exception(f"Error saving tasks: {e}")

    def add_task(self, title, category):
        if not title.strip():
            raise ValueError("Task title cannot be empty.")
        task = Task(title, category)
        self.tasks.append(task)
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
        if 1 <= index <= len(self.tasks):
            task = self.tasks[index - 1]
            task.mark_done()
            self.save_tasks()
            print(f"✅ '{self.tasks[index - 1].title}' marked as done.")
            return True
        else:
            logging.warning(f"Invalid task number: {index}. Cannot mark done.")
            return False

    def delete_task(self, index):
        """Delete a task by its index."""
        if 1 <= index <= len(self.tasks):
            removed = self.tasks.pop(index - 1)
            self.save_tasks()
            print(f"🗑️ Deleted: {removed.title}")
            return True
        else:
            logging.warning(f"Invalid index: {index}")
            print("❌ Invalid task number.")
            return False
