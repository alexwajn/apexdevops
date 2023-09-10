class Person:
    def __init__(self, f_name="", l_name="", phone=""):
        self.f_name = f_name
        self.l_name = l_name
        if self.check_phone(phone):
            self.phone = phone
        else: self.phone = 0
    
    def __str__(self):
        return f"{self.l_name}, {self.f_name}. Phone: {self.phone} "
    
    def check_phone(self, phone):
        ret = True
        for dig in phone:
            if dig not in "0123456789": ret = False
        if len(phone) != 9: ret = False
        return ret
    
    def set_fname(self, fname):
        self.f_name = fname
        
    def set_lname(self, lname):
        self.l_name = lname

    def set_phone(self, phone):
        if self.check_phone(phone):
            self.phone = phone
        else: self.phone = 0
    
    def get_fname(self):
        return self.f_name

    def get_lname(self):
        return self.l_name

    def get_phone(self):
        return self.phone