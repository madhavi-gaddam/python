#A list is a collection of items stored in one variable.
#list can store num,str,mixed data
#Indexing (Accessing Elements)
nums = [10, 20, 30, 40]

print(nums[0])   # 10
print(nums[2])   # 30

print(nums[0])   # 10
print(nums[2])   # 30

################################
#slicing

nums = [10, 20, 30, 40, 50]

print(nums[1:4])   # [20, 30, 40]
print(nums[:3])    # [10, 20, 30]
print(nums[2:])    # [30, 40, 50]

#step slicing

print(nums[::2])   # [10, 30, 50]

#list methods
#1 append
nums = [1, 2]
nums.append(3)

print(nums)   # [1, 2, 3]

#2. insert() → add at position
nums.insert(1, 100)

print(nums)   # [1, 100, 2, 3]

#3. remove() → remove value

nums.remove(100)
print(nums)

#4. pop() → remove by index
nums.pop(1)
print(nums)
# 5. sort()

nums = [5, 2, 8]
nums.sort()

print(nums)   # [2, 5, 8]

#6. reverse()
nums.reverse()
print(nums)

#7. len() → length

print(len(nums))
######################################################
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





























