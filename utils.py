import os
import json
from datetime import datetime, timezone


def check_entries_dir():
    """
    Check if entries directory is present, and if not, create the directory and an initial JSON file.
    """
    entries_dir = './entries'
    entries_file = './entries/entries.json'

    if not os.path.exists(entries_dir):
        os.makedirs(entries_dir)
        with open(entries_file, 'w') as f:
            # Create an empty array to store entries initially
            json.dump([], f)

    return entries_file



def current_datetime():
    """
    Get the current UTC datetime and format it to a more human-readable format.
    """
    # Get the current datetime in UTC timezone
    utc_datetime = datetime.now(timezone.utc) # TODO handle tz

    # Format the datetime object to a more human-readable format
    formatted_datetime = utc_datetime.strftime("%m/%d/%Y @ %I:%M:%S %p")

    return formatted_datetime

