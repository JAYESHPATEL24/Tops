from ENote_Book_Module import *


    # Main loop to display the menu and handle user choices
while True:
    display_menu()
    print("-"*40)
    choice = input("Enter your choice : ")
    print("-"*40)
    
    if choice == "1":
        add_note()
        print("-"*40)
        
    elif choice == "2":
        view_notes()
        print("-"*40)
        
    elif choice == "3":
        print("Exiting the application. Goodbye!")
        print("-"*40)
        break
    else:
        print(" xxxxxx Invalid choice. Please try again.")
        print("-"*40)


