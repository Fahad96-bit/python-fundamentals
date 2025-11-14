# https://programming-25.mooc.fi/part-2/4-simple-loops

# As you can see above, the program asks for several numbers, thanks to the while statement in the program. When the user types in -1, the break command is executed, which exits the loop and execution continues from the first line after the while block.

# With loops, it is crucial that there is always a way to exit the loop at some point in the code, otherwise the repetition could go on forever. To illustrate this, let's change the above example a little:

# number = int(input("Please type in a number, -1 to quit: "))
# while True:
#     if number == -1:
#         break

#     print(number ** 2)

# print("Thanks and bye!")


# The program uses two helper variables. The variable attempts keeps track of how many times the user has typed in a PIN. The variable success is set to either True or False based on whether the user is successful in signing in.

# attempts = 0

# while True:
#     code = input("Please type in your PIN: ")
#     attempts += 1

#     if code == "1234":
#         success = True
#         break

#     if attempts == 3:
#         success = False
#         break

#     # this is printed if the code was incorrect AND there have been less than three attempts
#     print("Incorrect...try again")

# if success:
#     print("Correct PIN entered!")
# else:
#     print("Too many attempts...")
