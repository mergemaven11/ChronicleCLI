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

### Contributing

We welcome contributions to improve the code quality of this project! Before submitting a pull request, please ensure that your changes adhere to our coding standards and pass all code quality checks.

### Code Quality Checks

We use various tools to maintain code quality, including formatting, linting, and static analysis. These tools are integrated into our development workflow using `pre-commit`, a framework for managing and maintaining multi-language pre-commit hooks.

To ensure that your changes meet our code quality standards, we recommend running `pre-commit` before committing your changes. This can be done by running the following command in your terminal:

```sh
pre-commit run -a
```

This command will execute all pre-commit hooks defined in our configuration file .pre-commit-config.yaml on all files in the repository.


### Running Tests

Before submitting a pull request, please make sure that your changes are covered by tests and that all existing tests pass. You can run the tests locally by following the instructions in our README file.

### Pull Request Guidelines

When submitting a pull request, please ensure the following:

- Provide a clear and descriptive title for the pull request.
- Explain the purpose of the changes and provide context in the pull request description.
- Include any necessary documentation updates.
- Ensure that your code adheres to our coding standards and passes all code quality checks.
- Reference any related issues or pull requests in the description.

Thank you for contributing to this project! I appreciate your efforts in helping to maintain code quality and improve the project for everyone.
