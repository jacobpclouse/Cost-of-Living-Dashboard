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
# Flask Bois
from flask import Flask, render_template, request, url_for, redirect, send_file, jsonify  # for web back end
from flask_cors import CORS 
# SQL and DB stuff
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
# Scraping stuff
import requests
import pandas as pd
from bs4 import BeautifulSoup


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Variables
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
DATABASE = 'WWR_Jobs_database.db'
basedir = os.path.abspath(os.path.dirname(__file__))

demo = Flask(__name__) # name of this python page (ie: demo.py)
demo.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, DATABASE)
# 'sqlite:///' + os.path.join(basedir, 'database.db')
demo.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(demo)


## DB creation!

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    job_title = db.Column(db.String(100), nullable=False)
    company_name = db.Column(db.String(100), nullable=False)
    job_location = db.Column(db.String(80), unique=True, nullable=False)
    # age = db.Column(db.Integer)
    # created_at = db.Column(db.DateTime(timezone=True),
    #                        server_default=func.now())
    # bio = db.Column(db.Text)

    def __repr__(self):
        return f'<Job Listing: {self.job_title}>'

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


# --- Function to get extension for retrieval ---
def need_extension(filename):
    name, extension = filename.split(".")
    upperCaseExt = extension.upper()  
    print(upperCaseExt)
    return upperCaseExt


# --- Function to scrape data ---
def scrape_url_function():
    title = "Jake N Dan COL Board | Scrape N Post!"
    print(" __                      _             ")
    print("/ _\ ___ _ __ __ _ _ __ (_)_ __   __ _ ")
    print("\ \ / __| '__/ _` | '_ \| | '_ \ / _` |")
    print("_\ \ (__| | | (_| | |_) | | | | | (_| |")
    print("\__/\___|_|  \__,_| .__/|_|_| |_|\__, |")
    print("                  |_|            |___/ ")

    # Define the URL of the job page you want to scrape
    url = 'https://weworkremotely.com/remote-full-time-jobs'


    # Send a GET request to retrieve the HTML content of the page
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Create a BeautifulSoup object to parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the specific elements or tags that contain the job listings
        job_elements = soup.find_all('li', class_='feature')
        
        # Create a list to store the extracted job listings
        job_listings_scrape = []
        
        # Extract the job data from the elements and store them in the list
        for element in job_elements:
            job_title_scrape = element.find('span', class_='title').text.strip()
            company_name_scrape = element.find('span', class_='company').text.strip()
            job_location_scrape = element.find('span', class_='region company').text.strip()
            job_listings_scrape.append({'Job Title': job_title_scrape, 'Company': company_name_scrape, 'Location': job_location_scrape})
            # Putting all values into one object and then adding/commiting that to the DB
            addAllVal = Job(job_title=job_title_scrape,company_name=company_name_scrape,job_location=job_location_scrape)

        # Create a DataFrame from the extracted job listings
        job_listings_df = pd.DataFrame(job_listings_scrape)
        
        # Print the extracted job listings
        print(job_listings_df)

## ASENDING ORDER BELOW -- commiting
        try:
            db.session.add(addAllVal)
            db.session.commit()
    #         return redirect('/unhandled')
            return "Commited values to the DB"
        except: 
            return "Failed to Commit"

    #     except: 
    #         return redirect('/404', title = title) # if there is an issue, will return to 404 page
    # else:
    #     print(f"Error: {response.status_code}")


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Routes
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
@demo.route('/')
def hello():
    our_Logo()
    return 'Hello, World!'

@demo.route('/scrape')
def scrapeRoute():
    # print("Scraping!")
    result = scrape_url_function()
    print(result)
    return 'Scraping!'



# -------------------------------------
# main statement - used to set dev mode and do auto reloading - remove this before going to production
# -------------------------------------
if __name__ == '__main__':
    demo.run(debug=True)