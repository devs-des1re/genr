"""Libraries"""
import pathlib

import typer
from rich.console import Console
from rich.markdown import Markdown

from .dialog import print_error, print_success
from .info import get_info
from .generate import generate_file

app = typer.Typer(no_args_is_help=True)
console = Console()

"""Functions"""
@app.command()
def generate(file: str):
    """Generates a file for a github repository

    Args:
        file (str): The filename you want to generate
    """
    cwd = pathlib.Path.cwd()
    try:
        generate_file(cwd, file)
        print_success("The file has successfully been generated!")
    except Exception as error:
        print_error(f"There was an error while generating the file: {error}")

@app.command()
def info(file: str):
    """Provides information about a template

    Args:
        file (str): The file you want information on
    """
    try:
        md = Markdown(get_info(file))
        print_success(md)
    except Exception as error:
        print_error(f"There was an error while retreiving the info: {error}")

@app.command()
def list():
    """Lists all the templates
    """
    templates = pathlib.Path(__file__).parent / "templates"
    templates_list = []

    for index, template in enumerate(templates.iterdir()):
        templates_list.append(f"**{index + 1}.** {template.name}")

    md = Markdown("\n\n".join(templates_list))
    print_success(md)

if __name__ == "__main__":
    app()
