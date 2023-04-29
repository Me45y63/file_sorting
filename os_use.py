#!/usr/bin/env python3

import os
from pathlib import Path
from sys import argv

# All directories should be separated by double backslaches eg. 'C:\\Users\\Username\\Desktop\\'

# Index 1: this position belongs to the starting directory
link1 = argv[1]

# Index 2: this position belongs to the end directory
link2 = argv[2]

# Search for file name using some keywords starting from index 3
args = argv[3:]

keywords = []
for arg in args:
    keywords.append(arg)

# Loop through the files in that location
for filename in os.listdir(os.chdir(link1)):

# Try and except any errors that may arise
    try:
        # If theres a file/files with such keywords the file should be located and populated with each iteration of the loop
        if all(keyword in filename for keyword in keywords):
            # Get starting directory
            start_dir = Path(f"{link1}\\{filename}")
            # Get ending directory
            end_dir = Path(f"{link2}\\{filename}")
            # Move to new destination

            start_dir.rename(end_dir)
        else:
            # If no files with such name this is the prompt which it gives
            print("Directory contains no such files")
            break
    except FileExistsError:
        pass

