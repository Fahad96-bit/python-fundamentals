# import csv

# with open("employees.csv") as my_file:
#     print(csv.reader(my_file, delimiter=";"))
#     for row in csv.reader(my_file, delimiter=";"):
#         print(row)
#     # for line in csv.reader(my_file, delimiter=";"):
#     #     print(line)


# Reading JSON files
# CSV is just one of many machine-readable data formats. JSON is another, and it is used often when data has to be transferred between applications.

# JSON files are text files with a strict format, which is perhaps a little less accessible to the human eye than the CSV format. The following example uses the file courses.json, which contains information about some courses:

# [
#     {
#         "name": "Introduction to Programming",
#         "abbreviation": "ItP",
#         "periods": [1, 3]
#     },
#     {
#         "name": "Advanced Course in Programming",
#         "abbreviation": "ACiP",
#         "periods": [2, 4]
#     },
#     {
#         "name": "Database Application",
#         "abbreviation": "DbApp",
#         "periods": [1, 2, 3, 4]
#     }
# ]


# The structure of a JSON file might look quite familiar to you by now. The JSON file above looks exactly like a Python list, which contains three Python dictionaries.

# The standard library has a module for working with JSON files: json. The function loads takes any argument passed in a JSON format and transforms it into a Python data structure. So, processing the courses.json file with the code below

# import json

# with open("courses.json") as my_file:
#     data = my_file.read()

# courses = json.loads(data)
# print(courses)
# would print out the following:

# Sample output
# [{'name': 'Introduction to Programming', 'abbreviation': 'ItP', 'periods': [1, 3]}, {'name': 'Advanced Course in Programming', 'abbreviation': 'ACiP', 'periods': [2, 4]}, {'name': 'Database Application', 'abbreviation': 'DbApp', 'periods': [1, 2, 3, 4]}]


# Retrieving a file from the internet
# The Python standard library also contains modules for dealing with online content, and one useful function is urllib.request.urlopen. You are encouraged to have a look at the entire module, but the following example should be enough for you to get to grips with the function. It can be used to retrieve content from the internet, so it can be processed in your programs.

# The following code would print out the contents of the University of Helsinki front page:

# import urllib.request

# my_request = urllib.request.urlopen("https://helsinki.fi")
# print(my_request.read())
# Pages intended for human eyes do not usually look very pretty when their code is printed out. In the following examples, however, we will work with machine-readable data from an online source. Much of the machine-readable data available online is in JSON format.
