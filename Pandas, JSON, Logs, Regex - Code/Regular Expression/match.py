import re

string = 'Selenium Automation'
pattern = 'Selenium'

match = re.match(pattern, string)
if match:
    print('Match found!')
else:
    print('No match found.')
