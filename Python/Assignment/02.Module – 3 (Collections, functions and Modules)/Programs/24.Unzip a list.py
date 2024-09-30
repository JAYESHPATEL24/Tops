# Write a Python program to unzip a list of tuples into individual lists.

    # list of tuples
tuple_list = [(1,2,3), (4,5,6), ("Radhe", "Shyam", "Ram")]

    # create individual lists from list of tuples.
l1, l2, l3 = [list(t) for t in tuple_list]

print(l1)
print(l2)
print(l3)