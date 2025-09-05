import typer
from rich.console import Console
from rich.table import Table
from todo_cli.core.todo import TodoApp

app = typer.Typer(help="A modern todo CLI application")
console = Console()

# Global todo instance
todo_app = TodoApp()

@app.command()
def add(description: str = typer.Argument(..., help="Task description")):
    """Add a new task"""
    task_id = todo_app.add_task(description)
    console.print(f"✅ Task {task_id} added successfully", style="green")

@app.command()
def list(
    all: bool = typer.Option(False, "--all", "-a", help="Show all tasks including completed"),
    format: str = typer.Option("table", "--format", "-f", help="Output format: table, json")
):
    """List all tasks"""
    tasks = todo_app.get_tasks(include_completed=all)
    
    if format == "json":
        console.print_json(data=tasks)
    else:
        table = Table(title="Todo Tasks")
        table.add_column("ID", style="cyan")
        table.add_column("Status", style="magenta")
        table.add_column("Description", style="white")
        table.add_column("Created", style="dim")
        
        for task in tasks:
            status = "✅" if task["completed"] else "⏳"
            table.add_row(
                str(task["id"]),
                status,
                task["description"],
                task["created_at"][:10]
            )
        
        console.print(table)

@app.command()
def complete(task_id: int = typer.Argument(..., help="Task ID to complete")):
    """Mark a task as completed"""
    if todo_app.complete_task(task_id):
        console.print(f"✅ Task {task_id} completed", style="green")
    else:
        console.print(f"❌ Task {task_id} not found", style="red")

@app.command()
def delete(task_id: int = typer.Argument(..., help="Task ID to delete")):
    """Delete a task"""
    if todo_app.delete_task(task_id):
        console.print(f"🗑️  Task {task_id} deleted", style="yellow")
    else:
        console.print(f"❌ Task {task_id} not found", style="red")

@app.command()
def edit(
    task_id: int = typer.Argument(..., help="Task ID to edit"),
    description: str = typer.Argument(..., help="New description")
):
    """Edit a task description"""
    if todo_app.edit_task(task_id, description):
        console.print(f"✏️  Task {task_id} updated", style="blue")
    else:
        console.print(f"❌ Task {task_id} not found", style="red")

if __name__ == "__main__":
    app()