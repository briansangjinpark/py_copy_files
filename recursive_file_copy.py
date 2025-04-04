import shutil
import os

source_dir = '/Users/brianpark/Library/CloudStorage/GoogleDrive-bpark@alkymi.io/Shared drives/Clients (contains client data)/Public Sector Pension Investment Board (PSP)/5 - Data/0 - Capital Notice'
dest_dir = '/Users/brianpark/Documents/Work/Dev/py - Copy Local Files/Destination/PSP_CN_InternalQA_04012025'
file_list_path = '/Users/brianpark/Documents/Work/Dev/py - Copy Local Files/file_lists/PSP_CN_InternalQA_04012025'

# Read the list of files to copy
with open(file_list_path, "r") as file:
    file_names = {line.strip() for line in file}

# Walk through all subdirectories in the source directory
for root, _, files in os.walk(source_dir):
    for file_name in files:
        if file_name in file_names:
            source_file = os.path.join(root, file_name)
            dest_file = os.path.join(dest_dir, file_name)
            
            # Copy the file, preserving metadata
            shutil.copy2(source_file, dest_file)
            print(f"Copied: {source_file} -> {dest_file}")
