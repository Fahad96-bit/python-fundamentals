# Formal vs actual, parameter vs argument
# The terminology around data passed to functions can feel confusing. To make matters worse, some sources refer to what we have called parameters and arguments as formal and actual parameters. Other sources call them formal and actual arguments. The Python documentation specifies only the terms argument and parameter, so that is what we will use as well.

# What actually happens when the function call greet("Emily") is executed?

# In the function definition greet(name) the parameter name behaves for all intents and purposes just like a normal variable. We can use it within the function just like we have used variables in the many main functions in our programs thus far.

# In the function call greet("Emily") the argument "Emily" is just like any other string we have come across before. For example, we can assign it to a variable.

# So, when the function call is executed, the value of the argument, "Emily", is assigned to the parameter variable name. For the duration of this execution of the function, name = "Emily". When the function is called with a different argument, the value of name will be different.

# This terminology may all seem a bit superfluous, but computer science as a discipline does aim to be as exact a science as possible. Using well defined terminology helps.


# A quick recap of the data types we've come across so far:

# Type	Python data type	Example
# integer	int	23
# floating point number	float	-0.45
# string	str	"Peter Python"
# Boolean value	bool	True


# def print_many_times(message: str, times: int):
#     print(message)
#     # while times > 0:
#     #     print(message)
#     #     times -= 1


# print_many_times("Hello there", "Emily")


# The problem here is that the second parameter times is compared to an integer, 0, on line 2 of the function definition. The argument given was "Emily", which is a string, not an integer. Strings and integers cannot be compared so simply, so an error ensues.

# To avoid issues like this you can include type hints in your function definitions. The type hint specifies the type of the argument intended for the function:

# def print_many_times(message : str, times : int):
#     while times > 0:
#         print(message)
#         times -= 1
# This tells anyone using the function that the argument stored in message is supposed to be a string, and the argument stored in times is supposed to be an integer.

# Similarly, the return value of a function can be hinted at in the function definition:

# def ask_for_name() -> str:
#     name = input("Mikä on nimesi? ")
#     return name
# This tells the user of the function that the function is supposed to return a string.

# NB: Type hinting is literally just hinting about the type of the argument or the return value. It is not a guarantee of type, and definitely not a safeguard against type errors. If a function receives an argument or returns a value of the wrong type, the function is still executed, but it might not work correctly.
