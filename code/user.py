import os, hashlib, pathlib, binascii, time, csv

class User():

    def __init__(self, UserName, UserFirstname, Age, Phone, Email, Password, CompanyID):
        self.name = UserName
        self.firstname = UserFirstname
        self.age = Age
        self.phone = Phone
        self.email = Email
        Login = User.create_login(UserName,UserFirstname)
        self.login = Login
        self.password = User.hash_psswd(Password)
        self.company_id = int(CompanyID)
        self.level = ""
        print ('login : ' + Login) 

##début des des getters and setters
    def get_user_name(self):
        return self.name

    def get_user_firstname(self):
        return self.firstname
    
    def get_user_age(self):
        return self.age

    def get_user_phone(self):
        return self.phone

    def get_user_email(self):
        return self.email
    
    def get_user_login(self):
        return self.login

    def get_user_password(self):
        return self.password

    def get_user_level(self):
        return self.level

    def get_user_company_id(self):
        return self.company_id

    def set_user_name(self, Name):
        self.name = Name

    def set_user_firstname(self, Firstname):
        self.firstname = Firstname
    
    def set_user_age(self, Age):
        self.age = Age

    def set_user_phone(self, Phone):
        self.phone = Phone

    def set_user_email(self, Email):
        self.email = Email
    
    def set_user_login(self, Login):
        self.login = Login

    def set_user_password(self, Password):
        self.password = User.hash_psswd(Password)

    def set_user_level(self, Level):
        self.level = Level
##fin des getters and setters



#debut create_login()
    def create_login(UserName,UserFirstname):
        usernameLow = str.lower(UserName)
        UserFirstnameLow = str.lower(UserFirstname)
        return UserFirstnameLow[0]+usernameLow
#fin create_login()


#debut hash_psswd()
    def hash_psswd(password):
        key = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        psswdHashed = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),key, 100000)
        psswdHashed = binascii.hexlify(psswdHashed)
        return (key + psswdHashed).decode('ascii')
#fin hash_psswd()


#debut verify_psswd()
    def verify_psswd(stored_password, provided_password):
        key = stored_password[:64]
        stored_password = stored_password[64:]
        psswdHashed = hashlib.pbkdf2_hmac('sha512', provided_password.encode('utf-8'), key.encode('ascii'), 100000)
        psswdHashed = binascii.hexlify(psswdHashed).decode('ascii')
        return psswdHashed == stored_password
#fin verify_psswd()

#debut create_userCSV()
    def create_userCSV(user_file_path):
        with open(user_file_path, 'w') as csvfile:
            filewriter = csv.writer(csvfile, lineterminator = '\n', delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(['UserName', 'UserFirstname', 'Age', 'Phone', 'Email', 'Login', 'Password', 'CompanyID'])
            csvfile.close()
#fin create_userCSV()


    def save_user(self,user_file_path):
            with open(user_file_path, 'a') as csvfile:
                filewriter = csv.writer(csvfile, lineterminator = '\n', delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                filewriter.writerow([self.get_user_name(), self.get_user_firstname(), self.get_user_age(), self.get_user_phone(), self.get_user_email(), self.get_user_login(), self.get_user_password(), self.get_user_company_id(), self.get_user_job()])
                csvfile.close()

