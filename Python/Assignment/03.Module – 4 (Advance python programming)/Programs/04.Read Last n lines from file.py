# Write a Python program to read last n lines of a file.


n = int(input("Enter the number of lines to read from the end : "))
    # open a file in read mode.
with open("hearme.txt", "r") as file:
    lines = file.readlines()
    last_n_lines = lines[-n:]
        # Loop to read and print the first n lines
    for i in last_n_lines:
        print(i,end="")
