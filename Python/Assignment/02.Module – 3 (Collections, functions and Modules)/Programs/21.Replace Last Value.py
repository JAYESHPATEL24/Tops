# Write a Python program to replace last value of tuples in a list. 

    # list of tuples
tuples_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
value = 100  # Value to replace the last element

    # Create a modified list of tuples
New_tuples = [t[:-1] + (value,) for t in tuples_list]

    # Print the results
print("Original list of tuples:", tuples_list)
print("Modified list of tuples:", New_tuples)
