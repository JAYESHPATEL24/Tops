# Write a Python program to remove duplicates from a list.  

    # User input for list length
n = int(input("Enter a length of list: "))

l = []

    # User inputs for list
for i in range(n):
    a = input("Enter an element: ")
    l.append(a)

print(f"Original list : {l} ")
    # Remove duplicates from the original list
i = 0
while i < len(l):
    if l.count(l[i]) > 1:
        l.remove(l[i])
    else:
        i += 1
        
    # print list after removing duplicates elements. 
print(f"List after removing duplicates: {l}")


