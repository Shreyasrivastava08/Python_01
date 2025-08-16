

import random


class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_number = random.randint(10**15, 10**16 - 1) 
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance!")

    def display_balance(self):
        print(f"Current Balance: ₹{self.balance}")


class SavingAccount(BankAccount):
    interest_rate = 0.04  

    def apply_interest(self):
        interest = self.balance * SavingAccount.interest_rate
        self.balance += interest
        print(f"Interest of ₹{interest:.2f} applied successfully.")



class CurrentAccount(BankAccount):
    overdraft_limit = 50000

    def withdraw(self, amount):
        if self.balance - amount >= -CurrentAccount.overdraft_limit:
            self.balance -= amount
            print(f"{amount} withdrawn successfully.")
        else:
            print("Transaction failed! Overdraft limit exceeded.")



def main():
    print("Welcome to the Bank System")
    acc_type = input("Enter account type (saving/current): ").strip().lower()
    name = input("Enter account holder name: ")
    balance = float(input("Enter initial balance: "))

    if acc_type == "saving":
        account = SavingAccount(name, balance)
        print("\nYour Saving Account has been created successfully.")
        print(f"Account Number: {account.account_number}")
        print("Interest Rate (Bank Fixed): 4%")

    elif acc_type == "current":
        account = CurrentAccount(name, balance)
        print("\nYour Current Account has been created successfully.")
        print(f"Account Number: {account.account_number}")
        print(f"Overdraft Limit (Bank Fixed): ₹{CurrentAccount.overdraft_limit}")

    else:
        print("Invalid account type!")
        return

    while True:
        print("\nChoose operation:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Display Balance")
        if isinstance(account, SavingAccount):
            print("4. Apply Interest (Bank-decided rate)")
            print("5. Exit")
        else:
            print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amt = float(input("Enter deposit amount: "))
            account.deposit(amt)

        elif choice == "2":
            amt = float(input("Enter withdraw amount: "))
            account.withdraw(amt)

        elif choice == "3":
            account.display_balance()

        elif choice == "4" and isinstance(account, SavingAccount):
            account.apply_interest()

        elif (choice == "4" and isinstance(account, CurrentAccount)) or \
             (choice == "5" and isinstance(account, SavingAccount)):
            print("Thank you for using our Bank System.")
            break

        else:
            print("Invalid choice, please try again.")



if __name__ == "__main__":
    main()