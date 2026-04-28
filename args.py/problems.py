#1. Sum of Numbers
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3, 4))  # 10
#2. Find Maximum
def find_max(*args):
    return max(args)

print(find_max(10, 50, 30))  # 50

#3. Multiply All Numbers

def multiply_all(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(multiply_all(2, 3, 4))  # 24
#4. Count Arguments
def count_args(*args):
    return len(args)

print(count_args(1, 2, 3, 4, 5))  # 5

#5. Filter Even Numbers

def even_numbers(*args):
    return [x for x in args if x % 2 == 0]

print(even_numbers(1, 2, 3, 4, 5, 6))  # [2, 4, 6]










