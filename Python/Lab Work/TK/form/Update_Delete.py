from tkinter import *
from tkinter import messagebox
from DATABASE import *


def enter_to_update_delete(root,email):
    email1 = email
    root.destroy()
    Update_delete(email1)


def Update_delete(email2):

    root = Tk()

    from sign_up import center_window
    center_window(root,400,500)

    root.title("Option Page")

    root.config(bg="lightblue")

    login_label = Label(root, text="Login Successfully!!!!!!!!", font=("Calibri",20,"bold"), bg="lightblue").pack(fill=X)

    sql = "SELECT * FROM Person where email = '%s'"
    args = (email2)

    cursor.execute(sql%args)

    info = cursor.fetchone()

    name = f"Welcome, {info[1]}"
    mobile = f"Mobile No : {info[3]}"
    mail = f"Email     : {info[2]}"

    welcome = Label(root, text=name, font=("Calibri",20,"bold"), bg="lightblue")
    welcome.pack(pady=(20,10))

    mobile = Label(root, text=mobile, font=("Calibri",20,"bold"), bg="lightblue")
    mobile.pack(pady=(5,10))

    user_email = Label(root, text=mail, font=("Calibri",20,"bold"), bg="lightblue")
    user_email.pack(pady=(5,10))

    Update_button = Button(root, text="Update Data", font=("Arial",10,"bold"),width=15, height=2, command= lambda : update(root,email2))
    Update_button.pack(pady=(20,10))

    delete_button = Button(root, text="Delete Data", font=("Arial",10,"bold"), width=15, height=2, command=lambda:delete(root,email2))
    delete_button.pack(pady=(10, 10))

    back_button = Button(root, text="Back", font=("Arial",10,"bold"), width=15, height=2, command=lambda:Back(root))
    back_button.pack(pady=(10, 10))

    exit_button = Button(root, text="Exit", font=("Arial",10,"bold"), width=15, height=2, command=lambda:exit(root))
    exit_button.pack(pady=(10, 20))

    root.mainloop()

def update(root,email):
    root.destroy()
    root = Tk()

    from sign_up import center_window
    center_window(root,300,400)

    root.title("Update Data")

    root.config(bg="lightblue")

    New_data = Label(root, text="Please Enter New Data", font=("Calibri",15,"bold"), bg="lightblue")
    New_data.pack(fill=X,pady=(20,10))

    Name = Label(root, text="Name", font=("Calibri",12,"bold"), bg="lightblue")
    Name.place(x=20,y=100)

    eName = Entry(root,bg="lightblue", font=("Calibri",12,"bold"))
    eName.place(x=100,y=100)

    Mobile_No = Label(root, text="Mobile No", font=("Calibri",12,"bold"), bg="lightblue")
    Mobile_No.place(x=20,y=150)

    eMobile_No = Entry(root,bg="lightblue", font=("Calibri",12,"bold"))
    eMobile_No.place(x=100,y=150)

    Password = Label(root, text="Password", font=("Calibri",12,"bold"), bg="lightblue")
    Password.place(x=20,y=200)

    epassword = Entry(root,bg="lightblue", show="*", font=("Calibri",12,"bold"))
    epassword.place(x=100,y=200)

    button = Button(root, text="Update", font=("Arial",12,"bold"), command=lambda:update_data(email, eName.get(), eMobile_No.get(), epassword.get(), root))
    button.place(x=40,y=275,height=40,width=100)

    button_return = Button(root, text="Cancel", font=("Arial",12,"bold"), command=lambda:cancel(root,email))
    button_return.place(x=160,y=275,height=40,width=100)

    root.mainloop()


def update_data(email,name,mobile,password,root):

    sql = "UPDATE Person SET Name = '%s', Moblie_No = '%s', Password = '%s' WHERE Email = '%s'"
    args = (name,mobile,password,email)

    cursor.execute(sql%args)

    db.commit()

    print("Data updated Successfully.!!!!")

    messagebox.showinfo("Update","Data Updated Successfully.!!!!!")

    root.destroy()

    Update_delete(email)



def delete(root,email):
    if messagebox.askyesno("Delete Data", "Do You Really want to delete Data?"):
        root.destroy()
        root = Tk()

        from sign_up import center_window
        center_window(root,300,300)
        root.title("Are You Sure????")

        root.config(bg="lightblue")

        enter_Password = Label(root, text="Please Enter you password", font=("Calibri",15,"bold"), bg="lightblue")
        enter_Password.pack(fill=X,pady=(20,10))

        Password = Label(root, text="Password", font=("Calibri",12,"bold"), bg="lightblue")
        Password.place(x=20,y=100)

        epassword = Entry(root,bg="lightblue", show="*", font=("Calibri",12,"bold"))
        epassword.place(x=100,y=100)

        button = Button(root, text="Delete", font=("Arial",12,"bold"), command=lambda:delete_data(email, epassword.get(), root))
        button.place(x=40,y=175,height=40,width=100)

        button_return = Button(root, text="Cancel", font=("Arial",12,"bold"), command=lambda:cancel(root,email))
        button_return.place(x=160,y=175,height=40,width=100)

        root.mainloop()

    else:
        root.destroy()
        Update_delete(email)

def delete_data(email,password,root):

    sql = "SELECT Password FROM Person where email = '%s'"
    args = (email)

    cursor.execute(sql%args)

    check = cursor.fetchone()

    if check[0] == password:
        print("correct Successfully.")
        sql = "DELETE FROM Person WHERE email = '%s'"
        args = (email)

        cursor.execute(sql%args)
        db.commit()

        print("Delete Data Successfully...!!!!")

        messagebox.showinfo("Delete","Data Deleted Successfully..!!!!")

        root.destroy()

        from sign_up import signup

        signup()


    else:
        print("Incorrect Password!!!")
        messagebox.showwarning("Password Error", "Incorrect Password!!!")
        
def cancel(root,email):
    root.destroy()
    Update_delete(email)

def Back(root):
    root.destroy()
    from Login_page import login
    login()

def exit(root):
    root.destroy()



