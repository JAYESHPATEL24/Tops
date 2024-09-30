# Write a Python program to count the occurrences of each word in a given sentence   


s = input("Enter a string: ")

words = s.split()

words_count = {}

for i in words:
                 # if space occcurs in string than skip the space.
    if i == ' ':     
        continue
    
                 # If the word is already in the dictionary, increment its count
    elif i in words_count:
        words_count[i] += 1
        
                 # If the word is not in the dictionary, add it with a count of 1
    else:
        words_count[i] = 1

                    # Print the word frequencies
print("word frequencies in the string are:")
for word, count in words_count.items():
    print(f"{word}: {count}")