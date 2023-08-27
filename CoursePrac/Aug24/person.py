import random

class Person:
    ID_LENGHT = 8
    MAJORITY_AGE = 18
    id_numbers = "0123456789"
    def __init__(self, name="", age=0, gender="", weight=0, height=0):
        self.id = self.generate_id()
        self.name = name
        self.age = age
        if self.check_gen(gender):
            self.gender = gender
        else: 
            print("Invalid gender. Set manually with set_gender('M or F')")
            self.gender = ""
        self.weight = weight
        self.height = height
        pass

    def check_gen(self, char):
        if char in "MF":
            return True
        else: return False

    def __str__(self):
        return f"{self.id}: {self.name}, {self.age} years old, {self.gender}, {self.weight}kg, {self.height}m" 

    def set_gender(self, gender):
        if self.check_gen(gender):
            self.gender = gender
        else: print("Invalid gender. Set manually with set_gender('M or F')")
        pass    
    
    def set_name(self, name):
        self.name = name
        pass    
    
    def set_age(self, age):
        self.age = age
        pass
    
    def set_weight(self, weight):
        self.weight = weight
        pass

    def set_height(self, height):
        self.height = height
        pass
    
    def calculate(self):  #Calculates BMI for the person and verifies according to stantard table
        bmi = self.weight / self.height ** 2
        if bmi < 18.5: result = -1
        elif bmi > 24.9: result = 1
        else: result = 0
        return result
    
    def is_over_maj_age(self):
        if self.age >= self.MAJORITY_AGE:
            return True
        else: return False
    
    def generate_id(self):
        generated_id = ""
        for i in range(self.ID_LENGHT):
            generated_id += self.id_numbers[random.randint(0,9)]
        return generated_id
