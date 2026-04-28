#access elements
t = (10, 20, 30, 40)
print(t[0])    # 10
print(t[-1])   # 40

#2. Slice a tuple
t = (1, 2, 3, 4, 5)

print(t[1:4])   # (2, 3, 4)
#3. Check element exists

t = (5, 10, 15)

print(10 in t)  # True


#4. Count occurrences
t = (1, 2, 2, 3, 2)
print(t.count(2))  # 3

#5. Find index
t = (100, 200, 300)

print(t.index(200))  # 1

#6. Convert tuple → list → modify → tuple
t = (1, 2, 3)

lst = list(t)
lst.append(4)
t = tuple(lst)
print(t)  # (1, 2, 3, 4)

#7. Sum of elements
t = (5, 10, 15)
print(sum(t))  # 30

#8. Find max and min
t = (8, 3, 12, 1)
print(max(t))  # 12
print(min(t))  # 1

#9. Reverse tuple

t = (1, 2, 3, 4)
print(t[::-1])  # (4, 3, 2, 1)


#10. Tuple unpacking
t = (10, 20, 30)

a, b, c = t
print(a, b, c)
#11.Remove duplicates (using set)

t = (1, 2, 2, 3, 4, 4)
t = tuple(set(t))
print(t)

#12. Sort a tuple
t = (4, 1, 3, 2)
t = tuple(sorted(t))
print(t)  # (1, 2, 3, 4)


#13.swap using tuple
a=5
b=20
a,b=b,a
print(a,b)






















