import requests

url = 'https://api.github.com/search/repositories?q=requests+language:python'

# Send a HEAD request to the URL
response = requests.head(url)

# Process the response
if response.status_code == 200:
    # Successful request
    print("Request successful")
    print("Response headers:")
    print(response.headers)
else:
    # Error handling
    print(f"Request failed with status code: {response.status_code}")


"""
In this example, i have sent a HEAD request to the URL . The response headers are then printed if the request is successful
(status code 200), providing information about the resource without downloading its content.

"""
