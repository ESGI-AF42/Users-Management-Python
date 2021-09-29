import os, hashlib, pathlib, binascii, time, csv
from user import User

class Director(User):

    def __init__(self,UserName, UserFirstname, Age, Phone, Email, Password, CompanyID, Job):
        User.__init__(self,UserName, UserFirstname, Age, Phone, Email, Password, CompanyID)
        self.set_user_level("director")
        self.job = Job
        
    def get_director_job(self):
        return self.job

    def create_root_user(CompanyID,user_user_file_path):
        RoottUser = Director('oot', 'r', 'None', 'None', 'None', 'root', 'None', CompanyID)
        Director.save_user(RoottUser,user_user_file_path)
        print ('password : root')
        print ('( please, change your default password )')


    def save_user(director,user_file_path):
            with open(user_file_path, 'a') as csvfile:
                filewriter = csv.writer(csvfile, lineterminator = '\n', delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                filewriter.writerow([director.get_user_name(), director.get_user_firstname(), director.get_user_age(), director.get_user_phone(), director.get_user_email(), director.get_user_login(), director.get_user_password(), director.get_user_company_id(), director.get_director_job()])
                csvfile.close()