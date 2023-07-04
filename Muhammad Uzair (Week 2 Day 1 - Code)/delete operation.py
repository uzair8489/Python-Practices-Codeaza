#                                                       DELETE OPERATION

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

# Deleting a post
try:
    response = requests.delete(url)
    print("Post deleted successfully.")
except Exception as e:
    print(f"Failed to delete the post: {e}")
    exit()

"""
The above code i wrote is to delete the data in the API, i have used delete method here. What thi method does is, it takes the post id
from the url and then finds that id in the data and uses the delete function to delete the post entirely. Else it shows the errors
encountered through the process.

"""

