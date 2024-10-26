# Coke Entry
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
