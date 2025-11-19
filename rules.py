# rules.py

def get_size_category(file_size):
    size_kb = file_size / 1024
    return "Small" if size_kb < 75 else "Large"
