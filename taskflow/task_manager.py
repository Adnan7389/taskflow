# taskflow/task_manager.py
import json
import os
import shutil
import logging
from .task import Task

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


class TaskManager:
    def __init__(self, file_path: str = "tasks.json"):
        self.file_path = file_path
        self.tasks: list[Task] = self.load_tasks()

    def load_tasks(self) -> list[Task]:
        """Load tasks from a JSON file with basic error handling."""
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
            try:
                shutil.copy(self.file_path, backup_path)
                logging.info(f"Backup created at: {backup_path}")
            except Exception:
                logging.exception("Failed to create backup of corrupted file.")
            return []

        except Exception as e:
            logging.exception(f"Unexpected error while loading tasks: {e}")
            return []

    def save_tasks(self) -> None:
        """Save all current tasks to a JSON file safely."""
        try:
            with open(self.file_path, "w", encoding="utf-8") as f:
                json.dump([t.to_dict() for t in self.tasks], f, indent=4)
        except Exception as e:
            logging.exception(f"Error saving tasks: {e}")

    def add_task(self, title: str, category: str) -> None:
        if not title.strip():
            raise ValueError("Task title cannot be empty.")
        task = Task(title, category)
        self.tasks.append(task)
        self.save_tasks()
        logging.info(f"Added: {title}")

    def list_tasks(self) -> list[Task]:
        """Return the task list (useful for CLI printing or tests)."""
        return list(self.tasks)  # return a copy

    def mark_done(self, index: int) -> bool:
        """Mark task (1-based index) as done; returns True on success."""
        if 1 <= index <= len(self.tasks):
            task = self.tasks[index - 1]
            task.mark_done()
            self.save_tasks()
            logging.info(f"Marked done: {task.title}")
            return True
        else:
            logging.warning(f"Invalid task number: {index}. Cannot mark done.")
            return False

    def delete_task(self, index: int) -> bool:
        """Delete a task by 1-based index."""
        if 1 <= index <= len(self.tasks):
            removed = self.tasks.pop(index - 1)
            self.save_tasks()
            logging.info(f"Deleted: {removed.title}")
            return True
        else:
            logging.warning(f"Invalid index: {index}")
            return False
