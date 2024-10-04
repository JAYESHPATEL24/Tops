from Bank_Module import *

menu = """
        WELCOME TO PYTHON BANK MANAGEMENT SYSTEM
        
        SELECT YOUR ROLE
        
        1)  BANKER
        2)  CUSTOMER
        
        3)  EXIT
        
        """
        
while True:
    
    print(menu)
    
    role = int(input("Enter your Role : "))
    
    if role == 1:
        banker()
    
    elif role == 2:
        customer()
        
    elif role == 3:
        print("Good BYE !!!")
        break
    
    else:
        print("XXX INVALID CHOICE.....!!")