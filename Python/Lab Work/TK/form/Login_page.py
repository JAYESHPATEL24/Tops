from tkinter import *
from DATABASE import *
from tkinter import messagebox
from sign_up import *

def loginopen(root):
    root.destroy()
    login()

def login():
    root = Tk()

    root.geometry("500x500")
    root.title("Login Page")

    root.config(bg="gray")

    email = Label(root, text="Email", font=("Calibri",15,"bold"), bg="gray")
    email.place(x=10,y=100)

    Password = Label(root, text="Password", font=("Calibri",15,"bold"), bg="gray")
    Password.place(x=10,y=150)

    cpassword = Label(root, text="Comfirm Password", font=("Calibri",15,"bold"), bg="gray")
    cpassword.place(x=10,y=200)

    eemail = Entry(root,bg="lightgray", font=("Calibri",15,"bold"))
    eemail.place(x=200,y=100,width=200)

    epassword = Entry(root,bg="lightgray", show="*", font=("Calibri",15,"bold"))
    epassword.place(x=200,y=150,width=200)

    ecpassword = Entry(root, bg="lightgray", show="*", font=("Calibri",15,"bold"))
    ecpassword.place(x=200,y=200,width=200)

    button = Button(root, text="Log in", font=("Arial",20,"bold"), command= lambda : check(eemail.get(), epassword.get(), ecpassword.get()))
    button.place(x=150,y=300,height=50,width=200)

    signup_button = Button(root, text="Login", font=("Arial",20,"bold"),command=lambda:signinreturn(root))
    signup_button.place(x=380,y=350,height=50,width=200)

    root.mainloop()

def check(email,password,cpassword):

    sql = "SELECT Password FROM Person where email = '%s'"
    args = (email)

    cursor.execute(sql%args)

    check = cursor.fetchone()

    print(check)

    if check:
        if password == cpassword:
            if check[0] == password:
                print("Login Successfully.")
                messagebox.showinfo("Success","Login Successfully.")
            else:
                print("Incorrect Password!!!")
                messagebox.showwarning("Password Error", "Incorrect Password!!!")
        else:
            print("Both Passwords are not Same......!!!")
            messagebox.showwarning("Password Error", "Both Passwords are not the Same......!!!")

    else:
        print(f"Email {email} is Not Exists..")
        messagebox.showwarning("Error",f"Email : {email} Not Found..")

def signinreturn(root):
    root.destroy()
    signup()
