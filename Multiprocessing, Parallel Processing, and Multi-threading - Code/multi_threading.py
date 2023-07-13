import requests
from concurrent.futures import ThreadPoolExecutor
import time

def send_requests(url, num_requests):
    def make_request(url):
        response = requests.get(url)
        print(response.status_code)

    with ThreadPoolExecutor() as executor:
        for _ in range(num_requests):
            executor.submit(make_request, url)

url = "http://www.google.com"
num_requests = 500

start = time.perf_counter()

send_requests(url, num_requests)

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
