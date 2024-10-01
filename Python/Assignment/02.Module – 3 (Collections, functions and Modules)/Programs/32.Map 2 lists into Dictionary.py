# Write a Python program to map two lists into a dictionary 

    # two Lists
l1 = [1, 2, 3, 4]
l2 = ["Hello", 6.8, 8, None, 5, "Hi"]

    # initilize Dictionary
d = {}

    # convert two lists into a Dictionary
for i in range(len(l1)):
    d[l1[i]] = l2[i]
    
print(d)