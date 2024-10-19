import time

def prime(n):   # function with parameter without return type
    c = 0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c == 2:
        print(f"{n} is a Prime Number.")
    else:
        print(f"{n} is not a Prime Number.")
        

def right():   # function without parameter without return type
    for i in range(5):
        for j in range(i+1):
            time.sleep(0.5)
            print("\U0001F4B8",end="")
        print()
        
def left():     # function without parameter without return type
    for i in range(5):
        for j in range(1,5-i):
            print("  ",end="")
        for k in range(i+1):
            time.sleep(0.2)
            print("\U0001F607",end="")
        print()
        
def triangle():    # function without parameter without return type
    for i in range(5):
        for j in range(1,5-i):
            print(" ",end="")
        for k in range(i+1):
            time.sleep(0.2)
            print("\U0001F488",end="")
        print()
              