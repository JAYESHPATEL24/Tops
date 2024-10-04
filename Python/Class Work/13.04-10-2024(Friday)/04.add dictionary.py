# d1 = {1 : 'a', 2:'b'}  d2 = {1 : 'c' 2: 'd'} add values d = {1: 'ac', 2:'bd'}

d1 = { 1 : 'a', 2 : 'b'}
d2 = {1 : 'c', 2 : 'd'}

d = {}

for i in d1.keys():
    for j in d2.keys():
        if i == j:
            d[i] = d1[i] + d2[j]

print(d)