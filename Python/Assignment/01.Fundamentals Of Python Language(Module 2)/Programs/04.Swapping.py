# Write python program that swap two number with temp variable and without temp variable.

print("Swapping with 3rd Variable : ")
print()
print("Enter two numbers : ")
x = int(input("X : ")) 
y = int(input("Y : "))

    # logic for swap two number using 3rd variable.
temp = x
x = y
y = temp

print(f"After Swapping : X = {x}  Y = {y}")

print()
print("Swapping Without 3rd Variable : ") 
print()
print("Enter two numbers : ")
a = int(input("A : ")) 
b = int(input("B : "))

    # logic for swap two number without using 3rd variable.
a,b = b,a

print(f"After Swapping : A = {a}  B = {b}")