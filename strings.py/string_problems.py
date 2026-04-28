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

