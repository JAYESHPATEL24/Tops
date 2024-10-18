import tkinter as tk
# Main Application
root = tk.Tk()
root.title("Billing Software")

# Customer Details Frame
customer_frame = tk.Frame(root)
customer_frame.pack(pady=10)

tk.Label(customer_frame, text="Customer Name:").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(customer_frame)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(customer_frame, text="Phone No:").grid(row=1, column=0, padx=10, pady=5)
phone_entry = tk.Entry(customer_frame)
phone_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(customer_frame, text="Bill No:").grid(row=2, column=0, padx=10, pady=5)
bill_entry = tk.Entry(customer_frame)
bill_entry.grid(row=2, column=1, padx=10, pady=5)

# Products Frame
products_frame = tk.Frame(root)
products_frame.pack(pady=10)

tk.Label(products_frame, text="Bath Soap:").grid(row=0, column=0, padx=10, pady=5)
soap_entry = tk.Entry(products_frame)
soap_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(products_frame, text="Face Cream:").grid(row=1, column=0, padx=10, pady=5)
cream_entry = tk.Entry(products_frame)
cream_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(products_frame, text="Face Wash:").grid(row=2, column=0, padx=10, pady=5)
wash_entry = tk.Entry(products_frame)
wash_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(products_frame, text="Hair Spray:").grid(row=3, column=0, padx=10, pady=5)
spray_entry = tk.Entry(products_frame)
spray_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(products_frame, text="Body Lotion:").grid(row=4, column=0, padx=10, pady=5)
lotion_entry = tk.Entry(products_frame)
lotion_entry.grid(row=4, column=1, padx=10, pady=5)

# Bill Area
bill_area_frame = tk.Frame(root)
bill_area_frame.pack(pady=10)

bill_text = tk.Text(bill_area_frame, width=40, height=15)

# Generate Bill Button
generate_button = tk.Button(root, text="Generate Bill")
generate_button.pack(pady=10)

root.mainloop()