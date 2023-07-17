import requests
import json

url = "https://caching.graphql.imdb.com/?operationName=TopRatedTvShowsPagination&variables=%7B%22first%22%3A125%2C%22locale%22%3A%22en-US%22%7D&extensions=%7B%22persistedQuery%22%3A%7B%22sha256Hash%22%3A%22550f61ea1a571f35ee3bcffaca64aef1efcaf53de3c8f55b2e5b43a3b0c400d9%22%2C%22version%22%3A1%7D%7D"

headers = {
  'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
  'sec-ch-ua-mobile': '?0',
  'x-amzn-sessionid': '131-0853773-2142650',
  'x-imdb-weblab-treatment-overrides': '{"IMDB_DESKTOP_SEARCH_ALGORITHM_UPDATES_577300":"T1"}',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
  'content-type': 'application/json',
  'x-imdb-client-rid': '30PBVQZ15C70K1015QGV',
  'accept': 'application/graphql+json, application/json',
  'x-imdb-client-name': 'imdb-web-next-localized',
  'x-imdb-user-country': 'US',
  'Referer': 'https://www.imdb.com/',
  'x-imdb-user-language': 'en-US',
  'sec-ch-ua-platform': '"Windows"'
}

response = requests.get(url, headers=headers)
data = json.loads(response.text)

# Extract specific data from the response
chart_titles = data['data']['chartTitles']['edges']

# Extract and print the names of the TV shows
for title in chart_titles:
    name_text = title['node']['principalCredits'][0]['credits'][0]['name']['nameText']['text']
    print(name_text)
