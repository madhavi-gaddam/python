def add(a, b):
    return a + b
result = add(3, 5)
print(result)   # Output: 8



def multiply(x, y):
    return x * y
result = multiply(3, 5)
print(result)   # Output: 15



def greet(name="Guest"):
    print("Hello,", name)

greet()        # Hello, Guest
greet("John")  # Hello, John


def introduce(name, age):
    print(name, "is", age, "years old")

introduce(age=25, name="Alice")

def calculate(a, b):
    return a + b, a * b

sum_val, prod_val = calculate(3, 4)












