class Employee:
    empCount = 0

    def __init__(self, name, salary, address="", sin=0, job_title="", dob=""):
        self.name = name
        self.salary = salary
        self.address = address
        self.sin = sin
        self.job_title = job_title
        self.dob = dob
        Employee.empCount += 1
    
    def __str__(self):
        return f"{self.name}, {self.job_title}, born in {self.dob}"

    def change_sal(self,difference): #use positive to increment salary or negative to decrement
        self.salary += difference
        print("Salary changed with success!")

    def set_name(self, name):
        self.name = name

    def set_address(self, address):
        self.address = address

    def set_jobtitle(self, job_title):
        self.job_title = job_title

    

    



    

        