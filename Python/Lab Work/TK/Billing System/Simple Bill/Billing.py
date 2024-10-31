from tkinter import *
from tkinter import messagebox
from database import mycursor,mydb
import os

flag = 0

if not os.path.exists("Bills"):
    os.makedirs("Bills")


def enter_customer_deatils():

    global flag
    flag = 0

    if ename.get()=='':
        messagebox.showerror("Name error","Please enter Customer Name ....!!!")

    elif ephone.get()=='':
        messagebox.showerror("Phone No error","Please enter the Customer Phone No.....!!!!!")

    elif ebill_No.get()=='':
        messagebox.showerror("Bill No error","Please enter Your Bill No ..!!!!")
    
    else:

        sql = "SELECT * FROM BILL WHERE Bill_No = '%s'"
        args = (ebill_No.get())

        mycursor.execute(sql%args)  
        bill_avail = mycursor.fetchone()

        if bill_avail:
            messagebox.showerror("Bill error",f"Bill {ebill_No.get()} already Exists......")
        else:
            textarea.config(state="normal")

            textarea.delete(1.0,END)
            textarea.insert(1.5,"\t******* Welcome To Store *******    \n")
            textarea.insert(END,f"\n Bill No : {ebill_No.get()}")
            textarea.insert(END,f"\n Customer Name : {ename.get()}")
            textarea.insert(END,f"\n Phone No : {ephone.get()}")
            textarea.insert(END,"\n===========================================")
            textarea.insert(END,"\nProduct \t\t\t Qty \t    Price")
            textarea.insert(END,"\n===========================================")

            textarea.config(state="disabled")
            
            flag = 1
        

def set_data():
    esoap.insert(0,0)
    ecream.insert(0,0,)
    efacewash.insert(0,0,)
    ehair_Spray.insert(0,0)
    ebody_lotion.insert(0,0)

    erice.insert(0,0)
    efood_oil.insert(0,0)
    edaal.insert(0,0)
    ewheat.insert(0,0)
    esuger.insert(0,0)

    emaza.insert(0,0)
    ecoke.insert(0,0)
    efrooti.insert(0,0)
    enimkos.insert(0,0)
    ebiscuits.insert(0,0)

def set_bill():

    textarea.config(state="normal")

    textarea.delete(1.0,END)
    
    textarea.insert(1.5,"\t******* Welcome To Store *******    \n")
    textarea.insert(END,"\n Bill No : ")
    textarea.insert(END,"\n Customer Name : ")
    textarea.insert(END,"\n Phone No : ")
    textarea.insert(END,"\n===========================================")
    textarea.insert(END,"\nProduct \t\t\t Qty \t    Price")
    textarea.insert(END,"\n===========================================")

    textarea.config(state="disabled")

    
def total():

    global flag
    

    if flag > 0:
        soap = int(esoap.get()) * 30
        cream = int(ecream.get()) * 150
        facewash = int(efacewash.get()) * 120
        hairapray = int(ehair_Spray.get()) * 200
        bodylotion = int(ebody_lotion.get()) * 250

        rice = int(erice.get()) * 60
        foodoil = int(efood_oil.get()) * 150
        daal = int(edaal.get()) * 90
        wheat = int(ewheat.get()) * 40
        suger = int(esuger.get()) * 45

        maza = int(emaza.get()) * 60
        coke = int(ecoke.get()) * 70
        frooti = int(efrooti.get()) * 50
        nimkos = int(enimkos.get()) * 20
        biscuits = int(ebiscuits.get()) * 25

        global total_tax,iteams,total_cosmeticas,total_grocery,total_others,taxofcosmetics,taxofgrocery,taxofothers,sub_total,total_bill

        total_cosmeticas = soap + cream + facewash + facewash + hairapray + bodylotion 
        total_grocery = rice + foodoil + daal + wheat + suger 
        total_others = maza + coke + frooti + nimkos + biscuits 

        taxofcosmetics = round(total_cosmeticas * 0.18,2)
        taxofgrocery = round(total_grocery * 0.05,2)
        taxofothers = round(total_others * 0.12,2)

        total_tax = taxofcosmetics + taxofgrocery + taxofothers

        sub_total = total_cosmeticas + total_grocery + total_others
        total_bill = sub_total + taxofcosmetics + taxofgrocery + taxofothers
    
        et_cosmetics.delete(0,END)
        et_cosmetics.insert(0,f"Rs.{total_cosmeticas}")
        et_grocery.delete(0,END)
        et_grocery.insert(0,f"Rs.{total_grocery}")
        et_others.delete(0,END)
        et_others.insert(0,f"Rs.{total_others}")

        etax_cosmetics.delete(0,END)
        etax_cosmetics.insert(0,f"Rs.{taxofcosmetics}")
        etax_grocery.delete(0,END)
        etax_grocery.insert(0,f"Rs.{taxofgrocery}")
        etax_others.delete(0,END)
        etax_others.insert(0,f"Rs.{taxofothers}")


        iteams = int(esoap.get()) + int(ecream.get()) + int(efacewash.get()) + int(ehair_Spray.get()) + int(ebody_lotion.get()) + int(erice.get()) + int(efood_oil.get()) + int(edaal.get()) + int(ewheat.get()) + int(esuger.get()) + int(emaza.get()) + int(ecoke.get()) + int(efrooti.get()) + int(enimkos.get()) + int(ebiscuits.get()) 

        if iteams == 0:
            flag = 1
        else:
            flag = 2
        
    else:
        messagebox.showerror("Customer Details","Please Enter Customer Details...")


