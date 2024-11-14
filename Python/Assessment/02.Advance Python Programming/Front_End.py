from tkinter import *
from Back_End import *


    # Base Window class to set up the main application window class Window
class Window:
    def __init__(self,root):
        self.root = root
             # Set the window title
        self.root.title("BILLING SOFTWARE")
            # Set window to full screen
        self.root.geometry(f"{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}+{-7}+{0}")


    # Class for the title section of the window
class Title(Window):
    def __init__(self, root):
        super().__init__(root)
        self.title()

        # Method to create the title label def title
    def title(self):
        title = Label(self.root, text="Billing Software", font=("times new roman", 25, "bold"), bg="#074463", fg='white', bd=12, relief=GROOVE, pady=2)
        title.pack(fill=X)

class Bill_Textarea(Title):
    def __init__(self, root):
        super().__init__(root)
            # Create the bill area
        self.create_bill_area() 
            # Create Click_Button instance with textarea
        self.clickbutton = Click_Button(self.textarea,self.root)
            # Set the initial bill
        self.clickbutton.set_bill()
    

    def create_bill_area(self):
            # bill area section
        self.bill = Frame(self.root, bd=5, relief=GROOVE)
        self.bill.place(x=1155, y=157,width=380, height=400 )

        bill_Area = Label(self.bill, text="Bill  Area", font=("arial", 12, "bold"), bd=5, relief=GROOVE).pack(fill=X)

            # create a Scrollbar for bill area
        scrolling = Scrollbar(self.bill,orient=VERTICAL)
            # create a text area for bill
        self.textarea=Text(self.bill,yscrollcommand=scrolling.set)
        scrolling.pack(side=RIGHT,fill=Y)
        scrolling.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)    


    # CustomerDetails class to set up customer details UI elements class
class CustomerDetails(Bill_Textarea):
    def __init__(self, root):
        super().__init__(root)
            # Create the customer details frame
        self.create_customerframe()
            # List to hold customer entry widgets
        self.customerentries = []
            # Create labels and entry widgets for customer details
        self.Customerdetails_Labels_Entries()
            # Create the enter button
        self.enter_button()

    def create_customerframe(self):
            # Create a labeled frame for customer details
        self.Customer_details_frame = LabelFrame(root, text=" Customer Details ", font=("arial", 12, "bold"), bg="#074463", fg="gold", relief=GROOVE, bd=5)
        self.Customer_details_frame.place(x=0, y=70, relwidth=1)
  
    
    def Customerdetails_Labels_Entries(self):
            # Define placeholders and validation commands for entries
        label_placeholder = { "Customer Name" : "Enter Customer Name",
                               "Phone No." : "Enter Phone Number",
                                "Bill No." : f"{genreate_bill_no():06d}" }
        

        cmds = { "Customer Name" : (self.root.register(Validation.validate_name), '%d', '%P'),
                 "Phone No." : (self.root.register(Validation.validate_phone), '%d', '%P'),
                 "Bill No." : (self.root.register(Validation.validate_bill_no), '%d', '%P') }
        
        index = 0
        for labelname,entryplaceholder in label_placeholder.items():
                # Create and place labels for customer details
            label = Label(self.Customer_details_frame, text=labelname, font=("times new roman",15,"bold"), bg="#074463",fg="White")
            label.grid(row=0, column=index*2, padx=20, pady=5)

            if labelname == "Bill No.":
                entry = Entry(self.Customer_details_frame, font=("Arial",15), bd=5, width=22, validate="key", validatecommand=cmds[labelname])
                entry.grid(row=0, column=index*2+1, padx=20, pady=5)
                entry.insert(0,entryplaceholder)

            else: 
                entry = PlaceholderEntry(self.Customer_details_frame, placeholder=entryplaceholder,fg="#708090",font=("Arial",15), bd=5, width=22,  validate="key", validatecommand=cmds[labelname])
                entry.grid(row=0, column=index*2+1, padx=20, pady=5)

                # Add the entry to the list of customer entries       
            self.customerentries.append(entry)
            index += 1

    def enter_button(self):
            # Create and place the Enter button
        enterbutton = Button(self.Customer_details_frame, text=" Enter ", font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=10, relief=GROOVE, command=lambda : self.clickbutton.enter(self.get_customerdetails()))
        enterbutton.grid(row=0, column=6, padx=22, pady=5)

        # Retrieve customer details from entries
    def get_customerdetails(self):
        customer = []
        for i in range(3):
            customer.append(self.customerentries[i].get())
        return customer


