import re

#Example 1
text = "Hello, World!"
# Replace world with python
new_text = re.sub(r"World", "Python", text)
print("Example 1's output:\n")
print(new_text)


#Example 2
text = "I love cats, but I'm allergic to dogs."
# Replace cats and dogs with birds
new_text = re.sub(r"(cats|dogs)", "birds", text)
print("\nExample 2's output:\n")
print(new_text)