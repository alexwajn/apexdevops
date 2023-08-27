import random

class Password:
    uppercase_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_chars = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    all_chars = uppercase_chars + lowercase_chars + numbers
    
    def __init__(self, lenght=8):
        passwd = ""
        for i in range(lenght):
            passwd = passwd + self.all_chars[random.randint(0,61)]
        self.lenght = lenght
        self.password = passwd
        pass

    def __str__(self):
        return f"{self.password}"

    def is_strong(self):
        upcase = 0
        lowercase = 0
        number = 0
        for char in self.password:
            if char in self.uppercase_chars: upcase += 1
            elif char in self.lowercase_chars: lowercase += 1
            elif char in self.numbers: number += 1
            else: pass
        if (upcase > 2) and (lowercase > 1) and (number > 5):
            return True
        else: return False

    def generate(self):    
        passwd = ""
        for i in range(self.lenght):
            passwd = passwd + self.all_chars[random.randint(0,61)]
        self.password = passwd
        return self.password
    
    def get_password(self):
        return self.password
    
    def get_lenght(self):
        return self.lenght
    
    def set_length(self, lenght):
        self.lenght = lenght
        pass





