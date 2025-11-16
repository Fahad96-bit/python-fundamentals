# it = iter("hel")
# print(it)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))


# 1) Iterator works with ANY iterable

# list

# tuple

# string

# dict

# set

# even custom objects

# Example:

# it = iter([1, 2, 3])   # list
# it = iter((1, 2, 3))   # tuple
# it = iter("hello")     # string


# All of these produce an iterator.


# ) Generator is made ONLY from a function using yield

# Example:


# def my_gen():
#     yield 1
#     yield 2


# g = my_gen()
# print(next(g))
# print(next(g))


# This produces a generator object (a special type of iterator).

# Generators don’t come from lists.
# Generators come from functions.


# 🌰 SIMPLEST REAL-LIFE COMPARISON
# Iterator = Box of mangoes

# All mangoes are already inside the box.

# When you say “next”, you pull out the next mango.

# Generator = Mango tree

# When you say “next”, the tree produces a mango right now.

# No mango exists until you ask.


# g = (x * x for x in range(5))
# print(g)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


# total = sum(x * x for x in range(5))
# print(total)


# 2️⃣ Memory difference: Generator vs List


# List version
# total = sum([x * x for x in range(5)])


# Steps:

# [x*x for x in range(5)] creates a list in memory: [0, 1, 4, 9, 16]

# sum() iterates over this list → adds values

# After sum, Python can free the list

# 💡 Memory: stores all 5 numbers at once (imagine if it’s 1,000,000 numbers → huge memory!)

# Generator version
# total = sum(x * x for x in range(5))


# Steps:

# (x*x for x in range(5)) creates a generator object (tiny, constant memory)

# sum() asks for next value from generator → 0 → adds to total

# Generator discards that value → asks for next → 1 → adds → discard

# Repeat for all numbers

# 💡 Memory: only 1 number exists in memory at a time → super space-efficient

# practical example:


# 1) Reading huge files (GBs) without crashing


# If you use a list:

# lines = file.readlines()  # loads whole file → RAM explodes


# But with a generator:

# def read_file():
#     with open("big.txt") as f:
#         for line in f:
#             yield line


#             🚀 3) Infinite sequences

# You cannot store infinite numbers in a list.

# Generator makes it possible:

# def counter():
#     n = 1
#     while True:
#         yield n
#         n += 1


# You can loop forever.

# 👉 Used in:

# event loops

# timers

# 🚀 5) More efficient loops

# 6) Lazy loading

# Instead of preparing all data in advance, you prepare it only when needed.

# Example: loading images in batches:

# def load_images():
#     for img_path in list_of_paths:
#         yield load_image(img_path)


# 👉 Used in ML training loops.
