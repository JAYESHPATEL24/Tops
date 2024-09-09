#  Write a Python program to check if a number is positive, negative or zero.  

n = int(input("Enter Any Number : "))

if n==0:
    print("Number is Zero.")
elif n>0:
    print(f"{n} is Positive Number.")
else:
    print(f"{n} is Negative Number.")