from person import *

def print_person_info(person):
    print(person)
    if person.calculate() == 1: print("Person is overweight.")
    elif person.calculate() == -1: print("Person is underweight.")
    else: print("Person is on normal weight.")
    if person.is_over_maj_age(): print("Person is of legal age.")
    else: print("Person is not of legal age.")
    pass

def main():
    persons = [0,1,2]
    name = input("Enter name:_")
    age = int(input("Enter age:_"))
    gender = input("Enter gender (M or F):_")
    weight = float(input("Enter weight in kg:_"))
    height = float(input("Enter height in m:_"))
    persons[0] = Person(name, age, gender, weight, height)
    persons[1] = Person(name, age, gender)
    persons[2] = Person()
    persons[1].set_weight(75)
    persons[1].set_height(1.90)
    persons[2].set_name("John Smith")
    persons[2].set_age(35)
    persons[2].set_gender("M")
    persons[2].set_height(1.76)
    persons[2].set_weight(89)
    for person in persons: print_person_info(person)
    pass

if __name__ == "__main__":
    main()
    pass