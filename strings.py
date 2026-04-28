#string slicing
s = "Python"

print(s[0])     # P
print(s[1:4])   # yth
print(s[:3])    # Pyt
print(s[::2])   # Pto
print(s[::-1])  # nohtyP (reverse)

#string manipulation
#CONCATENATION
a = "Hello"
b = "World"
print(a + " " + b)  # Hello World

#REPETITION
print("Hi " * 3)  # Hi Hi Hi


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


#PROBLEMS ON STRING
#1

# Take a number and check if it's even or odd
n = 7
print(n % 2 == 0)


#2
# Reverse a string
s = "Python"
print(s[::-1])

#3
# Count vowels in string
s = "hello"
count = 0

for ch in s:
    if ch in "aeiou":
        count += 1

print(count)


#4
# Check if two strings are equal ignoring case
a = "Hello"
b = "hello"

print(a.lower() == b.lower())




























