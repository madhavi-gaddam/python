age = int(input("Enter age: "))

if age < 18:
    raise ValueError("You must be 18+")


#Q: Raise error if number is negative

num = int(input("Enter number: "))

if num < 0:
    raise ValueError("Negative not allowed")
else:
    print("Valid number")












