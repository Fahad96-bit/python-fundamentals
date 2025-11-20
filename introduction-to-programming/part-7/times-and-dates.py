# The datetime object
# The Python datetime module includes the function now, which returns a datetime object containing the current date and time. The default printout of a datetime object looks like this:

# from datetime import datetime

# my_time = datetime.now()
# print(my_time)
# Sample output
# 2021-10-19 08:46:49.311393

# You can also define the object yourself:

# from datetime import datetime

# my_time = datetime(1952, 12, 24)
# print(my_time)
# Sample output
# 1952-12-24 00:00:00

# By default, the time is set to midnight, as we did not give a time of day in the example above.

# Different elements of the datetime object can be accessed in the following manner:

# from datetime import datetime

# my_time = datetime(1952, 12, 24)
# print("Day:", my_time.day)
# print("Month:", my_time.month)
# print("Year:", my_time.year)
# Sample output
# Day: 24
# Month: 12
# Year: 1952
