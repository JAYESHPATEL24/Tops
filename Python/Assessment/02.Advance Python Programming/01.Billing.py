from tkinter import *
from tkinter import messagebox

root = Tk()

root.geometry("1300x800")
root.title("Billing Software")
root.config(bg="white")
title = Label(root,text="Billing Software",font=("times new roman",25,"bold"),bg="#074463",fg = 'white',bd=12,relief=GROOVE,pady=2).pack(fill=X)

# Customer Details

Customer_details = LabelFrame(root, text=" Customer Details ", font=("arial", 12, "bold"), bg="#074463", fg="gold", relief=GROOVE, bd=5)
Customer_details.place(x=0, y=70, relwidth=1)

name = Label(Customer_details, text="Customer Name", font=("times new roman",15,"bold"), bg="#074463",fg="White")
name.grid(row=0, column=0, padx=10, pady=5 )

ename = Entry(Customer_details, font=("Arial",15), bd=5, width=20)
ename.grid(row=0, column=1, padx=10, pady=5)

phone_No = Label(Customer_details, text="Phone No.", font=("times new roman",15,"bold"), bg="#074463", fg="White")
phone_No.grid(row=0, column=2, padx=10, pady=5)

ephone = Entry(Customer_details, font=("arial",15), bd=5, width=20)
ephone.grid(row=0, column=3, padx=10, pady=5)

Bill_No = Label(Customer_details, text="Bill No.", font=("times new roman",15,"bold"), bg="#074463", fg="White")
Bill_No.grid(row=0, column=4, padx=10, pady=5)

ebill_No = Entry(Customer_details, font=("arial",15), bd=5, width=20)
ebill_No.grid(row=0, column=5, padx=10, pady=5)

enter = Button(Customer_details, text=" Enter ", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=7, relief=GROOVE)
enter.grid(row=0, column=6, padx=12, pady=5)

#Cosmetics

cosmetics = LabelFrame(root, text=" Cosmetics ", font=("arial", 12, "bold"), bd=5, bg="#074463", fg="gold", relief=GROOVE)
cosmetics.place(x=0, y=157, width=320, height=400)

#Grocery
grocery = LabelFrame(root, text=" Grocery ", font=("arial", 12, "bold"), bd=5, bg="#074463", fg="gold", relief=GROOVE)
grocery.place(x=325, y=157, width=320, height=400)

#others
others = LabelFrame(root, text=" Others ", font=("arial", 12, "bold"), bd=5, bg="#074463", fg="gold", relief=GROOVE)
others.place(x=650, y=157, width=320, height=400)

#Bill Area
bill = Frame(root, bd=5, relief=GROOVE)
bill.place(x=975, y=157,width=320, height=400 )

bill_Area = Label(bill, text="Bill  Area", font=("arial", 12, "bold"), bd=5, relief=GROOVE).pack(fill=X)


# Bill Menu
menu = LabelFrame(root, text=" Bill Menu ", font=("arial", 12, "bold"), bd=5, bg="#074463", fg="gold", relief=GROOVE)
menu.place(x=0, y=563, relwidth=1, relheight=1)
root.mainloop()