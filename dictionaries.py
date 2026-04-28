#A dictionary stores data in key → value pairs
student = {
    "name": "Madhavi",
    "age": 22,
    "course": "Python"
}
print(student["name"])   # Madhavi

print(student.get("age"))        # 22
print(student.get("marks"))      # None
print(student.get("marks", 0))   # 0 (default value)

#ADDING & UPDATING VALUES

student["marks"] = 90
print(student)


#UPDATE EXISTING KEY

student["age"] = 23

print(student)

#ADD MULTIPLE VALUES

student.update({"city": "Hyderabad", "grade": "A"})
print(student)

#REMOVING ITEMS
#using pop()
student.pop("age")
print(student)

#using del
del student["course"]
#remove last item
student.popitem()
print(student)

#clear all
student.clear()
print(student)
######################################
#get all keys
student = {
    "name": "Madhavi",
    "age": 22,
    "course": "Python"
}
print(student.keys())
print(student.values())
























































































