#Program to calculate total price of book based on given inputs.
#Defining class book
class book:
    #Accepting input from the user
    def accept_input (self):
    
        self.name=str(input("Enter name of Book:"))
        self.author=str(input("Enter author of Book:"))
        self.price=str(input("Enter price of Book:"))
        self.n_copies=str(input("Enter no. of copies to purches Book:"))
        
    #Calculating total price of books purchased
    def total_price(self):
        t=self.price*self.n_copies
        print("Total Price:",t)
        
    def details(self):
        print("purchase details".center(70,"-"))
        print("Name of Book:",self.name)
        print("Name of Book:",self.author)
        print("No of copies:"'self.n_copies)
              
#Calling the functions
obj=Book()
obj.accept_input
obj.details()
obj.total_price()
