# Write a Python program to remove duplicates from a list.  

n = int(input("Enter a length of list: "))

l = []

for i in range(n):
    a = input("Enter an element: ")
    l.append(a)
    
ul = []

for i in l:
    if i not in ul:
        ul.append(i)

print(f"Original list : {l} ")
print(f"List after removing duplicates : {ul}")


