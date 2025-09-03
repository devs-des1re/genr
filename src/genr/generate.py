"""Libraries"""
import pathlib
import shutil

templates = pathlib.Path(__file__).parent / "templates"

"""Functions"""
def generate_file(location: str, file: str):
    """Generates a template file

    Args:
        location (str): The location of the cli run
        file (str): The file you want to copy

    Raises:
        ValueError: _description_
    """
    for template in templates.iterdir():
        if template.name == file:
            for f in template.iterdir():
                if f.name != "README.md":
                    shutil.copy(f, location)
                    return
    raise ValueError("The file you have selected doesn't exist")
