import tkinter as tk
from tkinter import StringVar, messagebox

class CustomerDetailsApp:
    def __init__(self, master):
        self.master = master
        self.Customer_details_frame = tk.Frame(master)
        self.Customer_details_frame.pack()
        self.customerentries = []
        self.Customerdetails_Labels_Entries()

    def genreate_bill_no(self):
        # Generate your bill number here
        return 123456  # Example placeholder

    def validate_name(self, input_str):
        if all(char.isalpha() or char.isspace() for char in input_str):
            return True
        return False

    def validate_phone(self, input_str):
        return input_str.isdigit() and len(input_str) <= 10

    def validate_bill_no(self, input_str):
        return input_str.isdigit() and len(input_str) == 6

    def Customerdetails_Labels_Entries(self):
        label_placeholder = {
            "Customer Name": "Enter Customer Name",
            "Phone No.": "Enter Phone Number",
            "Bill No.": f"{self.genreate_bill_no():06d}"
        }
        
        index = 0
        for labelname, entryplaceholder in label_placeholder.items():
            label = tk.Label(self.Customer_details_frame, text=labelname, font=("times new roman", 15, "bold"), bg="#074463", fg="White")
            label.grid(row=0, column=index * 2, padx=20, pady=5)

            if labelname == "Bill No.":
                validate_cmd = self.master.register(self.validate_bill_no)
                entry = tk.Entry(self.Customer_details_frame, font=("Arial", 15), bd=5, width=22, validate='key', validatecommand=(validate_cmd, '%P'))
                entry.grid(row=0, column=index * 2 + 1, padx=20, pady=5)
                entry.insert(0, entryplaceholder)
                self.customerentries.append(entry)
            else:
                validate_cmd = self.master.register(self.validate_name if labelname == "Customer Name" else self.validate_phone)
                entry = tk.Entry(self.Customer_details_frame, font=("Arial", 15), bd=5, width=22, validate='key', validatecommand=(validate_cmd, '%P'))
                entry.grid(row=0, column=index * 2 + 1, padx=20, pady=5)
                entry.insert(0, entryplaceholder)
                self.customerentries.append(entry)

            index += 1

if __name__ == "__main__":
    root = tk.Tk()
    app = CustomerDetailsApp(root)
    root.mainloop()