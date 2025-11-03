# tests/test_task.py
from task import Task


def test_task_to_dict_from_dict():
    t = Task("Learn Python", "Study")
    d = t.to_dict()
    assert d["title"] == "Learn Python"
    assert d["category"] == "Study"
    assert not d["done"]

    t2 = Task.from_dict(d)
    assert isinstance(t2, Task)
    assert t2.title == "Learn Python"
    assert not t2.done


def test_mark_done():
    t = Task("Test", "Code")
    t.mark_done()
    assert t.done is True
