#   main.py

import time
from watchdog.observers import Observer
from watchdog.watchmedo import observe_with

from sorter.file_handler import FileHandler
from sorter.config import COLLECT_F

if __name__ == "__main__":
    print(f"Seaching folder: {COLLECT_F}")
    event_handler = FileHandler()
    observer = Observer()
    observer.schedule(event_handler, COLLECT_F, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
    print("Searching Stopped.")