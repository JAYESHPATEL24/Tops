# Write a Python program to get the Factorial number of given number. 

n = int(input("Enter any Number : "))

fact = 1 
for i in range(1,n+1): # loop for Find Factorial of Number.
    fact *= i
    
print(f"factorial of {n} is {fact}.")
