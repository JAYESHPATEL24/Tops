import datetime

customers = {}  # Shared customer database

def bank_menu():
    print()
    menu = """
        Operations Menu:
        1) Add Customer
        2) View Customer
        3) Search Customer
        4) View All Customers
        5) Total Amounts in Bank
        6) Exit
        """
    print(menu)

def customer_menu():
    print("Customer's Menu:")
    print("1) Withdraw Amount")
    print("2) Deposit Amount")
    print("3) View Balance")
    print("4) Exit")

def add_customer():
    account_no = input("Enter account number: ")
    name = input("Enter customer name: ")
    balance = float(input("Enter opening balance: "))
    opening_date = datetime.datetime.now()
    customers[account_no] = {'name': name, 'balance': balance, 'Opening Date': str(opening_date)}
    print("-"*40)
    print("Customer added successfully.")
    print("-"*40)

def view_customer():
    account_no = input("Enter account number to view: ")
    if account_no in customers:
        print("-"*40)
        print(customers[account_no])
        print("-"*40)
    else:
        print("-"*40)
        print("Customer not found.")
        print("-"*40)

def search_customer():
    name = input("Enter customer name to search: ")
    for account_no, details in customers.items():
        if details['name'] == name:
            print(f"Account No: {account_no}, Details: {details}")
            return
    print("-"*40)
    print("Customer not found.")
    print("-"*40)

def view_all_customers():
    if customers:
        for account_no, details in customers.items():
            print(f"Account No: {account_no}, Details: {details}")
    else:
        print("-"*40)
        print("No customers to display.")
        print("-"*40)

def total_amounts_in_bank():
    total = sum(details['balance'] for details in customers.values())
    print(f"Total amount in bank: {total}")

def withdraw_amount():
    account_no = input("Enter account number: ")
    amount = float(input("Enter amount to withdraw: "))
    if account_no in customers and customers[account_no]['balance'] >= amount:
        customers[account_no]['balance'] -= amount
        print("Withdrawal successful.")
    else:
        print("Insufficient funds or account not found.")

def deposit_amount():
    account_no = input("Enter account number: ")
    amount = float(input("Enter amount to deposit: "))
    if account_no in customers:
        customers[account_no]['balance'] += amount
        print("Deposit successful.")
    else:
        print("Account not found.")

def view_balance():
    account_no = input("Enter account number: ")
    if account_no in customers:
        print(f"Current balance: {customers[account_no]['balance']}")
    else:
        print("Account not found.")