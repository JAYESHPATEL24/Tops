# Function without parameter and with reurn type

def factorial():
    n = int(input("Enter a Number : "))
    
    fact = 1
    
    for i in range(1,n+1):
        fact *= i
    return fact
    
def add():
    a = int(input("Enter a Number : "))
    b = int(input("Enter a Number : "))
    
    return a+b

def cube():
    a = int(input("Enter a Number : "))
    return a*a*a

print(f"Factorial : {factorial()}")
print(f"Addition : {add()}")
print(f"Cube : {cube()}")