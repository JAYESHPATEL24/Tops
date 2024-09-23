# Write a Python function that takes a list and returns a new list with unique elements of the first list.  

    # function for create list from entered list.
def unique_list(l):
    ul = []
    for i in l:
        if i not in ul:
            ul.append(i)
    return ul
    
l = []

    # user input for length of list.
n = int(input("Enter a length list : "))

    # list elements from user.
for i in range(n):
    a = input("Enter a Element : ")
    l.append(a)

    # print entered list and unique list.
print(f"Original List : {l}")
print(f"Unique list : {unique_list(l)}")