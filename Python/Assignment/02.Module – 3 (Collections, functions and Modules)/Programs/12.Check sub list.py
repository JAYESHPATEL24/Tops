# Write a Python program to check whether a list contains a sub list. 

    # Initialize the main list and sublist
l = []
sl = []

    # Get the length of the main list from the user
n1 = int(input("Enter the length of main list : "))

    # Get elements for the main list
for i in range(n1):
    e1 = input("Enter an element: ")
    l.append(e1)
    
    # Get the length of the sublist from the user
n2 = int(input("Enter the length of sublist : "))

    # Get elements for the sublist
for i in range(n2):
    e2 = input("Enter an element: ")
    sl.append(e2)

    # Check if the sublist exists in the main list
found = False
for i in range(len(l) - len(sl) + 1):
    if l[i:i + len(sl)] == sl:
        found = True
        break

    # Print the result.
if found:
    print("The main list contains the sublist.")
else:
    print("The main list does not contain the sublist.")

