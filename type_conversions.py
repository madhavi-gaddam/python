#Variables & Data Types
#int, float, str, bool
#Type checking: type()
#Type conversion: int(), str(), float()
a=4
print(type(a))
print(str(a))
a = 10

# int → float
b = float(a)

# float → string
c = str(b)

# string → int
d = int("50")

print(a, b, c, d)

# Calculate total bill
price = "100"   # string
quantity = 3

# Convert price to int
price = int(price)

total = price * quantity
print("Total Bill:", total)