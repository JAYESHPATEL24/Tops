# Find duplicate values from list without using bulit in

l = [1,2,3,4,1,2]
l1 = []

for i in range(len(l)):
    k = 0
    for j in l:
        if j == l[i]:
            k+=1
    if k>1 and l[i] not in l1:
        l1.append(l[i])
       
print(l1) 

