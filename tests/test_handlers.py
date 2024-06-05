"""
Module to test cli handlers
"""

import json
from uuid import UUID

import pytest

from ..cli import handlers as handler


@pytest.fixture
def temp_entries_file(tmp_path):  # pylint: disable=W0621
    """
    Fixture to create a temporary file for entries.
    """
    entries_dir = tmp_path / "entries"
    entries_dir.mkdir()

    # Create 'entries.json' file with an empty list
    file_path = entries_dir / "entries.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump([], f)

    print("Temporary entries file created:", file_path)  # Add debug output
    return file_path


def test_add_entry_to_file(temp_entries_file):  # pylint: disable=W0621
    """Test add entry to file handler."""

    entry_data = {"title": "foo bar", "content": "Lorem ipsum"}

    # Add the entry to the temporary entries file
    handler.add_entry_to_file(entry_data, entries_file=str(temp_entries_file))

    # Load the entries from the file
    with open(temp_entries_file, "r", encoding="utf-8") as f:
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

