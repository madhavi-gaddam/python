#zip() is used to combine multiple iterables (like lists, tuples) into pairs (or groups).
l1 = [1, 2, 3]
l2 = ['a', 'b', 'c']

result = zip(l1, l2)
print(list(result))


l1 = [1, 2, 3]
l2 = ['a', 'b']

print(list(zip(l1, l2)))   #[(1, 'a'), (2, 'b')]

#3. Can zip more than 2 lists


l1 = [1, 2, 3]
l2 = ['a', 'b', 'c']
l3 = [10, 20, 30]

print(list(zip(l1, l2, l3)))

###########################
names = ["Madhavi", "Ravi"]
marks = [90, 85]

for name, mark in zip(names, marks):
    print(name, mark)












