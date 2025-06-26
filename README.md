# 🗂️ Auto File Sorter (Python)

A real-time Python automation tool that tracks/watches a folder for new files, automatically renaming them with timestamps, and sorts them into categorized folders (Images, Documents, Videos, etc.).

Ideal for organizing messy downloads or incoming project files.


---

## Features

- 📁 Monitors a folder in Real-time
- 🏷️ Automatically categorizes files by type
- 🕓 Adds timestamps to filenames
- 📦 Moves files into appropriate subfolders
- 💼 Modular codebase — ready for Modification, GUI and Expansion
---

## Folder Structure

<pre><code>auto_file_sorter/ 
  ├── drop_here/                     # Folder you drop unsorted files into 
  ├── sorted_output/                 # Destination folder where files are auto-organized 
  ├── sorter/                        # Python modules (core logic lives here) 
  │ ├── __init__.py 
  │ ├── config.py                    # File type definitions and folder settings 
  │ ├── categorizer.py               # Logic to classify files into categories 
  │ └── file_handler.py              # Moves & renames files based on events 
  └── main.py                        # Main runner that starts the folder watcher</code></pre>

---

## Start Guide

1. Install dependencies:

```bash
pip install watchdog
