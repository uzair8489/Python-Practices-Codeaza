import re

# example 1
# Matches one or more digits
pattern = r'\d+'
string = 'There are 123 apples and 456 bananas.'

matches = re.findall(pattern, string)
print("Example 1's output:\n")
print(matches)

# example 2
#finds the email form the string
text = "Contact us at uzair@gmail.com or ahad@gmail.com"
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

emails = re.findall(pattern, text)
print("\nExample 2's output:\n")
print(emails)
