from user import User

class Employee(User):

    def __init__(self, UserName, UserFirstname, Age, Phone, Email, Login, Password, CorpID, Job):
        User.__init__(self, UserName, UserFirstname, Age, Phone, Email, Login, Password, CorpID)
        self.set_user_level("employee")
        self.job = Job

    def get_employee_job(self):
        return self.job

