from tkinter import Entry,END, Label, Text, Toplevel,messagebox,Button, Tk
import random
from datetime import datetime
import os
from Database import *

    # PlaceholderEntry class
class PlaceholderEntry(Entry):
    def __init__(self, master=None, placeholder="", fg="black", validate = None, validatecommand = None,*args, **kwargs):
        super().__init__(master, *args, **kwargs)
            # Initialize attributes for placeholder, text color, and validation commands
        self.placeholder = placeholder
        self.validate = validate
        self.validatecommand = validatecommand
        self.fg = fg

            # Insert the placeholder text and set the initial foreground color
        self.insert(0, self.placeholder)
        self.config(fg=self.fg)

            # Bind the focus events to show/hide the placeholder text
        self.bind("<FocusIn>",self.on_click)
        self.bind("<FocusOut>",self.out)

        # Event handler for focus-in: clear the placeholder when clicked
    def on_click(self,event):
        if self.get() == self.placeholder or self.get() == "":
            self.delete(0,END)
            self.config(fg="black")
                # Apply validation if specified
            if self.validate:
                self.configure(validate="key", validatecommand=self.validatecommand)

        # Event handler for focus-out: if the entry is empty, revert to the placeholder text
    def out(self,event):
        if not self.get():
            # Insert the placeholder text
            self.insert(0, self.placeholder)
            self.config(fg=self.fg)

        # Reset the entry field to its placeholder state   
    def reset(self):
        self.delete(0, END)
        self.insert(0, self.placeholder)
        self.config(fg="#708090")

    # Validation class that contains methods to validate different fields like name, phone number, etc.
class Validation:
        # Method to validate a name (only allows letters and spaces)
    def validate_name(self,value): 
        return all(char.isspace() or char.isalpha() for char in value) or value == "" 
    
        # Method to validate a phone number (only digits and up to 10 characters)
    def validate_phone(self,value): 
        return value.isdigit() and len(value) <= 10  or value == ""
    
        # Method to validate a bill number (only digits and up to 6 characters)
    def validate_bill_no(self,value): 
        return value.isdigit() and len(value) <= 6 or value == ""
    
        # Method to validate the number of products (only digits and up to 3 characters)
    def validate_Products(self,value): 
        return value.isdigit() and len(value) <= 3  or value == ""


