import requests
import random
import csv
import concurrent.futures

#opens a csv file of proxies and prints out the ones that work with the url in the extract function

proxylist = []

with open('proxylist.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        proxylist.append(row[0])

def extract(proxy):
    try:
        #change the url to https://httpbin.org/ip that doesnt block anything
        r = requests.get('https://httpbin.org/ip', proxies={'http' : proxy,'https': proxy}, timeout=5)
        print(r.json(), ' | Works')
    except:
        pass
    return proxy

with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(extract, proxylist)