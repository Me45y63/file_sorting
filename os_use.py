import os
from pathlib import Path

# Search for file name using some keywords
keywords = ['AnimePahe', 'Death', 'Parade']

# Loop through the files in that location
for filename in os.listdir(os.chdir('YOUR_PATH_HERE')):

# Try and except any errors that may arise
    try:
        # If theres a file/files with such keywords the file should be located and populated with each iteration of the loop
        if all(keyword in filename for keyword in keywords):
            # Get starting directory
            start_dir = Path(f"YOUR_PATH_HERE\\{filename}")
            # Get ending directory
            end_dir = Path(f"YOUR_PATH_HERE\\{filename}")
            # Move to new destination
            start_dir.rename(end_dir)
        else:
            # If no files with such name this is the prompt which it gives
            print("Directory contains no such files")
    except FileExistsError:
        pass

