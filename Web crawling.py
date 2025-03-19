import requests
from bs4 import BeautifulSoup

# Send an HTTP request to get the webpage content
url = 'https://www.python.org/'
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print("Successfully retrieved the webpage")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Get all <a> tags inside <li> elements from the main navigation menu
categories = soup.select('nav ul[class="navigation menu"]  li  a[class]') 

# Print the category names
for category in categories:
    print(category.get_text(strip=True))