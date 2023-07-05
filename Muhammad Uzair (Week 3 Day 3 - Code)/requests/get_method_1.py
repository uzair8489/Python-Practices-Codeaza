#                                                   GET METHOD

import requests

url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"

try:
    # Making a GET request to the URL
    response = requests.get(url)

    # Processing the response
    if response.status_code == 200:
        # Successful request
        print("Request successful")
        print(response.text)
        data = response.json()
        print("Response content:")
        print(f"Bitcoin Price in USD: {data['bpi']['USD']['rate']}")
    else:
        # Error handling
        print(f"Request failed with status code: {response.status_code}")
# Showing failed requests
except requests.RequestException as e:
    print(f"An error occurred: {e}")

"""
This code covers some basic methods of requests making a GET request, processing the response, handling successful and failed requests, 
and handling potential exceptions that can occur during the request. It specifically retrieves the current Bitcoin price in USD from 
the CoinDesk API.

"""