# Write a Python program to read a file line by line and store it into a list.

    # itializes an empty list
lines = []
    # open a file in read mode.
with open("hearme.txt", "r") as file:
        # read a file line by line and store it into a list
    for line in file:
        lines.append(line.strip())  # strip() removes the newline characters


print(lines)


