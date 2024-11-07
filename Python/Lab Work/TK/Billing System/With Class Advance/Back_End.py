from tkinter import Entry,END,messagebox
import random
from datetime import datetime

class PlaceholderEntry(Entry):
    def __init__(self, master=None, placeholder="", validate = None, validatecommand = None,*args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.placeholder = placeholder
        self.validate = validate
        self.validatecommand = validatecommand
        self.insert(0, self.placeholder)
        self.config(fg="#708090")
        self.bind("<FocusIn>",self.on_click)
        self.bind("<FocusOut>",self.out)

    def on_click(self,event):
        if self.get() == self.placeholder:
            self.delete(0,END)
            self.config(fg="black")
            if self.validate:
                self.configure(validate="key", validatecommand=self.validatecommand)

    def out(self,event):
        if not self.get():
            self.insert(0, self.placeholder)
            self.config(fg="#708090")
    
class Validation:
    def validate_name(self,value): 
        return all(char.isspace() or char.isalpha() for char in value) or value == "" 
    def validate_phone(self,value): 
        return value.isdigit() and len(value) <= 10  or value == ""
    def validate_bill_no(self,value): 
        return value.isdigit() and len(value) <= 6 or value == ""
    def validate_Products(self,value): 
        return value.isdigit() and len(value) <= 3  or value == ""


class Click_Button:
    def __init__(self,textarea):
        self.textarea = textarea

    def enter(self, customer_inputs):

        self.customername = customer_inputs[0].title()
        self.phoneno = customer_inputs[1]
        if customer_inputs[2] == "":
            self.billno = 0
        else: 
            self.billno = f"{int(customer_inputs[2]):06d}"
        
        self.datetime = self.bill_time()

        if self.customername == "" or self.customername == "Enter Customer Name": 
            messagebox.showerror("Name Error","Please Enter Customer Name....!!!!!!!") 
        elif self.phoneno == "" or self.phoneno == "Enter Phone Number": 
            messagebox.showerror("Phone No Error","Please Enter Phone No....!!!") 
        elif len(self.phoneno) != 10: 
            messagebox.showerror("Phone Number Error", f"Only {len(self.phoneno)} digits entered..!! \nPhone number must have 10 digits.") 
        elif self.billno == 0: 
            messagebox.showerror("Bill No Error","Please Enter a Bill No ...!!! ") 
        else:
                # initilize bill
            self.textarea.config(state="normal")

            self.textarea.delete(1.0,END)
            
            self.textarea.insert(1.5,"\t******* Welcome To Store *******    \n")
            self.textarea.insert(END,f"\n Bill No       : {self.customername}")
            self.textarea.insert(END,f"\n Customer Name : {self.phoneno}")
            self.textarea.insert(END,f"\n Phone No      : {self.billno}")
            self.textarea.insert(END,f"\n Date          : {self.datetime}")
            self.textarea.insert(END,"\n===========================================")
            self.textarea.insert(END,"\nProduct \t\t Qty/ \t   Price   \t Total")
            self.textarea.insert(END,"\n        \t\t  Kg  \t (Unit/Kg) \t Price")
            self.textarea.insert(END,"\n===========================================")

            self.textarea.config(state="disabled")
        
    def total_bill(self,cosmeticiteams,groceryiteams,otherproductsiteams,menuentries):
        self.totaliteams = {**cosmeticiteams, **groceryiteams, **otherproductsiteams}
        self.iteam_price = {
            "Bath Soap" : 30,
            "Face Cream" : 150,
            "Face Wash" : 120, 
            "Hair Spray" : 200, 
            "Body Lotion" : 250,
            "Rice" : 60,
            "Food Oil" : 150,
            "Daal" : 90,
            "Wheat" : 40,
            "Sugar" : 45,
            "Maza" : 60,
            "Coke" : 70, 
            "Frooti" : 50, 
            "Nimkos" : 20, 
            "Biscuits" : 25
        }

        totalpriceiteams = {}

        for iteam, qty in self.totaliteams.items():
            if iteam in self.iteam_price:
                totalpriceiteams[iteam] = qty * self.iteam_price[iteam]

        totalpricecosmetics = 0
        totalpricegrocery = 0
        totalpriceotherproducts = 0
        total = 0
        index = 0
        for price in totalpriceiteams.values():
            total += price
            if index<5:
                totalpricecosmetics += price
            elif index<10:
                totalpricegrocery += price
            elif index<15:
                totalpriceotherproducts += price
            index += 1

        taxofcosmetics = round(totalpricecosmetics * 0.18,2)
        taxofgrocery = round(totalpricegrocery * 0.05,2)
        taxofotherproducts = round(totalpriceotherproducts * 0.12,2)

        self.totalamount = total + taxofcosmetics + taxofgrocery + taxofotherproducts

        menuentriesinputs = [totalpricecosmetics, totalpricegrocery, totalpriceotherproducts, taxofcosmetics, taxofgrocery, taxofotherproducts, self.totalamount]

        self.menuentries = menuentries 
    
        for index,entry in enumerate(self.menuentries):
            entry.config(state="normal")
            entry.config(fg="black")
            entry.delete(0,END)
            entry.insert(0,f"Rs.{menuentriesinputs[index]}")
            entry.config(state="disabled")

        
    def set_bill(self):

            # initilize bill
        self.textarea.config(state="normal")

        self.textarea.delete(1.0,END)
        
        self.textarea.insert(1.5,"\t******* Welcome To Store *******    \n")
        self.textarea.insert(END,"\n Bill No       : ")
        self.textarea.insert(END,"\n Customer Name : ")
        self.textarea.insert(END,"\n Phone No      : ")
        self.textarea.insert(END,"\n Date          : ")
        self.textarea.insert(END,"\n===========================================")
        self.textarea.insert(END,"\nProduct \t\t Qty/ \t   Price   \t Total")
        self.textarea.insert(END,"\n        \t\t  Kg  \t (Unit/Kg) \t Price")
        self.textarea.insert(END,"\n===========================================")

        self.textarea.config(state="disabled")

    def bill_time(self):
        now = datetime.now().strftime("%d/%m/%Y (%I.%M %p)")
        return now
        

def genreate_bill_no():
    return random.randint(1000,999999)



