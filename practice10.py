
# Practical 10: Payment System

# Problem Statement:
# Create a payment system using polymorphism.

# Create:

# Payment
#  ├── CreditCard
#  ├── UPI
#  └── PayPal

# Each class should implement:

# make_payment(amount)

# Sample Output:

# Payment of ₹5000 made using Credit Card.
# Payment of ₹2500 made using UPI.
# Payment of ₹3000 made using PayPal.

# Concepts: Polymorphism, Method Overriding

#-----------------------------------------------------------------------------------------------

class payment:

    def make_payment(amount):
        pass

class CreditCard(payment):

    def make_payment(self,amount):
        self.amount=amount
        print(" Payment of ",self.amount ," made using Credit Card.")

class UPI(payment):
    def make_payment(self,amount):
        self.amount=amount
        print(" Payment of ", self.amount ," made using UPI.")

class PayPal(payment):
    def make_payment(self,amount):
        self.amount=amount
        print(" Payment of ",self.amount, " made using paypal.")

a=CreditCard()
b=UPI()
c=PayPal()

a.make_payment(500000)
b.make_payment(7637637)
c.make_payment(156000)