"""
Module consist of tools, helper functions and utils
"""

import json
import os
import re
import typing as t
from datetime import datetime, timezone

ENTRIES_DIR = "./entries"
ENTRIES_FILE = "./entries/entries.json"


def check_entries_dir():
    """
    Check if entries directory is present, and if not, create the
    directory and an initial JSON file.
    """
    if not os.path.exists(ENTRIES_DIR):
        os.makedirs(ENTRIES_DIR)
        with open(ENTRIES_FILE, "w", encoding="utf-8") as f:
            # Create an empty array to store entries initially
            json.dump([], f)

    return ENTRIES_FILE


def current_datetime():
    """
    Get the current UTC datetime and format it to a more human-readable format.
    """
    # Get the current datetime in UTC timezone
    utc_datetime = datetime.now(timezone.utc)

    # Format the datetime object to a more human-readable format
    formatted_datetime = utc_datetime.strftime("%m/%d/%Y @ %I:%M:%S %p")

    return formatted_datetime


def search(keyword: str) -> t.List[t.Dict[str, str]]:
    """Pass a keyword in, uses regex to search the JSON file for entries.

    Args:
        keyword (str): Keyword used to query JSON file.

    Returns:
        search_data (List): List of entries matching the keyword.

    TODO: - Fix permissions issue
    """
    search_data = []

    if os.path.exists(ENTRIES_DIR):
        with open(ENTRIES_DIR, "r", encoding="utf-8") as file:
            entries = json.load(file)

            for entry in entries:
                if re.search(keyword, entry["title"], re.IGNORECASE) or re.search(
                    keyword, entry["content"], re.IGNORECASE
                ):
                    search_data.append(entry)

    if not search_data:
        print(f"There are no entries with keyword: {keyword}")

    return search_data
