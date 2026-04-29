#A function wrapper is simply a function that:

#takes another function as input
#adds extra behavior
#returns a new function
#Basic Example
def wrapper(func):
    def inner():
        print("Before function call")
        func()
        print("After function call")
    return inner


#with wrappers
def greet():
    print("Hello")

greet = wrapper(greet)
greet()








