#                                                         FULL UPDATE

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

#Fully Updating a post
updated_post = {
    "title": "Updated Post Title",
    "body": "This is the updated content of the post.",
    "userId": 1
}

try:
    response = requests.put(url, json=updated_post)
    created_post = response.json()
    print("Post fully updated with ID:", updated_post["id"])
except Exception as e:
    print(f"Failed to update the post: {e}")
    exit()


""""
In the above code, i have used put method.The PUT method is used to completely replace an existing resource with the new data provided
in the request. It requires sending the entire updated data of the resource, including any unchanged fields. If a field is not included
in the request data, it is assumed to be null or empty, and the existing value on the server may be overwritten or cleared.

"""