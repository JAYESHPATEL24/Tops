# Write a Python script to check if a given key already exists in a dictionary.  

    # dictionary
my_dict = {'A': 67, 'B': 23, 'C': 45, 'D': 56, 'E': 12, 'F': 69, 'G' : 50}

    # get key from the user.
key = input("Enter a Key : ")

    # check given key already exists in a dictionary. 
if key in my_dict:
    print(f"Key {key} does exist in dictionary.")
else:
    print(f"Key {key} does not exist in dictionary.")