# main.py

from pathlib import Path
from file_scanner import list_files
from file_classifier import get_main_category, get_sub_category
from rules import get_size_category
from file_mover import move_file


def get_downloads_folder():
    # Automatically detect Windows Downloads folder
    return Path.home() / "Downloads"


def organize_folder(folder_path):
    folder_path = str(folder_path)
    files = list_files(folder_path)

    for file in files:
        name = file["name"]
        size = file["size"]
        ext = name.split(".")[-1]

        main_cat = get_main_category(ext)
        sub_cat = get_sub_category(ext)
        size_cat = get_size_category(size)

        folder_chain = [main_cat, sub_cat, size_cat]

        moved_to = move_file(file["path"], folder_chain)
        print(f"Moved {name} → {moved_to}")


if __name__ == "__main__":
    print("Automatically detecting your Downloads folder...")
    downloads_folder = get_downloads_folder()
    print(f"Using Downloads at: {downloads_folder}\n")

    organize_folder(downloads_folder)