class Cosmetic(CustomerDetails):
    def __init__(self, root):
        super().__init__(root)
            # Create the frame for cosmetic products
        self.create_cosmeticframe()
            # List to store entry widgets for cosmetics
        self.cosmeticentries = []
            # List of cosmetic product names
        self.cosmeticlabels = ["Bath Soap","Face Cream","Face Wash", "Hair Spray", "Body Lotion"]
            # Generate labels and entry fields for cosmetic products
        self.cosmeticproducts_Labels_Entries()

        # Create and configure the frame for cosmetics
    def create_cosmeticframe(self):
        self.cosmetics_products_frame = LabelFrame(self.root, text=" Cosmetics ", font=("arial", 12, "bold"), bd=5, bg="#074463", fg="gold", relief=GROOVE)
        self.cosmetics_products_frame.place(x=0, y=157, width=380, height=400)

        # Create labels and entry widgets for each cosmetic product
    def cosmeticproducts_Labels_Entries(self):
        
        index = 0
        for labelname in self.cosmeticlabels:
                # Create label for each cosmetic product
            label = Label(self.cosmetics_products_frame, text= labelname, font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=10)
            label.grid(row=index, column=0, padx=20, pady=20)
 
                # Create an entry field for each cosmetic product with a placeholder
            entry = PlaceholderEntry(self.cosmetics_products_frame, fg="#708090", placeholder="0", font=("arial",12), width=15, bd=5, validate="key", validatecommand=(self.root.register(Validation.validate_Products), '%d', '%P'))
            entry.grid(row=index, column=1, padx=20, pady=20)

                # Add entry to the list of cosmetic entries
            self.cosmeticentries.append(entry)
            index += 1

        # Get the details of all cosmetic products entered by the user
    def get_cosmeticdetails(self):
            # Dictionary to store the product details
        cosmetics = {}
        for index, label in enumerate(self.cosmeticlabels):
                # If the entry is empty, set the quantity to 0
            if self.cosmeticentries[index].get() == "":
                cosmetics[label] = 0
            else:
                cosmetics[label] = int(self.cosmeticentries[index].get())
        return cosmetics
         

class Grocery(Cosmetic):
    def __init__(self, root):
        super().__init__(root)
            # Create the frame for Grocery products
        self.create_groceryframe()
            # List to store entry widgets for Grocery
        self.groceryentries = []
            # List of Gocery product names
        self.geocerylabels = ["Rice","Food Oil","Daal","Wheat","Sugar"]
            # Generate labels and entry fields for Grocery products
        self.groceryproducts_Labels_Entries()

        # Create and configure the frame for Grocery
    def create_groceryframe(self):
        self.grocery_products_frame = LabelFrame(self.root, text=" Grocery ", font=("arial", 12, "bold"), bd=5, bg="#074463", fg="gold", relief=GROOVE)
        self.grocery_products_frame.place(x=385, y=157, width=380, height=400)

        # Create labels and entry widgets for each Grocery product
    def groceryproducts_Labels_Entries(self):
        
        index = 0
        for labelname in self.geocerylabels:
                # Create label for each Grocery product
            label = Label(self.grocery_products_frame, text= labelname, font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=10)
            label.grid(row=index, column=0, padx=20, pady=20)
 
                # Create an entry field for each Grocery product with a placeholder
            entry = PlaceholderEntry(self.grocery_products_frame, placeholder="0", fg="#708090", font=("arial",12), width=15, bd=5, validate="key", validatecommand=(self.root.register(Validation.validate_Products), '%d', '%P'))
            entry.grid(row=index, column=1, padx=20, pady=20)

                # Add entry to the list of Grocery entries
            self.groceryentries.append(entry)
            index += 1
        
        # Get the details of all Grocery products entered by the user
    def get_grocerydetails(self):
            # Dictionary to store the product details
        grocery = {}
        for index, label in enumerate(self.geocerylabels):
                # If the entry is empty, set the quantity to 0
            if self.groceryentries[index].get() == "":
                grocery[label] = 0
            else:
                grocery[label] = int(self.groceryentries[index].get())
        return grocery


class Other_products(Grocery):
    def __init__(self, root):
        super().__init__(root)
            # Create the frame for Other products
        self.create_otherframe()
            # List to store entry widgets for other products 
        self.otherentries = []
            # List of other product names
        self.otherproductslabels = ["Maza", "Coke", "Frooti", "Nimkos", "Biscuits"]
            # Generate labels and entry fields for other products
        self.otherproducts_Labels_Entries()

        # Create and configure the frame for Other Products
    def create_otherframe(self):
        self.other_products_frame = LabelFrame(self.root, text=" Others ", font=("arial", 12, "bold"), bd=5, bg="#074463", fg="gold", relief=GROOVE)
        self.other_products_frame.place(x=770, y=157, width=380, height=400)

        # Create labels and entry widgets for each Other product
    def otherproducts_Labels_Entries(self):
        
        index = 0
        for labelname in self.otherproductslabels:
                # Create label for each Other product
            label = Label(self.other_products_frame, text= labelname, font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=10)
            label.grid(row=index, column=0, padx=20, pady=20)
 
                # Create an entry field for each Other product with a placeholder
            entry = PlaceholderEntry(self.other_products_frame, placeholder="0",fg="#708090", font=("arial",12), width=15, bd=5, validate="key", validatecommand=(self.root.register(Validation.validate_Products), '%d', '%P'))
            entry.grid(row=index, column=1, padx=20, pady=20)

                # Add entry to the list of cosmetic entries
            self.otherentries.append(entry)
            index += 1

        # Get the details of all cosmetic products entered by the user    
    def get_otherproductsdetails(self):
            # Dictionary to store the product details
        otherproducts = {}
        for index, label in enumerate(self.otherproductslabels):
                # If the entry is empty, set the quantity to 0
            if self.otherentries[index].get() == "":
                otherproducts[label] = 0
            else:
                otherproducts[label] = int(self.otherentries[index].get())
        return otherproducts
    

