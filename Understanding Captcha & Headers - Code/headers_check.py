import requests

url = "https://linkoye.co"

# Send a GET request to the URL
response = requests.get(url)

# Access the request headers
request_headers = response.request.headers

# Access the response headers
response_headers = response.headers

# Print the request headers
print("Request Headers:")
for header, value in request_headers.items():
    print(f"{header}: {value}")
print()

# Print the response headers
print("Response Headers:")
for header, value in response_headers.items():
    print(f"{header}: {value}")
