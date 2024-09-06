print("Hello", end=" ")
print("Welcome")

print()
print("Maths Operations : ")
a = int(input("Enter a Number 1 : "))
b = int(input("Enter a Number 2 : "))

print(f"Addition : {a+b}")
print(f"Substraction : {a-b}")
print(f"Multiplication : {a*b}")
print(f"Division : {a/b}")

print()
print("Swapping numbers : ")
x = int(input("Enter a Number 1 : "))
y= int(input("Enter a Number 2 : "))

x,y = y,x 

print(f"After Swapping :  X : {x} Y : {y} ")

print()

print("Even Odd")
z = int(input("Enter a Number : "))

if z==0:
    print(f"{z} is Zero")
elif z%2==0:
    print(f"{z} is Even number.")
else:
    print(f"{z} is Odd number.")