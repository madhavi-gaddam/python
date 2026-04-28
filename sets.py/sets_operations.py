#a set is a collection of unique elements
#no duplicates
#unordered
#mutable

#1. Union (Combine elements)
A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)          # {1, 2, 3, 4, 5}
print(A.union(B))

#2. Intersection (Common elements)

print(A & B)          # {3}
print(A.intersection(B))


#3. Difference (A - B)
print(A - B)          # {1, 2}
#4. Symmetric Difference
print(A ^ B)          # {1, 2, 4, 5}


#5. Subset & Superset


A = {1, 2}
B = {1, 2, 3}

print(A.issubset(B))     # True
print(B.issuperset(A))   # True


#6. Add / Remove Elements
s = {1, 2}

s.add(3) 
print(s)       # {1,2,3}
s.remove(2)  
print(s)    # removes 2 (error if not exists)
s.discard(5)  
print(s)   # safe remove

#7. Membership Check
if 2 in s:
    print("Exists")






