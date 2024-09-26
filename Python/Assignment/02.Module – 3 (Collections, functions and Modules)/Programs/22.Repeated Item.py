# Write a Python program to find the repeated items of a tuple.  

    # Define a tuple
t = (1, "Tops", 4.5, 8, 9, "beautiful", "see", 7, 6, 1, "Tops", 4.5)

    # Create an empty dictionary to store the count of each element
element_count = {}

    # count the occurrences of each element
for i in t:
    if i in element_count:
        element_count[i] += 1
    else:
        element_count[i] = 1

    # Find the repeated items
repeat = [i for i, count in element_count.items() if count > 1]

print(f"Tuple : {t}")
print(f"Repeated items in the tuple : {repeat} ")
