# Empress Djata
# modules = python file has functions or classes
# 1 or more modules
# modules can have 1 or more function
# break application into smaller task
# simplicity,maintainability, reusability, scoping
# function, modules and packages: modilarization

import os
# all function in os modules
print(dir(os))

# current working directory
print(os.getcwd())

# all files in dir
print(os.listdir('.'))
print(os.listdir())

# import my_calc

# from my_calc import add, sub

# from my_calc import *

# importing my_calc.py and nick naming it calc
import my_calc as calc

a = int(input("enter first number: "))
b = int(input("enter first number: "))

print('addition: ', calc.add(a, b))
print('subract: ', calc.sub(a, b))
print("multiple: ", calc.prod(a, b))
print('division: ', calc.div(a, b))

print(dir(calc))

import sys

print(sys.path)