class Bill_Menu(Other_products):
    def __init__(self, root):
        super().__init__(root)
            # Create the frame for the Bill Menu
        self.create_menu_frame()  
            # List to store entry widgets for the bill details
        self.menuentries = []  
            # Generate labels and entry fields for bill information
        self.menu_Labels_Entries()
            # Create buttons for generating and managing the bill  
        self.Menu_buttons()  
        
        # Create and configure the frame for the Bill Menu section
    def create_menu_frame(self):
        self.menu_frame = LabelFrame(self.root, text=" Bill Menu ", font=("arial", 12, "bold"), bd=5, bg="#074463", fg="gold", relief=GROOVE)
        self.menu_frame.place(x=0, y=563, relwidth=1, relheight=1)

        # Create labels and entry widgets for displaying bill details
    def menu_Labels_Entries(self):
            # Labels
        labels = ["Total Cosmetics", "Total Grocery", "Others Total", "Cosmetics Tax", "Grocery Tax", "Others Tax"]
         
        index = 0
        for labelname in labels:
                # create labels for taxes and total price
            label = Label(self.menu_frame, text= labelname, font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=10)
            label.grid(row=index%3, column=(index//3)*2, padx=30, pady=5)

                # create entries for taxes and total price
            entry = Entry(self.menu_frame, fg = "black", font=("arial",12), width=15, bd=5)
            entry.grid(row=index%3, column=((index//3)*2)+1, padx=30, pady=5)
            entry.insert(0,"Rs.00.00")

                # Add entry to the list of menu entries
            self.menuentries.append(entry)
            index += 1

            # Create a label for the "Total Amount" 
        label = Label(self.menu_frame, text="Total Amount", font=("times new roman", 15, "bold"), bg="#074463", fg="White", bd=5, width=12) 
        label.grid(row=3, column=0, padx=5, pady=10, columnspan=2, sticky='e') 

            # Create a entry for the "Total Amount" 
        total_amount_entry = Entry(self.menu_frame, fg = "black", font=("arial", 12), width=20, bd=5) 
        total_amount_entry.grid(row=3, column=2, columnspan=2, padx=10, pady=8,sticky='w')
        total_amount_entry.insert(0,"Rs.00.00")
        # total_amount_entry.config(state="disabled")
            # add entry to the list of menu entries
        self.menuentries.append(total_amount_entry)

        # Create buttons for the bill menu to perform actions like total calculation, bill generation, saving, etc.
    def Menu_buttons(self): 
            # Define a dictionary of button labels and corresponding commands (actions)
        Buttons = {"Total Bill" : lambda : self.clickbutton.total_bill(self.get_cosmeticdetails(),self.get_grocerydetails(),self.get_otherproductsdetails(),self.menuentries) , 
                   "Generate Bill" : lambda : self.clickbutton.generate_bill(self.get_customerdetails()), 
                   "Save Bill" : lambda : self.clickbutton.save_bill(self.get_customerdetails()), 
                   "Search Bill" : lambda : self.clickbutton.search_bill(root), 
                   "Clear" : lambda : self.clickbutton.clear(self.customerentries, self.cosmeticentries, self.groceryentries, self.otherentries, self.menuentries), 
                   "Exit" : lambda : self.clickbutton.exit(self.root)
            }

        index = 0
            # loop to create buttons with commands
        for button,cmd in Buttons.items():
            button = Button(self.menu_frame, text=button, font=("times new roman",15,"bold"), bg="#074463", fg="White", bd=5, width=15, relief=GROOVE, command=cmd)
            button.grid(row=(index // 3) *2 , column=index%3+4, padx=20, pady=5, rowspan=2, sticky="ew")
            index += 1


    # Class for the billing UI
class Bill_UI(Bill_Menu):
    def __init__(self, root):
        super().__init__(root)


    # create the tkinter main window
root = Tk()

    # create an object of the class.
go = Bill_UI(root)

root.mainloop()