#BUILT-IN STRING METHODS
s = "hello world"
print(s.upper())   # HELLO WORLD
print(s.lower())   # hello world
print(s.title())   # Hello World

#REPLACE
print(s.replace("world", "Python"))
# hello Python

#JOIN &SPLIT
words = s.split()  
print(words)  # ['hello', 'world']

new = "-".join(words)
print(new)    # hello-world


print("abc".isalpha())   # True
print("123".isdigit())   # True
print("abc123".isalnum())# True
#STRIP(remove spaces)

s = "  hello  "
print(s.strip())   # "hello"
