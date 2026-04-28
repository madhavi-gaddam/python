#problems
#Remove Duplicates
nums = [1, 2, 2, 3, 4, 4, 5]

unique = []

for n in nums:
    if n not in unique:
        unique.append(n)

print(unique)

#find common elements
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

common = []

for x in a:
    if x in b:
        common.append(x)

print(common)

#rotate list
nums = [1, 2, 3, 4, 5]

last = nums.pop()
nums.insert(0, last)

print(nums)





























