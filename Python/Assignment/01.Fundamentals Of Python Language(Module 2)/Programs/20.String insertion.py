# Write a Python function to insert a string in the middle of a string. 

        #main string
main_s = input("Enter the main string: ")

        # take user input to enter the string to insert
s = input("Enter the string to insert: ")

        # Calculate the middle index of the main string
middle = len(main_s) // 2


        # Insert the string at the middle index
result = main_s[:middle] + s + main_s[middle:]

        # Print the result
print(f"The new string is: {result}")
