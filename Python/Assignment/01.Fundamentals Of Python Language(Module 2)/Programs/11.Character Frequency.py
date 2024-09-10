# Write a Python program to count the number of characters (character frequency) in a string  


s = input("Enter a string: ")

count = 0

for i in s:
                # if space occcurs in string than skip the space.
    if i == ' ':     
        continue

                # if character occurs than increse the count by 1.
    else:
        count += 1
        
                    # Print the character frequency
print(f"Character frequency in the string is {count}.")
