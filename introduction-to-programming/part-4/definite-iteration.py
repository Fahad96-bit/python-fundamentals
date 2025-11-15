# The for loop
# When you want to go through some ready collection of items, the Python for loop will do this for you. For instance, the loop can go through all items in a list from first to last.

# When using a while loop the program doesn't "know" beforehand how many iterations the loop will perform. It will repeat until the condition becomes false, or the loop is otherwise broken out of. That is why it falls under indefinite iteration. With a for loop the number of iterations is determined when the loop is set up, and so it falls under definite iteration.

# The idea is that the for loop takes the items in the collection one by one and performs the same actions on each. The programmer does not have to worry about which item is being handled when. The syntax of the for loop is as follows:

# for <variable> in <collection>:
#     <block>


# With two arguments, the function will return a range between the two numbers. The function range(a,b) provides a range starting from a and ending at b-1:

# for i in range(3, 7):
#     print(i)
# Sample output
# 3
# 4
# 5
# 6

# Finally, with a third argument you can also specify the size of the step the range takes between each value. The function call range(a, b, c) provides a range starting from a, ending at b-1, and changing by c with every step:

# for i in range(1, 9, 2):
#     print(i)
# Sample output
# 1
# 3
# 5
# 7

# numbers = range(2, 7)
# print(numbers)


name = "Mark"
age = 37
print("Hi " + name + " your age is " + age + " years")