def create_bill():

    global flag

    if flag > 0:

        if flag > 1:
        
            textarea.delete(1.0,END)

            enter_customer_deatils()

            textarea.config(state="normal")
            

            if int(esoap.get()) > 0:
                textarea.insert(END,f"\nBath soap \t\t\t {esoap.get()} \t     {int(esoap.get())*30}") 
            if int(ecream.get()) > 0:
                textarea.insert(END,f"\nFace Cream \t\t\t {ecream.get()} \t     {int(ecream.get())*150}")
            if int(efacewash.get()) > 0:
                textarea.insert(END,f"\nFace Wash \t\t\t {efacewash.get()} \t     {int(efacewash.get())*120}")
            if int(ehair_Spray.get()) > 0:
                textarea.insert(END,f"\nHair Spray \t\t\t {ehair_Spray.get()} \t     {int(ehair_Spray.get())*200}")
            if int(ebody_lotion.get()) > 0:
                textarea.insert(END,f"\nBody Lotion \t\t\t {ebody_lotion.get()} \t     {int(ebody_lotion.get())*250}")

            if int(erice.get()) > 0:
                textarea.insert(END,f"\nRice \t\t\t {erice.get()} \t     {int(erice.get())*60}") 
            if int(efood_oil.get()) > 0:
                textarea.insert(END,f"\nFood Oil \t\t\t {efood_oil.get()} \t     {int(efood_oil.get())*150}")
            if int(edaal.get()) > 0:
                textarea.insert(END,f"\nDaal \t\t\t {edaal.get()} \t     {int(edaal.get())*90}")
            if int(ewheat.get()) > 0:
                textarea.insert(END,f"\nWheat \t\t\t {ewheat.get()} \t     {int(ewheat.get())*40}")
            if int(esuger.get()) > 0:
                textarea.insert(END,f"\nSugar \t\t\t {esuger.get()} \t     {int(esuger.get())*45}")

            if int(emaza.get()) > 0:
                textarea.insert(END,f"\nMaza \t\t\t {emaza.get()} \t     {int(emaza.get())*60}") 
            if int(ecoke.get()) > 0:
                textarea.insert(END,f"\nCoke \t\t\t {ecoke.get()} \t     {int(ecoke.get())*70}")
            if int(efrooti.get()) > 0:
                textarea.insert(END,f"\nFrooti \t\t\t {efrooti.get()} \t     {int(efrooti.get())*50}")
            if int(enimkos.get()) > 0:
                textarea.insert(END,f"\nNimkos \t\t\t {enimkos.get()} \t     {int(enimkos.get())*20}")
            if int(ebiscuits.get()) > 0:
                textarea.insert(END,f"\nBiscuits \t\t\t {ebiscuits.get()} \t     {int(ebiscuits.get())*25}")

            textarea.insert(END,"\n===========================================")

            textarea.insert(END,f"\nSub Total \t\t\t\t     {sub_total}")

            textarea.insert(END,"\n===========================================")

            if taxofcosmetics > 0 :
                textarea.insert(END,f"\nCosmetics Tax : \t\t\t\t     {taxofcosmetics}")
            if taxofgrocery > 0 :
                textarea.insert(END,f"\nGrocery Tax : \t\t\t\t     {taxofgrocery}")
            if taxofothers > 0 :
                textarea.insert(END,f"\nOther Tax : \t\t\t\t     {taxofothers}")

            textarea.insert(END,"\n===========================================")

            textarea.insert(END,f"\nTotal \t\t\t\t     {total_bill}")


            textarea.config(state="disabled")

            if messagebox.askyesno("Bill","Do yo want to save the bill ??"):
                file_path = os.path.join("Bills", f"{ebill_No.get()}.txt")
                if not os.path.exists(file_path):
                    with open(file_path, 'w') as file:
                        file.write(textarea.get(1.0, END))

                    messagebox.showinfo("Bill save",f"Bill No : {ebill_No.get()} Saved Successfully...")

            

                sql = "INSERT INTO BILL(Customer_Name, Phone_No, Bill_No, Items, Sub_Total, Tax, Total) VALUES ('%s','%s','%s','%s','%s','%s','%s')" 
                args = (ename.get(), ephone.get(), ebill_No.get(), iteams, sub_total, total_tax, total_bill)

                mycursor.execute(sql % args)
                mydb.commit()
        
        else: 
                messagebox.showerror("Iteams","At least one item must be purchased.")
    
    else:
        messagebox.showerror("Customer Details","Please Enter Customer Details...")


