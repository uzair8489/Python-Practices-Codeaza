#                                                        Data Abstraction



#example 1
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        return self.length * self.breadth

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius**2

rectangle = Rectangle(5, 3)
circle = Circle(7)

print("Example 1's Output:")
print(rectangle.calculate_area())  
print(circle.calculate_area())  
print()

"""
In the above example, I used the Abstract Base Class (ABC) module in Python to define an abstract base class called Shape. This class
has an abstract method calculate_area(), which must be implemented by its subclasses. The Rectangle and Circle classes inherit from
Shape and provide their own implementations of calculate_area().

"""


# example 2

class Rectangle:
    def __init__(self, length, breadth):
        self.__length = length
        self.__breadth = breadth

    def calculate_area(self):
        return self.__length * self.__breadth

class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def calculate_area(self):
        return 3.14 * self.__radius**2


rectangle = Rectangle(5, 3)
circle = Circle(7)

print("Example 2's Output:")
print(rectangle.calculate_area())  
print(circle.calculate_area()) 


"""
In the second approach, i achieve data abstraction by using private member variables (denoted by __ prefix) in the Rectangle and
Circle classes. These variables are not directly accessible from outside the class, encapsulating the data. The calculate_area()
methods provide the interface to access the data and perform the required calculations.

"""
