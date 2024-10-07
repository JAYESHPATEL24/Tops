# Write a Python program to count the frequency of words in a file.

    # Dictionary
word_count = {}
    # open a file in read mode.
with open("Hearme.txt", "r") as file:
        # store all words in to a list
    words = file.read().split()

    # count the frequency of words.
for i in words:
    if i in word_count:
        word_count[i] += 1
    else:
        word_count[i] = 1

print("Word frequencies:")
for word, count in word_count.items():
    print(f"{word}: {count}")
