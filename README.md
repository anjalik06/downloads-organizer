#  Downloads Folder Organizer

A Python automation tool that scans, classifies, and organizes files inside your Downloads folder based on file type and size.

## Features
- Automatically detects your Downloads folder
- Categorizes files (Documents, Images, Videos, Archives, Others)
- Sub‑categorizes files (PDF, PNG, MP4, ZIP, etc.)
- Size‑based grouping (Small / Large)
- Creates nested folders automatically
- Moves files safely without deleting anything
- No external libraries required (pure Python)

## Folder Structure Example
```
Downloads/
 ├── Documents/
 │    ├── PDF/
 │    │    ├── Small/
 │    │    └── Large/
 │    └── Word/
 │         ├── Small/
 │         └── Large/
 ├── Images/
 │    ├── JPG/
 │    ├── PNG/
 │    └── GIF/
 ├── Videos/
 ├── Archives/
 └── Others/
```

##  How to Run
### 1. Clone the repository
```
git clone https://github.com/your-username/downloads-organizer.git
cd downloads-organizer
```

### 2. Run the script
```
python main.py
```

## Project Files
- main.py — main script  
- file_scanner.py — scans folder & returns file info  
- file_classifier.py — categorizes files  
- file_mover.py — moves files & creates folders  
- rules.py — size rules  

## Requirements
- Python 3.8+
- No external dependencies

