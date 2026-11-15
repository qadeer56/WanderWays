# WanderWays – Travel Package Inventory

A beginner-friendly Python command-line application for managing travel packages. It stores the inventory in a local `packages.json` file.

## Requirements

- Python 3.10 or newer (the project uses only Python's standard library)
- Visual Studio Code or another Python editor (optional)

## Run the application

1. Download or clone this repository.
2. Open the `WanderWays` folder in a terminal.
3. Run:

   ```bash
   python main.py
   ```

4. Use the menu:
   - `1` – Add a travel package
   - `2` – View all travel packages
   - `3` – Exit

## Package data structure

Each package is stored as a Python dictionary with these fields:

```python
{
    "id": 101,
    "name": "Murree Tour",
    "price": 55000,
    "stock": 7
}
```

## JSON storage

- `load_packages()` reads the inventory from `packages.json`.
- If `packages.json` does not exist, the application creates it with an empty list (`[]`).
- `save_packages()` writes the current inventory to `packages.json`.
- New packages are saved immediately after they are added.

## Project files

```text
WanderWays/
├── main.py
├── packages.json
├── README.md
└── .gitignore
```

## Manual checks

- Start the app and choose `2` to view the sample packages.
- Choose `1` and add a package with a new ID; then choose `2` to confirm it appears.
- Close the app and run it again; confirm the package is still present.
- Temporarily move `packages.json` out of the folder and start the app; it should create a new `packages.json` containing `[]`.

## Scope

This project covers the core data model, JSON loading/saving, adding a package through user input, and a simple command-line menu. It is a learning project and does not use a database or web interface.
