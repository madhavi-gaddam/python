#1 sum of numbers


total = 0

for i in range(1, 11):
    total += i

print(total)

#2 Table of 5
for i in range(1, 11):
    print("5 x", i, "=", 5 * i)


#skip multiple of3
for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i)

#Find Prime Numbers (1–20)
for num in range(2, 21):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)


#fibonacci series
a, b = 0, 1

for i in range(10):
    print(a)
    a, b = b, a + b

#password attempts

correct = "admin123"

for i in range(3):
    pwd = input("Enter password: ")

    if pwd == correct:
        print("Access Granted")
        break
    else:
        print("Wrong password")

