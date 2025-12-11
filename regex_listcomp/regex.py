# regex

import re

string = 'Welcome 2026, we will be entering 01-Jan-26. Bye 2025'
pattern = '\\d+'

result = re.findall(pattern, string)
print(result)

pattern = '^a...e$'
test_string1 = 'apple'
result = re.match(pattern, test_string1)
 
if result:
    print("Match found")
else:
    print("No such word found")

