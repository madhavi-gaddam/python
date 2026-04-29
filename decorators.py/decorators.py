def wrapper(func):
    def inner():
        print("Before function call")
        func()
        print("After function call")
    return inner

@wrapper
def greet():
    print("Hello")

greet()