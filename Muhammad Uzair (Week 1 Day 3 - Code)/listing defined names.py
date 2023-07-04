#                                              Listing the defined names of module


#example 1
from folder_module import module2

module_names = dir(module2)
print()
print("My custom module's defined names:")
print(module_names)
print()



#example 2
import math

module_names = dir(math)
print()
print("Built-In module's defined names:")
print(module_names)
print()