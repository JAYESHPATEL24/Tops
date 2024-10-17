d1 = {'a' : 100, 'b':200, 'c':300}
d2 = {'a' : 300, 'b':200, 'd':400}

d3 = {}
for i in d1.keys():
    for j in d2.keys():
            # if both dictionaries have same key than add its values and insert it into d3 dictionary.
        if i == j: 
            d3[i] = d1[i] + d2[i]
            # if both dictionaries does not have same value than insert its value with its key in d3.
        else:
            d3[j] = d2[j]   # i loop is for d1 dictionary so store that key value pair as it is.
            d3[i] = d1[i]   # j loop is for d2 dictionary so store that key value pair as it is.
            
            
print(d3)