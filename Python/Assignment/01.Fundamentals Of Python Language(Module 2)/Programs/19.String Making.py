# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
# If the string length is less than 2, return instead of the empty string.  

s = input("Enter a string: ")

    # Check if the length of the string is less than 2
if len(s) < 2:
        # If the string length is less than 2, return a messsage
    print("String is Short.")
    
else:
        # Create a new string with the first 2 and last 2 characters
    print(f"The new string is: {s[:2] + s[-2:]}")
