# Write a Python program to check whether an element exists within a tuple. 


t = (1, "Tops", 4.5, 8, 9, "beautiful", "see", 7, 6,True)

        # Get the element to check from the user
e = input("Enter Element for Check: ")

        # Convert the input to the appropriate type
if e.isdigit():
    e = int(e)
elif e.replace('.', '', 1).isdigit() and e.count('.') < 2:
    e = float(e)
elif e.lower() == "true":
    e = True
elif e.lower() == "false":
    e = False

        # Check if the element exists in the tuple
if e in t:
    print(f"{e} is available in the tuple.")
else:
    print(f"{e} is not available in the tuple.")
