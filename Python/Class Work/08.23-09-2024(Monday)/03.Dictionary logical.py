# print 1 to 30 with  number as key and squre as value

d  = {}

for i in range(1,31):
    d[i] = i*i
    
print(d)


print()

# count words in string 
s = input("Enter a Name : ")
d1 = {}

# DishaD
# D : 1

for i in  s : 
    if i in d1:
        d1[i]+=1
    else:
        d1[i]=1
        
print(d1)


print()

# l as key and l1 as value
l = [1, 2, 3]
l1 = [4, 5, 6]

d2 = {}

a = 0
for i in l:
    a+=1
    
for i in range(a):
    d2[l[i]] = l1[i]

print(l)
print(l1)
print(d2)
