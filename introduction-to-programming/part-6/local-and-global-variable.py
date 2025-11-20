# The scope of a variable refers to the sections of a program where a variable is accessible. A local variable
# is only accessible in a defined section of the program, while a global variable is available for use in any
# section of the program.


# def testing():
#     x = 5
#     print(x)


# x = 3
# testing()
# print(x)


# Global variables
# Variables defined within the main function are global variables. We previously defined the main function as those sections of code in a Python program which do not fall within any other function. The value stored in a global variable can be accessed from any other function in the program, so the following does not cause any errors:

# def testing():
#     print(x)

# x = 3
# testing()
# Sample output
# 3

# A global variable cannot be changed directly from within another function. The following function has no effect on the value stored in the global variable:

# def testing():
#     x = 5
#     print(x)

# x = 3
# testing()
# print(x)
# Sample output
# 5
# 3

# Here the function testing creates a new, local variable x, which "masks" the global variable while the function is being executed. This variable has the value 5, but it is a different variable than the global x which is defined in the main function.

# But what would the following code do?

# def testing():
#     print(x)
#     x = 5

# x = 3
# testing()
# print(x)
# Sample output
# UnboundLocalError: local variable 'x' referenced before assignment

# The function testing assigns a value to the variable x, so Python interprets x to be a local variable instead of the global variable of the same name. The function attempts to access the variable before it is defined, so there is an error.

# If we wish to specify that we mean to change the global variable within a function, we will need the Python keyword global:

# def testing():
#     global x
#     x = 3
#     print(x)

# x = 5
# testing()
# print(x)
# Sample output
# 3
# 3

# Now the assignment x = 3 within the function also affects the main function. All sections of the program are using the same global variable x.


# def calculate_sum(a, b):
#     global result
#     print(result)
#     # result = a + b


# result = 5
# calculate_sum(2, 3)

# # print(result)


# ❗ If you remove the assignment, THEN it errors

# Example:

# def calculate_sum(a, b):
#     global result
#     print(result)  # trying to read it

# calculate_sum(2, 3)


# Now you get:

# NameError: name 'result' is not defined


# Because:

# You declared result global

# BUT you never assigned anything to it anywhere

# Reading an undefined global → ❌ error
# Assigning to an undefined global → ✔ creates it


# The advantage of the latter approach is that the function is an independent whole. It has certain, defined parameters, and it returns a result. It has no side effects, so it can be tested and changed independently of the other sections of the program.

# Global variables are useful in situations where we need to have some common, "higher level" information available to all functions in the program. The following is an example of just such a situation:

# def calculate_sum(a, b):
#     global count
#     count += 1
#     return a + b

# def calculate_difference(a, b):
#     global count
#     count += 1
#     return a - b


# count = 0
# print(calculate_sum(2, 3))
# print(calculate_sum(5, 5))
# print(calculate_difference(5, 2))
# print(calculate_sum(1, 0))
# print("There were", count, "function calls")
