# Write a Python program to print all unique values in a dictionary. 

    # Dictionary
d = {'a': 200, 'b': 100, 'c': 100, 'd': 200, 'e': 300}

ul = []

    # store unique Values in ul.
for i in d.values():
    if i not in ul:
        ul.append(i)
    
print(ul)