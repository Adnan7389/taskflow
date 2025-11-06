### Tests (keep your Week-3 tests but add CLI test)
# tests/test_task.py
from taskflow.task import Task

def test_to_from_dict():
    t = Task("Learn Python", "Study")
    d = t.to_dict()
    assert d["title"] == "Learn Python"
    assert d["category"] == "Study"
    assert d["done"] is False

    t2 = Task.from_dict(d)
    assert t2.title == "Learn Python"
    assert t2.done is False

def test_mark_done():
    t = Task("T", "C")
    t.mark_done()
    assert t.done is True
