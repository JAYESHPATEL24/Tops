# Write a Python program to count the frequency of words in a file.


word_count = {}

with open("Hearme.txt", "r") as file:
    content = file.read().lower()  # Convert to lowercase to count words case-insensitively
    words = content.split()

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word frequencies:")
for word, count in word_count.items():
    print(f"{word}: {count}")
