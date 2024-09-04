for i in range(1,6):
    for k in range(1,6-i):
        print(" ",end="")
    for j in range(1,i+1):
        print(chr(3),end="")
    print()



for i in range(5):
    for k in range(i,5):
        print(" ",end="")
    for j in range(i+1):
        print(chr(1),end="")
    print()
    

for i in range(1,6):
    print(" "*(6-i),"*"*i)