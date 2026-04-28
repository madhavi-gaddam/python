#A function is impure if:

#Output changes even with same input OR
#It modifies external state (variables, files, etc.)
total = 10

def add_to_total(x):
    return total + x

print(add_to_total(5))  # 15


x = 5

def add(y):
    return x + y




def update_list(lst):
    lst.append(10)
    return lst












