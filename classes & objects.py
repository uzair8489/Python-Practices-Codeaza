#                                           Classes and Objects

#example 1
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print(f"The {self.make} {self.model} engine is running.")

    def drive(self):
        print(f"The {self.make} {self.model} is being driven.")


print("Example 1's Output:")
my_car = Car("Toyota", "Camry")
my_car.start_engine()
my_car.drive()

print()

"""
The above example shows how we define class and its objects. We can access the objects and functions of a class very easily and can 
manipulate them according to our needs and we dont have to rewrite the same code if we have to use it elsewhere. We can simply just
call the class and use it. 
Here "self" is a special parameter that refers to the instance of a class.
It is used within the methods of a class to access and modify the instance's attributes and invoke other methods. 

"""

#example 2
class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. Balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawn {amount}. Balance: {self.balance}")
        else:
            print("Insufficient funds.")


print("Example 2's Output:")
my_account = BankAccount("123456789")
my_account.deposit(1000)
my_account.withdraw(500)

""""
The above code defines a class named 'BankAccount' that represents a bank account.

I have Initialized a BankAccount object with an account number and a balance of 0. deposit(): Increases the balance by the 
specified amount and prints the new balance. withdraw(): Decreases the balance by the specified amount if sufficient funds are 
available and prints the new balance. Otherwise, it prints "Insufficient funds."

"""