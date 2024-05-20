import os
import hashlib
from datetime import datetime

# Constants for file names
USER_FILE = 'users.txt'
TRANSACTION_FILE = 'transactions.txt'


# Utility functions
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def get_current_date():
    return datetime.today().strftime('%Y-%m-%d')


def create_file_if_not_exists(filename):
    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            pass


# User-related functions
def register_user(username, password):
    create_file_if_not_exists(USER_FILE)
    with open(USER_FILE, 'a') as file:
        file.write(f"{username},{hash_password(password)}\n")


def authenticate_user(username, password):
    create_file_if_not_exists(USER_FILE)
    with open(USER_FILE, 'r') as file:
        users = file.readlines()
    for user in users:
        stored_username, stored_password = user.strip().split(',')
        if stored_username == username and stored_password == hash_password(password):
            return True
    return False


# Transaction-related functions
def add_transaction(username, amount, category, description, date=None):
    create_file_if_not_exists(TRANSACTION_FILE)
    if date is None:
        date = get_current_date()
    with open(TRANSACTION_FILE, 'a') as file:
        file.write(f"{username},{amount},{category},{description},{date}\n")


def get_transactions(username):
    create_file_if_not_exists(TRANSACTION_FILE)
    transactions = []
    with open(TRANSACTION_FILE, 'r') as file:
        all_transactions = file.readlines()
    for transaction in all_transactions:
        stored_username, amount, category, description, date = transaction.strip().split(',')
        if stored_username == username:
            transactions.append((amount, category, description, date))
    return transactions


# Summary functions
def calculate_summary(transactions):
    income = sum(float(t[0]) for t in transactions if float(t[0]) > 0)
    expenses = sum(float(t[0]) for t in transactions if float(t[0]) < 0)
    balance = income + expenses
    return income, abs(expenses), balance


def print_summary(username):
    transactions = get_transactions(username)
    income, expenses, balance = calculate_summary(transactions)
    print("\nSummary:")
    print(f"Total Income: ${income:.2f}")
    print(f"Total Expenses: ${expenses:.2f}")
    print(f"Balance: ${balance:.2f}")


def print_transactions(username):
    transactions = get_transactions(username)
    print("\nTransactions:")
    for amount, category, description, date in transactions:
        print(f"Date: {date}, Amount: ${amount}, Category: {category}, Description: {description}")


def main():
    print("Welcome to the Personal Finance Tracker")
    
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            register_user(username, password)
            print("User registered successfully.")

        elif choice == '2':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if authenticate_user(username, password):
                print("Login successful.")
                while True:
                    print("\n1. Add Income")
                    print("2. Add Expense")
                    print("3. View Summary")
                    print("4. View All Transactions")
                    print("5. Logout")
                    user_choice = input("Choose an option: ")

                    if user_choice == '1':
                        amount = float(input("Enter income amount: "))
                        category = input("Enter category: ")
                        description = input("Enter description: ")
                        add_transaction(username, amount, category, description)
                        print("Income added successfully.")

                    elif user_choice == '2':
                        amount = float(input("Enter expense amount: ")) * -1
                        category = input("Enter category: ")
                        description = input("Enter description: ")
                        add_transaction(username, amount, category, description)
                        print("Expense added successfully.")

                    elif user_choice == '3':
                        print_summary(username)

                    elif user_choice == '4':
                        print_transactions(username)

                    elif user_choice == '5':
                        print("Logging out...")
                        break

                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Invalid username or password.")

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
