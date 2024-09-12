from pack import *

menu = """
        1.Prime Number
        2.Right Angle Pattern
        3.Left Angle Pattern
        4.Triangle
        5.Exit
    """ 
while True:
    print(menu)
    
    ch = int(input("Enter Your Choice : "))
    
    if ch == 1:
        n = int(input("Enter a Number : "))
        prime(n)
        
    elif ch == 2:
        right()
        
    elif ch == 3:
        left()
        
    elif ch == 4:
        triangle()
        
    elif ch == 5:
        print("Good Bye.")
        break
    
    else:
        print("XXX Invalid Choice....!!!!")
        print("Please Enter the Right Choice From Menu....")