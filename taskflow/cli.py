# taskflow/cli.py
import click
from .task_manager import TaskManager

@click.group()
@click.option("--data-file", "-d", default="tasks.json", help="Path to JSON file storing tasks.")
@click.pass_context
def main(ctx, data_file):
    """TaskFlow CLI — manage tasks from your terminal."""
    ctx.ensure_object(dict)
    ctx.obj["DATA_FILE"] = data_file
    # we create TaskManager lazily inside each command to reflect latest file path

@main.command("add")
@click.argument("title", nargs=1)
@click.option("--category", "-c", default="General", help="Task category.")
@click.pass_context
def add(ctx, title, category):
    """Add a new task: taskflow add "Some task" --category Work"""
    manager = TaskManager(file_path=ctx.obj["DATA_FILE"])
    try:
        manager.add_task(title, category)
        click.echo(f"✅ Added: {title} ({category})")
    except ValueError as e:
        click.echo(f"❌ {e}")

@main.command("list")
@click.pass_context
def list_cmd(ctx):
    """List all tasks."""
    manager = TaskManager(file_path=ctx.obj["DATA_FILE"])
    tasks = manager.list_tasks()
    if not tasks:
        click.echo("No tasks available.")
        return
    for i, t in enumerate(tasks, start=1):
        status = "✓" if t.done else " "
        click.echo(f"{i}. [{status}] {t.title} (Category: {t.category})")

@main.command("done")
@click.argument("index", type=int)
@click.pass_context
def done(ctx, index):
    """Mark a task as done by its number: taskflow done 1"""
    manager = TaskManager(file_path=ctx.obj["DATA_FILE"])
    ok = manager.mark_done(index)
    if ok:
        click.echo("✅ Task marked as done.")
    else:
        click.echo("❌ Invalid task number.")

@main.command("delete")
@click.argument("index", type=int)
@click.pass_context
def delete(ctx, index):
    """Delete a task by number: taskflow delete 1"""
    manager = TaskManager(file_path=ctx.obj["DATA_FILE"])
    ok = manager.delete_task(index)
    if ok:
        click.echo("🗑️ Task deleted.")
    else:
        click.echo("❌ Invalid task number.")
