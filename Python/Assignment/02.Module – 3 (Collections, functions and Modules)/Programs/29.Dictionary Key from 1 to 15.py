# Write a Python script to print a dictionary where the keys are numbers between 1 and 15. 

    # Create an empty dictionary
d = {}

    # Iterate through numbers from 1 to 15.
for i in range(1, 16):
    d[i] = i * i

print(d)
