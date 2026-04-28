#1. Sum of Values
def total_marks(**kwargs):
    total = 0
    for value in kwargs.values():
        total += value
    return total

print(total_marks(math=90, science=85, english=88))  # 263

#2. Find Maximum Value

def max_value(**kwargs):
    return max(kwargs.values())

print(max_value(a=10, b=50, c=30))  # 50

#3. Count Number of Arguments

def count_items(**kwargs):
    return len(kwargs)

print(count_items(name="A", age=20, city="Hyd"))  # 3

#4. Filter Values Greater Than 10
def greater_than_10(**kwargs):
    return {k: v for k, v in kwargs.items() if v > 10}

print(greater_than_10(a=5, b=12, c=20))
# {'b': 12, 'c': 20}

#5. Print Key-Value Pairs
def display(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

display(name="Madhavi", role="Engineer")




















