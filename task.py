# task.py

class Task:
    def __init__(self, title, category, done=False):
        """
        Initialize a Task object.

        Args:
            title (str): Task title (e.g. 'Buy groceries')
            category (str): Task category (e.g. 'Shopping')
            done (bool): Whether the task is done (default: False)
        """
        self.title = title
        self.category = category
        self.done = done

    def mark_done(self):
        """Mark this task as completed."""
        self.done = True

    def mark_pending(self):
        """Revert this task to pending."""
        self.done = False

    def to_dict(self):
        """Convert Task object to dictionary (for saving to file)."""
        return {
            "title": self.title,
            "category": self.category,
            "done": self.done
        }

    @staticmethod
    def from_dict(data):
        """Create a Task object from a dictionary (for loading from file)."""
        return Task(
            title=data["title"],
            category=data["category"],
            done=data.get("done", False)
        )

    def __str__(self):
        """Readable string representation of the task."""
        status = "✅" if self.done else "🕓"
        return f"{self.title} ({self.category}) - {status}"
