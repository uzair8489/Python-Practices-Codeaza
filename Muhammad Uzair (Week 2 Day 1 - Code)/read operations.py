#                                                       READ OPERATION

import requests
import pandas as pd

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
	"X-RapidAPI-Key": "eb496f5fb5msh7c07c193e8a1247p1a9724jsn25cc840951e7",
	"X-RapidAPI-Host": "covid-193.p.rapidapi.com"
}

# for retrieving the data
try:
    response = requests.get(url, headers=headers)
    api_data = response.json()
    print(api_data)
except Exception as e:
    print(f"Error occurred while fetching the API data: {e}")
    exit()


"""
In this code, i have used the get() function to read the data from an API. first i imported some modules and then i have used them
in the code for getting the HTTP request from the API. If it gets the data, it prints the data. And if there is any error, it also
prints in the terminal. This is how we can implement a read operation on an API for reading the data. 

"""

