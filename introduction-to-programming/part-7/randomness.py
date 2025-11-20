# Generating a random number
# The function randint(a, b) returns a random integer value between a and b, inclusive. For example, the following program works like a generic die:

# from random import randint

# print("The result of the throw:", randint(1, 6))


# More randomizing functions
# The function shuffle will shuffle any data structure passed as an argument, in place. For example, the following program shuffles a list of words:

# from random import shuffle

# words = ["atlas", "banana", "carrot"]
# shuffle(words)
# print(words)
# Sample output
# ['banana', 'atlas', 'carrot']

# The function choice returns a randomly picked item from a data structure:

# from random import choice

# words = ["atlas", "banana", "carrot"]
# print(choice(words))
# Sample output
# 'carrot'

# from random import randint, seed

# seed("asdasd")  # set the starting point
# print(randint(1, 100))  # will always produce the same number
# print(randint(1, 100))  # will always produce the same next number


# 1️⃣ Where do random numbers come from?

# Computers are deterministic → they can’t generate truly random numbers on their own

# Instead, they use algorithms to produce numbers that look random

# These are called pseudo-random numbers

# 2️⃣ What is a seed?

# A seed is the starting value for the random number generator (RNG) algorithm

# The same seed → the same sequence of “random” numbers

# Changing the seed → produces a different sequence
