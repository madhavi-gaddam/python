#Problem: Write a function to return the sum of two numbers.
def add(a, b):
    return a + b

print(add(3, 5))  # 8

#Problem: Check if a number is even or odd.

def is_even(n):
    return n % 2 == 0

print(is_even(4))  # True


#3. Maximum of Two Numbers
def maximum(a, b):
    return a if a > b else b

print(maximum(10, 20))  # 20

#4. Factorial (Using Loop)
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(factorial(5))  # 120

#5. Sum of List
def list_sum(nums):
    total = 0
    for n in nums:
        total += n
    return total

print(list_sum([1, 2, 3, 4]))  # 10


#6. Count Vowels in String
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

print(count_vowels("hello"))  # 2

#7. Reverse a String
def reverse_string(s):
    return s[::-1]

print(reverse_string("python"))  # nohtyp

#8. Prime Number Check

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

print(is_prime(7))  # True

#9. Fibonacci Series (n terms)

def fibonacci(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

print(fibonacci(5))  # [0, 1, 1, 2, 3]






















