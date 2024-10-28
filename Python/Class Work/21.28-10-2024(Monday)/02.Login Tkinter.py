from tkinter import *
from tkinter import messagebox
import pymysql

def insert():
    name = ename.get()
    email = eemail.get()
    mobile = emobile.get()
    Password = epassword.get()
    cpassword = ecpassword.get()
    
    if Password == cpassword:
        db = pymysql.connect(host="localhost", user="root", password="", database="Python")
        cursor = db.cursor()
        
        sql = "INSERT INTO Person(Name, Email, Moblie_No, Password) VALUES('%s','%s','%s','%s')"
        args = (name,email,mobile,Password)
        cursor.execute(sql%args)
        db.commit()
        
        print("Data Inserted Successfully......!!!")
        messagebox.showinfo("Success", "Data Inserted Successfully!")
        
        cursor.close()
        db.close()
        
        ename.delete(0, END)
        eemail.delete(0, END)
        emobile.delete(0, END)
        epassword.delete(0, END)
        ecpassword.delete(0, END)

        
    else:
        print("Both Passwords are not Same......!!!")
        messagebox.showwarning("Password Error", "Both Passwords are not the Same......!!!")
        
        
root = Tk()

root.geometry("1000x1000")
root.title("Sign Up")

root.config(bg="lightblue")

name = Label(root, text="Name", font=("Calibri",20,"bold"), bg="lightblue")
name.place(x=50,y=50)

email = Label(root, text="Email", font=("Calibri",20,"bold"), bg="lightblue")
email.place(x=50,y=100)

mobile = Label(root, text="Mobile No", font=("Calibri",20,"bold"), bg="lightblue")
mobile.place(x=50,y=150)

Password = Label(root, text="Password", font=("Calibri",20,"bold"), bg="lightblue")
Password.place(x=50,y=200)

cpassword = Label(root, text="Comfirm Password", font=("Calibri",20,"bold"), bg="lightblue")
cpassword.place(x=50,y=250)

ename = Entry(root,bg="lightgray", font=("Calibri",20,"bold"))
ename.place(x=300,y=50,height=40,width=300)

eemail = Entry(root,bg="lightgray", font=("Calibri",20,"bold"))
eemail.place(x=300,y=100,height=40,width=300)

emobile = Entry(root,bg="lightgray", font=("Calibri",20,"bold"))
emobile.place(x=300,y=150,height=40,width=300)

epassword = Entry(root,bg="lightgray", show="*", font=("Calibri",20,"bold"))
epassword.place(x=300,y=200,height=40,width=300)

ecpassword = Entry(root, bg="lightgray", show="*", font=("Calibri",20,"bold"))
ecpassword.place(x=300,y=250,height=40,width=300)

button = Button(root, text="Submit", font=("Arial",20,"bold"), command=insert)
button.place(x=200,y=350,height=50,width=200)

root.mainloop()