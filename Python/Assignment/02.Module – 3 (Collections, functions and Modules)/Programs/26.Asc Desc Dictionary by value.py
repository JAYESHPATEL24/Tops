# Write a Python script to sort (ascending and descending) a dictionary by value.  

    # dictionary
d = {'apple': 5, 'banana': 2, 'orange': 8, 'grape': 1}

    # Converting dictionary items to a list.
items = list(d.items())

    # Sorting the list of tuples by value in ascending order.
for i in range(len(items)):
    for j in range(i + 1, len(items)):
        if items[i][1] > items[j][1]:
            items[i], items[j] = items[j], items[i]

    # Converting the sorted list back to a dictionary.
asc = {key: value for key, value in items}

print("Ascending Order:", asc)

    # Sorting the list of tuples by value in descending order.
for i in range(len(items)):
    for j in range(i + 1, len(items)):
        if items[i][1] < items[j][1]:
            items[i], items[j] = items[j], items[i]

    # Converting the sorted list back to a dictionary.
desc = {key: value for key, value in items}

print("Descending Order:", desc)