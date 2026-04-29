#ABSTRACTION(hide complexity)
#show only important things ,hides internal logic
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class Car(Vehicle):
    def start(self):
        print("Car starts with key")
c = Car()
c.start()