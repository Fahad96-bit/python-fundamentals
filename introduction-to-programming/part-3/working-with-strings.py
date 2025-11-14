# https://programming-25.mooc.fi/part-3/2-working-with-strings
# word = "banana"
# print(3 * word)


# n = 10  # number of layers in the pyramid
# row = "*"

# while n > 0:
#     print(" " * n + row)
#     row += "**"
#     n -= 1


# s = "hello"
# print(s[1])


# input_string = input("Please type in a string: ")
# index = 0
# while index < len(input_string):
#     print(input_string[index])
#     index += 1


# You can also use negative indexing to access characters countin
# g from the end of the string. The last character in a string is at
# index -1, the second to last character is at index -2, and so forth. You
# can think of input_string[-1] as shorthand for input_string[len(input_string) - 1].

# animal = "giraffe"
# print(animal[-4])


# Substrings and slices
# A substring of a string is a sequence of characters that forms a part of the string. For example, the string example contains the substrings exam, amp and ple, among others. In Python programming, the process of selecting substrings is usually called slicing, and a substring is often referred to as a slice of the string. The two terms can often be used interchangeably.

# If you know the beginning and end indexes of the slice you wish to extract, you can do so with the notation [a:b]. This means the slice begins at the index a and ends at the last character before index b - that is, including the first, but excluding the last. You can think of the indexes as separator lines drawn on the left side of the indexed character, as illustrated in the image below:

input_string = "presumptious"

print(input_string[0:3])
print(input_string[4:10])

# if the beginning index is left out, it defaults to 0
print(input_string[:3])

# if the end index is left out, it defaults to the length of the string
print(input_string[4:])


# Half open intervals
# In Python string processing the interval [a:b] is half open, which in this case means that the character at the beginning index a is included in the interval, but the character at the end index b is left out. Why is that?

# There is no profound reason for this feature. Rather it is a convention inherited from other programming languages.

# Half open intervals may feel unintuitive, but in practice they do have some advantages. For example, you can easily calculate the length of a slice with b-a. On the other hand, you must always remember that the character at the end index b will not be included in the slice.


# Searching for substrings
# The in operator can tell us if a string contains a particular substring. The Boolean expression a in b is true, if b contains the substring a.

# For example, this bit of code

# input_string = "test"

# print("t" in input_string)
# print("x" in input_string)
# print("es" in input_string)
# print("ets" in input_string)


# input_string = "perpendicular"

# while True:
#     substring = input("What are you looking for? ")
#     if substring in input_string:
#         print("Found it")
#     else:
#         print("Not found")


# The operator in returns a Boolean value, so it will only tell us if a substring exists in a string, but it will not be useful in finding out where exactly it is. Instead, the Python string method find can be used for this purpose. It takes the substring searched for as an argument, and returns either the first index where it is found, or -1 if the substring is not found within the string.


# input_string = "test"

# print(input_string.find("t"))
# print(input_string.find("x"))
# print(input_string.find("es"))
# print(input_string.find("ets"))
