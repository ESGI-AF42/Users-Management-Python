from member import Member

class Director(Member):

    def __init__(self,UserName, UserFirstname, Age, Phone, Email, Login, Password, CorpID, Job):
        Member.__init__(self,UserName, UserFirstname, Age, Phone, Email, Login, Password, CorpID)
        self.set_member_level("director")
        self.job = Job
        
    def get_director_job(self):
        return self.job
