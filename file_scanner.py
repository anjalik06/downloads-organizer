# file_scanner.py

from pathlib import Path

def list_files(folder_path):
    """
    List all files in the folder (non-recursive)
    Returns a list of dictionaries with file info
    """
    files_info = []
    folder = Path(folder_path)
    
    if not folder.exists() or not folder.is_dir():
        raise ValueError(f"{folder_path} is not a valid folder.")
    
    for f in folder.iterdir():
        if f.is_file():
            files_info.append({
                "name": f.name,
                "path": str(f),
                "size": f.stat().st_size  # in bytes
            })
    
    return files_info