def clear():
    ename.delete(0,END)
    ephone.delete(0,END)
    ebill_No.delete(0,END)

    esoap.delete(0,END)
    ecream.delete(0,END)
    efacewash.delete(0,END)
    ehair_Spray.delete(0,END)
    ebody_lotion.delete(0,END)

    erice.delete(0,END)
    efood_oil.delete(0,END)
    edaal.delete(0,END)
    ewheat.delete(0,END)
    esuger.delete(0,END)

    emaza.delete(0,END)
    ecoke.delete(0,END)
    efrooti.delete(0,END)
    enimkos.delete(0,END)
    ebiscuits.delete(0,END)

    et_cosmetics.delete(0,END)
    et_grocery.delete(0,END)
    et_others.delete(0,END)

    etax_cosmetics.delete(0,END)
    etax_grocery.delete(0,END)
    etax_others.delete(0,END)

    set_data()

    

    set_bill()



def exit():
    root.destroy()


root = Tk()

root.geometry("1600x800")
root.title("Billing Software")
root.config(bg="white")
title = Label(root,text="Billing Software",font=("times new roman",25,"bold"),bg="#074463",fg = 'white',bd=12,relief=GROOVE,pady=2).pack(fill=X)

# Customer Details

Customer_details = LabelFrame(root, text=" Customer Details ", font=("arial", 12, "bold"), bg="#074463", fg="gold", relief=GROOVE, bd=5)
Customer_details.place(x=0, y=70, relwidth=1)

name = Label(Customer_details, text="Customer Name", font=("times new roman",15,"bold"), bg="#074463",fg="White")
name.grid(row=0, column=0, padx=20, pady=5 )

ename = Entry(Customer_details, font=("Arial",15), bd=5, width=22)
ename.grid(row=0, column=1, padx=20, pady=5)

phone_No = Label(Customer_details, text="Phone No.", font=("times new roman",15,"bold"), bg="#074463", fg="White")
phone_No.grid(row=0, column=2, padx=20, pady=5)

ephone = Entry(Customer_details, font=("arial",15), bd=5, width=22)
ephone.grid(row=0, column=3, padx=20, pady=5)

Bill_No = Label(Customer_details, text="Bill No.", font=("times new roman",15,"bold"), bg="#074463", fg="White")
Bill_No.grid(row=0, column=4, padx=20, pady=5)

ebill_No = Entry(Customer_details, font=("arial",15), bd=5, width=22)
ebill_No.grid(row=0, column=5, padx=20, pady=5)

