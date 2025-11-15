# # https://programming-25.mooc.fi/part-4/5-print-statement-formatting


# So far we have learnt three methods for formulating the argument given to the print command.

# The first is the + operator for strings. It allows simple concatenation of string segments:

# name = "Mark"
# age = 37
# print("Hi " + name + " your age is " + str(age) + " years" )
# This method will not work if any of the segments are not strings. In the example above, the variable age has been converted into a string with the str function, since it is an integer and cannot be concatenated as is.

# The second method is considering each segment of the argument as a separate argument, and splitting them up with commas:

# print("Hi", name, "your age is", age, "years" )
# This code produces the exact same result as the previous version. The print command normally adds a space character between each argument.The advantage here is that the segments can be of different types, so there is no need to convert anything into a string.

# If you want to remove the automatically added spaces, you can add a special named argument sep:

# print("Hi", name, "your age is", age, "years", sep="")
# This prints out

# Sample output
# HiMarkyour age is37years

# The argument sep="" is a keyword argument, and its name is short for separator. It specifies that the other arguments should now be separated by an empty string. You can set the separator to any string you like. For example, if you wanted each argument on a separate line, you could set the separator to "\n", which is the newline character:

# print("Hi", name, "your age is", age, "years", sep="\n")
# Sample output
# Hi
# Mark
# your age is
# 37
# years


# By default, the print command always ends in a newline character, but you can change this as well. The keyword argument end specifies what is put at the end of a line. Setting end to an empty string means that there is no newline character at the end of the printout:

# print("Hi ", end="")
# print("there!")
# Sample output
# Hi there!


# The specific format we want the number to be displayed in can be set within the curly brackets of the variable expression. Let's add a colon character and a format specifier after the variable name:

# number = 1/3
# print(f"The number is {number:.2f}")
# The number is 0.33
# The format specifier .2f states that we want to display 2 decimals. The letter f at the end means that we want the variable to be displayed as a float, i.e. a floating point number.

# Here's another example, where we specify the amount of whitespace reserved for the variable in the printout. Both times the variable name is included in the resulting string, it has a space of 15 characters reserved. First the names are justified to the left, and then they are justified to the right:

# names =  [ "Steve", "Jean", "Katherine", "Paul" ]
# for name in names:
#   print(f"{name:15} centre {name:>15}")
# Steve           centre           Steve
# Jean            centre            Jean
# Katherine       centre       Katherine
# Paul            centre            Paul
