#match()
#checks for a match only at the beginning of the string.
#must match from start
#returns match object or none
import re

text = "123 is my number"
result = re.match(r"\d+", text)

print(result.group())

text = "My number is 123"
result = re.match(r"\d+", text)

print(result)












































































