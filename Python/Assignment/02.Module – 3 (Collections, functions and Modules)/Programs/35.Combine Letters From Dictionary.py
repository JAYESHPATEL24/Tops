# Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.

"""  
Sample data: {'1': ['a','b'], '2': ['c','d']}  
Expected Output:  
ac ad bc bd 
"""

    # data
data = {'1': ['a', 'b'], '2': ['c', 'd'],'3':['e','f']}

    # Extract the lists of letters
l1 = data['1']
l2 = data['2']
l3 = data['3']

    # Generate and display combinations
for i in l1:
    for j in l2:
        for k in l3:
            print(i+j+k)
