# Write a Python function to reverses a string if its length is a multiple of 4.  

s = input("Enter a string: ")

        # Check if the length of the string is a multiple of 4
if len(s) % 4 == 0:
            # Reverse the string
    rs = s[::-1]
else:
        # If length is not multiply by 4, keep the string as it is
    rs = s

    # Print the rs
print(f"The result is: {rs}")
