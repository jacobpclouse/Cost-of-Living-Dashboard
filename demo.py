# Written by Dan B. and Jacob C. during Summer 2023
# Edited on Windows 10 - may need to be edited if you want to use on Linux/MacOS/Win 11

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Importing Libraries / Modules
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
import datetime
import os
# moving files and folders
import shutil  # used to move files around and clean folders
import zipfile  # used in zipping images
from flask import Flask, request, send_file, \
    jsonify  # for web back end
from flask_cors import CORS 



# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Variables
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
demo = Flask(__name__) # name of this python page (ie: demo.py)
DATABASE = 'Jobs_database.db'


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Functions
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def our_Logo():
    run_at_time = defang_datetime()
    print('Code designed, written & tested by:')
    print("  _____                _   _ _        _       _        ")
    print(" |  __ \              | \ | ( )      | |     | |       ")
    print(" | |  | | __ _ _ __   |  \| |/       | | __ _| | _____ ")
    print(" | |  | |/ _` | '_ \  | . ` |    _   | |/ _` | |/ / _ |")
    print(" | |__| | (_| | | | | | |\  |   | |__| | (_| |   <  __/")
    print(" |_____/ \__,_|_| |_| |_| \_|    \____/ \__,_|_|\_\___|")
    print('Built Summer 2023')
    print(f'Started at: {run_at_time}')


# --- Function to Defang date time ---
def defang_datetime():
    current_datetime = f"_{datetime.datetime.now()}"

    current_datetime = current_datetime.replace(":", "_")
    current_datetime = current_datetime.replace(".", "-")
    current_datetime = current_datetime.replace(" ", "_")

    return current_datetime


# --- Function to empty out a directory ---
def clean_out_directory(folderPath):
    for filename in os.listdir(folderPath):
        filePath = os.path.join(folderPath, filename)
        try:
            if os.path.isfile(filePath):
                os.unlink(filePath)
        except Exception as e:
            print(f"Failed to delete {filePath} due to {e}")


# --- Function to check and see if a directory exists and, if not, create that directory ---
def create_folder(folderPath):
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)


# -- Function that takes zip name and then an array of files to zip
def zip_files(zip_name, files_to_zip):
    with zipfile.ZipFile(zip_name, 'w') as zip_file:
        # Add each file to the zip file
        for file_path in files_to_zip:
            # Add the file to the zip file with its original name
            zip_file.write(file_path, arcname=file_path.split('/')[-1])


# --- Function that unzips files from zip file ---
def unzip_files(zip_name):
    # Create a ZipFile object with the name of the zip file and mode 'r' for read
    with zipfile.ZipFile(zip_name, mode='r') as zip_obj:
        # Print a list of all files in the zip file
        print("Files in zip file:")
        for file_name in zip_obj.namelist():
            print(f"- {file_name}")
        # Extract all files to the current working directory
        zip_obj.extractall()


# --- Function to remove unneeded zip files ---
def delete_zip_file(extraZip):
    if os.path.exists(extraZip) and extraZip.endswith('.zip'):
        os.remove(extraZip)
        print(f"{extraZip} has been deleted.")


# --- Function to get extension for retrieval --
def need_extension(filename):
    name, extension = filename.split(".")
    upperCaseExt = extension.upper()  
    print(upperCaseExt)
    return upperCaseExt

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Routes
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
@demo.route('/')
def hello():
    our_Logo()
    return 'Hello, World!'



# -------------------------------------
# main statement - used to set dev mode and do auto reloading - remove this before going to production
# -------------------------------------
if __name__ == '__main__':
    demo.run(debug=True)