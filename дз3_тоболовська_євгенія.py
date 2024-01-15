import os
import shutil
import argparse
from pathlib import Path

def copy_files(src, dst):
    for item in os.listdir(src):
        item_path = Path(src) / item
        if item_path.is_dir():
            copy_files(item_path, dst)  # Рекурсивний виклик для директорій
        else:
            subdir_name = item_path.suffix[1:] if item_path.suffix else 'no_extension'
            subdir_path = Path(dst) / subdir_name
            subdir_path.mkdir(parents=True, exist_ok=True)
            shutil.copy(item_path, subdir_path)

def main(source, destination):
    try:
        copy_files(source, destination)
    except Exception as e:
        print(f"Помилка: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Копіює файли за розширеннями в окремі піддиректорії.")
    parser.add_argument("source", type=str, help="Шлях до вихідної директорії")
    parser.add_argument("destination", type=str, help="Шлях до директорії призначення")
    args = parser.parse_args()

    main(args.source, args.destination)
