import shutil
import os

# Reference Dir Paths

# PSP
psp_cn_dir = '/Users/brianpark/Library/CloudStorage/GoogleDrive-bpark@alkymi.io/Shared drives/Clients (contains client data)/Public Sector Pension Investment Board (PSP)/5 - Data/0 - Capital Notice'
psp_cas_dir = '/Users/brianpark/Library/CloudStorage/GoogleDrive-bpark@alkymi.io/Shared drives/Clients (contains client data)/Public Sector Pension Investment Board (PSP)/5 - Data/1 - Capital Account Statement (CAS)'
psp_soi_dir = '/Users/brianpark/Library/CloudStorage/GoogleDrive-bpark@alkymi.io/Shared drives/Clients (contains client data)/Public Sector Pension Investment Board (PSP)/5 - Data/2 - Schedule of Investments (SOI)'

# SSBI 
ssbi_cn_dir = '/Users/brianpark/Library/CloudStorage/GoogleDrive-bpark@alkymi.io/Shared drives/Clients (contains client data)/SimCorp/Use Cases/Capital Notices/Capital Call Data/StateStreet'

# TRS
trs_cn_enri_dir = '/Users/brianpark/Library/CloudStorage/GoogleDrive-bpark@alkymi.io/Shared drives/Clients (contains client data)/Teacher Retirement System of Texas (TRS)/3 - Data/ENRI - Energy, Natural Resources, and Infrastructure'
trs_cn_re_dir = '/Users/brianpark/Library/CloudStorage/GoogleDrive-bpark@alkymi.io/Shared drives/Clients (contains client data)/Teacher Retirement System of Texas (TRS)/3 - Data/RE – Real Estate'
trs_cn_pe_dir = '/Users/brianpark/Library/CloudStorage/GoogleDrive-bpark@alkymi.io/Shared drives/Clients (contains client data)/Teacher Retirement System of Texas (TRS)/3 - Data/PE - Private Equity'
trs_cn_epu_dir = '/Users/brianpark/Library/CloudStorage/GoogleDrive-bpark@alkymi.io/Shared drives/Clients (contains client data)/Teacher Retirement System of Texas (TRS)/3 - Data/EPU - External Public Markets'

# source_dir = '/Users/brianpark/Library/CloudStorage/GoogleDrive-bpark@alkymi.io/Shared drives/Clients (contains client data)/Public Sector Pension Investment Board (PSP)/5 - Data/0 - Capital Notice'
source_dir = trs_cn_epu_dir

dest_dir = '/Users/brianpark/Documents/Work/Dev/py - Copy Local Files/src/destination/TRS/Capital Notice/EPU_GapAnalysis'
file_list_path = '/Users/brianpark/Documents/Work/Dev/py - Copy Local Files/src/file_lists/TRS/Capital Notice/Gap Analysis/EPU_GapAnalysis_07082025.txt'

# Read the list of files to copy
with open(file_list_path, "r") as file:
    file_names = {line.strip() for line in file}

print(f"Total files listed to copy: {len(file_names)}")

# Track results
copied_count = 0
copied_files = set()
copy_errors = {}
found_files = set()

# Walk through all subdirectories in the source directory
for root, _, files in os.walk(source_dir):
    for file_name in files:
        if file_name in file_names:
            found_files.add(file_name)
            source_file = os.path.join(root, file_name)
            dest_file = os.path.join(dest_dir, file_name)
            
            try:
                shutil.copy2(source_file, dest_file)
                copied_files.add(file_name)
                copied_count += 1
                print(f"Copied: {source_file} -> {dest_file}")
            except Exception as e:
                copy_errors[file_name] = str(e)
                print(f"Error copying {file_name}: {e}")

# Files not found at all
not_found_files = file_names - found_files

# Summary
print("\n--- Summary ---")
print(f"Total files listed to copy: {len(file_names)}")
print(f"Successfully copied: {copied_count}")
print(f"Files not found in source directory: {len(not_found_files)}")
print(f"Files that failed during copy: {len(copy_errors)}")

# Detailed error logs
if not_found_files:
    print("\n--- Files NOT FOUND ---")
    for fname in not_found_files:
        print(f"- {fname}")

if copy_errors:
    print("\n--- Files with COPY ERRORS ---")
    for fname, err in copy_errors.items():
        print(f"- {fname}: {err}")
