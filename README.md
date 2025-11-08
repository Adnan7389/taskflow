# TaskFlow — A Simple CLI To-Do Manager

TaskFlow is a command-line application for managing your to-do list. It's designed to be simple, fast, and easy to use, allowing you to handle tasks directly from your terminal.

## Features

- **Add Tasks**: Quickly add new tasks with a title and an optional category.
- **List Tasks**: View all your tasks, neatly organized with their status and category.
- **Mark as Done**: Mark tasks as completed.
- **Delete Tasks**: Remove tasks from your list.
- **Persistent Storage**: Your tasks are saved in a JSON file, so you never lose your data.

## Prerequisites

- Python 3.8 or higher.

## Installation

1.  **Clone the repository (optional):**
    ```bash
    git clone https://github.com/Adnan7389/taskflow.git
    cd taskflow
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For Linux/macOS
    python3 -m venv .venv
    source .venv/bin/activate

    # For Windows
    python -m venv .venv
    .venv\Scripts\activate
    ```

3.  **Install the package:**
    To make the `taskflow` command available in your terminal, install the package in editable mode:
    ```bash
    pip install -e .
    ```

## Usage

TaskFlow is easy to use. Here are the available commands:

### `add`

Add a new task to your list. You can also specify a category using the `--category` or `-c` option.

```bash
$ taskflow add "Write a blog post" --category "Writing"
✅ Added: Write a blog post (Writing)
```

### `list`

List all your tasks. Completed tasks are marked with a `✓`.

```bash
$ taskflow list
1. [ ] Write a blog post (Category: Writing)
2. [ ] Buy groceries (Category: Personal)
```

### `done`

Mark a task as done using its number from the list.

```bash
$ taskflow done 1
✅ Task marked as done.

$ taskflow list
1. [✓] Write a blog post (Category: Writing)
2. [ ] Buy groceries (Category: Personal)
```

### `delete`

Delete a task from the list using its number.

```bash
$ taskflow delete 2
🗑️ Task deleted.

$ taskflow list
1. [✓] Write a blog post (Category: Writing)
```

### Specifying a Data File

By default, tasks are stored in `tasks.json`. You can use a different file with the `--data-file` or `-d` option:

```bash
taskflow --data-file work_tasks.json add "Finish the project report"
```

## Development

To contribute to TaskFlow or run the tests, follow these steps:

1.  **Install development dependencies:**
    Make sure you have `pytest` installed, which is included in `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run tests:**
    To run the test suite, use `pytest`:
    ```bash
    pytest
    ```

## License

This project is licensed under the MIT License.
