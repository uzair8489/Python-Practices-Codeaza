#Example 1
import re

#Checking if the string starts with "The" and ends with "Spain":

txt = "The internship has been started"
x = re.search("^The.*started$", txt)

print("Example 1's output:\n")
if x:
  print("YES! We have a match!")
else:
  print("No match")


#Example 2
text = "The quick brown fox jumps over the lazy dog"
pattern = r'\bfox\b'

match = re.search(pattern, text)

print("\nExample 2's output:\n")
if match:
    print("Match found:", match)
else:
  print("No match")