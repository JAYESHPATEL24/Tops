# Write a Python program to read a file line by line and store it into a list.


lines = []
    # open a file in read mode.
with open("hearme.txt", "r") as file:
    for line in file:
        lines.append(line.strip())  # strip() removes the newline characters

print(lines)
