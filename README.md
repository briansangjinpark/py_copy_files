# Recursive File Copy Script

## Overview

This script searches for specific files in all subdirectories of a given source directory and copies them to a destination folder while preserving metadata.

## How It Works

The script reads a list of filenames from inventory.txt.
It recursively searches for these files within the source_dir.
If a matching file is found, it is copied to dest_dir.
The script maintains file metadata while copying.

## Requirements

- Python 3.x
- shutil and os modules (included in Python standard library)

## Usage

Update the script with the correct paths:

- `source_dir`: Directory to search for files.
- `dest_dir`: Directory where the files will be copied.
- `file_list_path`: Path to inventory.txt containing filenames to be copied.

Create an inventory.txt file listing the filenames to be copied, one per line.

Run the script using the command:

`python3 recursive_file_copy.py`

## Example

inventory.txt:

`file1.txt`
`image.png`
`data.csv`

## Command to Run:

python3 copy_files.py

## Notes

The script only copies files that exist in source_dir or its subdirectories.
If multiple copies of the same file exist in different subdirectories, all will be copied.
The script preserves original metadata during copying.

## License

This script is provided as-is, without warranty. Feel free to modify and use as needed.
