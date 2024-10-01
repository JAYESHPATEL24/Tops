# Write a Python program to find the highest 3 values in a dictionary.

    # Dictionary
d = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 900}

    # Create an empty list to hold the sorted items
sorted_items = []

    # ASCENDING Order
for key, value in d.items():
    # Insert the item in the correct position in the sorted_items list
    inserted = False
    for i in range(len(sorted_items)):
        if value < sorted_items[i][1]:  # Compare by value
            sorted_items.insert(i, (key, value))
            inserted = True
            break
    if not inserted:  # If it wasn't inserted, append it at the end
        sorted_items.append((key, value))

    # Convert the sorted items back into a dictionary
sd = dict(sorted_items)

print("highest 3 values in a dictionary : ", list(sd.items())[-3:])
