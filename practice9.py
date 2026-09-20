# Problem Statement:
# Create a program to calculate the area of different shapes using polymorphism.

# Create:

# Shape
#  ├── Circle
#  ├── Rectangle
#  └── Triangle

# Each class should contain:

# area()

# Requirements:

# Circle.area() → π × r²
# Rectangle.area() → length × width
# Triangle.area() → ½ × base × height
# Use the same method name area() in all classes.

# Sample Output:

# Circle Area: 78.54
# Rectangle Area: 50
# Triangle Area: 25

# Concepts: Method Overriding, Polymorphism

# --------------------------------------------------------------------------------------------

class shapes:

    def area(self):
        pass

class Circle(shapes):
    def __init__(self,r):
        self.r=r
        self.pi=3.14

    def area(self):
        area=self.pi*self.r*self.r
        print("area of circle is : ",area)

class Rectangle(shapes):
    def __init__(self,l,w):
        self.l=l
        self.w=w

    def area(self):
        area=self.l*self.w
        print("area of rectangle is : ",area)

class Triangle(shapes):    
    def __init__(self,b,h):
        self.b=b
        self.h=h

    def area(self):
        area=(1/2)*self.b*self.h
        print("area of triangle : ",area)

c=Circle(2)
r=Rectangle(5,10)
t=Triangle(5,8)  

c.area()
r.area()
t.area()

