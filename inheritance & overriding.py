#                                                        Inheritance


#example 1
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("The animal makes a sound.")


class Dog(Animal):
    def speak(self):
        print(self.name,"barks.")


class Cat(Animal):
    def speak(self):
       print(self.name,"meows.")


print("Example 2's Output:")
dog = Dog("Sandy")
dog.speak()

cat = Cat("Whiskers")
cat.speak()
print()

"""
In the above example, i have made the Animal class that is base class, while Dog and Cat are derived classes that inherit from
Animal. Each derived class overrides the speak method to provide its own implementation.

"""

#example 2
class Employee:
    def __init__(self, role, salary):
        self.role = role
        self.salary = salary

    def calculate_pay(self):
        return self.salary


class Manager(Employee):
    def calculate_pay(self):
        return self.salary + 5000


class Developer(Employee):
    def calculate_pay(self):
        return self.salary + 3000

print("Example 2's Output:")
manager = Manager("Manager", 50000)
print(manager.role,"salary:", manager.calculate_pay())

developer = Developer("Developer", 40000)
print(developer.role,"salary:", developer.calculate_pay())

""""
In this example, the Employee class is the base class, while Manager and Developer are derived classes. Each derived class overrides 
the calculate_pay method to show the salary calculation based on their specific roles.

"""
