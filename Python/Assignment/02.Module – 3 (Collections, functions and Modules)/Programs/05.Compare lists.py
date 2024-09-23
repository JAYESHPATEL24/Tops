# Write a Python function that takes two lists and returns true if they have at least one common member.  

def find_common(l1,l2):
    for i in l1:
        if i in l2:
            return True
    return False

l1 = []
l2 = []

n1 = (int(input("Enter a length of list 1 : ")))

for i in range(n1):
    a = input("Enter a Element : ")
    l1.append(a)
    

n2 = (int(input("Enter a length of list 1 : ")))

for i in range(n2):
    a = input("Enter a Element : ")
    l2.append(a)
        
print(find_common(l1,l2))

