# Find duplicate values from list without using bulit in

l = [1,2,3,4,1,2]
l1 = []

for i in range(len(l)):
    if l[i] not in l1:
       for j in range(i+1,len(l)):
           if l[i] == l[j]: 
               l1.append(l[i])
        
        
 
print(l1)