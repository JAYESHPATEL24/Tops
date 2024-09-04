n = int(input("Enter a Number : "))

fact = 1
for i in range(1,n+1):
    fact *= i

print(f"factorial of {n} is {fact}.")

print("Fabo Series : ")
m = int(input("Enter a Number : "))

fab1 = 0
fab2 = 1

print(fab1)
print(fab2)

for i in range(1,m-1):
    fab = fab1 + fab2
    print(fab)
    fab1,fab2 = fab2,fab
    
    