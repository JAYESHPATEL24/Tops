# Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user.

n = int(input("Enter a Number : "))

if n==0:            # if Number is Zero.
    print("Number is Zero.")

elif n%2==0:        # if Number is Even Number.
    print(f"{n} is Even Number.")
    
else:               # if number is odd Number.
    print(f"{n} is Odd Number.")  