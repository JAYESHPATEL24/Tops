import tkinter as tk
from tkinter import ttk

class AppBase:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1600x800")
        self.root.title("Billing Software")
        self.root.config(bg="white")
        self.create_title()

    def create_title(self):
        title = tk.Label(self.root, text="Billing Software", font=("times new roman", 25, "bold"), bg="#074463", fg='white', bd=12, relief=tk.GROOVE, pady=2)
        title.pack(fill=tk.X)

class CustomerDetails(AppBase):
    def __init__(self, root):
        super().__init__(root)
        self.create_customer_details()

    def create_customer_details(self):
        Customer_details = tk.LabelFrame(self.root, text=" Customer Details ", font=("arial", 12, "bold"), bg="#074463", fg="gold", relief=tk.GROOVE, bd=5)
        Customer_details.place(x=0, y=70, relwidth=1)
        
        self.create_placeholder_entry(Customer_details, "Customer Name", 0, 0, "Enter your name")
        self.create_placeholder_entry(Customer_details, "Phone No.", 0, 2, "Enter your phone number")
        self.create_placeholder_entry(Customer_details, "Bill No.", 0, 4, "Enter your bill number")
        
        enter = tk.Button(Customer_details, text=" Enter ", font=("times new roman", 15, "bold"), bg="#074463", fg="White", bd=5, width=10, relief=tk.GROOVE)
        enter.grid(row=0, column=6, padx=22, pady=5)

    def create_placeholder_entry(self, parent, label_text, row, column, placeholder):
        label = tk.Label(parent, text=label_text, font=("times new roman", 15, "bold"), bg="#074463", fg="White")
        label.grid(row=row, column=column, padx=20, pady=5)
        
        entry = tk.Entry(parent, font=("Arial", 15), bd=5, width=22)
        entry.insert(0, placeholder)
        entry.config(fg='grey')
        entry.bind('<FocusIn>', lambda event: self.on_entry_click(event, entry, placeholder))
        entry.bind('<FocusOut>', lambda event: self.on_focusout(event, entry, placeholder))
        entry.grid(row=row, column=column + 1, padx=20, pady=5)
    
    @staticmethod
    def on_entry_click(event, entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, "end")  # delete all the text in the entry
            entry.config(fg='black')
    
    @staticmethod
    def on_focusout(event, entry, placeholder):
        if entry.get() == '':
            entry.insert(0, placeholder)
            entry.config(fg='grey')

class ProductSection:
    def __init__(self, root, title, items, x, y, width, height):
        self.frame = tk.LabelFrame(root, text=title, font=("arial", 12, "bold"), bd=5, bg="#074463", fg="gold", relief=tk.GROOVE)
        self.frame.place(x=x, y=y, width=width, height=height)
        self.create_items(items)

    def create_items(self, items):
        for i, (label_text, placeholder) in enumerate(items):
            label = tk.Label(self.frame, text=label_text, font=("times new roman", 15, "bold"), bg="#074463", fg="White", bd=5, width=10)
            label.grid(row=i, column=0, padx=20, pady=20)
            entry = tk.Entry(self.frame, font=("arial", 12), width=15, bd=5)
            entry.insert(0, placeholder)
            entry.config(fg='grey')
            entry.bind('<FocusIn>', lambda event, e=entry, p=placeholder: self.on_entry_click(event, e, p))
            entry.bind('<FocusOut>', lambda event, e=entry, p=placeholder: self.on_focusout(event, e, p))
            entry.grid(row=i, column=1, padx=20, pady=20)

    @staticmethod
    def on_entry_click(event, entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, "end")  # delete all the text in the entry
            entry.config(fg='black')

    @staticmethod
    def on_focusout(event, entry, placeholder):
        if entry.get() == '':
            entry.insert(0, placeholder)
            entry.config(fg='grey')

class BillingSoftware(CustomerDetails):
    def __init__(self, root):
        super().__init__(root)
        self.create_sections()

    def create_sections(self):
        cosmetics_items = [
            ("Bath Soap", "Enter quantity"),
            ("Face Cream", "Enter quantity"),
            ("Face Wash", "Enter quantity"),
            ("Hair Spray", "Enter quantity"),
            ("Body Lotion", "Enter quantity")
        ]
        ProductSection(self.root, "Cosmetics", cosmetics_items, 0, 157, 380, 400)
        
        grocery_items = [
            ("Rice", "Enter quantity"),
            ("Food Oil", "Enter quantity"),
            ("Daal", "Enter quantity"),
            ("Wheat", "Enter quantity"),
            ("Sugar", "Enter quantity")
        ]
        ProductSection(self.root, "Grocery", grocery_items, 385, 157, 380, 400)
        
        others_items = [
            ("Maza", "Enter quantity"),
            ("Coke", "Enter quantity"),
            ("Frooti", "Enter quantity"),
            ("Nimkos", "Enter quantity"),
            ("Biscuits", "Enter quantity")
        ]
        ProductSection(self.root, "Others", others_items, 770, 157, 380, 400)

if __name__ == "__main__":
    root = tk.Tk()
    app = BillingSoftware(root)
    root.mainloop()
