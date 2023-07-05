import grequests

# Creates a list of URLs to request
urls = [
    'https://www.example.com',
    'https://www.google.com',
    'https://www.github.com'
]

# Creates a list of grequests GET requests
requests = [grequests.get(url) for url in urls]

# Send the requests asynchronously
responses = grequests.map(requests)

# Processes the responses
for response in responses:
    if response is not None:
        print(f"Response from {response.url}: {response.status_code}")
    else:
        print("Request failed")

