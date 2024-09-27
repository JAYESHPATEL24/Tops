# Write a Python program to read a random line from a file. 

import random


    # open the file in read mode
file  = open('C:\Users\jayes\OneDrive\Documents\MY CUTIPIE.txt', 'r')
    # Read all line into a List
lines = file.readlines()
    # Choose a random line from the list.
random_line = random.choice(lines) # strip my leading/trailing whitespace

print("Random line  : ")
print(random_line.strip())
