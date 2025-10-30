# models.py

from typing import TypedDict

class Task(TypedDict):
    title: str
    category: str
    done: bool
