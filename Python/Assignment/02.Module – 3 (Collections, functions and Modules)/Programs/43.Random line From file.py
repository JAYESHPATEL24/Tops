# Write a Python program to read a random line from a file. 

import random

file_name = 'random.txt'

with open(file_name, 'r+') as file:
    lines = file.readlines()
    random_line = random.choice(lines).strip()

print(random_line)



