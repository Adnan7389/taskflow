# tests/test_task_manager.py
import json
from taskflow.task_manager import TaskManager

def test_add_and_save(tmp_path):
    file_path = tmp_path / "tasks.json"
    tm = TaskManager(file_path=str(file_path))
    tm.add_task("T1", "Cat1")
    assert len(tm.tasks) == 1
    data = json.loads(file_path.read_text())
    assert data[0]["title"] == "T1"

def test_delete_invalid(tmp_path, caplog):
    file_path = tmp_path / "tasks.json"
    tm = TaskManager(file_path=str(file_path))
    tm.add_task("Only", "C")
    res = tm.delete_task(99)
    assert res is False
    assert "Invalid index" in caplog.text
