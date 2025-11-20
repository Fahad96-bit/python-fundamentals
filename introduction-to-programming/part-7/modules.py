# Using modules
# The Python language definition already contains some useful functions, such as the len function which returns the length of a string or a list, or the sum function which returns the sum of items in a data structure, but they will only get a programmer so far. The Python standard library is a collection of standardised functions and objects, which can be used to expand the expressive power of Python in many ways. We have already used some functions defined in the standard library in previous exercises, for example when calculating square roots.

# The standard library is comprised of modules, which contain functions and classes grouped around different themes and functionalities. In this part of the course we will familiarize ourselves with some useful Python modules. We will also learn to write our own modules.

# The command import makes the contents of the given module accessible in the current program. Let's have a closer look at working with the math module. It contains the definitions of some mathematical functions, such as sqrt for square root and log for logarithm.

# import math

# # The square root of the number 5
# print(math.sqrt(5))
# # the base 2 logarithm of the number 8
# print(math.log(8, 2))


# from math import sqrt, log

# print(sqrt(5))
# print(log(5,2))


# As you can see above, we do not need the math prefix when using the functions imported in this manner.

# Sometimes a handy shortcut is to import all the contents of a module with the star notation:

# from math import *

# print(sqrt(5))
# print(log(5,2))
# Importing modules with the star notation can be useful when testing and in some smaller projects, but it can pose some new problems, too. We will come across these later.
