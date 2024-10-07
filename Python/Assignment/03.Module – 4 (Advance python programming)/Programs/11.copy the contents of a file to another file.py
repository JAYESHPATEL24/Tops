# Write a Python program to copy the contents of a file to another file.

    # open two files one in read mode and  another in write mode
with open("Hearme.txt", "r") as sfile, open("Goal.txt","w") as file:
        # copy the contents of file to another file
    for i in sfile:
        file.write(i)
    
    print("Copy Successfully.")