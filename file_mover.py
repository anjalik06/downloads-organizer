# file_mover.py

from pathlib import Path

def move_file(file_path, folder_list):
    """
    folder_list example:
    ["Documents", "Word", "Small"]
    ["Images", "PNG", "Large"]
    ["Archives", "ZIP", "Small"]
    """
    source = Path(file_path)
    target_path = Path(source.parent)

    # Create nested folder chain
    for folder in folder_list:
        target_path = target_path / folder # downloads/Images
        if not target_path.exists():
            target_path.mkdir()

    new_location = target_path / source.name
    source.rename(new_location)

    return str(new_location)
