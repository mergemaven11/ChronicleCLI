"""
Module containing handlers for the CLI commands.
"""

import json
import typing as t
import uuid
import os
import pandas as pd
import datetime

from InquirerPy import prompt
from rich import print_json
from rich.console import Console

from . import utils

console = Console()


def add_entry_to_file(
    entry_obj: t.Dict[str, t.Any], entries_file: str = utils.ENTRIES_FILE
) -> None:
    """
    Add a JSON object representing a journal entry to the entries file.

    Args:
        entry_obj (Dict[str, Any]): Dictionary representing the journal entry.
        entries_file (str): Path to the entries file.

    Returns:
        None
    """
    # Load existing entries from the file
    with open(entries_file, "r", encoding="utf-8") as f:
        entries_data: list = json.load(f)

    # Generate a unique ID and timestamp for the new entry
    entry_obj["id"] = str(uuid.uuid4())
    entry_obj["timestamp"] = utils.current_datetime()

    # Append the new entry object to the existing list
    entries_data.append(entry_obj)

    # Write the updated entry data back to the file
    with open(entries_file, "w", encoding="utf-8") as f:
        json.dump(entries_data, f, indent=4)  # indent for pretty printing
        console.print(
            f"[bold green]Successfully added the following entry:[/bold green]\n"
            f"{json.dumps(entry_obj, indent=4)}",
            style="green",
        )


# Searching an entry


def search_entries(keyword: str):
    """Search Entries by title, dropdown selection for multiple finds.

    View all vs view one

    Args:
        keyword (str): Display all journal entries or view specific entries by date.
    """
    # Get the list of matching entries
    search_items = utils.search(keyword)

    if not search_items:
        console.print("[bold red]No entries found.[/bold red]")
        return

    # Create a list of choices for the dropdown
    choices = [
        f"{entry['title']} - {entry['timestamp']}" for entry in search_items
    ]  # type: ignore

    # Use InquirerPy to present a dropdown selection
    questions = [
        {
            "type": "list",
            "name": "selected_entry",
            "message": "Select an entry to view:",
            "choices": choices,
        }
    ]

    answers = prompt(questions)

    # Find the selected entry
    selected_entry = next(
        (
            item
            for item in search_items
            if f"{item['title']} - {item['timestamp']}" == answers["selected_entry"]
        ),
        None,
    )

    if selected_entry:
        # Pretty-print the selected entry using rich
        console.print("[bold green]Selected Entry:[/bold green]")
        print_json(json.dumps(selected_entry))
    else:
        console.print("[bold red]No entry selected.[/bold red]")


# Viewing an entry

# Delete Entries

# Edit Entries

# Export Entries

def export_entries(filetype: str, path: str):
    """ Export Journal Entries to chosen filetype (csv, pdf or docv)

    Args:
        filetype (str): csv, pdf or docv
    """
    if filetype.lower() not in ("csv", "pdf", "docv"):
       console.print(f"[bold red]{filetype} is not supported![/bold red]")
    
    if os.path.exists(path):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        if filetype.lower() == "csv":
            with open("./entries/entries.json", encoding='utf-8') as input_file:
               df = pd.read_json(input_file)
            df.to_csv(f"{path}/{timestamp}.csv",encoding='utf-8', index=False)
            console.print("[bold green]csv file created successfully![/bold green]")
            pass
        elif filetype.lower() == "pdf":
            pass
        elif filetype.lower() == "docv":
            pass
    else:
        console.print(f"[bold red]{path} doesn't exist![/bold red]")


    

