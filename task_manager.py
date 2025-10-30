# task_manager.py

from typing import List
from models import Task


class TaskManager:
    def __init__(self) -> None:
        self._tasks: List[Task] = []

    def add_task(self, title: str, category: str) -> None:
        task: Task = {"title": title, "category": category, "done": False}
        self._tasks.append(task)

    def view_tasks(self) -> List[Task]:
        return self._tasks.copy()

    def delete_task(self, index: int) -> bool:
        if 0 <= index < len(self._tasks):
            del self._tasks[index]
            return True
        return False
