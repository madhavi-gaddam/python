#POLYMORPHISM(many forms)
#same function= different behavior


#Example 1: Method Overriding
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

d = Dog()
d.sound()   # Bark

#Example 2: Duck Typing
class Bird:
    def fly(self):
        print("Flying")

class Airplane:
    def fly(self):
        print("Airplane flying")

for obj in [Bird(), Airplane()]:
    obj.fly()





















