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

