#                                               Polymorphism(Overloading)


#example 1
class MathOperations:
    def add(self, a, b):
        return a + b
    
    def add(self, a, b, c=0):
        return a + b + c

math = MathOperations()
print("Output of example 1")
print(math.add(2, 3))
print(math.add(2, 3, 4)) 
print()


"""
Above is the example of polymorphism achieved by overloading method, the add function takes two arguments a and b, with an optional 
argument c that defaults to 0. It can be seen that both functions have same name but the only difference is the third argument c.
If c is not provided, it adds a and b only. If c is provided, it adds all three numbers together.

"""


#example 2


class Shape:
    def calculate_area(self, length):
            area = length ** 2
            print(f"Area of square with side {length} is: {area}")
    def calculate_area(self, length, breadth=0):
            area = length * breadth
            print(f"Area of rectangle with length {length} and breadth {breadth} is: {area}")

shape = Shape()
shape.calculate_area(5)         
shape.calculate_area(4, 6)  

"""
In above example, the Shape class has a single method calculate_area that takes two parameters length and breadth. By checking the
presence of the breadth parameter, the method determines whether to calculate the area of a square or a rectangle. If only one argument
is provided, it calculates the area of a square, and if both arguments are provided, it calculates the area of a rectangle

"""

