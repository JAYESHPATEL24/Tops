from tkinter import Entry,END
import random
from datetime import datetime

class PlaceholderEntry(Entry):
    def __init__(self, master=None, placeholder="", default_value = "0", validate = None, validatecommand = None,*args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.placeholder = placeholder
        self.default_value = default_value
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
    def enter(self, customer_inputs):
        print("enter")

    def set_bill(self,textarea):
        self.textarea = textarea
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
        
        


def genreate_bill_no():
    return random.randint(1000,999999)

def purchase_datetime():
    return datetime.now()

