from member import Member

class Employee(Member):

    def __init__(self, UserName, UserFirstname, Age, Phone, Email, Login, Password, CorpID, Job):
        Member.__init__(self, UserName, UserFirstname, Age, Phone, Email, Login, Password, CorpID)
        self.set_member_level("employee")
        self.job = Job

    def get_employee_job(self):
        return self.job

