# num = 5
# print(id(num))


# Thus far we have thought of a variable as a sort of a "box" which contains the value of the variable. Technically this is not true in Python. What is stored in a variable is not the value per se, but a reference to the object which is the actual value of the variable. The object can be e.g. a number, a string or a list.

# In practice, this means that the value of the variable is not stored in the variable itself. Instead, there is information about the location in computer memory where the value can be found.

# A reference is often represented by an arrow from the variable to the actual value in memory:

# 5 2 1
# So, a reference tells us where the value can be found. The function id can be used to find out the exact location the variable points to:

# a = [1, 2, 3]
# print(id(a))
# b = "This is a reference, too"
# print(id(b))
# Sample output
# 4538357072
# 4537788912


# x = 10
# y = x

# y = y + 1
# print(x)


# x = 10
# y = x
# y = y + 1

# x → (int object 10)
# y → (same int object 10)


# Both point to the same object.

# Step 2: y = y + 1

# Python computes 10 + 1

# It produces a new int object 11

# Then it changes the reference inside y to point to 11

# x still points to the original 10

# x → (int object 10)
# y → (int object 11)   ← NEW object


# Many of the builtin types in Python, such as str, are immutable. This means the value of the object, or any part of it, cannot change. The value can be replaced with a new value:


# It may surprise you that also the basic data types int, float and bool are immutable in Python. Let's have a look at the following bit of code:

# number = 1
# number = 2
# number += 10
# It seems that the commands above are just changing the value stored in the variable, but in fact each command creates a whole new number in the computer's memory.

# The printout from the following program illuminates the situation:

# number = 1
# print(id(number))
# number += 10
# print(id(number))
# a = 1
# print(id(a))
# Sample output
# 4535856912
# 4535856944
# 4535856912

# At first, the variable number points to the memory location 4535856912. When number is assigned a new value, it points to the location 4535856944. Now, when the variable a is assigned the value 1, a points to the very same location where number was pointing, when it was also assigned the value 1.

# It seems Python has stored the value 1 in the memory location 4535856912. Whenever a variable is assigned the value 1, it refers to that location in computer memory.

# It is good to keep in mind that almost everything is a reference in Python, but all this is rarely relevant to everyday programming tasks. So let's get back to more practical matters.


# It is good to keep in mind that almost everything is a reference in Python, but all this is rarely relevant to everyday programming tasks. So let's get back to more practical matters.

# number = 1
# print(id(number))
# number += 10
# print(id(number))
# a = 1
# print(id(a))

# y = 1
# print(id(y))
# x = 1
# print(id(x))

# name = "fahad"
# print(id(name))
# namess = "fahads"
# print(id(namess))


# ✔️ Final Explanation (super simple)
# Expression	Meaning
# my_list[:] on the right	creates a copy
# my_list[:] = ... on the left	replaces list contents (same object)
