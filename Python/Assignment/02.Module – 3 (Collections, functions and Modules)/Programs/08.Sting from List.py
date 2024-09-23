# Write a Python program to convert a list of characters into a string.

l = []

    # user input for length of list.
n = int(input("Enter a length character list : "))

    # list elements from user.
for i in range(n):
    a = input("Enter a character Element : ")
    l.append(a)
    
    # create string from list.
s = "" 
for i in l:
    s += i

print(f"Entered character list : {l} ")
print(f"String From list : {s} ")