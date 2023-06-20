import requests
import pandas as pd
from bs4 import BeautifulSoup
'''
pip install requests
pip install pandas
pip install lxml
pip install html5lib

'''

# WORKING!!!

# Define the URL of the job page you want to scrape
url = 'https://weworkremotely.com/remote-full-time-jobs'


# Send a GET request to retrieve the HTML content of the page
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the specific elements or tags that contain the job listings
    # job_elements = soup.find_all('div', class_='job-listing')
    job_elements = soup.find_all('li', class_='feature')
    
    # Create a list to store the extracted job listings
    job_listings = []
    
    # Extract the job data from the elements and store them in the list
    for element in job_elements:
        job_title = element.find('span', class_='title').text.strip()
        company_name = element.find('span', class_='company').text.strip()
        job_location = element.find('span', class_='region company').text.strip()
        job_listings.append({'Job Title': job_title, 'Company': company_name, 'Location': job_location})
    
    # Create a DataFrame from the extracted job listings
    job_listings_df = pd.DataFrame(job_listings)
    
    # Process and manipulate the DataFrame as needed
    # ...
    
    # Print the extracted job listings
    print(job_listings_df)
else:
    print(f"Error: {response.status_code}")
