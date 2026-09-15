# Problem Statement:
# Create an employee management system using inheritance.

# Create a parent class:

# Employee

# Create two child classes:

# Manager
# Developer

# Employee should contain:

# Name
# Employee ID
# Salary

# Manager should contain:

# Team size
# Department

# Developer should contain:

# Programming language
# Experience

# Requirements:

# Use super() to initialize parent class attributes.
# Create objects of both child classes.
# Display their complete information.

# Concepts: Inheritance, super(), Method Reuse

# --------------------------------------------------------------------------------------------

class Employee:
    def __init__(self,Name,employee_id,Salary):
        self.Name=Name
        self.employee_id=employee_id
        self.Salary=Salary

    def Display_employee(self):
        print("name : ",self.Name)
        print("employee ID : ",self.employee_id)
        print("salary : ",self.Salary)    

class Manager(Employee):
    def __init__(self,Name,employee_id,Salary,Team_size,Department):
        self.Team_size=Team_size
        self.Department=Department
        super().__init__(Name,employee_id,Salary)

    def Display_manager(self):
        self.Display_employee()
        print("team size : ",self.Team_size)
        print("department : ",self.Department)    

class Developer(Employee):
    def __init__(self,Name,employee_id,Salary,language,Experience):
        self.language=language
        self.Experience=Experience
        super().__init__(Name,employee_id,Salary)

    def Display_developer(self):
        self.Display_employee()
        print("programing language : ",self.language)
        print("experience : ",self.Experience)

manager=Manager("harshit",1,500000,20,"IT")   
developer=Developer("harshit",2,8000000,"python","5 years")
print("-------------------------MANAGER------------------------------------- ")
manager.Display_manager()
print("-------------------------------developer---------------------------------")     
developer.Display_developer()