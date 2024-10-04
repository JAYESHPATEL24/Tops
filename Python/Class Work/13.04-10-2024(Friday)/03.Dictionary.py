# d ={1,2,3} d1 = {6,7,8} make d as key and d1 as value

d = [1,2,3]
d1 = [6,7,8]

dic = {}

for i in range(len(d)):
    dic[d[i]] = d1[i]
    
print(f"Dictionary : {dic}")