from tkinter import *

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

enter = Button(Customer_details, text=" Enter ", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=10, relief=GROOVE)
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

#Bill Area
bill = Frame(root, bd=5, relief=GROOVE)
bill.place(x=1155, y=157,width=380, height=400 )

bill_Area = Label(bill, text="Bill  Area", font=("arial", 12, "bold"), bd=5, relief=GROOVE).pack(fill=X)


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

enter = Button(menu, text=" Total ", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=8, relief=GROOVE)
enter.grid(row=1, column=4, padx=20, pady=5)

enter = Button(menu, text=" Generate Bill ", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=13, relief=GROOVE)
enter.grid(row=1, column=5, padx=20, pady=5)

enter = Button(menu, text=" Clear ", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=8, relief=GROOVE)
enter.grid(row=1, column=6, padx=20, pady=5)

enter = Button(menu, text=" Exit ", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=8, relief=GROOVE)
enter.grid(row=1, column=7, padx=20, pady=5)


root.mainloop()