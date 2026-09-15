# The Scenario: You are building an application that uses different types of predictive models. 
# You want to force a strict rule: every model added to the system must have a predict() method, otherwise, the code should fail.

# Your Task:
# Write a code using Python's abc module:

# Create an abstract base class called BaseModel.

# Inside it, define an abstract method called predict(self, data).

# Create two concrete child classes: SalesPredictor and LogoDetector.

# In SalesPredictor, implement predict() to print: "Analyzing previous year data to predict next year sales..."

# In LogoDetector, implement predict() to print: "Drawing bounding boxes on detected logos..."

# Instantiate both child classes and call their predict() methods

from abc import ABC,abstractmethod

class BaseModel(ABC):
    
    @abstractmethod
    def predict(self,data):
        pass

class SalesPredictor(BaseModel):
    def predict(self,data):
        return "Analyzing previous year data to predict next year sales..."

class LogoDetector(BaseModel):
    def predict(self,data):
        return "Drawing bounding boxes on detected logos..."      

obj1=SalesPredictor()
obj2=LogoDetector()
print(obj1.predict(100))
print(obj2.predict("harshit"))
          