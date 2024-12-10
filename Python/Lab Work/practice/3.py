for i in range(10, 0, -1):
    for j in range(1,i+1):
        if j==i:
            print(i, end=" ")
        else:
            print("0",end=" ")
    print()  
