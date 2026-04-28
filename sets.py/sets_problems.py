#Pattern 1: Remove Duplicates

arr = [1, 2, 2, 3, 4, 4]

unique = list(set(arr))
print(unique)


#Pattern 2: Check Common Elements
A = [1, 2, 3]
B = [3, 4, 5]

if set(A) & set(B):
    print("Common elements exist")


#Pattern 3: Find Missing Number

n = 5
arr = [1, 2, 4, 5]

missing = set(range(1, n+1)) - set(arr)
print(missing)   # {3}

#Pattern 4: Check Duplicates

arr = [1, 2, 3, 2]

if len(arr) != len(set(arr)):
    print("Duplicates found")

#Pattern 5: Unique Characters in String

s = "hello"

print(len(set(s)))   # unique characters


#Pattern 6: Two Sum


arr = [2, 7, 11, 15]
target = 9

seen = set()

for num in arr:
    if target - num in seen:
        print("Found pair")
    seen.add(num)












