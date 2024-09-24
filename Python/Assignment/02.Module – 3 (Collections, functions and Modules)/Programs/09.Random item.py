# Write a Python program to select an item randomly from a list. 

import random

    # enter length of list.
n = int(input("Enter a length list : "))

l = []

    # enter elements of list
for i in range(n):
    a = input("Enter a element : ")
    l.append(a)


print(f"Entered list : {l}")
    # Select a random item from the list
random_item = random.choice(l)

print("Randomly selected item:", random_item)
