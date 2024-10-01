# Write a Python program to convert a list of tuples into a dictionary.

    # list of tuples
tuples_list = [('a', 1), ('b', 2), ('c', 3)]

    # Converting the list of tuples into a dictionary
d = {key: value for key, value in tuples_list}


print(d)
 