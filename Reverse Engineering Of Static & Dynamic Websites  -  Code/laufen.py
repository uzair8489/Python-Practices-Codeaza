import requests

url = "https://www.laufen.co.at/automatic-category-detail?p_p_id=ProductList_INSTANCE_80H5hgzHtYEp&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&roca_env=3vjR5WgLKZIHLB3Uu8eoUA%3D%3D"

payload = ""
headers = {
  'Accept': '*/*',
  'Accept-Language': 'en-US,en;q=0.9,ur;q=0.8,es;q=0.7',
  'Connection': 'keep-alive',
  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'Cookie': 'GUEST_LANGUAGE_ID=de_DE; _fbp=fb.2.1688803230252.2019502732; _pin_unauth=dWlkPU1EbG1OV016WVRRdE5HVXdaQzAwWkRVMkxUa3hOak10TjJGbVptSmxObUl4TWpSaQ; OptanonAlertBoxClosed=2023-07-08T08:00:37.015Z; _gid=GA1.3.1865511199.1688803238; ln_or=eyI1NTgwMjMzIjoiZCJ9; _ga=GA1.1.1810830037.1688803232; LFR_SESSION_STATE_20103=1689037083756; _ga_NGNL8PVVV5=GS1.1.1689036807.32.1.1689037089.54.0.0; _ga_BPY6HHXTQX=GS1.1.1689036807.32.1.1689037089.54.0.0; JSESSIONID=81E181A6E0284BDC2E9EC1BFD73DD8FA; OptanonConsent=isGpcEnabled=0&datestamp=Tue+Jul+11+2023+04%3A31%3A42+GMT%2B0300+(Arabian+Standard+Time)&version=202210.1.0&isIABGlobal=false&hosts=&consentId=31707897-7f47-446e-9c4a-bc26cda7c861&interactionCount=1&landingPath=NotLandingPage&groups=C0004%3A1%2CC0005%3A1%2CC0002%3A1%2CC0003%3A1%2CC0001%3A1&geolocation=%3B&AwaitingReconsent=false; GUEST_LANGUAGE_ID=de_DE',
  'Origin': 'https://www.laufen.co.at',
  'Referer': 'https://www.laufen.co.at/produkte/waschtische',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
  'X-Requested-With': 'XMLHttpRequest',
  'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"'
}
response = requests.request("POST", url, headers=headers, data=payload)

# Converted Data into json format
data = response.json()

# Searching through the data dictonary
print(data['products'][0]['url'])
