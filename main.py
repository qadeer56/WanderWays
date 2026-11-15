import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent / "packages.json"


def load_packages():
    """Load packages from packages.json; create an empty file if it is missing."""
    if not DATA_FILE.exists():
        save_packages([])
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            packages = json.load(file)
    except json.JSONDecodeError as error:
        raise ValueError(
            f"{DATA_FILE.name} contains invalid JSON. Fix the file before continuing."
        ) from error

    if not isinstance(packages, list):
        raise ValueError(f"{DATA_FILE.name} must contain a JSON list.")

    return packages


def save_packages(packages):
    """Save the current package list to packages.json."""
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(packages, file, indent=4, ensure_ascii=False)
        file.write("\n")


def add_package(packages):
    """Collect package details, validate them, and save the new package."""
    print("\n--- ADD NEW TRAVEL PACKAGE ---")

    try:
        package_id = int(input("Enter package ID: ").strip())
        if package_id <= 0:
            print("Package ID must be a positive number.")
            return

        if any(package.get("id") == package_id for package in packages):
            print("That package ID already exists. Please use a different ID.")
            return

        name = input("Enter package name: ").strip()
        if not name:
            print("Package name cannot be empty.")
            return

        price = float(input("Enter package price: ").strip())
        if price < 0:
            print("Price cannot be negative.")
            return

        stock = int(input("Enter stock count: ").strip())
        if stock < 0:
            print("Stock count cannot be negative.")
            return

    except ValueError:
        print("Invalid input. ID and stock must be whole numbers; price must be a number.")
        return

    new_package = {
        "id": package_id,
        "name": name,
        "price": price,
        "stock": stock,
    }

    packages.append(new_package)
    save_packages(packages)
    print("\nPackage added and saved successfully!")


def view_packages(packages):
    """Display all packages currently in the inventory."""
    print("\n--- ALL TRAVEL PACKAGES ---")

    if not packages:
        print("No packages found.")
        return

    for package in packages:
        print("-" * 30)
        print(f"ID:    {package['id']}")
        print(f"Name:  {package['name']}")
        print(f"Price: {package['price']}")
        print(f"Stock: {package['stock']}")
    print("-" * 30)


def main():
    try:
        packages = load_packages()
    except (ValueError, OSError) as error:
        print(f"Could not load inventory: {error}")
        return

    while True:
        print("\n===== WANDERWAYS INVENTORY =====")
        print("1. Add Package")
        print("2. View Packages")
        print("3. Exit")

        choice = input("\nEnter your choice (1-3): ").strip()

        if choice == "1":
            try:
                add_package(packages)
            except OSError as error:
                print(f"Could not save package: {error}")
                # Reload so in-memory data matches the file if saving failed.
                try:
                    packages = load_packages()
                except (ValueError, OSError):
                    pass
        elif choice == "2":
            view_packages(packages)
        elif choice == "3":
            print("\nThank you for using WanderWays!")
            break
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
