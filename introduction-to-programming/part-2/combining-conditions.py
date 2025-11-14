# https://programming-25.mooc.fi/part-2/3-combining-conditions

# Logical operators
# You can combine conditions with the logical operators and and or. The operator and specifies that all the given conditions must be true at the same time. The operator or specifies that at least one of the given conditions must be true.

# For example, the condition number >= 5 and number <= 8 determines that number must simultaneously be at least 5 and at most 8. That is, it must be between 5 and 8.

# number = int(input("Please type in a number: "))
# if number >= 5 and number <= 8:
#     print("The number is between 5 and 8")
# Meanwhile, the condition number < 5 or number > 8 determines that number must be either less than 5 or greater than 8. That is, it must not be within the range of 5 to 8.

# number = int(input("Please type in a number: "))
# if number < 5 or number > 8:
#     print("The number is not within the range of 5 to 8")


# number = int(input("Please type in a number: "))
# if not (number >= 5 and number <= 8):
#     print("The number is not within the range of 5 to 8")


# Simplified combined conditions
# The condition x >= a and x <= b is a very common way of checking whether the number x falls within the range of a to b. An expression with this structure works the same way in most programming languages.

# Python also allows a simplified notation for combining conditions: a <= x <= b achieves
# the same result as the longer version using and. This shorter notation might be more familiar
#  from mathematics, but it is not very widely used in Python programming, possibly because very
#  few other programming languages have a similar shorthan

# x = 5
# a = 1
# b = 10

# # Long version
# if a <= x and x <= b:
#     print("x is between a and b")

# # Shorter Python version
# if a <= x <= b:
#     print("x is between a and b")


# is_raining = True
# activity = "Stay inside" if is_raining else "Go for a walk"
# print(activity)  # Output: Stay inside


# doubled = list(map(lambda x: x*2, numbers))
# This line has three things happening:

# lambda x: x*2

# This is an anonymous function (a function without a name).

# It says: “Take an input x and return x*2.”

# Example: if x=3 → returns 6

# map(lambda x: x*2, numbers)

# map applies the function (lambda x: x*2) to every item in the numbers list.

# So internally:

# 1 → 1*2 → 2

# 2 → 2*2 → 4

# 3 → 3*2 → 6

# But map doesn’t give a list immediately — it gives a special map object (like a generator).

# list(...)

# We wrap it in list() to convert the map object into a normal list.

# So doubled becomes [2, 4, 6].
