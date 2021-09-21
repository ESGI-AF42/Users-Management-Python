from member import Member

class Employee(Member):

    def __init__(self, CorpName, CorpType, CorpSector, CorpCountry, CorpAddress , UserName, UserFirstname, Age, Phone, Email, Login, Password,Job):
        Member.__init__(self, CorpName, CorpType, CorpSector, CorpCountry, CorpAddress , UserName, UserFirstname, Age, Phone, Email, Login, Password)
        self.job = Job



    def get_employee_age(self):
        return self.age

    def get_employee_phone(self):
        return self.phone
    
    def get_employee_salary(self):
        return self.salary
    
    def get_employee_fonction(self):
        return self.fonction
