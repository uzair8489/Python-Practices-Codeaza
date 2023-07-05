import requests

response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
    headers={'Accept': 'application/json'},
)

# View the new `text-matches` array which provides information
# about your search term within the results
json_response = response.json()
print(json_response['items'][0]['owner'])

"""
In above code i have used params and headers to specify some methods, params take the query and put it after the url and in headers,
i have defined the result type which will be got after running the script.

"""