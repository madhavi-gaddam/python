#RegEx (regular expression) is a patten matching tool used to search match and manipulate text
"""
Validate Input

Check if data follows a format:

Email validation
Phone numbers
Password rules
"""
import re

pattern = r"^[a-z]+@gmail\.com$"
print(re.match(pattern, "abc@gmail.com"))  # valid

#ssearch patterns in text
text = "My number is 9876543210"
print(re.findall(r"\d+", text))  # finds numbers

#replace text
text = "Hello 123"
print(re.sub(r"\d+", "NUM", text))  
# Output: Hello NUM

#extract data
# used in fataanalysis, logs parsing, web scraping
text = "Price: 500 INR"
print(re.findall(r"\d+", text))  # ['500']

"""

Common RegEx Symbols
Symbol	   Meaning	    Example
.	    any character	a.c → abc
\d	    digit       	0–9
\w	    word            (a-z, A-Z, 0-9)	
+	    one or more	     \d+
*	    zero or more	
^	    start of string	
$	    end of string

"""