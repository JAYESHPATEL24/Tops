# Write a Python program to read a file line by line store it into a variable.

    # open a file in read mode.
with open("hearme.txt","r") as file:
    a = file.read()
    
print(a)