# Problem Statement:
# Create a BankAccount class that performs basic banking operations.

# Requirements:
# Create the following attributes:

# Account number
# Account holder name
# Balance

# Create the following methods:
# deposit(amount)
# withdraw(amount)
# check_balance()
# display_account()

# Deposit amount must be greater than 0.
# Withdrawal amount must not exceed the balance.
# Display an appropriate message for invalid transactions.

class BankAccount:

    def __init__(self,Account_name,Account_holder_name,balance):
        self.Account_name=Account_name
        self.Account_holder_name=Account_holder_name
        self.balance=balance

    def deposit(self,deposit_amount):
        self.deposit_amount=deposit_amount

        if deposit_amount > 0:
            self.balance=self.balance+deposit_amount
        else:
            print("amount must be greater then 0")    

    def withdraw(self,withdraw_amount):
        self.withdraw_amount=withdraw_amount

        if withdraw_amount > 0 and withdraw_amount <= self.balance :
            self.balance=self.balance-self.withdraw_amount     
        else :     
            print("amount must be greater then 0 and not more then your balance")

    def check_balance(self):
        print("-------------------------------------")
        print("your current balance : ",self.balance)

    def display_account(self):
        print("-----------------your bank details---------------------------")
        print("account name : ", self.Account_name) 
        print("account holder name : ", self.Account_holder_name)    
        print("account balance : ", self.balance)    

Account_name=str(input("enter account name : "))
Account_holder_name=str(input("enter account holder name : "))
balance=int(input("enter your current balance : "))               

bank=BankAccount(Account_name,Account_holder_name,balance)

while True:

    print("-------------------------------------------------")
    print("enter 1 to display bank account details ")
    print("enter 2 to deposite amount")
    print("enter 3 to withdraw amount")
    print("enter 4 to check balance")
    print("enter 5 to exit")
    a=int(input("enter your choise : "))

    match a:
        case 1:
            bank.display_account()
        case 2:
            deposit_amount=int(input("enter deposite amount : "))
            bank.deposit(deposit_amount)
        case 3:
            withdraw_amount=int(input("enter withdraw amount : "))
            bank.withdraw(withdraw_amount)   
        case 4:
            bank.check_balance()
        case 5:
            break
        case _:
            print("enter valid number")           