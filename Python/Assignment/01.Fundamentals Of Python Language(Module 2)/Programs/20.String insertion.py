# Write a Python function to insert a string in the middle of a string. 

def insert_String(main_s,s):
                # Calculate the middle index of the main string
        middle = len(main_s) // 2


                # Insert the string at the middle index
        return main_s[:middle] + s + main_s[middle:]
        
        #main string
main_string = input("Enter the main string: ")

        # take user input to enter the string to insert
str = input("Enter the string to insert: ")
print(f"The new string is: {insert_String(main_string,str)}")
