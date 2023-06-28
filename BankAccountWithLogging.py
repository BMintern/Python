import logging
import random
import pandas as pd
import os
import openpyxl

# Configure logging
logging.basicConfig(filename='bank_account.log', level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

# Create a DataFrame to store account details
account_df = pd.DataFrame(columns=['Account Number', 'Username'])

class BankAccount:
    def __init__(self, account_number, username):
        self.account_number = account_number
        self.username = username
        self.balance = 0.0
        account_df.loc[len(account_df)] = [account_number, username]
        logging.info(f"Account {account_number}: Created successfully. Username: {username}")

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            logging.warning(f"Account {self.account_number}: Insufficient funds.")

    def get_balance(self):
        return self.balance

# Dictionary to store user accounts
accounts = {}

def create_account(username):
    account_number = random.randint(100000, 999999)
    if account_number not in accounts:
        account = BankAccount(account_number, username)
        accounts[account_number] = account
        print(f"Welcome, {username}! This is your account number: {account_number}")
        
    else:
        logging.warning("Account number already exists.")

def main_1():
    # Add the logging handler to the root logger
    logger = logging.getLogger()
    logger.addHandler(logging.FileHandler('bank_account.log'))

    while True:
        print("\n=== Online Banking System ===")
        print("1. Create an account")
        print("2. Login to an account")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter your username: ")
            create_account(username)

        elif choice == "2":
            account_number = int(input("Enter your account number: "))
            if account_number in accounts:
                account = accounts[account_number]
                logging.info(f"Account {account_number}: User logged in. Username: {account.username}")

                while True:
                    print("\n=== Account Menu ===")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Logout")

                    option = input("Enter your option: ")

                    if option == "1":
                        amount = float(input("Enter the amount to deposit: "))
                        account.deposit(amount)
                        print(f"Deposit of {amount} successful. New balance: {account.get_balance()}")
                        logging.info(f"Account {account_number}: Deposit of {amount} successful. New balance: {account.get_balance()}")

                    elif option == "2":
                        amount = float(input("Enter the amount to withdraw: "))
                        account.withdraw(amount)
                        print(f"Withdrawal of {amount} successful. New balance: {account.get_balance()}")
                        logging.info(f"Account {account_number}: Withdrawal of {amount} successful. New balance: {account.get_balance()}")

                    elif option == "3":
                        balance = account.get_balance()
                        print(f"Current balance: {balance}")
                        logging.info(f"Account {account_number}: Current balance: {balance}")

                    elif option == "4":
                        print("User logged out.")
                        logging.info(f"Account {account_number}: User logged out.")
                        break

                    else:
                        print("Invalid option. Please try again.")
                        logging.warning(f"Account {account_number}: Invalid option.")

            else:
                print("Invalid account number. Please try again.")
                logging.warning(f"Invalid account number: {account_number}")

        elif choice == "3":
            print("Thank you for using the Online Banking System. Goodbye!")
            logging.info("Online Banking System: Program terminated.")
            break

        else:
            print("Invalid choice. Please try again.")
            logging.warning("Invalid choice.")

    # Save the account DataFrame to an Excel file
    if 'bank_account_details.xlsx' in os.listdir():
        with pd.ExcelWriter('bank_account_details.xlsx', engine='openpyxl', mode='a') as writer:
            account_df.to_excel(writer, index=False, header=not bool(writer.sheets))
    else:
        account_df.to_excel('bank_account_details.xlsx', index=False)

# if __name__ == "__main__":
    main_1()
