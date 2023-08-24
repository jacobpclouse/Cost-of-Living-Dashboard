import requests
from bs4 import BeautifulSoup

# URL of the LinkedIn page with software jobs
url = "https://www.linkedin.com/jobs/collections/recommended/"

# Send a GET request to retrieve the page content
response = requests.get(url)

# Create a BeautifulSoup object
soup = BeautifulSoup(response.content, "html.parser")

# Use Beautiful Soup to extract the relevant job information
job_listings = soup.find_all("li", class_="jobs-search-results__list-item")

# Print out the job details
for job in job_listings:
    title_element = job.find("a", class_="job-card-list__title")
    company_element = job.find("h4", class_="base-search-card__subtitle")
    location_element = job.find("span", class_="job-search-card__location")
    description_element = job.find("p", class_="base-search-card__snippet")

    if title_element:
        title = title_element.text.strip()
        print("Job Title:", title)

    if company_element:
        company = company_element.text.strip()
        print("Company:", company)

    if location_element:
        location = location_element.text.strip()
        print("Location:", location)

    if description_element:
        description = description_element.text.strip()
        print("Description:", description)

    print("--------------------")