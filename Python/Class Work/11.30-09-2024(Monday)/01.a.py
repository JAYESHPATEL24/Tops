try:
    n = int(input("Enter a Number : "))
    n1 = int(input("Enter a Number : "))
    
    print(f"Addition = {n+n1}")
    print(f"Division = {n/n1}")
    
except ZeroDivisionError as e:
    print(e)
    
except ValueError as e:
    print(e)
    
else:
    print("Try and else executed!!!!")
    
finally:
    print("Thank you!!!")
    
    
    
    
try:
    l = [1,2,3,4,5,6,7]
    
    n = int(input("Enter a Number : "))
    
    print(f"Value is : {l[n]}")
    
except IndexError as e:
    print(e)
    
    
try:
    n = int(input("Enter a Number : "))
    n1 = int(input("Enter a Number : "))
    
    print(f"Addition = {n+n1}")
    print(f"Division = {n/n1}")
    
except:
    print("Invalid Input !!!!!")