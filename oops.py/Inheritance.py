#INHERITANCE(CODE REUSE)
#child class inherits from parent class
class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("Barking")
d = Dog()
d.eat()
d.bark()


#super() keyword
#used to call parent constructor

class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary









