from person import *

class Account:

    def __init__(self, acnum="", owner="", balance=0):
        self.acnum = acnum
        self.owner = owner
        if self.checkbal(balance):
            self.balance = balance
        else: self.balance = 0 
    
    def __str__(self):
        return f"Acc #: {self.acnum}, {self.owner}, Bal: {self.balance}"
    
    def checkbal(self, balance):
        if balance < 0:
            return False
        else: return True
    
    def transaction(self, type, amount):
        prevBal = self.balance
        if type == "W":
            self.balance -= amount
            print("Transaction type: Withdrawal")
        elif type == "D":
            self.balance += amount
            print("Transaction type: Deposit")
        print(f"Previous Balance: {prevBal}")
        print(f"Amount: {amount}")
        print(f"New balance: {self.balance}")

person1 = Person("John", "Smith", "235556985")
print(person1)
acc1 = Account("0001", person1, 500)
print(acc1)
acc1.transaction("W", 35)
print(acc1)
