# Write a Python program to get the Fibonacci series of given range.  

n = int(input("Enter any Number : "))

fab1 = 0
fab2 = 1

print("Fibonacci Series : ")
print(fab1)
print(fab2)

for i in range(1,n-1):
    fab = fab1 + fab2 
    print(fab)
    fab2,fab1 = fab,fab2
    