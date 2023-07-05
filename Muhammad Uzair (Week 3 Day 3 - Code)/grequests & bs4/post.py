import grequests

# Define the POST data
data = {'title': 'New Post', 'content': 'Hello, World!'}

# Create a list of grequests POST requests
requests = [
    grequests.post('https://api.example.com/posts', json=data),
    grequests.post('https://api.example.com/posts', data=data),
]

# Send the requests asynchronously
responses = grequests.map(requests)

# Process the responses...
for response in responses:
    print(response.status_code)
    print(response.text)
