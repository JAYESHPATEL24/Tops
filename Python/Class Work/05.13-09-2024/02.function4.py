def division(a,b): # function with parameter and with return type
    return a/b

def factorial(n): # function with parameter and with return type
    
    fact = 1
    
    for i in range(1,n+1):
        fact *= i
    return fact

def cube(x): # function with parameter and with return type
    return x*x*x

x = int(input("Enter a number : "))
y = int(input("Enter a Number : "))

print(f"Division : {division(x,y)} \U0001F607")

z = int(input("Enter a number : "))
print(f"Factorial : {factorial(z)} \U0001F60A")

j = int(input("Enter a number : "))
print(f"Cube : {cube(j)} \U0001F4B8")