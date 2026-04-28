#Problem 1: Access Value
d = {"a": 10, "b": 20}
print(d["b"])

#Problem 2: Add New Key

d["c"] = 30


#Problem 3: Update Value
d["a"] = 100


#Problem 4: Count Frequency of Elements
lst = [1, 2, 2, 3, 3, 3]

freq = {}

for num in lst:
    freq[num] = freq.get(num, 0) + 1

print(freq)

#Problem 5: Find Max Value Key
d = {"a": 10, "b": 50, "c": 30}

max_key = max(d, key=d.get)
print(max_key)
#Problem 6: Remove a Key Safely

d.pop("x", None)

#Problem 7: Merge Two Dictionaries

d1 = {"a": 1}
d2 = {"b": 2}

d1.update(d2)
print(d1)
#🔹 Problem 8: Find Duplicate Values
d = {"a": 1, "b": 2, "c": 1, "d": 3}
values = list(d.values())
duplicates = []

for v in values:
    if values.count(v) > 1 and v not in duplicates:
        duplicates.append(v)

print(duplicates)


#Problem 9: Student Marks Analysis

students = {
    "Madhavi": 85,
    "Ravi": 90,
    "Sita": 78
}
# Highest
top = max(students, key=students.get)
print(top)

# Average
avg = sum(students.values()) / len(students)
print(avg)












