print("Hello", end=" ")
print("Welcome")

print()
print("Maths Operations : ")

# input() is use for a take input from the user.
# int is type casting.
# by default input() takes input as String.
a = int(input("Enter a Number 1 : "))
b = int(input("Enter a Number 2 : "))

print("A : ",a)
print("B : ",b)

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

