"""
Entry point module that consist of all the CLI commands
"""

import typer

from cli import handlers as handler
from cli import utils as util

# from .cli import handlers as handler


app = typer.Typer()

# def main():
#     print("Hello World")


# Add imported commands to the main Typer application instance
@app.command()
def add(entries_file: str):  # Add entries_file as an argument
    """
    Adds a new journal entry.

    Prompts the user to enter a title and a journal entry.
    Sends the data to the add handler to be added to the file.

    Parameters:
        entries_file (str): Path to the entries file.

    Returns:
        None
    """
    title = typer.prompt("Please enter a title")
    entry = typer.prompt("Please enter your journal entry")
    # Send data to add handler
    handler.add_entry_to_file(
        entries_file=entries_file, entry_obj={"Title": title, "Entry": entry}
    )  # Pass entries_file argument


# @app.command()
# def view(name: str):
#     typer.echo(f"Hello {name}")


# @app.command()
# def export(name: str):
#     typer.echo(f"Hello {name}")


# @app.command()
# def search(keyword: str):
#     handler.search_entries(keyword)


# @app.command()
# def delete(name: str):
#     typer.echo(f"Hello {name}")


# @app.command()
# def edit(name: str):
#     typer.echo(f"Hello {name}")


if __name__ == "__main__":
    # Check if first entry, if so create the dir and file.
    util.check_entries_dir()  # pylint: disable=E1120
    app()
