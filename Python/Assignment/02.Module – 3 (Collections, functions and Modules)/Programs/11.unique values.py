# Write a Python program to get unique values from a list .


l = []

    # Get the length of the list from the user
n = int(input("Enter the length of the list: "))

    # Get elements from the user and add them to the list
for i in range(n):
    e = input("Enter an element: ")
    l.append(e)
    
print(f"Entered List: {l}")

    # print unique elements
for i in range(n):
    is_unique = True
    for j in range(i):
        if l[i] == l[j]:
            is_unique = False
            break
    if is_unique:
        print(l[i])

