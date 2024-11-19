from tkinter import *
from tkinter import messagebox
from database import mycursor,mydb
import os


class Billingsoftware:
    def __init__(self,root):
            # Initialize the main window
        self.root = root
        self.root.geometry("1600x800")
        self.root.title("Billing Software")
        self.root.config(bg="white")

            # check and create a folder for save the bills.....
        if not os.path.exists("Bills"):
             os.makedirs("Bills")

            # Flag to track some state
        self.flag = 0
            
             # Create all the widgets in the application
        self.create_widgets()
        
    def create_widgets(self):
            # Title label for the application
        title = Label(self.root, text="Billing Software", font=("times new roman", 25, "bold"), bg="#074463", fg='white', bd=12, relief=GROOVE, pady=2)
        title.pack(fill=X)

            # Create customer detail input fields
        self.create_customer_detail()
            # Create cosmetics input fields
        self.create_cosmetics()
            # Create grocery input fields
        self.create_grocery()
            # Create other items input fields
        self.create_others()
            # set all the iteams to 0 
        self.set_data()
            # Create bill area for displaying the bill
        self.create_bill_area()
            # Create menu buttons for actions
        self.create_menu()

    def create_customer_detail(self):
            #Customer Details Section
        Customer_details = LabelFrame(self.root, text=" Customer Details ", font=("arial", 12, "bold"), bg="#074463", fg="gold", relief=GROOVE, bd=5)
        Customer_details.place(x=0, y=70, relwidth=1)

            # Customer name input
        name = Label(Customer_details, text="Customer Name", font=("times new roman",15,"bold"), bg="#074463",fg="White")
        name.grid(row=0, column=0, padx=20, pady=5 )

        self.ename = Entry(Customer_details, font=("Arial",15), bd=5, width=22)
        self.ename.grid(row=0, column=1, padx=20, pady=5)

            #Customer Phone No input
        phone_No = Label(Customer_details, text="Phone No.", font=("times new roman",15,"bold"), bg="#074463", fg="White")
        phone_No.grid(row=0, column=2, padx=20, pady=5)

        self.ephone = Entry(Customer_details, font=("arial",15), bd=5, width=22)
        self.ephone.grid(row=0, column=3, padx=20, pady=5)

            #Customer Bill No input
        Bill_No = Label(Customer_details, text="Bill No.", font=("times new roman",15,"bold"), bg="#074463", fg="White")
        Bill_No.grid(row=0, column=4, padx=20, pady=5)

        self.ebill_No = Entry(Customer_details, font=("arial",15), bd=5, width=22)
        self.ebill_No.grid(row=0, column=5, padx=20, pady=5)

            # Enter button to submit customer details
        enter = Button(Customer_details, text=" Enter ", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=10, relief=GROOVE, command=self.enter_customer_deatils)
        enter.grid(row=0, column=6, padx=22, pady=5)

        

    def create_cosmetics(self):
            #cosmetics section
        cosmetics = LabelFrame(self.root, text=" Cosmetics ", font=("arial", 12, "bold"), bd=5, bg="#074463", fg="gold", relief=GROOVE)
        cosmetics.place(x=0, y=157, width=380, height=400)

            # Cosmetic products inputs
        soap = Label(cosmetics, text= "Bath Soap", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=10)
        soap.grid(row=0, column=0, padx=20, pady=20)

        self.esoap = Entry(cosmetics, font=("arial",12), width=15, bd=5)
        self.esoap.grid(row=0, column=1, padx=20, pady=20)

        cream = Label(cosmetics, text= "Face Cream", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=10)
        cream.grid(row=1, column=0, padx=20, pady=20)

        self.ecream = Entry(cosmetics, font=("arial",12), width=15, bd=5)
        self.ecream.grid(row=1, column=1, padx=20, pady=20)

        facewash = Label(cosmetics, text= "Face Wash", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=10)
        facewash.grid(row=2, column=0, padx=20, pady=20)

        self.efacewash = Entry(cosmetics, font=("arial",12), width=15, bd=5)
        self.efacewash.grid(row=2, column=1, padx=20, pady=20)

        hair_Spray = Label(cosmetics, text= "Hair Spray", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=10)
        hair_Spray.grid(row=3, column=0, padx=20, pady=20)

        self.ehair_Spray = Entry(cosmetics, font=("arial",12), width=15, bd=5)
        self.ehair_Spray.grid(row=3, column=1, padx=20, pady=20)

        body_lotion = Label(cosmetics, text= "Body Lotion", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=10)
        body_lotion.grid(row=4, column=0, padx=20, pady=20)

        self.ebody_lotion = Entry(cosmetics, font=("arial",12), width=15, bd=5)
        self.ebody_lotion.grid(row=4, column=1, padx=20, pady=20)


    def create_grocery(self):
            # Grocery section
        grocery = LabelFrame(self.root, text=" Grocery ", font=("arial", 12, "bold"), bd=5, bg="#074463", fg="gold", relief=GROOVE)
        grocery.place(x=385, y=157, width=380, height=400)

            # Grocery products inputs
        rice = Label(grocery, text= "Rice", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=10)
        rice.grid(row=0, column=0, padx=20, pady=20)

        self.erice = Entry(grocery, font=("arial",12), width=15, bd=5)
        self.erice.grid(row=0, column=1, padx=20, pady=20)

        food_oil = Label(grocery, text= "Food Oil", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=10)
        food_oil.grid(row=1, column=0, padx=20, pady=20)

        self.efood_oil = Entry(grocery, font=("arial",12), width=15, bd=5)
        self.efood_oil.grid(row=1, column=1, padx=20, pady=20)

        daal = Label(grocery, text= "Daal", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=10)
        daal.grid(row=2, column=0, padx=20, pady=20)

        self.edaal = Entry(grocery, font=("arial",12), width=15, bd=5)
        self.edaal.grid(row=2, column=1, padx=20, pady=20)

        wheat = Label(grocery, text= "Wheat", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=10)
        wheat.grid(row=3, column=0, padx=20, pady=20)

        self.ewheat = Entry(grocery, font=("arial",12), width=15, bd=5)
        self.ewheat.grid(row=3, column=1, padx=20, pady=20)

        suger = Label(grocery, text= "Suger", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=10)
        suger.grid(row=4, column=0, padx=20, pady=20)

        self.esuger = Entry(grocery, font=("arial",12), width=15, bd=5)
        self.esuger.grid(row=4, column=1, padx=20, pady=20)

    def create_others(self):
            # Other items section
        others = LabelFrame(self.root, text=" Others ", font=("arial", 12, "bold"), bd=5, bg="#074463", fg="gold", relief=GROOVE)
        others.place(x=770, y=157, width=380, height=400)

            # Grocery products inputs
        maza = Label(others, text= "Maza", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=10)
        maza.grid(row=0, column=0, padx=20, pady=20)

        self.emaza = Entry(others, font=("arial",12), width=15, bd=5)
        self.emaza.grid(row=0, column=1, padx=20, pady=20)

        coke = Label(others, text= "Coke", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=10)
        coke.grid(row=1, column=0, padx=20, pady=20)

        self.ecoke = Entry(others, font=("arial",12), width=15, bd=5)
        self.ecoke.grid(row=1, column=1, padx=20, pady=20)

        frooti = Label(others, text= "Frooti", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=10)
        frooti.grid(row=2, column=0, padx=20, pady=20)

        self.efrooti = Entry(others, font=("arial",12), width=15, bd=5)
        self.efrooti.grid(row=2, column=1, padx=20, pady=20)

        nimkos = Label(others, text= "Nimkos", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=10)
        nimkos.grid(row=3, column=0, padx=20, pady=20)

        self.enimkos = Entry(others, font=("arial",12), width=15, bd=5)
        self.enimkos.grid(row=3, column=1, padx=20, pady=20)

        biscuits = Label(others, text= "Biscuits", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=10)
        biscuits.grid(row=4, column=0, padx=20, pady=20)

        self.ebiscuits = Entry(others, font=("arial",12), width=15, bd=5)
        self.ebiscuits.grid(row=4, column=1, padx=20, pady=20)
    
    def create_bill_area(self):
            # bill area section
        bill = Frame(self.root, bd=5, relief=GROOVE)
        bill.place(x=1155, y=157,width=380, height=400 )

        bill_Area = Label(bill, text="Bill  Area", font=("arial", 12, "bold"), bd=5, relief=GROOVE).pack(fill=X)

            # create a Scrollbar for bill area
        scrolling = Scrollbar(bill,orient=VERTICAL)
            # create a text area for bill
        self.textarea=Text(bill,yscrollcommand=scrolling.set)
        scrolling.pack(side=RIGHT,fill=Y)
        scrolling.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

            # Initilize the bill
        self.set_bill()
            
    def create_menu(self):
            # Bill Menu Section
        menu = LabelFrame(self.root, text=" Bill Menu ", font=("arial", 12, "bold"), bd=5, bg="#074463", fg="gold", relief=GROOVE)
        menu.place(x=0, y=563, relwidth=1, relheight=1)

            # total price of cosmetics
        t_cosmetics = Label(menu, text= "Total Cosmetics", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=10)
        t_cosmetics.grid(row=0, column=0, padx=30, pady=15)

        self.et_cosmetics = Entry(menu, font=("arial",12), width=15, bd=5)
        self.et_cosmetics.grid(row=0, column=1, padx=30, pady=15)

            # total price of grocery products
        t_grocery = Label(menu, text= "Total Grocery", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=10)
        t_grocery.grid(row=1, column=0, padx=30, pady=15)

        self.et_grocery = Entry(menu, font=("arial",12), width=15, bd=5)
        self.et_grocery.grid(row=1, column=1, padx=30, pady=15)

            # total price of other products
        t_others = Label(menu, text= "Others Total", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=10)
        t_others.grid(row=2, column=0, padx=30, pady=15)

        self.et_others = Entry(menu, font=("arial",12), width=15, bd=5)
        self.et_others.grid(row=2, column=1, padx=30, pady=15)

            # total tax on cosmetics products
        tax_cosmetics = Label(menu, text= "Cosmetics Tax", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=10)
        tax_cosmetics.grid(row=0, column=2, padx=30, pady=15)

        self.etax_cosmetics = Entry(menu, font=("arial",12), width=15, bd=5)
        self.etax_cosmetics.grid(row=0, column=3, padx=30, pady=15)

            # total tax on Grocery products
        tax_grocery = Label(menu, text= "Grocery Tax", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=10)
        tax_grocery.grid(row=1, column=2, padx=30, pady=15)

        self.etax_grocery = Entry(menu, font=("arial",12), width=15, bd=5)
        self.etax_grocery.grid(row=1, column=3, padx=30, pady=15)

            # total tax on other products
        tax_others = Label(menu, text= "Others Tax", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=10)
        tax_others.grid(row=2, column=2, padx=30, pady=15)

        self.etax_others = Entry(menu, font=("arial",12), width=15, bd=5)
        self.etax_others.grid(row=2, column=3, padx=30, pady=15)

            # Total Button
        Total = Button(menu, text=" Total ", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=8, relief=GROOVE, command=self.total)
        Total.grid(row=1, column=4, padx=20, pady=5)

            # Generate Bill Button
        Generate_Bill = Button(menu, text=" Generate Bill ", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=13, relief=GROOVE,command=self.create_bill)
        Generate_Bill.grid(row=1, column=5, padx=20, pady=5)

            # Clear Data Button
        Clear = Button(menu, text=" Clear ", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=8, relief=GROOVE, command=self.clear)
        Clear.grid(row=1, column=6, padx=20, pady=5)

            # exit Button
        exit_app = Button(menu, text=" Exit ", font=("times new roman",15,"bold"), bg="#074463", fg="white", bd=5, width=8, relief=GROOVE, command=self.exit)
        exit_app.grid(row=1, column=7, padx=20, pady=5)
    
    def set_data(self):
            # initilize all cosmetic products 
        self.esoap.insert(0,0)
        self.ecream.insert(0,0,)
        self.efacewash.insert(0,0,)
        self.ehair_Spray.insert(0,0)
        self.ebody_lotion.insert(0,0)

            # initilize all grocery products
        self.erice.insert(0,0)
        self.efood_oil.insert(0,0)
        self.edaal.insert(0,0)
        self.ewheat.insert(0,0)
        self.esuger.insert(0,0)

            # initilize all other products 
        self.emaza.insert(0,0)
        self.ecoke.insert(0,0)
        self.efrooti.insert(0,0)
        self.enimkos.insert(0,0)
        self.ebiscuits.insert(0,0)

    def set_bill(self):
            # initilize bill
        self.textarea.config(state="normal")

        self.textarea.delete(1.0,END)
        
        self.textarea.insert(1.5,"\t******* Welcome To Store *******    \n")
        self.textarea.insert(END,"\n Bill No : ")
        self.textarea.insert(END,"\n Customer Name : ")
        self.textarea.insert(END,"\n Phone No : ")
        self.textarea.insert(END,"\n===========================================")
        self.textarea.insert(END,"\nProduct \t\t\t Qty \t    Price")
        self.textarea.insert(END,"\n===========================================")

        self.textarea.config(state="disabled")

    # ----------------------------- Click Button functions ----------------------------
    
    def enter_customer_deatils(self):
            # check user input the customer name or not.
        if self.ename.get()=='':
            messagebox.showerror("Name error","Please enter Customer Name ....!!!")

            # check user input the customer Phone No or not.
        elif self.ephone.get()=='':
            messagebox.showerror("Phone No error","Please enter the Customer Phone No.....!!!!!")

            # check user input Bill No or not.
        elif self.ebill_No.get()=='':
            messagebox.showerror("Bill No error","Please enter Your Bill No ..!!!!")
        
            # if all customer Details are entered......
        else:
            # check entered bill no are already exists or not
            sql = "SELECT * FROM BILL WHERE Bill_No = '%s'"
            args = (self.ebill_No.get())

            mycursor.execute(sql%args)  
            bill_avail = mycursor.fetchone()

                # if bill already exists with given bill no then show message box
            if bill_avail:
                messagebox.showerror("Bill error",f"Bill {self.ebill_No.get()} already Exists......")
                # if bill already doesn't exists with given bill no then store details
            else:
                self.textarea.config(state="normal")

                self.textarea.delete(1.0,END)
                self.textarea.insert(1.5,"\t******* Welcome To Store *******    \n")
                self.textarea.insert(END,f"\n Bill No : {self.ebill_No.get()}")
                self.textarea.insert(END,f"\n Customer Name : {self.ename.get()}")
                self.textarea.insert(END,f"\n Phone No : {self.ephone.get()}")
                self.textarea.insert(END,"\n===========================================")
                self.textarea.insert(END,"\nProduct \t\t\t Qty \t    Price")
                self.textarea.insert(END,"\n===========================================")

                self.textarea.config(state="disabled")

                    # if customer details are correct than value of flag set to 1.
                self.flag = 1

    def total(self):
            # if flag value is more than 0 means customer details are entered 
        if self.flag > 0:
                # calculate prices of each cosmetic products using user inputs
            soap = int(self.esoap.get()) * 30
            cream = int(self.ecream.get()) * 150
            facewash = int(self.efacewash.get()) * 120
            hairapray = int(self.ehair_Spray.get()) * 200
            bodylotion = int(self.ebody_lotion.get()) * 250

                # calculate prices of each Grocery products using user inputs
            rice = int(self.erice.get()) * 60
            foodoil = int(self.efood_oil.get()) * 150
            daal = int(self.edaal.get()) * 90
            wheat = int(self.ewheat.get()) * 40
            suger = int(self.esuger.get()) * 45

                # calculate prices of each other products using user inputs
            maza = int(self.emaza.get()) * 60
            coke = int(self.ecoke.get()) * 70
            frooti = int(self.efrooti.get()) * 50
            nimkos = int(self.enimkos.get()) * 20
            biscuits = int(self.ebiscuits.get()) * 25

                # calculate prices of each sections
            self.total_cosmeticas = soap + cream + facewash + facewash + hairapray + bodylotion 
            self.total_grocery = rice + foodoil + daal + wheat + suger 
            self.total_others = maza + coke + frooti + nimkos + biscuits 

                # calculate tax of each section
            self.taxofcosmetics = round(self.total_cosmeticas * 0.18,2)
            self.taxofgrocery = round(self.total_grocery * 0.05,2)
            self.taxofothers = round(self.total_others * 0.12,2)

                # Calculate Total Tax
            self.total_tax = self.taxofcosmetics + self.taxofgrocery + self.taxofothers

                # Calculte sub Total(without tax) and Total(including tax)
            self.sub_total = self.total_cosmeticas + self.total_grocery + self.total_others
            self.total_bill = self.sub_total + self.taxofcosmetics + self.taxofgrocery + self.taxofothers
        
                # set the Calculated data into the Bill Menu Section
            self.et_cosmetics.delete(0,END)
            self.et_cosmetics.insert(0,f"Rs.{self.total_cosmeticas}")
            self.et_grocery.delete(0,END)
            self.et_grocery.insert(0,f"Rs.{self.total_grocery}")
            self.et_others.delete(0,END)
            self.et_others.insert(0,f"Rs.{self.total_others}")

            self.etax_cosmetics.delete(0,END)
            self.etax_cosmetics.insert(0,f"Rs.{self.taxofcosmetics}")
            self.etax_grocery.delete(0,END)
            self.etax_grocery.insert(0,f"Rs.{self.taxofgrocery}")
            self.etax_others.delete(0,END)
            self.etax_others.insert(0,f"Rs.{self.taxofothers}")

                # Calculte tptal Iteams
            self.iteams = int(self.esoap.get()) + int(self.ecream.get()) + int(self.efacewash.get()) + int(self.ehair_Spray.get()) + int(self.ebody_lotion.get()) + int(self.erice.get()) + int(self.efood_oil.get()) + int(self.edaal.get()) + int(self.ewheat.get()) + int(self.esuger.get()) + int(self.emaza.get()) + int(self.ecoke.get()) + int(self.efrooti.get()) + int(self.enimkos.get()) + int(self.ebiscuits.get()) 

                # if user buy nothing the flag is set to 1 otherwise flag is set to 2
            if self.iteams == 0:
                self.flag = 1
            else:
                self.flag = 2
            
            # if flag value isn't more than 0 means customer details are not entered
        else:
            messagebox.showerror("Customer Details","Please Enter Customer Details...")


    def create_bill(self):
            # check if user entered customer details or not
        if self.flag > 0:
                # check if user buy atleast one iteam/more iteams or not
            if self.flag > 1:

                # generate bill
                self.textarea.delete(1.0,END)

                self.enter_customer_deatils()

                self.textarea.config(state="normal")
                
                    # Enter cosmetic Details into Bill Area
                if int(self.esoap.get()) > 0:
                    self.textarea.insert(END,f"\nBath soap   \t\t\t {self.esoap.get()} \t    {int(self.esoap.get())*30}") 
                if int(self.ecream.get()) > 0:
                    self.textarea.insert(END,f"\nFace Cream  \t\t\t {self.ecream.get()} \t    {int(self.ecream.get())*150}")
                if int(self.efacewash.get()) > 0:
                    self.textarea.insert(END,f"\nFace Wash   \t\t\t {self.efacewash.get()} \t    {int(self.efacewash.get())*120}")
                if int(self.ehair_Spray.get()) > 0:
                    self.textarea.insert(END,f"\nHair Spray  \t\t\t {self.ehair_Spray.get()} \t    {int(self.ehair_Spray.get())*200}")
                if int(self.ebody_lotion.get()) > 0:
                    self.textarea.insert(END,f"\nBody Lotion \t\t\t {self.ebody_lotion.get()} \t    {int(self.ebody_lotion.get())*250}")

                    # Enter Grocery Details into Bill Area
                if int(self.erice.get()) > 0:
                    self.textarea.insert(END,f"\nRice        \t\t\t {self.erice.get()} \t    {int(self.erice.get())*60}") 
                if int(self.efood_oil.get()) > 0:
                    self.textarea.insert(END,f"\nFood Oil    \t\t\t {self.efood_oil.get()} \t    {int(self.efood_oil.get())*150}")
                if int(self.edaal.get()) > 0:
                    self.textarea.insert(END,f"\nDaal        \t\t\t {self.edaal.get()} \t    {int(self.edaal.get())*90}")
                if int(self.ewheat.get()) > 0:
                    self.textarea.insert(END,f"\nWheat       \t\t\t {self.ewheat.get()} \t    {int(self.ewheat.get())*40}")
                if int(self.esuger.get()) > 0:
                    self.textarea.insert(END,f"\nSugar       \t\t\t {self.esuger.get()} \t    {int(self.esuger.get())*45}")

                    # Enter Others Details into Bill Area
                if int(self.emaza.get()) > 0:
                    self.textarea.insert(END,f"\nMaza        \t\t\t {self.emaza.get()} \t    {int(self.emaza.get())*60}") 
                if int(self.ecoke.get()) > 0:
                    self.textarea.insert(END,f"\nCoke        \t\t\t {self.ecoke.get()} \t    {int(self.ecoke.get())*70}")
                if int(self.efrooti.get()) > 0:
                    self.textarea.insert(END,f"\nFrooti      \t\t\t {self.efrooti.get()} \t    {int(self.efrooti.get())*50}")
                if int(self.enimkos.get()) > 0:
                    self.textarea.insert(END,f"\nNimkos      \t\t\t {self.enimkos.get()} \t    {int(self.enimkos.get())*20}")
                if int(self.ebiscuits.get()) > 0:
                    self.textarea.insert(END,f"\nBiscuits    \t\t\t {self.ebiscuits.get()} \t    {int(self.ebiscuits.get())*25}")

                    # Enter total Details
                self.textarea.insert(END,"\n===========================================")

                self.textarea.insert(END,f"\nSub Total     : \t\t\t\t    {self.sub_total}")

                self.textarea.insert(END,"\n===========================================")

                if self.taxofcosmetics > 0 :
                    self.textarea.insert(END,f"\nCosmetics Tax : \t\t\t\t    {self.taxofcosmetics}")
                if self.taxofgrocery > 0 :
                    self.textarea.insert(END,f"\nGrocery Tax   : \t\t\t\t    {self.taxofgrocery}")
                if self.taxofothers > 0 :
                    self.textarea.insert(END,f"\nOther Tax     : \t\t\t\t    {self.taxofothers}")

                self.textarea.insert(END,"\n===========================================")

                self.textarea.insert(END,f"\nTotal         : \t\t\t\t    {self.total_bill}")

                self.textarea.insert(END,"\n===========================================")

                self.textarea.insert(END,"\n              THANK YOU ....               ")


                self.textarea.config(state="disabled")

                    # ask user for save bill
                if messagebox.askyesno("Bill","Do yo want to save the bill ??"):
                    # Generate txt file of bill
                    file_path = os.path.join("Bills", f"{self.ebill_No.get()}.txt")
                    if not os.path.exists(file_path):
                        with open(file_path, 'w') as file:
                            file.write(self.textarea.get(1.0, END))

                        messagebox.showinfo("Bill save",f"Bill No : {self.ebill_No.get()} Saved Successfully...")

                        # Store Data into Database.. 
                    sql = "INSERT INTO BILL(Customer_Name, Phone_No, Bill_No, Items, Sub_Total, Tax, Total) VALUES ('%s','%s','%s','%s','%s','%s','%s')" 
                    args = (self.ename.get(), self.ephone.get(), self.ebill_No.get(), self.iteams, self.sub_total, self.total_tax, self.total_bill)

                    mycursor.execute(sql % args)
                    mydb.commit()
            
            else: 
                    messagebox.showerror("Iteams","At least one item must be purchased.")
        
        else:
            messagebox.showerror("Customer Details","Please Enter Customer Details...")

    
    def clear(self):
        if messagebox.askokcancel("clear","Do you want to clear ?"):
                # Clear Customer Details
            self.ename.delete(0,END)
            self.ephone.delete(0,END)
            self.ebill_No.delete(0,END)

                # Clear Cosmetic Product Details
            self.esoap.delete(0,END)
            self.ecream.delete(0,END)
            self.efacewash.delete(0,END)
            self.ehair_Spray.delete(0,END)
            self.ebody_lotion.delete(0,END)

                # Clear Grocery Product Details
            self.erice.delete(0,END)
            self.efood_oil.delete(0,END)
            self.edaal.delete(0,END)
            self.ewheat.delete(0,END)
            self.esuger.delete(0,END)

                # Clear Other Product Details
            self.emaza.delete(0,END)
            self.ecoke.delete(0,END)
            self.efrooti.delete(0,END)
            self.enimkos.delete(0,END)
            self.ebiscuits.delete(0,END)

                # Clear Menu details
            self.et_cosmetics.delete(0,END)
            self.et_grocery.delete(0,END)
            self.et_others.delete(0,END)

            self.etax_cosmetics.delete(0,END)
            self.etax_grocery.delete(0,END)
            self.etax_others.delete(0,END)

                # set product data to initial state
            self.set_data()
                # set Bill area to initial state
            self.set_bill()

    def exit(self):
            # exit from the sofware
        root.destroy()

root = Tk()

Software = Billingsoftware(root)

root.mainloop()