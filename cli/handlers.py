import json
import uuid
import typing as t


from InquirerPy import prompt
from rich import print_json
from rich.console import Console

from . import utils

console = Console()


def add_entry_to_file(entry_obj: t.Dict[str, t.Any], entries_file: str) -> None:
    """
    Add a JSON object representing a journal entry to the entries file.

    Args:
        entry_obj (Dict[str, Any]): Dictionary representing the journal entry.
        entries_file (str): Path to the entries file.

    Returns:
        None
    """
    # Load existing entries from the file
    with open(entries_file, 'r') as f:
        entries_data: list = json.load(f)

    # Generate a unique ID and timestamp for the new entry
    entry_obj['id'] = str(uuid.uuid4())
    entry_obj['timestamp'] = utils.current_datetime()

    # Append the new entry object to the existing list
    entries_data.append(entry_obj)

    # Write the updated entry data back to the file
    with open(entries_file, 'w') as f:
        json.dump(entries_data, f, indent=4)  # indent for pretty printing

# Searching an entry

def search_entries(keyword: str):
    """ Search Entries by title, dropdown selection for multiple finds.  

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
    choices = [f"{entry['title']} - {entry['timestamp']}" for entry in search_items]

    # Use InquirerPy to present a dropdown selection
    questions = [
        {
            'type': 'list',
            'name': 'selected_entry',
            'message': "Select an entry to view:",
            'choices': choices
        }
    ]
    
    answers = prompt(questions)
    
    # Find the selected entry
    selected_entry = next((item for item in search_items if f"{item['title']} - {item['timestamp']}" == answers['selected_entry']), None)
    
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