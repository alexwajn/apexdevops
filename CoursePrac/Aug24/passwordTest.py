from password import *

class PasswordExec():
    
    def main_method(self):
        passwords = []
        lenghts = 50 #int(input("Enter with the lenghts of the passwords:_"))
        lenght_passwd_array = 10 #int(input("Enter with the number of the passwords to compute:_"))
        for i in range(lenght_passwd_array):
            password = Password(lenghts)
            password_tuple = password.get_password(), password.is_strong()
            passwords.append(password_tuple)
            print(password_tuple)
        

def main():
    password_test = PasswordExec()
    password_test.main_method()
    pass

if __name__ == "__main__":
    main()
    pass