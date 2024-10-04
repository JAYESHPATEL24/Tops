# Find duplicate values from list without using bulit in

l = [1,2,3,4,1,2]
l1 = []
l2 = []
for i in l:
    if i in l1:
       l2.append(i)
       
    else:
        l1.append(i)
        
        
 
print(l2)