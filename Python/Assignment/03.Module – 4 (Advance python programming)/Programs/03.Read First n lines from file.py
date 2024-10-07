# Write a Python program to read first n lines of a file. 

    # Get the user input for number of lines.
n = int(input("Enter the number of lines to read : "))
print()
    # Open the file in read mode
with open("hearme.txt", "r") as file:
        # Loop to read and print the first n lines
    for i in range(n):
        print(file.readline())
