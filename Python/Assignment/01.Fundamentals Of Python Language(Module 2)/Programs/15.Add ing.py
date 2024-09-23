# Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
# If the given string already ends with 'ing' then add 'ly' instead 
# if the string length of the given string is less than 3, leave it unchanged. 

s = input("Enter a String : ")

ls = 0

        # count length of string.
for i in s :
    ls += 1

    # Check the length of the string
if ls >= 3:
    # Check if the string ends with 'ing'
    if s.endswith('ing'):
             # Add 'ly' if the string ends with 'ing'
        s1 = s + 'ly'
    else:
        # Add 'ing' if the string does not end with 'ing'
        s1 = s + 'ing'
else:
    # Leave the string unchanged if its length is less than 3
    s1 = s

# Print the resulting string
print(f"The resulting string is: {s1}")
