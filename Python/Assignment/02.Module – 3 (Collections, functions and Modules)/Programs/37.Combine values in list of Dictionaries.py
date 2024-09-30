# Write a Python program to combine values in python list of dictionaries. 
"""
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':  
300}, o {'item': 'item1', 'amount': 750}]  
Expected Output: 
Counter ({'item1': 1150, 'item2': 300})  
"""

from collections import Counter

data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}, {'item': 'item2', 'amount': 1000}]

    # Initialize a Counter object
c = Counter()

    # Iterate through the list of dictionaries
for i in data:
    c[i['item']] += i['amount']

    # Print the combined values
print(c)
