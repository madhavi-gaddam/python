#Reduces a list to one value
#Sum of all numbers
from functools import reduce

numbers = [1, 2, 3, 4]

result = reduce(lambda a, b: a + b, numbers)
print(result)

#Find product (multiplication of all numbers):
nums = [2, 3, 4]

from functools import reduce

result = reduce(lambda a, b: a * b, nums)
print(result)  # 24


















