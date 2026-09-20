# Problem Statement:
# Create an abstract class Shape using Python's abc module.

# Requirements:

# Create an abstract method:
# area()
# Create child classes:
# Circle
# Rectangle
# Triangle
# Each child class must implement area().

# Concepts: Abstract Class, Abstract Method, ABC

# ------------------------------------------------------------------------------

from abc import ABC , abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class circle(Shape):
    def __init__(self,r):
        self.r=r
        self.pi=3.14

    def area(self):
        area=self.pi*self.r*self.r
        print("area of circle is : ",area)

class rectangle(Shape):
    def __init__(self,l,w):
        self.l=l
        self.w=w

    def area(self):
        area=self.l*self.w
        print("area of rectangle is : ",area)

class triangle(Shape):       
    def __init__(self,b,h):
        self.b=b
        self.h=h

    def area(self):
        area=(1/2)*self.b*self.h
        print("area of triangle : ",area)

c=circle(2)
r=rectangle(5,10)
t=triangle(5,8)  

c.area()
r.area()
t.area()