import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError

# Defining retries
github_adapter = HTTPAdapter(max_retries=3)

session = requests.Session()

# Use `github_adapter` for all requests to endpoints that start with this URL
session.mount('https://api.github.com', github_adapter)

try:
    session.get('https://api.github.com', timeout=5)  # Adding a timeout of 5 seconds
except ConnectionError as ce:
    print(ce)


"""
In this example, the timeout parameter is added to the session.get() method, specifying a maximum time of 5 seconds to wait for
a response. If the request exceeds this timeout, a ConnectionError will be raised, and you can handle it accordingly.

"""