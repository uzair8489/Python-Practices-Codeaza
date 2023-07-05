from bs4 import BeautifulSoup
import grequests
import pandas as pd

def get_urls():
    # Define a list to store the URLs
    urls = []
    urls.append('https://news.google.com/search?q=IT%20industry&hl=en-US&gl=US&ceid=US%3Aen')
    return urls

def get_data(urls):
    # Create a list of grequests for each URL
    reqs = [grequests.get(link) for link in urls]
    # Send the requests asynchronously and get the responses
    resp = grequests.map(reqs)
    return resp

def parse(resp):
    # Create a list to store the parsed article data
    articlelist = []
    for r in resp:
        # Parse the response using BeautifulSoup
        sp = BeautifulSoup(r.text, 'lxml')
        # Find all the article elements with the specified class name
        items = sp.find_all('article', {'class': 'MQsxIb xTewfe R7GTQ keNKEd j7vNaf Cc0Z5d EjqUne'})
        for item in items:
            article = {
                'title' : item.find('h3').find('a').text.strip(),
                'post_date' : item.find('div', {'class' : 'QmrVtf RD0gLb kybdz'}).find('div').find('time').text.strip()
            }
            articlelist.append(article)  # Append the article data to the list
    return articlelist


urls = get_urls() 
resp = get_data(urls)
df = pd.DataFrame(parse(resp))  # Parse the responses and create a DataFrame
df.to_csv('articles.csv', index=False)  # Save the DataFrame as a CSV file
