
import os 
from datetime import datetime
from zipfile import ZipFile
import py7zr
import pandas as pd


# Base Folder
base_folder = '.\\versao 2'

# Downloads Staging Area
downloads_folder = base_folder + '\\downloads'

# Datasets Staging Area
datasets_folder = base_folder + '\\datasets'


log = {'filename':[], 'modified_at': [], 'extracted_at':[]}


files = os.listdir(downloads_folder)

for file in files:

    now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    file_path = downloads_folder + '\\' + file

    # Get timestamp from files:
    timestamp = (os.path.getmtime(file_path))
    modified_at = datetime.fromtimestamp(timestamp)
    date_str = modified_at.strftime("%d-%m-%Y %H:%M:%S") 

    # Check if exists on 'log' dict:
    if file not in log['filename'] and date_str not in log['modified_at']:
        log['filename'].append(file)
        log['modified_at'].append(date_str)
        
        # Append to 'log' table
        print(f"The file '{file}' modified in '{date_str}' does not exist in the logs. Proceeding to extract.")
        
        # Decompress files from the Downloads area to Datasets area
        file_details = file.split(sep = '.', maxsplit=1)
        folder_name = file_details[0] + ' ' + modified_at.strftime("%d-%m-%Y %H.%M.%S") 

        # Check if .zip or .7zip
        file_ext = file_details[-1]

        # 7z extract
        if '7z' in file_ext:
            with py7zr.SevenZipFile(file_path, 'r') as f:
                f.extract(datasets_folder + '\\' + folder_name)
                log['extracted_at'].append(now)
                print('File extracted successfully')

        # zip extract
        elif file_ext == 'zip':
            with ZipFile(file_path, 'r') as f:
                f.extractall(datasets_folder + '\\' + folder_name)
                log['extracted_at'].append(now)
                print('File extracted successfully')

        else:
            print(f"File: '{file}' - extension not supported. Please use '.zip' or '.7z' files only.")

        download_log = pd.DataFrame.from_dict(log)
        download_log.to_csv('.\\versao 2\download_logs.csv', index = False)

    else:
        print(f"* The file '{file}' with '{date_str}' already exists on the log. Skipping file.")


download_log.head().sort_values('extracted_at', ascending = False)


