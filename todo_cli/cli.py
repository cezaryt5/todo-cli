"""Main CLI entry point for Todo CLI application."""

import typer
from rich.console import Console
from rich.table import Table
from typing import Optional

from .core import TodoApp


app = typer.Typer(
    help="A modern command-line todo application",
    add_completion=False
)
console = Console()

# Global todo instance
todo_app = TodoApp()


@app.command()
def add(
    description: str = typer.Argument(
        ...,
        help="Task description"
    )
):
    """Add a new task to your todo list."""
    task_id = todo_app.add_task(description)
    console.print(f"✅ Task {task_id} added successfully!", style="green")


@app.command(name="list")
def list_tasks(
    all: bool = typer.Option(
        False,
        "--all",
        "-a",
        help="Show all tasks including completed ones"
    ),
    format: str = typer.Option(
        "table",
        "--format",
        "-f",
        help="Output format: table or json"
    )
):
    """List all tasks in your todo list."""
    tasks = todo_app.get_tasks(include_completed=all)
    
    if not tasks:
        console.print("📭 No tasks found!", style="yellow")
        return
    
    if format.lower() == "json":
        console.print_json(data=tasks)
    else:
        table = Table(title="📝 Todo Tasks")
        table.add_column("ID", style="cyan", justify="center")
        table.add_column("Status", style="magenta", justify="center")
        table.add_column("Description", style="white")
        table.add_column("Created", style="dim")
        
        for task in tasks:
            status = "✅" if task["completed"] else "⏳"
            created = task["created_at"][:10] if task["created_at"] else "N/A"
            table.add_row(
                str(task["id"]),
                status,
                task["description"],
                created
            )
        
        console.print(table)


@app.command()
def complete(
    task_id: int = typer.Argument(
        ...,
        help="ID of the task to mark as completed"
    )
):
    """Mark a task as completed."""
    if todo_app.complete_task(task_id):
        console.print(f"✅ Task {task_id} marked as completed!", style="green")
    else:
        console.print(f"❌ Task {task_id} not found!", style="red")


@app.command()
def delete(
    task_id: int = typer.Argument(
        ...,
        help="ID of the task to delete"
    ),
    force: bool = typer.Option(
        False,
        "--force",
        "-f",
        help="Skip confirmation prompt"
    )
):
    """Delete a task from your todo list."""
    if not force:
        confirm = typer.confirm(f"Are you sure you want to delete task {task_id}?")
        if not confirm:
            console.print("❌ Deletion cancelled.", style="yellow")
            return
    
    if todo_app.delete_task(task_id):
        console.print(f"🗑️  Task {task_id} deleted successfully!", style="green")
    else:
        console.print(f"❌ Task {task_id} not found!", style="red")


@app.command()
def edit(
    task_id: int = typer.Argument(
        ...,
        help="ID of the task to edit"
    ),
    description: str = typer.Argument(
        ...,
        help="New description for the task"
    )
):
    """Edit an existing task's description."""
    if todo_app.edit_task(task_id, description):
        console.print(f"✏️  Task {task_id} updated successfully!", style="green")
    else:
        console.print(f"❌ Task {task_id} not found!", style="red")


@app.command()
def show(
    task_id: int = typer.Argument(
        ...,
        help="ID of the task to show"
    )
):
    """Show detailed information about a specific task."""
    task = todo_app.get_task(task_id)
    
    if not task:
        console.print(f"❌ Task {task_id} not found!", style="red")
        return
    
    status = "✅ Completed" if task["completed"] else "⏳ Pending"
    status_style = "green" if task["completed"] else "yellow"
    
    console.print(f"\n[bold cyan]Task #{task['id']}[/bold cyan]")
    console.print(f"Status: [{status_style}]{status}[/{status_style}]")
    console.print(f"Description: {task['description']}")
    console.print(f"Created: {task['created_at']}")
    if task["completed_at"]:
        console.print(f"Completed: {task['completed_at']}")
    console.print()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show version information"
    )
):
    """Todo CLI - A modern command-line todo application."""
    if version:
        from . import __version__
        console.print(f"Todo CLI v{__version__}")
        raise typer.Exit()


if __name__ == "__main__":
    app()