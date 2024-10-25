# Pascal's Triangle

#     1
#    1 1 
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1

n = int(input("Enter a Number: "))
        
for i in range(n):
    for k in range(n-i):
        print(" ",end = "")
    c = 1
    for j in range(i+1):
        print(c,end = " ")
        c = c * (i-j) // (j+1)
    print()    