def banker():
    customers = []

    menu = """
Welcome to Banker's App
            Operations Menu
            1)  Add Customer
            2)  View Customer
            3)  Search Customer
            4)  View All Customers
            5)  Exit
    """
    while True:
        print(menu)
        ch = int(input("Enter your choice: "))

        if ch == 1:
            name = input("Enter customer name: ")
            account_number = input("Enter account number: ")
            balance = float(input("Enter initial balance: "))
            customers.append({"name": name, "account_number": account_number, "balance": balance})
            print("Customer added successfully.")

        elif ch == 2:
            account_number = input("Enter account number: ")
            for customer in customers:
                if customer["account_number"] == account_number:
                    print(customer)
                    break
            else:
                print("Customer not found.")

        elif ch == 3:
            name = input("Enter customer name to search: ")
            for customer in customers:
                if customer["name"] == name:
                    print(customer)
                    break
            else:
                print("Customer not found.")

        elif ch == 4:
            if customers:
                for customer in customers:
                    print(customer)
            else:
                print("No customers to display.")

        elif ch == 5:
            print("Exiting the Banker's App")
            break

        else:
            print("Invalid choice, please try again.")


def customer():
    balance = 0  # Initial balance

    menu = """
Welcome to Customer's App
            Operations Menu
            1)  Withdraw amount
            2)  Deposit amount
            3)  View Balance
            4)  Exit
    """
    while True:
        print(menu)
        
        ch = int(input("Enter your choice: "))
        
        if ch == 1:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print(f"Withdrawal successful. New balance: {balance}")
            else:
                print("Insufficient funds.")

        elif ch == 2:
            amount = float(input("Enter amount to deposit: "))
            balance += amount
            print(f"Deposit successful. New balance: {balance}")

        elif ch == 3:
            print(f"Current balance: {balance}")

        elif ch == 4:
            print("Exiting the application.")
            break

        else:
            print("Invalid choice, please try again.")
