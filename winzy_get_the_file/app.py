import os
import glob
from random import choice
import argparse


def last_modified_file(pathpattern) -> str:
    """Returns the last modified file in the specified folder."""
    files = glob.glob(pathpattern)
    if not files:
        return None

    # Find the latest modified time and corresponding file
    latest_time = 0
    latest_file = None
    for file in files:
        mtime = os.path.getmtime(file)
        if mtime > latest_time:
            latest_time = mtime
            latest_file = file

    return latest_file


def last_created_file(pathpattern) -> str:
    """Returns the last created file (or accessed) in the specified folder."""
    files = glob.glob(pathpattern)
    if not files:
        return None

    # Find the latest access time and corresponding file
    latest_time = 0
    latest_file = None
    for file in files:
        atime = os.path.getatime(file)
        if atime > latest_time:
            latest_time = atime
            latest_file = file

    return latest_file


def oldest_file(pathpattern) -> str:
    """Returns the oldest file in the specified folder."""
    files = glob.glob(pathpattern)
    if not files:
        return None

    # Find the earliest modified time and corresponding file
    earliest_time = float("inf")
    earliest_file = None
    for file in files:
        mtime = os.path.getmtime(file)
        if mtime < earliest_time:
            earliest_time = mtime
            earliest_file = file

    return earliest_file


def random_file(pathpattern) -> str:
    """Returns a random file from the specified folder."""
    files = glob.glob(pathpattern)
    if not files:
        return None

    # Return a random file
    return choice(files)


def main():
    parser = argparse.ArgumentParser(description="File Operations CLI")

    parser.add_argument(
        "-f",
        "--folder",
        type=str,
        default=os.getcwd(),
        help="Folder path to search. Defaults to the current directory.",
    )
    parser.add_argument(
        "-p", "--pattern", required=True, help="Pattern to match files."
    )
    parser.add_argument(
        "-t",
        "--type",
        choices=["latest", "oldest", "random", "lastcreated"],
        default="latest",
        help='Type of file to return. Defaults to "latest".',
    )

    args = parser.parse_args()

    folder_path = args.folder
    pattern = args.pattern
    file_type = args.type

    if file_type == "latest":
        result = last_modified_file(folder_path, pattern)
    elif file_type == "oldest":
        result = oldest_file(folder_path, pattern)
    elif file_type == "random":
        result = random_file(folder_path, pattern)
    else:  # file_type == 'lastcreated'
        result = last_created_file(folder_path, pattern)

    if result:
        print(result)
    else:
        print(f"No files matching the pattern '{pattern}' found in {folder_path}")
