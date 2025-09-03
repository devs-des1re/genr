"""Libraries"""
import click
from rich.console import Console
from rich.panel import Panel

console = Console()

"""Functions"""
def print_success(message: str):
    """Prints out a success message

    Args:
        message (str): The message you want to send
    """
    panel = Panel(
        message,
        title="Success",
        title_align="left",
        expand=True,
        border_style="green"
    )
    console.print(panel)

def print_error(error: str):
    """Prints out a error message

    Args:
        error (str): The error you want to send
    """
    raise click.UsageError(error)
