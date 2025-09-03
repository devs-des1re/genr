"""Libraries"""
import pathlib

templates = pathlib.Path(__file__).parent / "templates"

"""Functions"""
def get_info(file: str):
    """Gets the information of a template

    Args:
        file (str): The file you want to get the info on
    """
    for template in templates.iterdir():
        if template.name == file:
            with open(template / "README.md", "r", encoding="utf-8") as f:
                return f.read()
    raise ValueError("The file you have selected doesn't exist")
