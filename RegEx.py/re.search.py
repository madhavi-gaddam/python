#search()
#finds th efirst occurrence of the pattern anywhere in the string.
#returns a match object
import re

text = "My number is 123"
result = re.search(r"\d+", text)

print(result.group())