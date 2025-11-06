# tests/test_cli.py
from click.testing import CliRunner
from taskflow.cli import main
import json

def test_cli_add_list(tmp_path):
    data_file = tmp_path / "tasks.json"
    runner = CliRunner()
    # add a task
    result = runner.invoke(main, ["--data-file", str(data_file), "add", "TaskCLI", "--category", "X"])
    assert result.exit_code == 0
    # list should show the task
    result = runner.invoke(main, ["--data-file", str(data_file), "list"])
    assert "TaskCLI" in result.output
    # check file contents
    data = json.loads(data_file.read_text())
    assert data[0]["title"] == "TaskCLI"

def test_cli_done_delete(tmp_path):
    data_file = tmp_path / "tasks.json"
    runner = CliRunner()
    # add a task
    runner.invoke(main, ["--data-file", str(data_file), "add", "TaskToComplete", "--category", "Y"])
    # mark as done
    result = runner.invoke(main, ["--data-file", str(data_file), "done", "1"])
    assert "marked as done" in result.output
    # list should show it as done
    result = runner.invoke(main, ["--data-file", str(data_file), "list"])
    assert "[✓]" in result.output
    # delete the task
    result = runner.invoke(main, ["--data-file", str(data_file), "delete", "1"])
    assert "Task deleted" in result.output
    # list should be empty now
    result = runner.invoke(main, ["--data-file", str(data_file), "list"])
    assert "No tasks available" in result.output

def test_cli_invalid_done_delete(tmp_path):
    data_file = tmp_path / "tasks.json"
    runner = CliRunner()
    # add a task
    runner.invoke(main, ["--data-file", str(data_file), "add", "TaskInvalid", "--category", "Z"])
    # try to mark invalid index as done
    result = runner.invoke(main, ["--data-file", str(data_file), "done", "99"])
    assert "Invalid task number" in result.output
    # try to delete invalid index
    result = runner.invoke(main, ["--data-file", str(data_file), "delete", "99"])
    assert "Invalid task number" in result.output

def test_cli_add_empty_title(tmp_path):
    data_file = tmp_path / "tasks.json"
    runner = CliRunner()
    # try to add a task with empty title
    result = runner.invoke(main, ["--data-file", str(data_file), "add", "", "--category", "NoTitle"])
    assert "Task title cannot be empty" in result.output

# Note: More tests can be added for edge cases as needed.
