# ethos-firmware
This project is a Raspberry Pi firmware application that incorporates PySide6 for the graphical user interface (GUI) and SQLite for database functionality.

## Key Features

- Raspberry Pi firmware
- PySide6 GUI
- SQLite database
- Modular folder structure
- Unit tests

## Getting Started

### Prerequisites

- Python 3.x
- Virtual environment tool (e.g., venv)

### Installation

1. Set up a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Usage

Run the application using the provided script:

```bash
python run.py

## Folder Structure
firmware/: Main firmware logic and sensor interactions.
gui/: PySide6 GUI code and Qt Designer UI file.
database/: SQLite database connection and schema.
tests/: Unit tests for firmware, GUI, and database.
requirements.txt: List of project dependencies.