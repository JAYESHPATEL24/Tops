from tkinter import *

def enter_to_update_delete(root):
    root.destroy()
    Update_delete()


def Update_delete():

    root = Tk()

    root.geometry("400x400")
    root.title("Option Page")

    root.config(bg="lightblue")

    email = Label(root, text="Login Successfully!!!!!!!!", font=("Calibri",20,"bold"), bg="gray")
    email.place(x=75,y=100,)

    Update_button = Button(root, text="Update Data", font=("Arial",10,"bold"))
    Update_button.place(x=80,y=200,height=50,width=100)

    signup_button = Button(root, text="Delete Data", font=("Arial",10,"bold"), command=lambda:delete(root))
    signup_button.place(x=220,y=200,height=50,width=100)

    root.mainloop()

def delete(root):
    root.destroy()
    root = Tk()

    root.geometry("500x500")
    root.title("Login Page")

    root.config(bg="lightblue")

    email = Label(root, text="Email", font=("Calibri",15,"bold"), bg="lightblue")
    email.place(x=10,y=100)

    Password = Label(root, text="Password", font=("Calibri",15,"bold"), bg="lightblue")
    Password.place(x=10,y=150)

    cpassword = Label(root, text="Comfirm Password", font=("Calibri",15,"bold"), bg="lightblue")
    cpassword.place(x=10,y=200)

    eemail = Entry(root,bg="lightblue", font=("Calibri",15,"bold"))
    eemail.place(x=200,y=100,width=200)

    epassword = Entry(root,bg="lightblue", show="*", font=("Calibri",15,"bold"))
    epassword.place(x=200,y=150,width=200)

    ecpassword = Entry(root, bg="lightblue", show="*", font=("Calibri",15,"bold"))
    ecpassword.place(x=200,y=200,width=200)

    button = Button(root, text="Delete", font=("Arial",15,"bold"))
    button.place(x=80,y=300,height=50,width=100)

    signup_button = Button(root, text="Option", font=("Arial",15,"bold"))
    signup_button.place(x=220,y=300,height=50,width=100)

    root.mainloop()



