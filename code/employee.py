from corp import Corp
from member import Member

class Employee(Member):

    def __init__(self, Job):
        self.job = Job


    def get_employee_age(self):
        return self.age

    def get_employee_phone(self):
        return self.phone
    
    def get_employee_salary(self):
        return self.salary
    
    def get_employee_fonction(self):
        return self.fonction
