class Book():
    copies_lent = 0
    
    def __init__(self, title, author, total_copies):
        self.title = title
        self.author = author
        self.total_copies = total_copies
    
    def __str__(self):
        return f"{self.title} by {self.author}"

    def get_title(self): 
        return self.title

    def get_author(self): 
        return self.author

    def get_total_copies(self): 
        return self.total_copies
    
    def set_total_copies(self, total_copies):
        self.total_copies = total_copies
        pass

    def loan(self):
        if self.copies_lent < self.total_copies:
            print("Loan authorized, copy transferred to in use.")
            self.copies_lent += 1
            return True
        else:
            print("Unable to perform operation, no copies available.")
            return False
        
    def returns(self):
        if self.copies_lent != 0:
            print("Copy returned succesfully!")
            self.copies_lent -= 1
            return True
        else: 
            print("Unable to perform operation, no copies lent at the moment.")
            return False