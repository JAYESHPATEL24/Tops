#  Write a Python program to test whether a passed letter is a vowel or not.  

vowels = "aeiouAEIOU"       # Define a string containing all vowels (both lowercase and uppercase)

letter = input("Enter any letter : ")

if letter in vowels:        # Check if the entered letter is in the string of vowels or not
    print(f"{letter} is Vowel.")
else:
    print(f"{letter} is not Vowel.")