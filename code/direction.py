from member import Member

class Direction(Member):

    def __init__(self, CorpName, CorpType, CorpSector, CorpCountry, CorpAddress , UserName, UserFirstname, Age, Phone, Email, Login, Password,Job):
        Member.__init__(self, CorpName, CorpType, CorpSector, CorpCountry, CorpAddress , UserName, UserFirstname, Age, Phone, Email, Login, Password)
        self.job = Job
        
    def get_age(self):
        return self.age
    
    def get_phone(self):
        return self.phone
    
    def get_email(self):
        return self.email

    def get_login(self):
        return self.login

    def get_password(self):
        return self.password

    def get_salary(self):
        return self.salary
