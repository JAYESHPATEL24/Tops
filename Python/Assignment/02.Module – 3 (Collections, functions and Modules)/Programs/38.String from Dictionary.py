# Write a Python program to create a dictionary from a string.  
"""
Note: Track the count of the letters from the string.  
Sample string: 'w3resource'  
Expected output:  
{'3': 1,'s': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
"""  
    # get a String from user.
s = input("Enter a String : ")

d = {}

    # count the letters from string and store into dictionary.
for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
        
    # print Dictionary.
print(d)