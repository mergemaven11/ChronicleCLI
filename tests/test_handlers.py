import json
import os
from datetime import datetime
from uuid import UUID

import pytest

import cli.handlers as handler  # TODO: fix packging issue


@pytest.fixture
def temp_entries_file(tmp_path):
    """
    Fixture to create a temporary file for entries.
    """
    entries_dir = tmp_path / "entries"
    entries_dir.mkdir()

    # Create 'entries.json' file with an empty list
    entries_file = entries_dir / "entries.json"
    with open(entries_file, "w") as f:
        json.dump([], f)

    print("Temporary entries file created:", entries_file)  # Add debug output
    return entries_file


def test_add_entry_to_file(temp_entries_file):
    """Test add entry to file handler."""

    entry_data = {"title": "foo bar", "content": "Lorem ipsum"}

    # Add the entry to the temporary entries file
    handler.add_entry_to_file(entry_data, entries_file=str(temp_entries_file))

    # Load the entries from the file
    with open(temp_entries_file, "r") as f:
        entries = json.load(f)

    # Check if one entry was added
    assert len(entries) == 1

    # Validate the entry fields
    entry = entries[0]
    assert "id" in entry
    assert "title" in entry
    assert "content" in entry
    assert "timestamp" in entry

    # Check if the ID is a valid UUID
    try:
        UUID(entry["id"], version=4)
    except ValueError:
        pytest.fail("Invalid UUID")

    # Check the values
    assert entry["title"] == "foo bar"
    assert entry["content"] == "Lorem ipsum"

    # Check if the timestamp is not none
    try:
        assert entry["timestamp"] is not None
    except ValueError:
        pytest.fail("Timestamp is empty")
