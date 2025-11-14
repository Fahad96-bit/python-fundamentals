# https://programming-25.mooc.fi/part-2/1-programming-terminology


# Statement
# A statement is a part of the program which executes something. It often, but not always, refers to a single command.

# For example, print("Hi!") is a statement which prints out a line of text. Likewise, number = 2 is a statement which assigns a value to a variable.

# A statement can also be more complicated. It can, for instance, contain other statements. The following statement spans three lines:

# if name == "Anna":
#     print("Hi!")
#     number = 2


#     Block
# A block is a group of consecutive statements that are at the same level in the structure of the program. For example, the block of a conditional statement contains those statements which are executed only if the condition is true.

# if age > 17:
#     # beginning of the conditional block
#     print("You are of age!")
#     age = age + 1
#     print("You are now one year older...")
#     # end of the conditional block

# print("This here belongs to another block")


# Expression
# An expression is a bit of code that results in a determined data type. When the program is executed, the expression is evaluated so that it has a value that can then be used in the program.

# Here are a few examples of expressions:

# Expression	Value	Type	Python data type
# 2 + 4 + 3	9	integer	int
# "abc" + "de"	"abcde"	string	str
# 11 / 2	5.5	floating point number	float
# 2 * 5 > 9	True	Boolean value	bool


# Function
# A function executes some functionality. Functions can also take one or more arguments, which are data that can be fed to and processed by the function. Arguments are sometimes also referred to as parameters. There is a technical distinction between an argument and a parameter, but the words are often used interchangeably. For now it should suffice to remember that both terms refer to the idea of some data passed to the function.

# A function is executed when it is called. That is, when the function (and its arguments, if any) is mentioned in the code. The following statement calls the print function with the argument "this is an argument":

# print("this is an argument")

name = "Anna"
result = 100

print(type("Anna"))
print(type(100))
