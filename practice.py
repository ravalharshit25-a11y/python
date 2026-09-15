# The Scenario: You are building the backend for a Supermarket application and need to ensure that the internal cost of an 
# item cannot be modified directly from outside the class.

# Your Task:
# Write a code to create a Product class with the following requirements:

# An __init__ method that accepts name, cost_price, and selling_price.

# Make cost_price a private attribute, while name and selling_price remain public.

# Create a public method called calculate_profit() that returns the difference between the selling price and the private cost price.

# Create an object from this class (e.g., a bag of apples) and print the result of calculate_profit()

class product:

    def __init__(self,name,cost_price,selling_price):
        self.name=name
        self.__cost_price=cost_price
        self.selling_price=selling_price

    def calculate_profit(self):
        self.profit=self.selling_price-self.__cost_price
        # print("profit : ",self.profit)
        return self.profit

obj=product("apple",50,65)
print(obj.calculate_profit())             


