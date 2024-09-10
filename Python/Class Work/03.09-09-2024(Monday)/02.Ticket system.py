print()
print("**************** Let's Watch Movie ***********************")
total = 0
    
while True:
    print()
    print("Please Choose a Cinema...... ")
    print()
    print("--------------------------------------------")
    print()
    print("1.PVR")
    print("2.RAJHANS")
    print("3.MIRAJ")
    print("4.MULTIPLEX")
    print()
    print("--------------------------------------------")
    print()
    ch = int(input("Enter your Choice : "))
    print()
    print("--------------------------------------------")
    print()
    
    count = 0
    if ch == 1:
        print(f"\U0001F64F  Welcome to PVR Cinema....... \U0001F64F\U0001F64F\U0001F64F")
        print()
        print("Please SELECT one option.....")
        print()
        print("-------------|-------------------------------")
        print("1.Silver     | Rs.150")
        print("2.Gold       | Rs.200")
        print("3.premium    | Rs.250")
        print("--------------------------------------------")
        ch1 = int(input("Enter Your Choice : "))
        print("--------------------------------------------")
        if ch1 == 1:
            print("You choose Silver...")
            print("How many Tickets You wanna Buy \U00002753\U00002753 ")
            n = int(input("Enter a number of Tickets : "))
            count = n*150
            print("\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911")
            print(f"Amount = Rs.{count}")
            
        elif ch1 == 2:
            print("You Choose Gold....")
            print("How many Tickets You wanna Buy \U00002753\U00002753 ")
            n = int(input("Enter a number of Tickets : "))
            count = n*200
            print("\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911")
            print(f"Amount = Rs.{count}")
             
        elif ch1 == 3:
            print("You Choose Premium....")
            print("How many Tickets You wanna Buy \U00002753\U00002753 ")
            n = int(input("Enter a number of Tickets : "))
            count = n*250
            print("\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911")
            print(f"Amount = Rs.{count}")

        else:
            print(" XXX INCORRECT CHOICE.")
            print(" Please Enter a CORRECT choice..")
            print()
            
    elif ch == 2:
        print(f"\U0001F64F  Welcome to RAJHANS Cinema....... \U0001F64F\U0001F64F\U0001F64F")
        print()
        print("please SELECT one option.....")
        print()
        print("-------------|-------------------------------")
        print("1.Silver     | Rs.120")
        print("2.Gold       | Rs.180")
        print("3.premium    | Rs.200")
        print("--------------------------------------------")
        ch1 = int(input("Enter Your Choice : "))
        print("--------------------------------------------")
        if ch1 == 1:
            print("You choose Silver...")
            print("How many Tickets You wanna Buy \U00002753\U00002753 ")
            n = int(input("Enter a number of Tickets : "))
            count = n*120
            print("\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911")
            print(f"Amount = Rs.{count}")
            
        elif ch1 == 2:
            print("You Choose Gold....")
            print("How many Tickets You wanna Buy \U00002753\U00002753 ")
            n = int(input("Enter a number of Tickets : "))
            count = n*180
            print("\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911")
            print(f"Amount = Rs.{count}")
             
        elif ch1 == 3:
            print("You Choose Premium....")
            print("How many Tickets You wanna Buy \U00002753\U00002753 ")
            n = int(input("Enter a number of Tickets : "))
            count = n*200
            print("\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911")
            print(f"Amount = Rs.{count}")

        else:
            print(" XXX INCORRECT CHOICE.")
            print(" Please Enter a CORRECT choice..")
            print()
        
    elif ch == 3:
        print(f"\U0001F64F  Welcome to MIRAJ Cinema....... \U0001F64F\U0001F64F\U0001F64F")
        print()
        print("please SELECT one option.....")
        print()
        print("-------------|-------------------------------")
        print("1.Silver     | Rs.100")
        print("2.Gold       | Rs.150")
        print("3.premium    | Rs.180")
        print("--------------------------------------------")
        ch1 = int(input("Enter Your Choice : "))
        print("--------------------------------------------")
        if ch1 == 1:
            print("You choose Silver...")
            print("How many Tickets You wanna Buy \U00002753\U00002753 ")
            n = int(input("Enter a number of Tickets : "))
            count = n*100
            print("\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911")
            print(f"Amount = Rs.{count}")
            
        elif ch1 == 2:
            print("You Choose Gold....")
            print("How many Tickets You wanna Buy \U00002753\U00002753 ")
            n = int(input("Enter a number of Tickets : "))
            count = n*150
            print("\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911")
            print(f"Amount = Rs.{count}")
             
        elif ch1 == 3:
            print("You Choose Premium....")
            print("How many Tickets You wanna Buy \U00002753\U00002753 ")
            n = int(input("Enter a number of Tickets : "))
            count = n*180
            print("\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911")
            print(f"Amount = Rs.{count}")

        else:
            print(" XXX INCORRECT CHOICE.")
            print(" Please Enter a CORRECT choice..")
            print()
    
    elif ch == 4:
        print(f"\U0001F64F  Welcome to MULTIPLEX Cinema....... \U0001F64F\U0001F64F\U0001F64F")
        print()
        print("please SELECT one option.....")
        print()
        print("-------------|-------------------------------")
        print("1.Silver     | Rs.130")
        print("2.Gold       | Rs.210")
        print("3.premium    | Rs.240")
        print("--------------------------------------------")
        ch1 = int(input("Enter Your Choice : "))
        print("--------------------------------------------")
        if ch1 == 1:
            print("You choose Silver...")
            print("How many Tickets You wanna Buy \U00002753\U00002753 ")
            n = int(input("Enter a number of Tickets : "))
            count = n*130
            print("\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911")
            print(f"Amount = Rs.{count}")
            
        elif ch1 == 2:
            print("You Choose Gold....")
            print("How many Tickets You wanna Buy \U00002753\U00002753 ")
            n = int(input("Enter a number of Tickets : "))
            count = n*210
            print("\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911")
            print(f"Amount = Rs.{count}")
             
        elif ch1 == 3:
            print("You Choose Premium....")
            print("How many Tickets You wanna Buy \U00002753\U00002753 ")
            n = int(input("Enter a number of Tickets : "))
            count = n*240
            print("\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911\U0001F911")
            print(f"Amount = Rs.{count}")
            
        else:
            print(" XXX INCORRECT CHOICE.")
            print(" Please Enter a CORRECT choice..")
            print()
    
    else:
        print(" XXX INCORRECT CHOICE.")
        print(" Please Enter a CORRECT choice..")
        print()
        
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    total = total + count
    print(f"Total Amount = Rs.{total} \U0001F4B8\U0001F4B8")
    print("vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
    
    print("Do you Wanna order more tickets ? \U0001F914\U0001F914 ")
    ch2 = input("Enter 'y' for Yes or 'n' for No : ")
    
    while ch2!='y' and ch2!='n':
        print("please Enter a right choice......")
        ch2=input("Enter correct choice('y' 0r 'n') : ")
    
    if ch2 == 'n':
        print()
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print(f"Total Amount = Rs.{total} \U0001F4B8\U0001F4B8")
        print("vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
        print()
        print(f" THANK U SO MUCH FOR VISITING ....\U0001F60A\U0001F60A\U0001F60A ")
        print(" VISIT AGAIN \U0001F607\U0001F607\U0001F607............!!!!")
        print()
        print("*********************************************")
        print()
        break
             
			
    
    