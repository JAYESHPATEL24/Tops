from tkinter import *
from DATABASE import *
from tkinter import messagebox
from Update_Delete import *



def loginopen(root):
    root.destroy()
    login()

def login():
    root = Tk()

    from sign_up import center_window
    center_window(root,450,400)
    
    root.title("Login Page")

    root.config(bg="gray")

    email = Label(root, text="Email", font=("Calibri",15,"bold"), bg="gray")
    email.place(x=20,y=50)

    Password = Label(root, text="Password", font=("Calibri",15,"bold"), bg="gray")
    Password.place(x=20,y=100)

    cpassword = Label(root, text="Comfirm Password", font=("Calibri",15,"bold"), bg="gray")
    cpassword.place(x=20,y=150)

    eemail = Entry(root,bg="lightgray", font=("Calibri",15,"bold"))
    eemail.place(x=200,y=50,width=200)

    epassword = Entry(root,bg="lightgray", show="*", font=("Calibri",15,"bold"))
    epassword.place(x=200,y=100,width=200)

    ecpassword = Entry(root, bg="lightgray", show="*", font=("Calibri",15,"bold"))
    ecpassword.place(x=200,y=150,width=200)

    button = Button(root, text="Log in", font=("Arial",15,"bold"), command= lambda : check(eemail.get(), epassword.get(), ecpassword.get(), root))
    button.place(x=100,y=250,height=50,width=100)

    signup_button = Button(root, text="Sign Up", font=("Arial",15,"bold"),command=lambda:signinreturn(root))
    signup_button.place(x=240,y=250,height=50,width=100)

    exit_button = Button(root, text="Exit", font=("Arial",15,"bold"),command=lambda:exit(root))
    exit_button.place(x=170,y=320,height=50,width=100)

    root.mainloop()

def check(email,password,cpassword,root):

    sql = "SELECT Password FROM Person where email = '%s'"
    args = (email)

    cursor.execute(sql%args)

    check = cursor.fetchone()

    if check:
        if password == cpassword:
            if check[0] == password:
                print("Login Successfully.")
                enter_to_update_delete(root,email)

            else:
                print("Incorrect Password!!!")
                messagebox.showwarning("Password Error", "Incorrect Password!!!")
        else:
            print("Both Passwords are not Same......!!!")
            messagebox.showwarning("Password Error", "Both Passwords are not the Same......!!!")

    else:
        print(f"Email {email} is Not Exists..")
        messagebox.showwarning("Error",f"Email : {email} Not Found..\n PLEASE SIGN UP")

def signinreturn(root):
    root.destroy()
    from sign_up import signup
    signup()

def exit(root):
    root.destroy()