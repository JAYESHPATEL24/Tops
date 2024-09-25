# Write a Python program to find the second smallest number in a list. 

l = []
ul = []
l1 = []
    # enter length of list.
n = int(input("Enter length of list : "))

    # enter elements of list
for i in range(n):
    e = int(input("Enter a Element : "))
    l.append(e)

print(f"Entered List : {l} ")
    
    # Ascending order
for i in range(n):
    for j in range(i+1,n):
        if l[i]>l[j]:
            l[i],l[j] = l[j],l[i]
        l1.append(l[i])

    #remove Duplicate numbers.
for i in l1:
    if i not in ul:
        ul.append(i)

print(f"Second smallest Number of List : {ul[1]}")