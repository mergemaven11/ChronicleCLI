import typing as t
import json
import os
import uuid  # Import the uuid module to generate unique IDs
import utils as util


# Add entry

def add_entry_to_file(entry_obj: t.Dict[str, any]):
    """
    Add a JSON object representing a journal entry to the entries file.

    # Example usage
        new_entry = {
            "id": "982ija902i28129",
            "date": "2024-05-17",
            "title": "My New Entry",
            "content": "This is my new journal entry."
        }
    """
    entries_file = 'entries/entries.json'

    # Check if the entries file exists, if not, create it with an empty list
    if not os.path.exists(entries_file):
        with open(entries_file, 'w') as f:
            json.dump([], f)

    # Load existing entries from the file
    with open(entries_file, 'r') as f:
        entries_data = json.load(f)

    # Generate a unique ID for the new entry
    entry_id = str(uuid.uuid4())

    # Add the ID to the entry object
    entry_obj['id'] = entry_id

    # Add the datetime stamp 
    entry_obj['timestamp'] = util.current_datetime()

    # Append the new entry object to the existing list
    entries_data.append(entry_obj)

    # Write the updated entries data back to the file
    with open(entries_file, 'w') as f:
        json.dump(entries_data, f, indent=4)  # indent for pretty printing
    
    print(entry_obj)


# Searching an entry

def search_entries(title: str):
    """ Search Entires by title, dropdown selection for muliple finds.  

    View all vs view one

    Args:
        title (str): _description_
    """
    pass

# viewing an entry 
