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
