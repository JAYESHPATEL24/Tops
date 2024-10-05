from Bank_Module import *

def banker():
    
    while True:
        
        bank_menu()
        
        print("-"*40)
        choice = int(input("Enter your choice: "))
        print("-"*40)
        
        if choice == 1:
            add_customer()
        elif choice == 2:
            view_customer()
        elif choice == 3:
            search_customer()
        elif choice == 4:
            view_all_customers()
        elif choice == 5:
            total_amounts_in_bank()
        elif choice == 6:
            print("Exiting the application.")
            break
        else:
            print("Invalid choice, please try again.")

def customer():
    while True:
        customer_menu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            withdraw_amount()
        elif choice == 2:
            deposit_amount()
        elif choice == 3:
            view_balance()
        elif choice == 4:
            print("Exiting the application.")
            break
        else:
            print("Invalid choice, please try again.")


menu = """
    WELCOME TO PYTHON BANK MANAGEMENT SYSTEM
    
    SELECT YOUR ROLE
    
    1)  BANKER
    2)  CUSTOMER
    
    3)  EXIT
    """
    
    
while True:
    
    print(menu)
    
    print("-"*40)
    role = int(input("Enter your Role : "))
    print("-"*40)
    
    if role == 1:
        banker()
    elif role == 2:
        customer()
    elif role == 3:
        print("Good BYE !!!")
        break
    else:
        print("XXX INVALID CHOICE.....!!")