enter = Button(Customer_details, text=" Enter ", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=10, relief=GROOVE, command=enter_customer_deatils)
enter.grid(row=0, column=6, padx=22, pady=5)

#Cosmetics

cosmetics = LabelFrame(root, text=" Cosmetics ", font=("arial", 12, "bold"), bd=5, bg="#074463", fg="gold", relief=GROOVE)
cosmetics.place(x=0, y=157, width=380, height=400)

soap = Label(cosmetics, text= "Bath Soap", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=10)
soap.grid(row=0, column=0, padx=20, pady=20)

esoap = Entry(cosmetics, font=("arial",12), width=15, bd=5)
esoap.grid(row=0, column=1, padx=20, pady=20)

cream = Label(cosmetics, text= "Face Cream", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=10)
cream.grid(row=1, column=0, padx=20, pady=20)

ecream = Entry(cosmetics, font=("arial",12), width=15, bd=5)
ecream.grid(row=1, column=1, padx=20, pady=20)

facewash = Label(cosmetics, text= "Face Wash", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=10)
facewash.grid(row=2, column=0, padx=20, pady=20)

efacewash = Entry(cosmetics, font=("arial",12), width=15, bd=5)
efacewash.grid(row=2, column=1, padx=20, pady=20)

hair_Spray = Label(cosmetics, text= "Hair Spray", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=10)
hair_Spray.grid(row=3, column=0, padx=20, pady=20)

ehair_Spray = Entry(cosmetics, font=("arial",12), width=15, bd=5)
ehair_Spray.grid(row=3, column=1, padx=20, pady=20)

body_lotion = Label(cosmetics, text= "Body Lotion", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=10)
body_lotion.grid(row=4, column=0, padx=20, pady=20)

ebody_lotion = Entry(cosmetics, font=("arial",12), width=15, bd=5)
ebody_lotion.grid(row=4, column=1, padx=20, pady=20)


#Grocery
grocery = LabelFrame(root, text=" Grocery ", font=("arial", 12, "bold"), bd=5, bg="#074463", fg="gold", relief=GROOVE)
grocery.place(x=385, y=157, width=380, height=400)

rice = Label(grocery, text= "Rice", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=10)
rice.grid(row=0, column=0, padx=20, pady=20)

erice = Entry(grocery, font=("arial",12), width=15, bd=5)
erice.grid(row=0, column=1, padx=20, pady=20)

food_oil = Label(grocery, text= "Food Oil", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=10)
food_oil.grid(row=1, column=0, padx=20, pady=20)

efood_oil = Entry(grocery, font=("arial",12), width=15, bd=5)
efood_oil.grid(row=1, column=1, padx=20, pady=20)

daal = Label(grocery, text= "Daal", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=10)
daal.grid(row=2, column=0, padx=20, pady=20)

edaal = Entry(grocery, font=("arial",12), width=15, bd=5)
edaal.grid(row=2, column=1, padx=20, pady=20)

wheat = Label(grocery, text= "Wheat", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=10)
wheat.grid(row=3, column=0, padx=20, pady=20)

ewheat = Entry(grocery, font=("arial",12), width=15, bd=5)
ewheat.grid(row=3, column=1, padx=20, pady=20)

suger = Label(grocery, text= "Suger", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=10)
suger.grid(row=4, column=0, padx=20, pady=20)

esuger = Entry(grocery, font=("arial",12), width=15, bd=5)
esuger.grid(row=4, column=1, padx=20, pady=20)

#others
others = LabelFrame(root, text=" Others ", font=("arial", 12, "bold"), bd=5, bg="#074463", fg="gold", relief=GROOVE)
others.place(x=770, y=157, width=380, height=400)

maza = Label(others, text= "Maza", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=10)
maza.grid(row=0, column=0, padx=20, pady=20)

emaza = Entry(others, font=("arial",12), width=15, bd=5)
emaza.grid(row=0, column=1, padx=20, pady=20)

coke = Label(others, text= "Coke", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=10)
coke.grid(row=1, column=0, padx=20, pady=20)

ecoke = Entry(others, font=("arial",12), width=15, bd=5)
ecoke.grid(row=1, column=1, padx=20, pady=20)

