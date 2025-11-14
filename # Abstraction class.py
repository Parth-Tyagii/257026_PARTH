# Abstraction---hiding details and showing only essential information to the user

from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class rectangle(shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
class circle(shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
#object creation
rect = rectangle(10,5) 
print("Area of rectangle:",rect.area())
circ = circle(7)
print("Area of circle:",circ.area())
