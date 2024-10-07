# Write a Python program to read a file line by line store it into a variable.

    # initilize a variable
a = "" 
    # open a file in read mode.
with open("hearme.txt","r") as file:
        # read a file line by line and store it into a variable
    for i in file:
        a += i
        
print(a)