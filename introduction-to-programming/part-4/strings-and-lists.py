# my_list = [1, 2, 3, 4, 5, 6, 7, 8]

# print(my_list[::-1])


# More slices
# In fact, the [] syntax works very similarly to the range function, which means we can also give it a step:

# my_string = "exemplary"
# print(my_string[0:7:2])
# my_list = [1,2,3,4,5,6,7,8]
# print(my_list[6:2:-1])
# Sample output
# eepa
# [7, 6, 5, 4]

# If we omit either of the indexes, the operator defaults to including everything. Among other things, this allows us to write a very short program to reverse a string:

# my_string = input("Please type in a string: ")
# print(my_string[::-1])
# Sample output
# Please type in a string: exemplary
# yralpmexe


# Strings are immutable
# Strings and lists have a lot in common, especially in the way they behave with different operators. The main difference is that strings are immutable. That means they cannot be changed.

# my_string = "exemplary"
# my_string[0] = "a"
# Strings cannot be changed, so the execution of this program causes an error:

# Sample output
# TypeError: 'str' object does not support item assignment

# A similar error follows if you try to sort a string with the sort method.

# Strings themselves are immutable, but the variables holding them are not. A string can be replaced by another string.

# The following two examples are thus fundamentally different:

# my_list = [1,2,3]
# my_list[0] = 10


# my_string = "Hey"
# my_string = my_string + "!"

# The first example changes the contents of the referenced list. The second example replaces the reference to the original string with a reference to another string. The original string is still somewhere in computer memory, but there is no reference to it, and it cannot be used in the program any longer.

# We will return to this subject in the next part, where references to lists are explored in more detail.


# More methods for lists and strings
# The method count counts the number of times the specified item or substring occurs in the target. The method works similarly with both strings and lists:

# my_string = "How much wood would a woodchuck chuck if a woodchuck could chuck wood"
# print(my_string.count("ch"))

# my_list = [1,2,3,1,4,5,1,6]
# print(my_list.count(1))


# The method will not count overlapping occurrences. For example, in the string aaaa the method counts only two occurrences of the substring aa, even though there would actually be three if overlapping occurrences were allowed.

# The method replace creates a new string, where a specified substring is replaced with another string:

# my_string = "Hi there"
# new_string = my_string.replace("Hi", "Hey")
# print(new_string)
# Sample output
# Hey there

# The method will replace all occurrences of the substring:

# sentence = "sheila sells seashells on the seashore"
# print(sentence.replace("she", "SHE"))
# Sample output
# SHEila sells seaSHElls on the seashore
