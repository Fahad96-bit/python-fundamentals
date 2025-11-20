# with open("example.txt") as new_file:
#     contents = new_file.read()
#     print(contents)


# with open("example.txt") as new_file:
#     count = 0
#     total_length = 0

#     for line in new_file:
#         # line = line.replace("\n", "")
#         count += 1
#         print("Line", count, line)
#         length = len(line)
#         total_length += length

# print("Total length of lines:", total_length)


# 1️⃣ Whole file with .read()

# File example.txt:

# Hello there!
# This example file contains three lines of text.
# This is the last line.

# with open("example.txt") as f:
#     contents = f.read()
#     print(contents)


# contents is a single string:

# "Hello there!\nThis example file contains three lines of text.\nThis is the last line.\n"


# \n = line breaks inside the string

# print(contents) → interprets \n as line breaks

# Output:

# Hello there!
# This example file contains three lines of text.
# This is the last line.


# ✅ No extra blank lines.
# Why? Because print() adds only one newline at the end, which is fine.

# 2️⃣ Iterating line by line
# with open("example.txt") as f:
#     for line in f:
#         print(line)


# Each line is:

# "Hello there!\n"
# "This example file contains three lines of text.\n"
# "This is the last line.\n"


# Notice: each line already has its own \n

# print(line) → adds another newline after printing

# So the output looks like:

# Hello there!

# This example file contains three lines of text!

# This is the last line.


# ✅ Extra blank line appears because line already ends with \n + print adds its own newline.


# ✅ What is CSV?

# CSV = Comma-Separated Values

# It’s a plain text file that stores tabular data (like a spreadsheet or database table)

# Each row in the file is a record

# Each column is separated by a comma (or sometimes a semicolon)

# Example of a CSV file:
# Name,Age,City
# Alice,25,New York
# Bob,30,Los Angeles
# Charlie,22,Chicago


# First line → headers (column names)

# Next lines → data rows

# ✅ Why we need CSV?

# Easy to store structured data

# Works like a mini database without installing anything

# Easy to share

# Almost every software (Excel, Google Sheets, Python, databases) can read/write CSV

# Lightweight & human-readable

# You can open it in any text editor

# Automation friendly

# Python, Java, or any programming language can process CSV easily


# Paul;5;4;5;3;4;5;5;4;2;4
# Beth;3;4;2;4;4;2;3;1;3;3
# Ruth;4;5;5;4;5;5;4;5;4;4


# with open("grades.csv") as new_file:
#     for line in new_file:
#         line = line.replace("\n", "")
#         parts = line.split(";")
#         name = parts[0]
#         grades = parts[1:]
#         print("Name:", name)
#         print("Grades:", grades)
# Sample output
# Name: Paul
# Grades: ['5', '4', '5', '3', '4', '5', '5', '4', '2', '4']
# Name: Beth
# Grades: ['3', '4', '2', '4', '4', '2', '3', '1', '3', '3']
# Name: Ruth
# Grades: ['4', '5', '5', '4', '5', '5', '4', '5', '4', '4']

# with open("people.csv") as new_file:
#     # print out the names
#     for line in new_file:
#         parts = line.split(";")
#         print("Name:", parts[0])

# with open("people.csv") as new_file:
#     # find the oldest
#     age_of_oldest = -1
#     for line in new_file:
#         parts = line.split(";")
#         name = parts[0]
#         age = int(parts[1])
#         if age > age_of_oldest:
#             age_of_oldest = age
#             oldest = name
#     print("the oldest is", oldest)


# names = {}

# with open("employees.csv") as new_file:
#     for line in new_file:
#         parts = line.split(";")
#         if parts[0] == "pic":
#             continue
#         names[parts[0]] = parts[1]

# salaries = {}

# with open("salaries.csv") as new_file:
#     for line in new_file:
#         parts = line.split(";")
#         if parts[0] == "pic":
#             continue
#         salaries[parts[0]] = int(parts[1]) + int(parts[2])

# print("incomes:")

# for pic, name in names.items():
#     if pic in salaries:
#         salary = salaries[pic]
#         print(f"{name:16} {salary} euros")
#     else:
#         print(f"{name:16} 0 euros")
