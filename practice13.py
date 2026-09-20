# Problem Statement:
# Develop a library management system using Python OOP.

# Classes:

# Book
# Member
# Library

# Book attributes:

# Book ID
# Title
# Author
# Availability

# Member attributes:

# Member ID
# Name

# Library methods:

# add_book()
# remove_book()
# search_book()
# issue_book()
# return_book()
# display_books()

# Rules:

# A book can only be issued if available.
# A member can return only a book that they have issued.
# Search should work by title or author.

# Concepts: Classes, Objects, Encapsulation, Composition

# ------------------------------------------------------------------------------


class Book:
    def __init__(self,book_ID,title,Author):
        self._book_ID=book_ID
        self.title=title
        self.Author=Author
        self.Availability=True
        self.issue_to=None

    def get_id(self):
        return self._book_ID  

class Member:
    def __init__(self,member_ID,name):
        self._member_ID=member_ID
        self.name=name
        self.book_issued=[]

    def member_id(self):
        return self._member_ID

    def display_members(self):
        print("member id : ",self._member_ID)  
        print("member name : ",self.name)  


class Library:      
    def __init__(self):
        self._books=[]
        self._member=[]

    def add_book(self,book):
        self._books.append(book)   
        print("book added successfully !")
        print("--------------------------------------------")

    def add_member(self,member):
        self._member.append(member)
        print("member added successfully")

    def display_member(self):
        for member in self._member:
            print("------------members----------------")
            member.display_members()
            print("books :")
            for book in member.book_issued:
                print(book.title) 

    def remove_book(self,book_id):
        for book in self._books:
            if book.get_id() == book_id:
                if book.Availability:
                    self._books.remove(book)
                    print("------------------------book delete------------------------")
                    print("book deleted successfully")
                else:
                    print("------------------------book delete------------------------")
                    print("book is currenty not available.")
                return

        print("------------------------book delete------------------------")
        print("book not found.")        

    def search_Book(self,search_book):
        found=False
        for book in self._books:
            
            if book.title == search_book:
                print("----------------search book----------------------------")
                print("book id : ",book.get_id())
                print("book title : ",book.title)
                print("book author : ",book.Author)
                print("book availablity : ",book.Availability)
                found=True
        if found==False:
            print("----------------search book----------------------------")
            print("book not found.")

    def display_book(self):
        for book in self._books:
            print("--------------------------books details---------------------------------")
            print("book id : ",book.get_id())
            print("book title : ",book.title)
            print("book author : ",book.Author)
            print("book availablity : ",book.Availability)    

    def issue_book(self,member_id,book_title):
        m=None

        for member in self._member:
            if member.member_id()== member_id:
                m=member
                break

        if m == None:
            print("---------------book issued-----------------------")
            print("invalid member") 
            return       

        for book in self._books:
            if book.title==book_title:
                if book.Availability:
                    print("----------------book issue-------------------")
                    print("book is issued to you.")
                    book.Availability=False    
                    found=True
                    book.issue_to=member_id
                    m.book_issued.append(book)
                else:
                    print("----------------book issue-------------------")
                    print("currently book is not available")                    
                return

        print("----------------book issue-------------------")
        print("book not found.")   

    def return_book(self,member_id,book_title):
        m=None

        for member in self._member:
            if member.member_id()==member_id:
                m=member
                break

        if m==None:
            print("-----------------book return----------------------")
            print("enter valid member id.")
            return     
    
        for book in self._books:
            if book.title==book_title:
                if book.Availability==False and book.issue_to==member_id:
                    book.Availability=True
                    book.issue_to=None
                    m.book_issued.remove(book)
                    print("----------------book return-------------------")
                    print("book return successfully.")
                    found=True
                elif book.issue_to!=member_id and book.Availability==False:
                    print("----------------book return-------------------")
                    print("this book is not ours.")  
                else:
                    print("----------------book return-------------------")
                    print("book is not issued yet.")   
                return    


book1=Book(1,"python","meet")
book2=Book(2,"java","harshit")
book3=Book(3,"ai/ml","naman")

member1=Member(1,"harshit")
member2=Member(2,"naman")
member3=Member(3,"yash")

lib=Library()
lib.add_book(book1)
lib.add_book(book2)
lib.add_book(book3)
lib.add_member(member1)
lib.add_member(member2)
lib.add_member(member3)
lib.display_member()
# lib.remove_book(4)
# lib.search_Book("ai/ml")
# lib.display_book()
lib.issue_book(1,"java")
lib.issue_book(1,"ai/ml")
lib.display_member()
lib.display_book()
lib.remove_book(3)
# lib.display_book()
lib.return_book(1,"java")
lib.remove_book(2)
lib.display_member()
lib.display_book()
lib.issue_book(2,"java")
lib.display_member()
lib.display_book()