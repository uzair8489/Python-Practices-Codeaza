import requests

def test_proxy(proxy):
    # Set up the proxy
    proxies = {
        'http': f'http://{proxy}',
        'https': f'https://{proxy}'
    }

    test_url = 'https://httpbin.org/ip'  # URL to test the proxy

    try:
        response = requests.get(test_url, proxies=proxies)
        if response.status_code == 200:
            print(f"Proxy {proxy} is working fine.")
        else:
            print(f"Proxy {proxy} is not functioning properly. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while testing the proxy {proxy}: {str(e)}")

# Example usage
proxy = '103.125.240.242:8080'
test_proxy(proxy)
