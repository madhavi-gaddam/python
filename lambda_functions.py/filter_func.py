#Selects elements where condition is True
#Get even numbers
numbers = [1, 2, 3, 4, 5, 6]

result = list(filter(lambda x: x % 2 == 0, numbers))
print(result)


#Get numbers greater than 5:

nums = [3, 7, 2, 9, 4]

result = list(filter(lambda x: x > 5, nums))
print(result)  # [7, 9]













