# Write a Python program to append text to a file and display the text.


    # Open the file in append and read mode
with open("hearme.txt", "a+") as file:
        # Move the file pointer to the beginning of the file before reading
    file.seek(0)
    print("Befor Appending : ")
    print(file.read())
    
        # Append the new text
    file.write( "\nDon't let failure defeat you. Let it motivate you." + "\n")

    print("\nAfter appending:")
        # Move the file pointer to the beginning of the file again before reading
    file.seek(0)
    print(file.read())