class Click_Button:
    def __init__(self,textarea,root):
            # Text area for displaying the bill
        self.textarea = textarea
            # Dictionary to hold all items purchased
        self.totaliteams = {}
            # Database object for saving and checking data
        self.database = Database()
            # Flag to track the status of the bill (0 = not started, 1 = initialized, 2 = generated)
        self.flag = 0

            # Dummy label to handle focus events
        self.dummy_label =Label(root, text="") 
        self.dummy_label.pack()
        

        # Method to initialize the bill with customer details like name, phone number, and bill number
    def enter(self, customer_inputs):

        self.customername = customer_inputs[0].title()
        self.phoneno = customer_inputs[1]

            # If bill number is empty, set it to 0; otherwise, format it to a 6-digit string
        if customer_inputs[2] == "":
            self.billno = 0
        else: 
            self.billno = f"{int(customer_inputs[2]):06d}"
        
            # Get current date and time for the bill
        self.datetime = self.bill_time()

            # Validate customer details
        if self.customername == "" or self.customername == "Enter Customer Name": 
            messagebox.showerror("Name Error","Please Enter Customer Name....!!!!!!!") 
        elif self.phoneno == "" or self.phoneno == "Enter Phone Number": 
            messagebox.showerror("Phone No Error","Please Enter Phone No....!!!") 
        elif len(self.phoneno) != 10: 
            messagebox.showerror("Phone Number Error", f"Only {len(self.phoneno)} digits entered..!! \nPhone number must have 10 digits.") 
        elif self.billno == 0: 
            messagebox.showerror("Bill No Error","Please Enter a Bill No ...!!! ")
        elif self.database.checkdata(self.billno):
                # Check if bill number already exists in the database
            messagebox.showerror("Bill Error",f"Bill {self.billno} already Exists......")

        else:
                # Set focus on the dummy label (hack to remove focus from entry fields)
            self.dummy_label.focus_set()

                # Initialize bill text area
            self.textarea.config(state="normal")

            self.textarea.delete(1.0,END)
            
            self.textarea.insert(1.5,"\t******* Welcome To Store *******    \n")
            self.textarea.insert(END,f"\n Bill No       : {self.billno}")
            self.textarea.insert(END,f"\n Customer Name : {self.customername}")
            self.textarea.insert(END,f"\n Phone No      : {self.phoneno}")
            self.textarea.insert(END,f"\n Date          : {self.datetime}")
            self.textarea.insert(END,"\n===========================================")
            self.textarea.insert(END,"\nProduct \t\t Qty/ \t   Price   \t Total")
            self.textarea.insert(END,"\n        \t\t  Kg  \t (Unit/Kg) \t Price")
            self.textarea.insert(END,"\n===========================================")

            self.textarea.config(state="disabled")

                # Set flag to indicate that the bill has been initialized
            self.flag = 1
        
        # Method to calculate the total bill based on the purchased items and quantities
    def total_bill(self,cosmeticiteams,groceryiteams,otherproductsiteams,menuentries):
        if self.flag > 0:
                # Set focus on the dummy label (hack to remove focus from entry fields)
            self.dummy_label.focus_set()

                # Combine all the purchased items into a single dictionary
            self.totaliteams = {**cosmeticiteams, **groceryiteams, **otherproductsiteams}

                # Define the price list for items
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

                # Dictionary to store total price for each item
            self.totalpriceiteams = {}

                # total quantity of items purchased
            self.totaliteams_qty = 0

                # Calculate the total price for each item and total iteams quantity
            for iteam, qty in self.totaliteams.items():
                self.totaliteams_qty += qty
                if iteam in self.iteam_price:
                    self.totalpriceiteams[iteam] = qty * self.iteam_price[iteam]

                # Separate the total prices based on categories
            totalpricecosmetics = 0
            totalpricegrocery = 0
            totalpriceotherproducts = 0

                # Overall total price 
            self.total = 0
            index = 0
            for price in self.totalpriceiteams.values():
                self.total += price
                    # Categorize the prices based on item index
                if index<5:
                    totalpricecosmetics += price
                elif index<10:
                    totalpricegrocery += price
                elif index<15:
                    totalpriceotherproducts += price
                index += 1

                # Calculate taxes for different categories
            taxofcosmetics = round(totalpricecosmetics * 0.18,2)
            taxofgrocery = round(totalpricegrocery * 0.05,2)
            taxofotherproducts = round(totalpriceotherproducts * 0.12,2)

                # Calculate the total amount including taxes
            self.totalamount = round((self.total + taxofcosmetics + taxofgrocery + taxofotherproducts),2)

                # Prepare the inputs for the menu entries
            self.menuentriesinputs = [totalpricecosmetics, totalpricegrocery, totalpriceotherproducts, taxofcosmetics, taxofgrocery, taxofotherproducts, self.totalamount]

            self.menuentries = menuentries


                # Update the menu entries with calculated values           
            for index,entry in enumerate(self.menuentries):
                # entry.config(state="normal")
                entry.delete(0, END)
                entry.config(fg="black")

                entry.insert(0, f"Rs.{self.menuentriesinputs[index]}") 
                # entry.config(state="disabled")
        
        else:
            messagebox.showerror("Details Error","Please Enter Customer details....!!!!!!!")
    

        # Method to generate the final bill after customer details and items are entered
    def generate_bill(self, customer_inputs):
        if self.flag > 0:

            if self.totaliteams_qty == 0:
                    messagebox.showerror("Iteam Error","Please purchase at least one item before generating the bill.....!!!!!!!")
                
            else:
                    # Set focus on the dummy label (hack to remove focus from entry fields)
                self.dummy_label.focus_set()
                    # Clear previous bill content
                self.textarea.delete(1.0,END)
                    # Re-enter customer details into the bill
                self.enter(customer_inputs)

                    # Start writing item details into the bill
                self.textarea.config(state="normal")

                for iteam, qty in self.totaliteams.items():
                    if self.totaliteams[iteam] == 0:
                        continue
                    else:
                        self.textarea.insert(END,f"\n{iteam}  \t\t  {qty} \t   {self.iteam_price[iteam]:5d}\t  {self.totalpriceiteams[iteam]:7d}") 

                self.textarea.insert(END,"\n===========================================")
                self.textarea.insert(END,f"\nSub Total          : \t\t\t\tRs.{self.total:7d}")
                self.textarea.insert(END,"\n===========================================")
                self.textarea.insert(END,f"\nCosmetics Tax      : \t\t\t\tRs.{self.menuentriesinputs[3]:7.2f}")
                self.textarea.insert(END,f"\nGrocery Tax        : \t\t\t\tRs.{self.menuentriesinputs[4]:7.2f}")
                self.textarea.insert(END,f"\nother Products Tax : \t\t\t\tRs.{self.menuentriesinputs[5]:7.2f}")
                self.textarea.insert(END,"\n===========================================")
                self.textarea.insert(END,f"\nTotal Amount       : \t\t\t\tRs.{self.totalamount:7.2f}")
                self.textarea.insert(END,"\n===========================================")
                self.textarea.insert(END,"\n         THANK YOU......       ")
                
                self.textarea.config(state="disabled")
                    # Mark the bill as generated
                self.flag = 2
        
        else:
            messagebox.showerror("Details Error","Please Enter Customer details....!!!!!!!")

        # method for Save the bill to a file and the database
    def save_bill(self,customerdata):

        if self.flag > 0:

            if self.flag > 1 : 

                if messagebox.askyesno("Save", "Do you want to save the Bill?"):

                        # Create a directory for storing the bills if it doesn't exist
                    if not os.path.exists("Customer Bill"):
                        os.makedirs("Customer Bill")

                    file_path = os.path.join("Customer Bill", f"{self.billno}.txt") 

                        # Check if the file exists and save if it does not 
                    if not os.path.exists(file_path): 
                        with open(file_path, 'w') as file: 
                            file.write(self.textarea.get(1.0, END))
                        
                        # Save the customer data and the total amount into the database
                    self.database.database_dataentry(customerdata,self.totalamount,self.totaliteams, self.totaliteams_qty)

                    messagebox.showinfo("Save bill", "Your Bill Save Successfully....!!!")
            
            else:
                messagebox.showerror("Bill Error","Please Generate a Bill before saving the bill....!!!!!!!")
        
        else:
            messagebox.showerror("Details Error","Please Enter Customer details....!!!!!!!")

    
    def search_bill(self, root):
        """ This function will close the current main window and open a new window for searching a bill by Bill No. """
        
        # Hide the main window
        root.withdraw()

        # Create a new window for searching the bill
        search_window = Toplevel()
        search_window.title("Search Bill")
        search_window.config(bg="#074463")
        search_window.geometry("450x650")  

            # Create a label and an entry widget to take the bill number as input
        bill_label = Label(search_window, text="Bill No:", font=("times new roman", 15, "bold"), bg="#074463", fg="White")
        bill_label.pack(pady=20)

        bill_entry = PlaceholderEntry(search_window, placeholder="Enter Bill No", font=("arial", 12), width=30)
        bill_entry.pack(pady=10)

            # Create a text area to show the bill content
        bill_text_area = Text(search_window, font=("arial", 12), width=70, height=20)
        bill_text_area.pack(pady=20, padx=25)  # Add horizontal padding

            # Function to search for the bill based on the entered Bill No.
        def search_and_display_bill():
            bill_no = bill_entry.get()
            if bill_no == "" or bill_no == "Enter Bill No":
                messagebox.showerror("Error", "Please enter a Bill No.")
                return

                # Check if the bill file exists in the "Customer Bills" directory
            file_path = os.path.join("Customer Bill", f"{bill_no}.txt")
            if os.path.exists(file_path):
                with open(file_path, 'r') as file:
                    bill_content = file.read()
                    bill_text_area.delete(1.0, END)
                    bill_text_area.insert(END, bill_content)
            else:
                messagebox.showerror("Error", "Bill not found.")

            # Add a button to search and display the bill
        search_button = Button(search_window, text="Search Bill", font=("arial", 12, "bold"), command=search_and_display_bill)
        search_button.pack(pady=10)

            # Back button to return to the main window
        def go_back():
                # Close the search window
            search_window.destroy()  
                # Re-show the main window
            root.deiconify()  

            # Add a button to back to the main bill window
        back_button = Button(search_window, text="Back", font=("arial", 12, "bold"), command=go_back)
        back_button.pack(pady=10)

        # method for clear all fields
    def clear(self, customerentries, cosmeticentries, groceryentries, otherentries, menuentries): 
        
        if messagebox.askyesno("Clear", "Are you sure you want to clear the form?"):
            self.dummy_label.focus_set()
            # Clear all the entries in the customer details, cosmetics, grocery, and other products sections 
            for entry in customerentries + cosmeticentries + groceryentries + otherentries: 
                if entry == customerentries[2]:
                    entry.delete(0, END) 
                    entry.insert(0, f"{genreate_bill_no():06d}")
                else:
                    entry.reset() 
            # Reset all the bill menu fields 
            for entry in menuentries: 
                entry.delete(0, END) 
                entry.insert(0, "Rs.00.00") 
            # Reset the bill area text 
            self.textarea.config(state="normal") 
            self.textarea.delete(1.0, END) 
            self.set_bill() 
            self.textarea.config(state="disabled")
        
        # method for exit main window
    def exit(self,root):
        if messagebox.askyesno("Exit", "Do you really want to exit?"):
            root.destroy()

        # method for initilize bill in textarea
    def set_bill(self):

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

        # method for current date and time
    def bill_time(self):
        now = datetime.now().strftime("%d/%m/%Y (%I.%M %p)")
        return now
        
        # method for generate unique bill no
def genreate_bill_no():
    databse = Database()
    while True: 
        number = random.randint(1000, 999999) 
        if not databse.checkdata(number): 
            return number


