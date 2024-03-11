import sys
import os
import datetime
from pathlib import Path

def rename_one_file(filename, filepath, directory):
    # Get the file's creation time in seconds since the epoch
    creation_time = Path(filepath).stat().st_birthtime

    # Convert the creation time to a datetime object
    creation_datetime = datetime.datetime.fromtimestamp(creation_time)

    # Format the creation datetime as a string
    new_filename = creation_datetime.strftime("%Y-%m-%d_%H-%M-%S") + os.path.splitext(filename)[1]
    if new_filename == filename:
        print(f"Filename '{filename}' is already desired format")
        return

    original_new_filepath = os.path.join(directory, new_filename)
    new_filepath = original_new_filepath
    i = 1

    while os.path.exists(new_filepath):
        print(f"New file '{new_filepath}' exists")
        basepath, ext = os.path.splitext(original_new_filepath)
        new_filepath = basepath + '(' + str(i) + ')' + ext
        i += 1
        print(f"Change to '{new_filepath}'")

    # Rename the file
    os.rename(filepath, new_filepath)
    print(f"Renamed '{filepath}' to '{new_filepath}'")
     

def rename_one_file_by_creation_datetime(filepath):
    if not os.path.exists(filepath): return
    filename = os.path.basename(filepath)
    directory = os.path.dirname(filepath)
    rename_one_file(filename, filepath, directory)


def rename_files_by_creation_datetime(directory):
    for filename in os.listdir(directory):
        if filename.startswith("."): continue
        filepath = os.path.join(directory, filename)
        if not os.path.exists(filepath): continue
        rename_one_file(filename, filepath, directory)


for path in sys.argv[1:]:
    #print(f"path='{path}'")

    if os.path.isfile(path):
        print(f"{path} is a file!")
        rename_one_file_by_creation_datetime(path)
    elif os.path.isdir(path):
        print(f"{path} is a directory!")
        rename_files_by_creation_datetime(path)
    else:
        print(f"{path} is neither a file nor a directory.")
