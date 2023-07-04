#                                                   CREATE OPERATION


import requests

url = "https://jsonplaceholder.typicode.com/posts"

# Creating a new post
new_post = {
    "title": "My New Post",
    "body": "This is the content of my new post.",
    "userId": 1
}

try:
    response = requests.post(url, json=new_post)
    created_post = response.json()
    print("New post created with ID:", created_post["id"])
except Exception as e:
    print(f"Failed to create the post: {e}")
    exit()

"""
In the above code, i have used an API and performed a create operation in it which stores a new data in the posts section with a new
post using the 'POST' function which automatically performs the create functionaliy.

"""