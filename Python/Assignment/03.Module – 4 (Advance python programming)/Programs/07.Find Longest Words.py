# Write a python program to find the longest words. 

with open("Hearme.txt", "r") as file:
    words = file.read().split()
    longest_words = sorted(words, key=len, reverse=True)
    max_length = len(longest_words[0])
    result = [word for word in longest_words if len(word) == max_length]

print("The longest words are:", result)
