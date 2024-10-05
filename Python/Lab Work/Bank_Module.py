import datetime

def main_menu():
    print("Operations Menu:")
    print("1) Add Customer")
    print("2) View Customer")
    print("3) Search Customer")
    print("4) View All Customers")
    print("5) Total Amounts in Bank")
    print("6) Exit")

def customer_menu():
    print("Customer's Menu:")
    print("1) Withdraw Amount")
    print("2) Deposit Amount")
    print("3) View Balance")
    print("4) Exit")

def add_customer(customers):
    account_no = input("Enter account number: ")
    name = input("Enter customer name: ")
    balance = float(input("Enter opening balance: "))
    opening_date = datetime.datetime.now()
    customers[account_no] = {'name': name, 'balance': balance, 'Opening Date': str(opening_date)}
    print("Customer added successfully.")

def view_customer(customers):
    account_no = input("Enter account number to view: ")
    if account_no in customers:
        print(customers[account_no])
    else:
        print("Customer not found.")

def search_customer(customers):
    name = input("Enter customer name to search: ")
    for account_no, details in customers.items():
        if details['name'] == name:
            print(f"Account No: {account_no}, Details: {details}")
            return
    print("Customer not found.")

def view_all_customers(customers):
    if customers:
        for account_no, details in customers.items():
            print(f"Account No: {account_no}, Details: {details}")
    else:
        print("No customers to display.")

def total_amounts_in_bank(customers):
    total = sum(details['balance'] for details in customers.values())
    print(f"Total amount in bank: {total}")

def withdraw_amount(customers):
    account_no = input("Enter account number: ")
    amount = float(input("Enter amount to withdraw: "))
    if account_no in customers and customers[account_no]['balance'] >= amount:
        customers[account_no]['balance'] -= amount
        print("Withdrawal successful.")
    else:
        print("Insufficient funds or account not found.")

def deposit_amount(customers):
    account_no = input("Enter account number: ")
    amount = float(input("Enter amount to deposit: "))
    if account_no in customers:
        customers[account_no]['balance'] += amount
        print("Deposit successful.")
    else:
        print("Account not found.")

def view_balance(customers):
    account_no = input("Enter account number: ")
    if account_no in customers:
        print(f"Current balance: {customers[account_no]['balance']}")
    else:
        print("Account not found.")


