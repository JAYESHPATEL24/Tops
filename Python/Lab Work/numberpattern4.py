# 1 2 3 4 5
# 2 3 4 5 1
# 3 4 5 1 2
# 4 5 1 2 3
# 5 1 2 3 4

n = int(input("Enter a Number : "))

for i in range(1,n+1):
    for j in range(1,n+1):
        k = (j + i - 1 ) % n
        if k == 0:
            k = n
        print(k,end=" ")
    print()
    
    