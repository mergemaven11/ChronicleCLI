# ChronicleCLI

**ChronicleCLI** is a command-line application for keeping a personal journal. It allows users to add, view, and manage journal entries efficiently from the terminal. Whether you want to jot down your thoughts, record daily activities, or maintain notes, ChronicleCLI provides a simple and intuitive interface to do so.

## Features

- **Add Entries**: Quickly add new journal entries with titles and content.
- **View Entries**: Display all journal entries or view specific entries by date.
- **Search Entries**: Search for entries by keyword or date.
- **Delete Entries**: Remove unwanted entries from your journal.
- **Edit Entries**: Modify existing entries.
- **Export Entries**: Export entries to a text file for backup or sharing.

## Installation

To install ChronicleCLI, you need to have Python installed on your machine. You can install ChronicleCLI by cloning the repository and running the setup script.

```bash
git clone https://github.com/yourusername/ChronicleCLI.git
cd ChronicleCLI
poetry install
```

## Usage

Once installed, you can start using ChronicleCLI by running the journal.py script.

```bash
python journal.py
```

## Commands

ChronicleCLI supports the following commands:

| Command         | Description                                           |
|-----------------|-------------------------------------------------------|
| Add Entry       | Add a new journal entry.                              |
| View Entries    | View all journal entries.                             |
| Search Entries  | Search for entries by keyword or date.                |
| Delete Entry    | Delete a journal entry by date.                       |
| Edit Entry      | Edit an existing journal entry.                       |
| Export Entries  | Export entries to a text file.                        |

### Examples

#### Adding an Entry

```bash
$ python journal.py
ChronicleCLI> add
Title: My First Entry
Content: Today I started using ChronicleCLI. It's really cool!
Entry added successfully!
```

#### Viewing Entries

```bash
$ python journal.py
ChronicleCLI> view
Date: 2023-05-16
Title: My First Entry
Content: Today I started using ChronicleCLI. It's really cool!
```

#### Searching Entries

```bash
$ python journal.py
ChronicleCLI> search
Keyword or Date: started
Date: 2023-05-16
Title: My First Entry
Content: Today I started using ChronicleCLI. It's really cool!
```

#### Deleting an Entry

```bash
$ python journal.py
ChronicleCLI> delete
Date: 2023-05-16
Are you sure you want to delete the entry for 2023-05-16? (y/n): y
Entry deleted successfully!
```
