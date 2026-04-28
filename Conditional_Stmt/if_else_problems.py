#Conditional statements let your program make decisions.

#👉 “If something is true → do this
#Else → do something else”








#######################################
#1 Check if a number is even or odd

num = 7

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


#🟢 Problem 2: Positive, Negative, Zero

num = -5

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

#🟢 Problem 3: Largest of Two Numbers
a = 10
b = 20

if a > b:
    print("a is largest")
else:
    print("b is largest")


#Problem 4: Largest of Three Numbers

a = 5
b = 8
c = 3

if a > b and a > c:
    print("a is largest")
elif b > c:
    print("b is largest")
else:
    print("c is largest")

#Problem 5: Check Leap Year

year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")

#Problem 6: Simple Calculator

num1 = 10
num2 = 5
op = "+"


if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Invalid operator")

#Discount System

amount = 1200
if amount > 1000:
    discount = amount * 0.10
elif amount > 500:
    discount = amount * 0.05
else:
    discount = 0

print("Discount:", discount)
print("Final Price:", amount - discount)


#Triangle Validity

a = 3
b = 4
c = 5

if a + b > c and a + c > b and b + c > a:
    print("Valid Triangle")
else:
    print("Invalid Triangle")

#Problem: Login System

username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Credentials")