frooti = Label(others, text= "Frooti", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=10)
frooti.grid(row=2, column=0, padx=20, pady=20)

efrooti = Entry(others, font=("arial",12), width=15, bd=5)
efrooti.grid(row=2, column=1, padx=20, pady=20)

nimkos = Label(others, text= "Nimkos", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=10)
nimkos.grid(row=3, column=0, padx=20, pady=20)

enimkos = Entry(others, font=("arial",12), width=15, bd=5)
enimkos.grid(row=3, column=1, padx=20, pady=20)

biscuits = Label(others, text= "Biscuits", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=10)
biscuits.grid(row=4, column=0, padx=20, pady=20)

ebiscuits = Entry(others, font=("arial",12), width=15, bd=5)
ebiscuits.grid(row=4, column=1, padx=20, pady=20)

set_data()

#Bill Area
bill = Frame(root, bd=5, relief=GROOVE)
bill.place(x=1155, y=157,width=380, height=400 )

bill_Area = Label(bill, text="Bill  Area", font=("arial", 12, "bold"), bd=5, relief=GROOVE).pack(fill=X)

scrolling = Scrollbar(bill,orient=VERTICAL)
textarea=Text(bill,yscrollcommand=scrolling.set)
scrolling.pack(side=RIGHT,fill=Y)
scrolling.config(command=textarea.yview)
textarea.pack(fill=BOTH,expand=1)

set_bill()

# Bill Menu
menu = LabelFrame(root, text=" Bill Menu ", font=("arial", 12, "bold"), bd=5, bg="#074463", fg="gold", relief=GROOVE)
menu.place(x=0, y=563, relwidth=1, relheight=1)


t_cosmetics = Label(menu, text= "Total Cosmetics", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=10)
t_cosmetics.grid(row=0, column=0, padx=30, pady=15)

et_cosmetics = Entry(menu, font=("arial",12), width=15, bd=5)
et_cosmetics.grid(row=0, column=1, padx=30, pady=15)


t_grocery = Label(menu, text= "Total Grocery", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=10)
t_grocery.grid(row=1, column=0, padx=30, pady=15)

et_grocery = Entry(menu, font=("arial",12), width=15, bd=5)
et_grocery.grid(row=1, column=1, padx=30, pady=15)


t_others = Label(menu, text= "Others Total", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=10)
t_others.grid(row=2, column=0, padx=30, pady=15)

et_others = Entry(menu, font=("arial",12), width=15, bd=5)
et_others.grid(row=2, column=1, padx=30, pady=15)

tax_cosmetics = Label(menu, text= "Cosmetics Tax", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=10)
tax_cosmetics.grid(row=0, column=2, padx=30, pady=15)

etax_cosmetics = Entry(menu, font=("arial",12), width=15, bd=5)
etax_cosmetics.grid(row=0, column=3, padx=30, pady=15)


tax_grocery = Label(menu, text= "Grocery Tax", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=10)
tax_grocery.grid(row=1, column=2, padx=30, pady=15)

etax_grocery = Entry(menu, font=("arial",12), width=15, bd=5)
etax_grocery.grid(row=1, column=3, padx=30, pady=15)


tax_others = Label(menu, text= "Others Tax", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=10)
tax_others.grid(row=2, column=2, padx=30, pady=15)

etax_others = Entry(menu, font=("arial",12), width=15, bd=5)
etax_others.grid(row=2, column=3, padx=30, pady=15)

Total = Button(menu, text=" Total ", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=8, relief=GROOVE, command=total)
Total.grid(row=1, column=4, padx=20, pady=5)

Generate_Bill = Button(menu, text=" Generate Bill ", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=13, relief=GROOVE,command=create_bill)
Generate_Bill.grid(row=1, column=5, padx=20, pady=5)

Clear = Button(menu, text=" Clear ", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=8, relief=GROOVE, command=clear)
Clear.grid(row=1, column=6, padx=20, pady=5)

exit_app = Button(menu, text=" Exit ", font=("times new roman",15,"bold"), bg="#074463", fg="white", bd=5, width=8, relief=GROOVE, command=exit)
exit_app.grid(row=1, column=7, padx=20, pady=5)

root.mainloop()