# Write a Python function that takes a list of words and returns the length of the longest one.


def longest_word_length(words):
    
        # variable to store the length of the longest word
    l = 0

    for i in words:
            # Update max_length if the current word is longer than previous word
        if len(i) > l:
            l = len(i)
    return l


        #user input
words = input("Enter a list of words separated by spaces: ").split()
        #function call
print(f"ther longest length of word from words is {longest_word_length(words)}.")






