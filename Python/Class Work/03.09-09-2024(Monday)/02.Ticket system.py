print()
print("**************** Lets Watch Movie ***********************")
total = 0
print()
    
while True:
    print()
    print("Please Choose one Option : ")
    print()
    print("--------------------------------------------")
    print()
    print("1.PVR")
    print("2.Rajhansh")
    print("3.Miraj")
    print("4.Multiplex")
    print()
    print("--------------------------------------------")
    print()
    ch = int(input("Enter your Choice : "))
    print()
    print("--------------------------------------------")
    print()
    
    count = 0
    if ch == 1:
        print(f"Welcome to PVR.......{chr(1)}{chr(1)}{chr(1)}")
        print()
        print("--------------------------------------------")
        print()
        print("please SELECT one option.....")
        print()
        print("----------|----------------------------------")
        print("1.Silver  | Rs.150")
        print("2.Gold    | Rs.200")
        print("3.premiem | Rs.250")
        ch1 = int(input("Enter Your Choice : "))
        if ch1 == 1:
            print("You choose Silver...")
            print("How many Tickets You wanna Buy ? ")
            n = int(input("Enter a number of Tickets : "))
            count = n*150
            print(f"Amount = {count}")
            
        elif ch1 == 2:
            print("You Choose Gold....")
            print("How many Tickets You wanna Buy ? ")
            n = int(input("Enter a number of Tickets : "))
            count = 5
            n*200
            print(f"Amount = {count}(with Gst)")
             
        elif ch1 == 3:
            print("You Choose Premium....")
            print("How many Tickets You wanna Buy ? ")
            n = int(input("Enter a number of Tickets : "))
            count = n*250
            print(f"Amount = {count}")

    elif ch == 2:
        print("Welcome to Rajhansh.......")
        print("please SELECT one option.....")
        print("1.Silver  Rs.120")
        print("2.Gold    Rs.180")
        print("3.premium Rs.200")
        ch1 = int(input("Enter Your Choice : "))
        if ch1 == 1:
            print("You choose Silver...")
            print("How many Tickets You wanna Buy ? ")
            n = int(input("Enter a number of Tickets : "))
            count = n*120
            print(f"Amount = {count}")
            
        elif ch1 == 2:
            print("You Choose Gold....")
            print("How many Tickets You wanna Buy ? ")
            n = int(input("Enter a number of Tickets : "))
            count = n*180
            print(f"Amount = {count}")
             
        elif ch1 == 3:
            print("You Choose Premium....")
            print("How many Tickets You wanna Buy ? ")
            n = int(input("Enter a number of Tickets : "))
            count = n*200
            print(f"Amount = {count}")

        
    elif ch == 3:
        print("Welcome to Miraj.....")
        print("please SELECT one option.....")
        print("1.Silver  Rs.100")
        print("2.Gold    Rs.150")
        print("3.premiem Rs.180")
        ch1 = int(input("Enter Your Choice : "))
        if ch1 == 1:
            print("You choose Silver...")
            print("How many Tickets You wanna Buy ? ")
            n = int(input("Enter a number of Tickets : "))
            count = n*100
            print(f"Amount = {count}")
            
        elif ch1 == 2:
            print("You Choose Gold....")
            print("How many Tickets You wanna Buy ? ")
            n = int(input("Enter a number of Tickets : "))
            count = n*150
            print(f"Amount = {count}")
             
        elif ch1 == 3:
            print("You Choose Premium....")
            print("How many Tickets You wanna Buy ? ")
            n = int(input("Enter a number of Tickets : "))
            count = n*180
            print(f"Amount = {count}")

    
    elif ch == 4:
        print("Welcome to Multiplex.....")
        print("please SELECT one option.....")
        print("1.Silver  Rs.130")
        print("2.Gold    Rs.210")
        print("3.premiem Rs.240")
        ch1 = int(input("Enter Your Choice : "))
        if ch1 == 1:
            print("You choose Silver...")
            print("How many Tickets You wanna Buy ? ")
            n = int(input("Enter a number of Tickets : "))
            count = n*130
            print(f"Amount = {count}")
            
        elif ch1 == 2:
            print("You Choose Gold....")
            print("How many Tickets You wanna Buy ? ")
            n = int(input("Enter a number of Tickets : "))
            count = n*210
            print(f"Amount = {count}")
             
        elif ch1 == 3:
            print("You Choose Premium....")
            print("How many Tickets You wanna Buy ? ")
            n = int(input("Enter a number of Tickets : "))
            count = n*240
            print(f"Amount = {count}")
    
    else:
        print("Please Enter Right Choice.....")
        
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    total = total + count
    print(f"Total Amount = {total}")
    print("vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
        
    print("Do you Wanna order more tickets ? ")
    ch2 = input("Enter 'y' for Yes or 'n' for No : ")
    
    
    if ch2 == 'n':
        break
    elif ch2 == 'y':
        continue
    else:
        print("Please Enter Right Choice....")
             
    while ch2!='y' and ch2!='n':
        print("Enter a right choice......")
        ch2=input("Enter correct choice('y' 0r 'n') : ")
			
    
    