#                                                      Encapsulation

#example 1
class Employee:
    def __init__(self, name, salary):
        self._name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary


emp = Employee("John", 5000)
print(emp._name, "'s salary is", emp.get_salary()) 

"""
In the above example i have made an employee class having basic attributes like name and salary to demonstrate encapsulation method. 
Another worth mentioning thing is that i have made some variables private. We can make variables private by using '__'
before the variable name. This way we can protect the data from public or from any unwanted. We can't access the private variables
outside this class.

"""

#example 2
class Car:
    def __init__(self, make, model):
        self.__make = make  # Private attribute
        self.__model = model  # Private attribute

    def get_make_model(self):
        return f"{self.__make} {self.__model}"


my_car = Car("Toyota", "Corolla")
print(my_car.get_make_model())  # Accessing private attributes through a getter method

""""
In above example, i have created an instance of the Car class is created with the make "Toyota" and model "Corolla" using 
the my_car variable. The get_make_model method is then called on my_car to retrieve and print the car's make and model.

"""
