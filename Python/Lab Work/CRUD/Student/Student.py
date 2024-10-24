from Database import *

while True:
    
    Viewmenu()
    print("-"*46)
    choice = int(input("Enter your choice : "))
    print("-"*46)
    print()
    
    match choice:
        case 1:
            Insert()
        
        case 2:
            Update()
            
        case 3:
            Delete()
        
        case 4:
            View_Data()
            
        case 5:
            print("Thank You..!!!!")
            print()
            break
        
        case _:
            print("XXXXX INVALID CHOICE...!!!!!")