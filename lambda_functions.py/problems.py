#Square only even numbers
nums = [1, 2, 3, 4, 5, 6]
# Step 1: Filter even
evens = filter(lambda x: x % 2 == 0, nums)

# Step 2: Square them
result = list(map(lambda x: x * x, evens))

print(result)  # [4, 16, 36]

#Sum of even numbers

nums = [1, 2, 3, 4, 5, 6]


from functools import reduce

evens = filter(lambda x: x % 2 == 0, nums)
result = reduce(lambda a, b: a + b, evens)

print(result)  # 12

#Convert names to uppercase

names = ["ram", "shyam", "hari"]

result = list(map(lambda x: x.upper(), names))
print(result)  # ['RAM', 'SHYAM', 'HARI']









