import random

try:
    
    d = {}

    menu = """
            Press 1 for Sign Up
            press 2 for Login
            Press 3 for Forgot Password
            Press 4 Exit
            """
            
    while True :
        print(menu)
        
        choice = int(input("Enter your Choice : "))
        
        if choice == 1:
            print("*"*50,"Welcome to Signup Page","*"*50)
            name = input("Enter your name : ")
            email = input("Enter your email : ")
            mobile = int(input("Enter your Mobile No : "))
            password = input("Enter your Password : ")
            cpassword = input("Enter your Confirm Password : ")
            
            if password == cpassword:
                d['name'] = name
                d['email'] = email
                d['mobile'] = mobile
                d['password'] = password
                print("Sign Up Successfully!!")
                
            else:
                print("Password and Confirm Password Not Match..!!")
                
        elif choice == 2:
            print("*"*50,"Welcome to Login Page","*"*50)
            email = input("Enter your email : ")
            password = int(input("Enter your Password : "))
            
            if d['email'] == email and d['password'] == password:
                print("Login Successfull...!!!!")
            else:
                print("Invalid Credentials!!")
        
        elif choice == 3:
            print("*"*50,"Welcome to Forgot Password Page","*"*50)
            mobile = int(input("Enter your Mobile No : "))
            
            otp = random.randint(1000,9999)
            
            if d['mobile'] == mobile:
                print(f"your otp : {otp}")
                
                uotp = int(input("Enter a OTP : "))
            
            else: 
                print("XXXX Invalid Mobile Number....!!  ")    
                if otp == uotp:
                    password = input("Enter your New Password : ")
                    d['password'] = password
                    print("Password Change successfully!!!")
                    
        
        elif choice == 4:
            print("Thank You") 
            break
            
        else:
            print("Invalid Choice!!!")  
            break         

except ValueError as e:
    print(e)
             
except:
    print("Invalid input!!")