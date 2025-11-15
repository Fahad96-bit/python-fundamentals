# Lists within lists
# The items in a list can be lists themselves:

# my_list = [[5, 2, 3], [4, 1], [2, 2, 5, 1]]
# print(my_list)
# print(my_list[1])
# print(my_list[1][0])
# Sample output
# [[5, 2, 3], [4, 1], [2, 2, 5, 1]]
# [4, 1]
# 4


# Matrices
# A two-dimensional array, or a matrix, is also a natural application of a list within a list.


# Accessing items in a matrix
# Accessing a single row within a matrix is simple - just choose the desired row. The following function calculates the sum of the elements on a chosen row:

# def sum_of_row(my_matrix, row_no: int):
#     # choose the desired row from within the matrix
#     row = my_matrix[row_no]
#     row_sum = 0
#     for item in row:
#         row_sum += item

#     return row_sum

# m = [[4, 2, 3, 2], [9, 1, 12, 11], [7, 8, 9, 5], [2, 9, 15, 1]]

# my_sum = sum_of_row(m, 1)
# print(my_sum) # prints out 33 (which equals 9 + 1 + 12 + 11)
# Working with columns within a matrix is slightly more complicated, as the matrix is stored by rows:

# def sum_of_column(my_matrix, column_no: int):
#     # go through each row and select the item at the chosen position
#     column_sum = 0
#     for row in my_matrix:
#         column_sum += row[column_no]

#     return column_sum

# m = [[4, 2, 3, 2], [9, 1, 12, 11], [7, 8, 9, 5], [2, 9, 15, 1]]

# my_sum = sum_of_column(m, 2)
# print(my_sum) # prints out 39 (which equals 3 + 12 + 9 + 15)
