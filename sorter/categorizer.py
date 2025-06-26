#   sorter/categorizer.py

import os
from .config import FILE_CATEGORIES

def get_cat(f_name):
    ext = os.path.splitext(f_name)[1].lower() #spliting the extension from the filename

    #checking it with file extensions in config
    for category, extenions in FILE_CATEGORIES.items():
        if ext in extenions:
            return category

    return "Others"