a = int(input("Enter a Number 1 : "))
b = int(input("Enter a Number 2 : "))
c = int(input("Enter a Number 3 : "))

# nested if....else
if a>b:
    if a>c:
        print(f"{a} is Gretest Number.")
    else:
        print(f"{c} is Gretest Number.")

else:
    if b>c:
        print(f"{b} is Gretest Number.")
    else:
        print(f"{c} is Gretest Number.")
        
# ladder if......else
print("Even Odd")
z = int(input("Enter a Number : "))

if z==0:
    print(f"{z} is Zero")
elif z%2==0:
    print(f"{z} is Even number.")
else:
    print(f"{z} is Odd number.")