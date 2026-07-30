#===================Bank Balance Simulator

# ask user what operation they want to perform Deposit ,withdrawal,balance check aske to exit 



# def deposit_money(balance):

# =================== Bank Balance Simulator ===================

# Input Validation Function
def get_float_input(field_name):
    while True:
        try:
            return float(input(f"Enter {field_name}: "))
        except ValueError:
            print("Invalid amount. Please enter a valid number.")


# Deposit Function
def deposit_money(balance, transactions):
    amount = get_float_input("deposit amount (₹)")

    if amount <= 0:
        print("Amount must be greater than zero.")
        return balance

    balance += amount

    transactions.append(f"Deposit    : ₹{amount:,.2f}")

    print(f"₹{amount:,.2f} deposited successfully.")

    return balance


# Withdrawal Function
def withdraw_money(balance, transactions):
    amount = get_float_input("withdrawal amount (₹)")

    if amount <= 0:
        print("Amount must be greater than zero.")
        return balance

    if amount > balance:
        print("Insufficient funds!")
        return balance

    balance -= amount

    transactions.append(f"Withdrawal : ₹{amount:,.2f}")

    print(f"₹{amount:,.2f} withdrawn successfully.")

    return balance


# Balance Check Function
def check_balance(balance):
    print(f"\nCurrent Balance : ₹{balance:,.2f}")


# Statement Function
def print_statement(balance, transactions):

    print("\n========== ACCOUNT STATEMENT ==========")

    if not transactions:
        print("No transactions found.")
    else:
        for transaction in transactions:
            print(transaction)

    print("--------------------------------------")
    print(f"Current Balance : ₹{balance:,.2f}")
    print("=======================================")


# =================== Main Program ===================

balance = get_float_input("starting balance (₹)")
transactions = []

while True:

    print("\n========== BANK MENU ==========")
    print("1. Deposit")
    print("2. Withdrawal")
    print("3. Balance Check")
    print("4. Statement")
    print("5. Exit")

    choice = input("Choose an option (1-5): ").strip()

    if choice == "1":
        balance = deposit_money(balance, transactions)

    elif choice == "2":
        balance = withdraw_money(balance, transactions)

    elif choice == "3":
        check_balance(balance)

    elif choice == "4":
        print_statement(balance, transactions)

    elif choice == "5":
        print("\nThank you for using the Bank Balance Simulator!")
        break

    else:
        print("Invalid choice. Please choose between 1 and 5.")