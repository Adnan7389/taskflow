# tests/test_task_manager.py
import json
import pytest
import os
from task_manager import TaskManager
from task import Task


def test_add_task_and_save(tmp_path):
    file_path = tmp_path / "tasks.json"
    tm = TaskManager(file_path=str(file_path))
    tm.add_task("Task 1", "Study")

    # Check in-memory
    assert len(tm.tasks) == 1
    assert tm.tasks[0].title == "Task 1"

    # Check file saved
    data = json.loads(file_path.read_text())
    assert data[0]["title"] == "Task 1"


def test_delete_task(tmp_path):
    file_path = tmp_path / "tasks.json"
    tm = TaskManager(file_path=str(file_path))
    tm.add_task("Task A", "CatA")
    tm.add_task("Task B", "CatB")

    result = tm.delete_task(1)
    assert result is True
    assert len(tm.tasks) == 1
    assert tm.tasks[0].title == "Task B"


def test_delete_invalid_index_logs_warning(tmp_path, caplog):
    file_path = tmp_path / "tasks.json"
    tm = TaskManager(file_path=str(file_path))
    tm.add_task("Only Task", "General")
    result = tm.delete_task(99)
    assert result is False
    assert "Invalid index" in caplog.text


def test_load_corrupted_json(tmp_path):
    file_path = tmp_path / "tasks.json"
    # Create corrupted JSON
    file_path.write_text("{ invalid json }")
    tm = TaskManager(file_path=str(file_path))
    assert tm.tasks == []  # should recover with empty list

    backup_file = file_path.with_suffix(".json.bak")
    assert backup_file.exists() or (file_path.parent / "tasks.json.bak").exists()


def test_mark_done(tmp_path):
    file_path = tmp_path / "tasks.json"
    tm = TaskManager(file_path=str(file_path))
    tm.add_task("Task 1", "Study")
    tm.mark_done(1)
    assert tm.tasks[0].done is True
