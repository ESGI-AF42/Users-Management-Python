from user import User

class Director(User):

    def __init__(self,UserName, UserFirstname, Age, Phone, Email, Login, Password, CorpID, Job):
        User.__init__(self,UserName, UserFirstname, Age, Phone, Email, Login, Password, CorpID)
        self.set_user_level("director")
        self.job = Job
        
    def get_director_job(self):
        return self.job

    def create_root_user(CorpID):
        RoottUser = Director('None', 'None', 'None', 'None', 'None', 'root', 'root', 'None', CorpID)
