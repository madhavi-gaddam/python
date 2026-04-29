#oops - object oriented programming

#CLASS AND OBJECT
#class=blueprint
#object= actual thing created from class

class Car:          #creating class
    pass
car1 = Car()    #creating object
car2 = Car()


#############################################3
#init(constructor)
#used to initialize object values

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

car1 = Car("Toyota", "Red")

print(car1.brand)   # Toyota
print(car1.color)   # Red


#self = current object
#__init__ runs automatically when object is created

###########################################################
#instance methods
#function inside class

class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(self.brand, "is starting")

car1 = Car("BMW")
car1.start()

##############################################
#attributes
#1 instance variables(inside init)
"""
self.brand = brand
"""

#2 class variables(shared by all objects)

class Car:
    wheels = 4

























