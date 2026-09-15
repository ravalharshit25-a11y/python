# The Scenario: You are designing a Ticket Approval Workflow System. There are standard tickets, but you also need a special
# type of ticket for urgent issues that requires higher-level authorization.

# Your Task:
# Write a code with two classes:

# A parent class Ticket that initializes with ticket_id and description. It should have a method get_status() that returns "Pending".

# A child class UrgentTicket that inherits from Ticket.

# Use super().__init__() to pass the ticket_id and description to the parent, but add a new attribute 
# specific to the child called manager_approval_required and set it to True.

# Create an instance of UrgentTicket and print its description and its manager_approval_required status

class ticket:

    def __init__(self,ticket_id,description):
        self.ticket_id=ticket_id
        self.description=description

    def get_status(self):
        print("pending")

class UrgentTicket(ticket):
    def __init__(self,ticket_id,description):
        super().__init__(ticket_id,description)   
        self.manager_approval_required=True

obj=UrgentTicket(1,"i have a problem in my laptop")   
print(obj.description)    
print(obj.manager_approval_required)          