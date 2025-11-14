# https://programming-25.mooc.fi/part-3/3-more-loops

# for i in range(3):
#     print(i)

# for i in range(3):
#     print(i)

# for i in range(3):
#     print(i)

# for i in range(3):
#     print(i)


# The continue command
# Another way to change the way a loop is ex
# ecuted is the continue command. It causes the execution
# of the loop to jump straight to the beginning of the loop,
# where the condition of the loop is. Then the execution continues
# normally with checking the condition:


# sum = 0

# while True:
#     number = int(input("Please type in a number, -1 to exit: "))
#     if number == -1:
#         break
#     if number >= 10:
#         continue
#     sum += number

# print (f"The sum is {sum}")


# Nested loops
# Just like if statements, loops can also be placed inside other loops. For example, the following program uses a loop to ask the user to input numbers. It then uses another loop inside the first one to print a countdown from the given number down to 1:

# while True:
#     number = int(input("Please type in a number: "))
#     if number == -1:
#         break
#     while number > 0:
#         print(number)
#         number -= 1
