import requests
from concurrent.futures import ProcessPoolExecutor
import time

url = "https://www.google.com"

def send_request(url):
    response = requests.get(url)
    # Process the response as needed
    print(response.status_code)

if __name__ == '__main__':
    num_requests = 500

    start_time = time.perf_counter()

    with ProcessPoolExecutor() as executor:
        # Submit the requests to the executor
        futures = [executor.submit(send_request, url) for _ in range(num_requests)]

        # Wait for all tasks to complete
        for future in futures:
            future.result()

    end_time = time.perf_counter()

    print(f'Total Execution Time: {end_time - start_time:.2f} seconds')
