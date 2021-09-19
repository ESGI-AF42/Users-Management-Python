from corp import Corp
class Employee():

        def __init__(self, Age, Phone, Salary, Fonction):
        self.age = Age
        self.phone = Phone
        self.salary = Salary
        self.fonction = Fonction

    def get_employee_age(self):
        return self.age

    def get_employee_phone(self):
        return self.phone
    
    def get_employee_salary(self):
        return self.salary
    
    def get_employee_fonction(self):
        return self.fonction
