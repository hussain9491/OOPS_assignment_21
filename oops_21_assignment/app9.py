#  Abstract Classes and Methods
# Assignment: 9
# Use the abc module to create an abstract class Shape with an abstract method area().
#  Inherit a class Rectangle that implements area().
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        super().__init__() 
    def area(self):
        return  f" Area of Rectangle: {self.width * self.height}"     
show = Rectangle(5, 10)
print(show.area())  