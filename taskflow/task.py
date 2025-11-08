# taskflow/task.py

class Task:
    def __init__(self, title: str, category: str, done: bool = False):
        """
        Represent a single task.
        """
        self.title = title
        self.category = category
        self.done = done

    def mark_done(self) -> None:
        """Mark this task as completed."""
        self.done = True

    def mark_pending(self) -> None:
        """Revert this task to pending."""
        self.done = False

    def to_dict(self) -> dict:
        """Convert Task to a serializable dict."""
        return {"title": self.title, "category": self.category, "done": self.done}

    @staticmethod
    def from_dict(data: dict) -> "Task":
        """Create a Task from a dict (used when loading)."""
        return Task(title=data["title"], category=data["category"], done=data.get("done", False))

    def __str__(self) -> str:
        status = "✅" if self.done else "🕓"
        return f"{self.title} ({self.category}) - {status}"
