from Bank_Module import *
import os

menu = """
        WELCOME TO PYTHON BANK MANAGEMENT SYSTEM
        
        SELECT YOUR ROLE
        
        1)  BANKER
        2)  CUSTOMER
        
        3)  EXIT
        
        """
        
while True:
    
    role = int(input("Enter your Role : "))
    
    if role == 1:
        print("")