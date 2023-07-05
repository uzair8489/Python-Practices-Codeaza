import requests

url = 'https://httpbin.org/get'

# Send an OPTIONS request to retrieve available methods and headers
response = requests.options(url)

# Process the response
if response.status_code == 200:
    print("Options request successful")
    print("Response content:")
    print(response.text)
else:
    print("Options request failed with status code:", response.status_code)


"""
n this example, the code sends an OPTIONS request to the specified URL. This request is used to retrieve the available methods and
headers for the specified resource. After sending the request, the response status code is checked. If it is 200, it indicates a 
successful request. The response content is printed, and if the status code is different, an appropriate error message is displayed.

"""