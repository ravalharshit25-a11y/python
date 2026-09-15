# Problem Statement:
# Create a Python program using a class Student to store and display student information.

# Requirements:

# Create a class Student.
# Store:
# Roll number
# Name
# Course
# Age
# Create a method display_details() to display the information.
# Create at least 3 student objects.

class student:

    def __init__(self,roll_no,name,course,Age):
        self.roll_no=roll_no
        self.name=name
        self.course=course
        self.Age=Age
   

    def display_details(self):
        print("---------------------------------------------------------")
        print("name : ", self.name) 
        print("roll no : ", self.roll_no)    
        print("course : ", self.course)
        print("age : ", self.Age)

b=[]

a=int(input("enter no of students"))

for i in range(a):
    name=str(input("enter your name : "))
    roll_no=int(input("enter your roll number : "))   
    course=str(input("enter your course : "))
    Age=int(input("enter your age : "))       

    stu=student(roll_no,name,course,Age)
    b.append(stu)

for stu in b:
    stu.display_details()
    print("------------------------------------------")