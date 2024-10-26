import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("1000x1000")
root.title("Billing Software")
root.config(bg="white")

# Section: Customer Details
customer_frame = tk.LabelFrame(root, text="Customer Details", font=("Arial", 15, "bold"), bg="white")
customer_frame.place(x=0, y=0, relwidth=1)

tk.Label(customer_frame, text="Customer Name", font=("Arial", 12, "bold"), bg="white").grid(row=0, column=0, padx=10, pady=5)
customer_name = tk.Entry(customer_frame, bd=7, relief=tk.SUNKEN, width=15, font="arial 12")
customer_name.grid(row=0, column=1, pady=5, padx=10)

tk.Label(customer_frame, text="Phone No", font=("Arial", 12, "bold"), bg="white").grid(row=0, column=2, padx=10, pady=5)
customer_phone = tk.Entry(customer_frame, bd=7, relief=tk.SUNKEN, width=15, font="arial 12")
customer_phone.grid(row=0, column=3, pady=5, padx=10)

tk.Label(customer_frame, text="Bill No", font=("Arial", 12, "bold"), bg="white").grid(row=0, column=4, padx=10, pady=5)
bill_no = tk.Entry(customer_frame, bd=7, relief=tk.SUNKEN, width=15, font="arial 12")
bill_no.grid(row=0, column=5, pady=5, padx=10)

# Section: Product Categories
products_frame = tk.LabelFrame(root, text="Products", font=("Arial", 15, "bold"), bg="white")
products_frame.place(x=5, y=180, width=325, height=380)

# Cosmetics Frame
cosmetics_frame = tk.LabelFrame(products_frame, text="Cosmetics", font=("Arial", 12, "bold"), bg="white")
cosmetics_frame.pack(fill="both", expand="yes", padx=10, pady=5)

tk.Label(cosmetics_frame, text="Bath Soap", font=("Arial", 12, "bold"), bg="white").grid(row=0, column=0, padx=10, pady=5, sticky="w")
bath_soap = tk.Entry(cosmetics_frame, bd=5, relief=tk.SUNKEN, width=8, font="arial 12")
bath_soap.grid(row=0, column=1, padx=10, pady=5)

tk.Label(cosmetics_frame, text="Face Cream", font=("Arial", 12, "bold"), bg="white").grid(row=1, column=0, padx=10, pady=5, sticky="w")
face_cream = tk.Entry(cosmetics_frame, bd=5, relief=tk.SUNKEN, width=8, font="arial 12")
face_cream.grid(row=1, column=1, padx=10, pady=5)

tk.Label(cosmetics_frame, text="Face Wash", font=("Arial", 12, "bold"), bg="white").grid(row=2, column=0, padx=10, pady=5, sticky="w")
face_wash = tk.Entry(cosmetics_frame, bd=5, relief=tk.SUNKEN, width=8, font="arial 12")
face_wash.grid(row=2, column=1, padx=10, pady=5)

# Grocery Frame
grocery_frame = tk.LabelFrame(products_frame, text="Grocery", font=("Arial", 12, "bold"), bg="white")
grocery_frame.pack(fill="both", expand="yes", padx=10, pady=5)

tk.Label(grocery_frame, text="Rice", font=("Arial", 12, "bold"), bg="white").grid(row=0, column=0, padx=10, pady=5, sticky="w")
rice = tk.Entry(grocery_frame, bd=5, relief=tk.SUNKEN, width=8, font="arial 12")
rice.grid(row=0, column=1, padx=10, pady=5)

tk.Label(grocery_frame, text="Food Oil", font=("Arial", 12, "bold"), bg="white").grid(row=1, column=0, padx=10, pady=5, sticky="w")
food_oil = tk.Entry(grocery_frame, bd=5, relief=tk.SUNKEN, width=8, font="arial 12")
food_oil.grid(row=1, column=1, padx=10, pady=5)

tk.Label(grocery_frame, text="Daal", font=("Arial", 12, "bold"), bg="white").grid(row=2, column=0, padx=10, pady=5, sticky="w")
daal = tk.Entry(grocery_frame, bd=5, relief=tk.SUNKEN, width=8, font="arial 12")
daal.grid(row=2, column=1, padx=10, pady=5)

# Others Frame
others_frame = tk.LabelFrame(products_frame, text="Others", font=("Arial", 12, "bold"), bg="white")
others_frame.pack(fill="both", expand="yes", padx=10, pady=5)

tk.Label(others_frame, text="Maza", font=("Arial", 12, "bold"), bg="white").grid(row=0, column=0, padx=10, pady=5, sticky="w")
maza = tk.Entry(others_frame, bd=5, relief=tk.SUNKEN, width=8, font="arial 12")
maza.grid(row=0, column=1, padx=10, pady=5)

tk.Label(others_frame, text="Coke", font=("Arial", 12, "bold"), bg="white").grid(row=1, column=0, padx=10, pady=5, sticky="w")
coke = tk.Entry(others_frame, bd=5, relief=tk.SUNKEN, width=8, font="arial 12")
coke.grid(row=1, column=1, padx=10, pady=5)

# Total Bill Section
total_frame = tk.LabelFrame(root, text="Total Bill", font=("Arial", 15, "bold"), bg="white")
total_frame.place(x=350, y=180, width=620, height=380)

tk.Label(total_frame, text="Total", font=("Arial", 12, "bold"), bg="white").grid(row=0, column=0, padx=10, pady=5)
total_amount = tk.Entry(total_frame, bd=7, relief=tk.SUNKEN, width=15, font="arial 12", state='readonly')
total_amount.grid(row=0, column=1, pady=5, padx=10)

# Function to calculate total bill
def calculate_total():
    total = 0
    
    # Get quantities from entry fields
    products = [
        bath_soap, face_cream, face_wash, 
        rice, food_oil, daal, 
        maza, coke
    ]
    
    # Assuming fixed prices for simplicity
    prices = [20, 30, 25, 40, 50, 30, 15, 10]  # prices for the products

    for entry, price in zip(products, prices):
        try:
            quantity = int(entry.get()) if entry.get() else 0
            total += quantity * price
        except ValueError:
            total += 0  # If there's a non-integer value, add 0
    
    total_amount.config(state='normal')
    total_amount.delete(0, tk.END)
    total_amount.insert(0, str(total))
    total_amount.config(state='readonly')

# Calculate Button
calculate_button = tk.Button(total_frame, text="Calculate Total", font=("Arial", 12, "bold"), bg="lightblue", command=calculate_total)
calculate_button.grid(row=1, column=0, columnspan=2, pady=20)

# Run the application
root.mainloop()
