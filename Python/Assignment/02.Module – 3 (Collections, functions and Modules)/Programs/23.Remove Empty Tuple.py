# Write a Python program to remove an empty tuple(s) from a list of tuples. 

    # tuple Creation
l = [(1,), (), ("Jay",4,5.5), (), ("Ganesha", 5, 8), (4.5, 5.5, 56), ()]

l1 = []
    # remove empty tuples from the List.
for i in l:
    if i:
       l1.append(i)
     
print(f"Original List : {l}")
print(f"After Remove an empty tuples list : {l1}") 