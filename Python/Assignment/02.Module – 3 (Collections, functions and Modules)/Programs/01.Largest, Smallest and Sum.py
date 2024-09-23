# Write a Python function to get the largest number, smallest num and sum of all from a list. 

        # create a function for find large & small number and sum of list.
def large_small_sum(l): 
    
    l1 = []
    sum = 0
    
        # convert list in ascending order.
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i]>l[j]:
                l[i],l[j] = l[j],l[i]
        l1.append(l[i])
    
        # count sum of all number in the list
    for i in l1:
        sum += i 
        
    
    print(f"Largest number : {l[-1]}")
    print(f"Smallest number : {l[0]}")
    print(f"Sum of all numbers from the list : {sum}")



    # user input for list length.
n = int(input("Enter Length of list : "))

l = []

    # add user inputs in list.
for i in range(n):
    o = int(input("Enter a element : "))
    l.append(o)
    
    # function call
large_small_sum(l)
    
    