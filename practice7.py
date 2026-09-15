# Problem Statement:
# Create a Student class where student marks cannot be directly accessed outside the class.

# Requirements:

# Create private variable __marks.
# Create:
# set_marks()
# get_marks()
# calculate_percentage()
# calculate_grade()

# Rules:

# Marks must be between 0 and 100.
# Calculate grade according to percentage.

# Sample Output:

# Marks: 85
# Percentage: 85%
# Grade: A

# Concepts: Encapsulation, Private Variables, Getter, Setter

class student:

    def __init__(self):
        self.__marks=[]

    def get_marks(self):
        print("marks : " ,self.__marks)

    def set_marks(self,marks):
        self.__marks.append(marks)
             
 
    def calculate_percentage(self,a,b):
        self.total=sum(self.__marks)
        self.b=b
        self.percentage=(self.total*100)/(a*self.b)
        print("percentage : ",self.percentage)

    def calculate_grade(self):

        if self.percentage > 90:
            print("grage A")    
        elif self.percentage > 80:
            print("grage B")
        elif self.percentage > 70:
            print("grage C")  
        elif self.percentage > 60:
            print("grage D")        
        elif self.percentage > 50:
            print("grage E")
        else :
            print("fail")    

a=int(input("how many subject marks you mant to enter : "))
b=int(input("total marks of one subject : "))

stu=student()
i=0

while i < a:
    marks=int(input("enter your marks"))
    if marks >=0 and marks <= b:
        stu.set_marks(marks)
        i=i+1
    else :
        print("marks must be between 0 to ",b)    

stu.get_marks()
stu.calculate_percentage(a,b)
stu.calculate_grade()            