# Adding items to a list
# The append method adds items to the end of a list. It works like this:

# numbers = []
# numbers.append(5)
# numbers.append(10)
# numbers.append(3)
# print(numbers)


# Adding to a specific location
# If you want to specify a location in the list where an item should be added, you can use the insert method. The method adds an item at the specified index. All the items already in the list with an index equal to or higher than the specified index are moved one index further, "to the right":


# Removing items from a list
# There are two different approaches to removing an item from a list:

# If the index of the item is known, you can use the method pop.
# If the contents of the item are known, you can use the method remove.
# So, the method pop takes the index of the item you want to remove as its argument. The following program removes items at indexes 2 and 3 from the list. Notice how the indexes of the remaining items change when one is removed.

# The method remove, on the other hand, takes the value of the item to be removed as its argument. For example, this program

# my_list = [1, 2, 3, 4, 5, 6]

# my_list.remove(2)
# print(my_list)
# my_list.remove(5)
# print(my_list)
# prints out this:

# Sample output
# [1, 3, 4, 5, 6]
# [1, 3, 4, 6]

# The method removes the first occurrence of the value in the list, much like the string function find returns the first occurrence of a substring:

# my_list = [1, 2, 1, 2]

# my_list.remove(1)
# print(my_list)
# my_list.remove(1)
# print(my_list)


# numbers = [1, 2, 3, 4, 5, 6]
# numbers.insert(0, 10)
# print(numbers)
# numbers.insert(2, 20)
# print(numbers)


# Sorting lists
# The items in a list can be sorted from smallest to greatest with the method sort.

# my_list = [2,5,1,2,4]
# my_list.sort()
# print(my_list)
# Sample output
# [1, 2, 2, 4, 5]

# Notice how the method modifies the list itself. Sometimes we don't want to change the original list, so we use the function sorted instead. It returns a sorted list:

# my_list = [2,5,1,2,4]
# print(sorted(my_list)))
# Sample output
# [1, 2, 2, 4, 5]

# Remember the difference between the two: sort changes the order of the original list in place, whereas sorted creates a new, ordered copy of the list. With sorted we can preserve the original order of the list:

# original = [2, 5, 1, 2, 4]
# in_order = sorted(original)
# print(original)
# print(in_order)
# Sample output
# [2, 5, 1, 2, 4]
# [1, 2, 2, 4, 5]
