#                                                 Built-in Modules


#example 1

import datetime

current_date = datetime.date.today()
print(current_date)                     

current_time = datetime.datetime.now()
print(current_time)                     

weekday = current_date.strftime('%A')
print(weekday)

year = current_date.year
print(year)    

""" 
In the example above, i've imported the datetime module, which is a built-in module in Python used for working with dates and 
times. The date.today() method to get the current date, and the datetime.now() method to get the current date and time. 
These values are stored in variables current_date and current_time, respectively.

"""

#example 2

import random

# Generate a random integer between 1 and 10
random_number = random.randint(1, 10)
print(random_number)

# Shuffle a list
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)


"""
The code above uses the builtin random module to generate a random number between 1 and 10  using 'random.randit()' function and
it also shuffles a list using 'random.shuffle()' function.

"""