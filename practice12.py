# Problem Statement:
# Create an abstract class BankAccount for different types of bank accounts.

# Create:

# BankAccount
#  ├── SavingsAccount
#  └── CurrentAccount

# The abstract class should define:

# deposit()
# withdraw()
# calculate_interest()

# Implement these methods differently in the child classes.

# Concepts: Abstraction, Inheritance, Polymorphism

# ---------------------------------------------------------------------------------------

from abc import ABC , abstractmethod

class BankAccount(ABC):

    @abstractmethod
    def deposit(self,amount):
        pass

    @abstractmethod
    def withdraw(self,amount):
        pass 

    @abstractmethod
    def calculate_interest(self):
        pass

class SavingsAccount(BankAccount):
    def __init__(self):
        self.total_balance=0

    def deposit(self,amount):
        if amount > 0:
            print("amount ",amount," deposited successfully.")
            self.total_balance=self.total_balance+amount
            print("balance : ", self.total_balance)
        else:   
            print("enter valid amount.")   

    def withdraw(self,amount):
        if amount <= self.total_balance and amount >= 0:
            self.total_balance=self.total_balance-amount
            print(amount," withdraw success.")
            print("balance : ", self.total_balance)
        else:
            print("enter valid amount.")   

    def calculate_interest(self):
        interest=self.total_balance*0.2
        print("saving account interest : ", interest)


class CurrentAccount(BankAccount):   
    def __init__(self):
        self.total_balance=0

    def deposit(self,amount):
        if amount > 0:
            print("amount ",amount," deposited successfully.")
            self.total_balance=self.total_balance+amount
            print("balance : ", self.total_balance)
        else:   
            print("enter valid amount.")   

    def withdraw(self,amount):
        if amount <= self.total_balance and amount >= 0:
            self.total_balance=self.total_balance-amount
            print(amount," withdraw success.")
            print("balance : ", self.total_balance)
        else:
            print("enter valid amount.")   

    def calculate_interest(self):
        interest=self.total_balance*0.5
        print("current account interest : ", interest)     


SA=SavingsAccount()
CA=CurrentAccount()

SA.deposit(50000)
SA.withdraw(7000)
SA.calculate_interest()

CA.deposit(50000)
CA.withdraw(7000)
CA.calculate_interest()