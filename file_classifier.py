# file_classifier.py

def get_main_category(ext):
    ext = ext.lower()
    if ext in ["pdf", "doc", "docx", "txt", "ppt", "pptx", "xls", "xlsx"]:
        return "Documents"
    elif ext in ["jpg", "jpeg", "png", "gif", "bmp"]:
        return "Images"
    elif ext in ["mp4", "mkv", "avi", "mov"]:
        return "Videos"
    elif ext in ["zip", "rar", "7z", "tar", "gz"]:
        return "Archives"
    else:
        return "Others"


def get_sub_category(ext):
    ext = ext.lower()
    return {
        "pdf": "PDF",
        "doc": "Word",
        "docx": "Word",
        "txt": "Text",
        "ppt": "PowerPoint",
        "pptx": "PowerPoint",
        "xls": "Excel",
        "xlsx": "Excel",
        "jpg": "JPG",
        "jpeg": "JPG",
        "png": "PNG",
        "gif": "GIF",
        "bmp": "BMP",
        "mp4": "MP4",
        "mkv": "MKV",
        "avi": "AVI",
        "mov": "MOV",
        "zip": "ZIP",
        "rar": "RAR",
        "7z": "7Z",
        "tar": "TAR",
        "gz": "GZ"
    }.get(ext, "Misc")
