# Write a Python program to count the number of lines in a text file. 

count = 0
    # open a file in read mode.
with open("Hearme.txt", 'r') as file:
        # count the number of lines in a text file
    for i in file:
        count += 1

print(f"Number of lines in the file: {count}")