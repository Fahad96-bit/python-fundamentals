# Tuple is a data structure which is, in many ways, similar to a list. The most important differences between the two are:

# Tuples are enclosed in parentheses (), while lists are enclosed in square brackets []
# Tuples are immutable, while the contents of a list may change
# The following bit of code creates a tuple containing the coordinates of a point:

# point = (10, 20)

# The values stored in a tuple cannot be changed after the tuple has been defined. The following will not work:

# point = (10, 20)
# point[0] = 15
# Sample output
# TypeError: 'tuple' object does not support item assignment


# 3️⃣ Tuples can be used as Dictionary Keys

# Lists can’t be dictionary keys because they are mutable.

# locations = {
#     (24.8607, 67.0011): "Karachi",
#     (25.3960, 68.3578): "Hyderabad"
# }


# If these coordinates were lists:

# [[24.8607, 67.0011]]  # ❌ cannot be dict key

# Why does immutability matter?

# Because some things in programming should never change:

# coordinates (x, y)

# date (year, month, day)

# color (r, g, b)

# database primary keys

# config values

# If something should stay constant → tuple.


# def minmax(my_list):
#     return min(my_list), max(my_list)


# my_list = [33, 5, 21, 7, 88, 312, 5]

# min_value, max_value = minmax(my_list)
# print(min_value)
# print(max_value)


# Tuples without parentheses
# The parentheses are not strictly necessary when defining tuples. The following two variable assignments are identical in their results:

# numbers = (1, 2, 3)
# numbers = 1, 2, 3


# You may remember the dictionary method items in the previous section. We used it to access all the keys and values stored in a dictionary:

# my_dictionary = {}

# my_dictionary["apina"] = "monkey"
# my_dictionary["banaani"] = "banana"
# my_dictionary["cembalo"] = "harpsichord"

# for key, value in my_dictionary.items():
#     print("key:", key)
#     print("value:", value)
# Tuples are at work here, too. The method my_dictionary.items() returns each key-value pair as a tuple, where the first item is the key and the second item is the value.

# Another common use case for tuples is swapping the values of two variables:

# number1, number2 = number2, number1
# The assignment statement above swaps the values stored in the variables number1 and number2. The result is identical to what is achieved with the following bit of code, using a helper variable:

# helper_var = number1
# number1 = number2
# number2 = helper_var
