import typer
from rich.console import Console
from rich.table import Table
from core.core import todo_app



todo = todo_app()
console = Console()

app = typer.Typer(help="my first cli app")


@app.command()
def list(
    all: bool = typer.Option(False, "--all", "a" , help="Display all tasks"),
    format: str =  typer.Option("table", "-format", "f", help="Change output format")
):
    tasks = todo_app.list()
    if format == "json":
        console.print_json(data=tasks)
    else:
        table = Table(title="Todo tasks")
        table.add_column("Id", style="cyan")
        table.add_column("Status", style="blue")
        table.add_column("Description", style='white')
        table.add_column("Created at", style='yellow')
        table.add_column("Completed at", style="green")

