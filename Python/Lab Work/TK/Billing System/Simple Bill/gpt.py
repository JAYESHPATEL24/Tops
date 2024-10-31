from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.master.geometry("1600x800")
        self.master.title("Billing Software")
        self.master.config(bg="white")

        self.title_label = Label(self.master, text="Billing Software", font=("times new roman", 25, "bold"),
                                 bg="#074463", fg='white', bd=12, relief=GROOVE, pady=2)
        self.title_label.pack(fill=X)

        self.customer_details_frame = CustomerDetails(self.master)
        self.customer_details_frame.pack(pady=10)

        self.cosmetics_frame = ProductFrame(self.master, "Cosmetics", self.add_cosmetics)
        self.cosmetics_frame.pack(side=LEFT, padx=10)

        self.grocery_frame = ProductFrame(self.master, "Grocery", self.add_grocery)
        self.grocery_frame.pack(side=LEFT, padx=10)

        self.others_frame = ProductFrame(self.master, "Others", self.add_others)
        self.others_frame.pack(side=LEFT, padx=10)

        self.bill_area_frame = BillArea(self.master)
        self.bill_area_frame.pack(side=RIGHT, padx=10)

        self.menu_frame = MenuFrame(self.master)
        self.menu_frame.pack(pady=10)

    def add_cosmetics(self, product_name, quantity):
        self.bill_area_frame.add_to_bill(product_name, quantity)

    def add_grocery(self, product_name, quantity):
        self.bill_area_frame.add_to_bill(product_name, quantity)

    def add_others(self, product_name, quantity):
        self.bill_area_frame.add_to_bill(product_name, quantity)


class CustomerDetails(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        self.customer_details_label = LabelFrame(self, text=" Customer Details ", font=("arial", 12, "bold"),
                                                  bg="#074463", fg="gold", relief=GROOVE, bd=5)
        self.customer_details_label.pack(fill=X)

        Label(self.customer_details_label, text="Customer Name", font=("times new roman", 15, "bold"),
              bg="#074463", fg="White").grid(row=0, column=0, padx=20, pady=5)
        self.name_entry = Entry(self.customer_details_label, font=("Arial", 15), bd=5, width=22)
        self.name_entry.grid(row=0, column=1, padx=20, pady=5)

        Label(self.customer_details_label, text="Phone No.", font=("times new roman", 15, "bold"),
              bg="#074463", fg="White").grid(row=0, column=2, padx=20, pady=5)
        self.phone_entry = Entry(self.customer_details_label, font=("Arial", 15), bd=5, width=22)
        self.phone_entry.grid(row=0, column=3, padx=20, pady=5)

        Label(self.customer_details_label, text="Bill No.", font=("times new roman", 15, "bold"),
              bg="#074463", fg="White").grid(row=0, column=4, padx=20, pady=5)
        self.bill_entry = Entry(self.customer_details_label, font=("Arial", 15), bd=5, width=22)
        self.bill_entry.grid(row=0, column=5, padx=20, pady=5)

        Button(self.customer_details_label, text="Enter", font=("times new roman", 15, "bold"),
               bg="#074463", fg="White", bd=5, width=10, relief=GROOVE).grid(row=0, column=6, padx=22, pady=5)


class ProductFrame(Frame):
    def __init__(self, master, title, add_function):
        super().__init__(master)
        self.title = title
        self.add_function = add_function
        self.create_widgets()

    def create_widgets(self):
        self.label_frame = LabelFrame(self, text=self.title, font=("arial", 12, "bold"),
                                      bd=5, bg="#074463", fg="gold", relief=GROOVE)
        self.label_frame.pack(fill="both", expand="yes")

        self.products = {
            "Product1": 0,
            "Product2": 0,
            "Product3": 0,
        }

        row = 0
        for product in self.products:
            Label(self.label_frame, text=product, font=("times new roman", 15, "bold"),
                  bg="#074463", fg="White", bd=5, width=10).grid(row=row, column=0, padx=20, pady=20)
            entry = Entry(self.label_frame, font=("arial", 12), width=15, bd=5)
            entry.grid(row=row, column=1, padx=20, pady=20)
            button = Button(self.label_frame, text="Add", command=lambda p=product, e=entry: self.add_product(p, e),
                            font=("times new roman", 12, "bold"), bg="#074463", fg="White")
            button.grid(row=row, column=2, padx=20, pady=20)
            row += 1

    def add_product(self, product_name, entry):
        quantity = entry.get()
        if quantity:
            self.add_function(product_name, quantity)


class BillArea(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        self.label = Label(self, text="Bill Area", font=("arial", 12, "bold"), bd=5, relief=GROOVE)
        self.label.pack(fill=X)
        
        self.scrollbar = Scrollbar(self, orient=VERTICAL)
        self.textarea = Text(self, yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.scrollbar.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)
        self.textarea.insert(1.0, " ******** Welcome To Store ********* ")

    def add_to_bill(self, product_name, quantity):
        self.textarea.insert(END, f"{product_name}: {quantity}\n")


class MenuFrame(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        self.label_frame = LabelFrame(self, text=" Bill Menu ", font=("arial", 12, "bold"),
                                      bd=5, bg="#074463", fg="gold", relief=GROOVE)
        self.label_frame.pack(fill="both", expand="yes")

        # Sample menu items
        for i in range(3):
            Label(self.label_frame, text=f"Item {i+1}", font=("times new roman", 15, "bold"),
                  bg="#074463", fg="White", bd=5, width=10).grid(row=i, column=0, padx=30, pady=15)
            Entry(self.label_frame, font=("arial", 12), width=15, bd=5).grid(row=i, column=1, padx=30, pady=15)

        Button(self.label_frame, text="Total", font=("times new roman", 15, "bold"),
               bg="#074463", fg="White", bd=5, width=8, relief=GROOVE).grid(row=1, column=4, padx=20, pady=5)
        Button(self.label_frame, text="Generate Bill", font=("times new roman", 15, "bold"),
               bg="#074463", fg="White", bd=5, width=13, relief=GROOVE).grid(row=1, column=5, padx=20, pady=5)
        Button(self.label_frame, text="Clear", font=("times new roman", 15, "bold"),
               bg="#074463", fg="White", bd=5, width=8, relief=GROOVE).grid(row=1, column=6, padx=20, pady=5)
        Button(self.label_frame, text="Exit", font=("times new roman", 15, "bold"),
               bg="#074463", fg="White", bd=5, width=8, relief=GROOVE).grid(row=1, column=7, padx=20, pady=5)


if __name__ == "__main__":
    root = Tk()
    app = Application(master=root)
    app.mainloop()
