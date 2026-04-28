#**kwargs allows a function to accept any number of keyword (named) arguments
# It stores them as a dictionary
def show_details(**kwargs):
    print(kwargs)

show_details(name="Madhavi", age=22)


data = {"a": 10, "b": 20}

def show(**kwargs):
    print(kwargs)

show(**data)   # unpacking


def create_profile(**details):
    return details

profile = create_profile(name="Madhavi", age=22, skill="Python")
print(profile)

























