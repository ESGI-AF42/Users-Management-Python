from user import User

class Employee(User):

    def __init__(self, UserName, UserFirstname, Age, Phone, Email, Login, Password, CompanyID, Job):
        User.__init__(self, UserName, UserFirstname, Age, Phone, Email, Login, Password, CompanyID)
        self.set_user_level("employee")
        self.job = Job

    def get_user_job(self):
        return self.job

