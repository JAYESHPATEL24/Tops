# Write a Python function to get the largest number, smallest num and sum of all from a list. 

def large_small_sum(l):
    
    l1 = []
    sum = 0
    
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i]>l[j]:
                l[i],l[j] = l[j],l[i]
        l1.append(l[i])
    
    for i in l1:
        sum += i 
        
    print(f"Largest number : {l[-1]}")
    print(f"Smallest number : {l[0]}")
    print(f"Sum of all numbers from the list : {sum}")




n = int(input("Enter Length of list : "))
l = []

for i in range(n):
    o = int(input("Enter a element : "))
    l.append(o)
    
large_small_sum(l)
    
    