# Write a Python program to count the occurrences of each word in a given sentence   

"""
s = input("Enter a string: ")

words_count = {}

for char in s:
                 # if space occcurs in string than skip the space.
    if char == ' ':     
        continue
    
                 # If the character is already in the dictionary, increment its count
    elif char in words_count:
        words_count[char] += 1
        
                 # If the character is not in the dictionary, add it with a count of 1
    else:
        words_count[char] = 1

                    # Print the character frequencies
print("Character frequencies in the string are:")
for word, count in words_count.items():
    print(f"{word}: {count}")

"""

s = input("Enter a string: ")

for i in range(65, 123):
    count = 0
    for char in s:
        if char == chr(i):
            count += 1
    if count != 0:
        print(f"{chr(i)} : {count}")
