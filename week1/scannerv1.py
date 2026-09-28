from pathlib import Path

folder = Path(r"C:\Users\HP\Downloads")

if not folder.is_dir():
    print("folder not found")
else:
    files=list(folder.glob("*.xlsx"))

    print(f"Found {len(files)} Excel files in the folder.")

    for f in files:
        print(f.name)