#else runs only if no exception occurs
try:
    num = int(input("Enter number: "))
except ValueError:
    print("Invalid input")
else:
    print("Valid number:", num)


#Q: Print square only if input is valid.

try:
    num = int(input("Enter number: "))
except ValueError:
    print("Invalid input")
else:
    print("Square is:", num * num)







