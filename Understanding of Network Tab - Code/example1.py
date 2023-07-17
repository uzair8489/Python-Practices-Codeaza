import requests

url = 'https://restcountries.com/v3/all'

response = requests.get(url)
data = response.json()

# Extract specific data from the response
countries = []
for item in data:
    country = {
        'Name': item['name']['official'],
        'Capital': item['capital'][0],
        'Region': item['region'],
        'Population': item['population'],
        'Languages': item['languages'],
    }
    countries.append(country)

# Print the extracted data for each country

print(countries)