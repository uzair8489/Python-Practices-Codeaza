#                                                         PATRIAL UPDATE

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

# Updating a post
updated_post = {
    "title": "Updated Post Title",
}

try:
    response = requests.patch(url, json=updated_post)
    # response = requests.put(url, json=updated_post)
    created_post = response.json()
    print("Post Title updated with ID:", updated_post["id"])
except Exception as e:
    print(f"Failed to update the post: {e}")
    exit()

"""
The above code i wrote is to update the data in the API, i have used patch method here. The PATCH method is used to partially
update an existing data with the new data provided in the request. It allows sending only the specific fields that need to be updated,
without requiring the entire data of the resource. The server then applies the provided changes to the existing resource, leaving any
unchanged fields intact. The PATCH method is useful when you want to update specific properties of a resource without affecting the rest of the fields.

"""