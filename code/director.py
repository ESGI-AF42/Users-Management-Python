import os, hashlib, pathlib, binascii, time, csv
from user import User

class Director(User):

    def __init__(self,UserName, UserFirstname, Age, Phone, Email, Password, CompanyID, Job):
        User.__init__(self,UserName, UserFirstname, Age, Phone, Email, Password, CompanyID)
        self.set_user_level("director")
        self.job = Job
        
    def get_user_job(self):
        return self.job

    def create_root_user(CompanyID,user_user_file_path):
        RoottUser = Director('oot', 'r', 'None', 'None', 'None', 'root', CompanyID, 'None')
        User.save_user(RoottUser,user_user_file_path)
        print ('password : root')
        print ('( please, change your default password )')


