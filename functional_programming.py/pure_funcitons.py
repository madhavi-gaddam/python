#A function is pure if:

#Same input → same output (always)
#No side effects (doesn’t change anything outside)

def square(x):
    return x * x

print(square(4))  # 16
print(square(4))  # 16 (always same)


def add_item(lst):
    new_list = lst.copy()
    new_list.append(5)
    return new_list



