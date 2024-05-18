import json
import uuid
import typing as t

import cli.utils as util  # Import utility functions

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
    entry_obj['timestamp'] = util.current_datetime()

    # Append the new entry object to the existing list
    entries_data.append(entry_obj)

    # Write the updated entry data back to the file
    with open(entries_file, 'w') as f:
        json.dump(entries_data, f, indent=4)  # indent for pretty printing

# Searching an entry

def search_entries(title: str):
    """ Search Entires by title, dropdown selection for muliple finds.  

    View all vs view one

    Args:
        title (str): _description_
    """
    pass

# viewing an entry 