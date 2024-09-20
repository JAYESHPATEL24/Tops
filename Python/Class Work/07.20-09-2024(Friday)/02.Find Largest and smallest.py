n = int(input("Enter Length of list : "))
l = []

for i in range(n):
    o = int(input("Enter a element : "))
    l.append(o)
    
print(l)

l1 = []

for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            l[i],l[j] = l[j],l[i]
    print(l[i])
    l1.append(l[i])
    
print(f"Smallest number : {l[0]}")
print(f"Gretest number : {l[-1]}")
print(f"second largest number : {l[-2]}")
    
