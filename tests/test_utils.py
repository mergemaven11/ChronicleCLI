"""Module for testing all utils"""
import json
import os

import pytest

from ..cli import utils as util


@pytest.fixture
def temp_entries_env(tmp_path):  # pylint: disable=W0621
    """
    Fixture to create a temporary directory for entries.
    """
    original_dir = os.getcwd()
    temp_dir = tmp_path / "entries_test"
    # Create directory if it doesn't exist
    temp_dir.mkdir(parents=True, exist_ok=True)

    # Change the current directory to the temp directory
    os.chdir(temp_dir)

    # Yield to the test
    yield

    # After the test, restore the original working directory
    os.chdir(original_dir)


def test_check_entries_dir(temp_entries_env):  # pylint: disable=W0621,W0613
    """Test the check_entries_dir function."""

    entries_dir = "./entries"
    entries_file = "./entries/entries.json"

    # Call the function to check and create the directory and file
    result_file = util.check_entries_dir()

    # Verify the directory was created
    assert os.path.exists(entries_dir)
    assert os.path.isdir(entries_dir)

    # Verify the file was created
    assert os.path.exists(entries_file)
    assert os.path.isfile(entries_file)

    # Verify the file content is an empty list
    with open(entries_file, "r", encoding="utf-8") as f:
        content = json.load(f)
    assert content == []

    # Verify the function returns the correct file path
    assert result_file == entries_file
