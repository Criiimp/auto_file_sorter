#   sorter/file_handler.py

import os, shutil, time
from datetime import datetime

from unicodedata import category
from watchdog.events import FileSystemEventHandler, DirCreatedEvent, FileCreatedEvent

from .categorizer import get_cat
from .config import OUTPUT_F

class FileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        f_path = event.src_path
        f_name = os.path.basename(f_path)

        for attempt in range(10):
            try:
                with open(f_path, 'rb'):
                    break
            except PermissionError:
                print(f"Waiting for file to be ready: {f_name}")
                time.sleep(1)

        category = get_cat(f_name)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        ext = os.path.splitext(f_name)[1]
        new_f_name = f"{category.lower()}_{timestamp}{ext}"

        category_f = os.path.join(OUTPUT_F, category)
        os.makedirs(category_f,exist_ok=True)

        dest_path = os.path.join(category_f, new_f_name)

        try:
            shutil.move(f_path, dest_path)
            print(f"Moved!! {f_name} -> {dest_path}")
        except Exception as e:
            print(f"Error moving {f_name}: {e}")

