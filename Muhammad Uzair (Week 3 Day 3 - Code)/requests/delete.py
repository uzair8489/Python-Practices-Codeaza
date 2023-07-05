import requests

url = 'https://httpbin.org/'

# Send a DELETE request to delete a post
response = requests.delete(url)

# Process the response
if response.status_code == 204:
    print("Post deleted successfully")
else:
    print("Failed to delete post with status code:", response.status_code)


"""
In this example, the code sends a DELETE request to the specified URL to delete a post. The response status code is checked
and if it is 204, it indicates that the request was successful. Otherwise, an appropriate error message is displayed.

"""
