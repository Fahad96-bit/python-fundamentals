# https://programming-25.mooc.fi/part-5/3-dictionary

# my_dictionary = {
#     "apple": "a fruit",
#     "banana": "a fruit",
#     "cherry": "a fruit",
# }

# print(my_dictionary["apple"])

# my_dictionary["apple"] = "a fruit"
# print(my_dictionary["apple"])

# my_dictionary["apple"] = "a fruit"


# Lists can be handy in many situations, but they are limited by the fact that the items are accessed through indexes; 0, 1, 2, and so forth. If you want to find some item in a list, you will either have to know its index, or, at worst, traverse through the entire list.

# Another central data structure in Python is the dictionary. In a dictionary, the items are indexed by keys. Each key maps to a value. The values stored in the dictionary can be accessed and changed using the key.

# person = {[1, 2]: "Fahad", 5: 28, "city": "Karachi"}


# for key in person:
#     print(key)


# for value in person.values():
#     print(value)


# for key, value in person.items():
#     print(key, value)

# print(person.values())
# print(person.keys())
# print(person.items())


# All keys in a dictionary must be immutable. So, a list cannot be used as a key, because it can be changed. For example, executing the following code causes an error:

# my_dictionary[[1, 2, 3]] = 5
# Sample output
# TypeError: unhashable type: 'list'


# Hash table
# Notice the word 'unhashable' in the error message above. This is a reference to the inner workings of the dictionary data type. Python stores the contents of a dictionary in a hash table. Each key is reduced to a hash value, which determines where the key is stored in computer memory. The error message above indicates that a list cannot be processed into a hash value, so it cannot be used as a key in a dictionary.

# The Data Structures and Algorithms courses will further explore hash tables.


# def counts(my_list):
#     words = {}
#     for word in my_list:
#         # if the word is not yet in the dictionary, initialize the value to zero
#         if word not in words:
#             words[word] = 0
#         # increment the value
#         words[word] += 1
#     return words

# # call the function
# print(counts(word_list))


# Removing keys and values from a dictionary
# It is naturally possible to also remove key-value pairs from the dictionary. There are two ways to accomplish this. The first is the command del:

# staff = {"Alan": "lecturer", "Emily": "professor", "David": "lecturer"}
# del staff["David"]
# print(staff)
# Sample output
# {'Alan': 'lecturer', 'Emily': 'professor'}

# If you try to use the del command to delete a key which doesn't exist in the dictionary, there will be an error:

# staff = {"Alan": "lecturer", "Emily": "professor", "David": "lecturer"}
# del staff["Paul"]
# Sample output
# >>> del staff["Paul"]
# Traceback (most recent call last):
#   File "", line 1, in
# KeyError: 'Paul'

# The other way to delete entries in a dictionary is the method pop:

# staff = {"Alan": "lecturer", "Emily": "professor", "David": "lecturer"}
# deleted = staff.pop("sadsa")
# print(staff)
# print(deleted, "deleted")
# Sample output
# {'Alan': 'lecturer', 'Emily': 'professor'}
# lecturer deleted


# As you can see above, pop also returns the value from the deleted entry.

# By default, pop will also cause an error if you try to delete a key which is not present in the dictionary. It is possible to avoid this by giving the method a second argument, which contains a default return value. This value is returned in case the key is not found in the dictionary. The special Python value None will work here:

# staff = {"Alan": "lecturer", "Emily": "professor", "David": "lecturer"}
# deleted = staff.pop("Paul", None)
# if deleted == None:
#   print("This person is not a staff member")
# else:
#   print(deleted, "deleted")
# Sample output
# This person is not a staff member


# NB: if you need to delete the contents of the entire dictionary, and try to do it with a for loop, like so

# staff = {"Alan": "lecturer", "Emily": "professor", "David": "lecturer"}
# for key in staff:
#   del staff[key]
# you will receive an error message:

# Sample output
# RuntimeError: dictionary changed size during iteration

# When traversing a collection with a for loop, the contents may not change while the loop is in progress.

# Luckily, there is a dictionary method for just this purpose:

# staff.clear()


# Using dictionaries for structured data
# Dictionaries are very useful for structuring data. The following code will create a dictionary which contains some personal data:

# person = {"name": "Pippa Python", "height": 154, "weight": 61, "age": 44}
# This means that we have here a person named Pippa Python, whose height is 154, weight 61, and age 44. The same information could just as well be stored in variables:
