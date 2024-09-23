# Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30.

l = []
    # create a list of first and last 5 elements where the values are square of numbers between 1 and 30.
for i in range(1,31):
    if i<6 or i>25:
        l.append(i*i)
    
    # print list
print(l)