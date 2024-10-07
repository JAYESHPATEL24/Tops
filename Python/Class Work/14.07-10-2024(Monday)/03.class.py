
class Alpha:
    def factorial(self):
        fact = 1
        print("Factorial Number : ")
        n = int(input("Enter a Number : "))
        
        for i in range(1,n+1):
            fact *= i
            
        print(f"Factorial of number {n} : {fact}")
        
    def addition(self):
        print("Addition")
        a = int(input("Enter a number : "))
        b = int(input("Enter a number : "))
        
        print(f"Addition = {a+b}")
        
        
class Beta:
    def rightangle(self):
        print("Right Angle Pattern ")
        n = int(input("Enter a Number : "))
        for i in range(1,n+1):
            print("*"*i)
            
    def substraction(self):
        print("Subtraction")
        a = int(input("Enter a number : "))
        b = int(input("Enter a number : "))
        
        print(f"Subtraction = {a-b}")
        
        
class Gaama:
    def Fibonacci(self):
        print("Fibbonaci Series ")
        n = int(input("Enter a Number : "))
        n1 = 0
        n2 = 1
        
        for i in range(n):
            print(n1)
            n3 = n1 + n2
            
            n1,n2 = n2,n3
            
            
    def divison(self):
        print("Division")
        a = int(input("Enter a number : "))
        b = int(input("Enter a number : "))
        
        print(f"Division = {a/b}")
        
        
class Delta:
    def LeftAngle(self):
        print("Left Angle Pattern ")
        n = int(input("Enter a Number : "))
        for i in range(1,n+1):
            print(" "*(n-i),"*"*i)
        
    
    def multiplication(self):
        print("Multiplication")
        a = int(input("Enter a number : "))
        b = int(input("Enter a number : "))
        
        print(f"Multiplication = {a*b}")
        
        
        
objalpha = Alpha()
objbeta = Beta()
objgamma = Gaama()
objdelta = Delta()


objalpha.addition()
objalpha.factorial()

objbeta.rightangle()
objbeta.substraction()

objgamma.divison()
objgamma.Fibonacci()

objdelta.LeftAngle()
objdelta.multiplication()