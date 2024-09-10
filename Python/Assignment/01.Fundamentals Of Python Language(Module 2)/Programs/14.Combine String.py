#  Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

    #  input  two strings from the user.
s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

    # Check if both strings have at least two characters
if len(s1) < 2 or len(s2) < 2:
    print("Both strings must have at least two characters.")
else:
        # Swap the first two characters of each string
    new_s1 = s2[:2] + s1[2:]
    new_s2 = s1[:2] + s2[2:]

    # Combine the new strings with a space in between
    print(new_s1 + " " + new_s2)
