# Write a Python program to calculate the area of a trapezoid 
# Area = 1/2*(a+b)*h

    # get the parameters from the user.
a = float(input("Enter the length of the first base of a Trapezoid : "))
b = float(input("Enter the length of the second base of a Trapezoid : "))
h = float(input("Enter the height of a Trapezoid : "))

    # calculate area of a trapezoid
a = 0.5 * (a+b) * h

print(f"Area of Trapezoid : {a}")