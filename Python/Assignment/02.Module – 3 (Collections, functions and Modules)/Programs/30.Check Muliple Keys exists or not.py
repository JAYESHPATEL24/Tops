# Write a Python program to check multiple keys exists in a dictionary.

    # Dictionary
d = {"name": "jay", "age": 24, "city": "Ahemdabad", "Language" : "Gujarati" }

    # List of keys to check
keys = ["name", "age", "country"]

    # Initialize a flag to track if all keys exist
flag = True

    # Check each key
for i in keys:
    if i not in d:
        flag = False
        break  # Exit the loop if a key is not found

    # The result
if flag:
    print("All keys exist.")
else:
    print("Not all keys exist.")
