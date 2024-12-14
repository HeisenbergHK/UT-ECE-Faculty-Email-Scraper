import os

import requests
from bs4 import BeautifulSoup

# Base URL for the faculty directory
base_url = "https://www.ece.utoronto.ca/faculty/faculty-directory/"

# Send a request to the base page
response = requests.get(base_url)
response.raise_for_status()  # Check if the request was successful

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find all the links to faculty pages (you may need to adjust this based on the page structure)
faculty_links = soup.find_all("a", href=True)  # Find all <a> tags with href attribute

# Filter out non-faculty links, you might need to inspect the page to filter properly
faculty_urls = [link["href"] for link in faculty_links if "/people/" in link["href"]]

# Create a directory to save the HTML pages
os.makedirs("faculty_members", exist_ok=True)

for url in faculty_urls:
    response = requests.get(url=url)
    response.raise_for_status()  # Check if the request was successful
    name = url.split("/")[-2]
    print(name)
    with open(file=f"faculty_members/{name}.html", mode="w", encoding="utf-8") as page:
        page.write(response.text)
