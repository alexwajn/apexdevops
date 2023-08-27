from book import *

book1 = Book("Lord rings", "Tolkien", 10) 
for i in range(11):book1.loan()
book1.set_total_copies(20)
for i in range(4):book1.loan()
print(book1.copies_lent)
book1.returns()