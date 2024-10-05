# Write a Python program to count the number of lines in a text file. 

line_count = 0

with open("Hearme.txt", 'r') as file:
    for line in file:
        line_count += 1

print(f"Number of lines in the file: {line_count}")