# Creating a new file
# If you want to create a new file, you would call the open function with the additional argument w, to signify that the file should be opened in write mode. So, the function call could look like this:

# with open("new_file.txt", "w") as my_file:
#     # code to write something to the file
# NB: if the file already exists, all the contents will be overwritten. It pays to be very careful when creating new files.

# With the file open you can write data to it. You can use the method write, which takes the string that is to be written as its argument.

# with open("new_file.txt", "w") as my_file:
#     my_file.write("Hello there!")
# When you execute the program, a new file named new_file.txt appears in the directory. The contents would look like this:

# Sample data
# Hello there!


# Appending data to an existing file
# If you want to append data to the end of a file, instead of overwriting the entire file, you should open the file in append mode with the argument a.

# If the file doesn't yet exist, append mode works exatly like write mode.

# The following program opens the file new_file.txt and appends a couple of lines of text to the end:

# with open("new_file.txt", "a") as my_file:
#     my_file.write("This is the 4th line\n")
#     my_file.write("And yet another line.\n")
# After this program is executed the contents of the file would look like this:

# Sample output
# Hello there!
# This is the second line
# This is the last line
# This is the 4th line
# And yet another line.


# Writing CSV files
# CSV files can be written line by line with the write method just like any other file. The following example creates the file coders.csv, with each line containing the name, working environment, favourite language and years of experience of a single programmer. The fields are separated by a semicolon.

# with open("coders.csv", "w") as my_file:
#     my_file.write("Eric;Windows;Pascal;10\n")
#     my_file.write("Matt;Linux;PHP;2\n")
#     my_file.write("Alan;Linux;Java;17\n")
#     my_file.write("Emily;Mac;Cobol;9\n")
# Executing this program would result in the following file:

# Sample output
# Eric;Windows;Pascal;10
# Matt;Linux;PHP;2
# Alan;Linux;Java;17
# Emily;Mac;Cobol;9

# What if the data to be written is stored in computer memory in a list?

# coders = []
# coders.append(["Eric", "Windows", "Pascal", 10])
# coders.append(["Matt", "Linux", "PHP", 2])
# coders.append(["Alan", "Linux", "Java", 17])
# coders.append(["Emily", "Mac", "Cobol", 9])
# We can build the string we want to write as an f-string, and write the ready line to the file like so:

# with open("coders.csv", "w") as my_file:
#     for coder in coders:
#         line = f"{coder[0]};{coder[1]};{coder[2]};{coder[3]}"
#         my_file.write(line+"\n")


# line = "Alice;25;Python;"
# line = line[:-3]  # removes last ';'
# print(line)

# open("dummy.txt", "w").close()


# Clearing file contents and deleting files
# Sometimes it is necessary to clear the contents of an existing file. Opening the file in write mode and closing the file immediately will achieve just this:

# with open("file_to_be_cleared.txt", "w") as my_file:
#     pass
# Now the with block only contains the command pass, which doesn't actually do anything. Python does not allow empty blocks, so the command is necessary here.

# It is possible to also bypass the with block by using the following oneliner:

# open('file_to_be_cleared.txt', 'w').close()
# Deleting files
# You can also delete a file entirely. We will have to ask for help from the operating system to achieve this:

# # the command to delete files is in the os module
# import os

# os.remove("unnecessary_file.csv")
# NB: this will not work when running the automatic tests on the course servers due to technical limitations in the testing environment. If you are asked to clear the contents of a file, use the methods described above.
