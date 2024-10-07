# Write a python program to find the longest words. 

    # open a file in read mode.
with open("Hearme.txt", 'r') as file:

    words = file.read().split()
    
    longest_words = [] # initilize a list
    l = 0   # intilize max length
    
    for i in words:
        if len(i) > l:
            l = len(i)
            longest_words = [i]  # Start a new list with the new longest word
        elif len(i) == l:
            longest_words.append(i)  # Add to the list of longest words in case same length of already add word.

if len(longest_words) == 1:
    print("The longest word is : ", longest_words)
else:
    print("The longest words are : ", longest_words)
