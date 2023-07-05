import requests
from bs4 import BeautifulSoup

# Send a GET request to the Amazon Best Sellers in Laptop Computers page
url = 'https://www.amazon.com/gp/bestsellers/electronics/13896609011/'
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the laptop items on the page
laptop_items = soup.find_all('div', {'class': 'p13n-sc-uncoverable-faceout'})

# Iterate over each laptop item and extract the title and price
for item in laptop_items:
    # Extract the title
    title = item.find('span', {'class': 'a-size-medium a-color-base a-text-normal'}).text.strip()
    
    # Extract the price
    price = item.find('span', {'class': 'a-price-whole'}).text.strip()
    
    # Print the title and price
    print('Title:', title)
    print('Price:', price)
