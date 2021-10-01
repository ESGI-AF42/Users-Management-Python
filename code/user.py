import os, hashlib, pathlib, binascii, time, csv, Team_IT_functions
import company
from getpass import getpass

class User():

    def __init__(self, UserName, UserFirstname, Age, Phone, Email, Login, Password, CompanyID, State):     
        self.name = UserName
        self.firstname = UserFirstname
        self.age = Age
        self.phone = Phone
        self.email = Email
        self.login = Login
        self.password = Password
        self.company_id = int(CompanyID)
        self.state = State

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

    def get_user_state(self):
        return self.state

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

    def set_user_state(self, State):
        self.state = State
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
            filewriter.writerow(['UserName', 'UserFirstname', 'Age', 'Phone', 'Email', 'Login', 'Password', 'CompanyID' , 'State', 'Job', 'Level'])
            csvfile.close()
#fin create_userCSV()

#debut save_user()
    def save_user(self,user_file_path):
        UserName = self.get_user_name() 
        UserFirstname = self.get_user_firstname()
        with open(user_file_path, 'a') as csvfile:
            filewriter = csv.writer(csvfile, lineterminator = '\n', delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow([UserName, UserFirstname, self.get_user_age(), self.get_user_phone(), self.get_user_email(), User.create_login(UserName,UserFirstname), User.hash_psswd(self.get_user_password()), self.get_user_company_id(), self.get_user_state(), self.get_user_job(), self.get_user_level()])
            csvfile.close()
#fin save_user()

#debut connect()
    def connect(company_file_path,user_file_path,choosed_company):
        Connected = False
        user_list = Team_IT_functions.load_user_from_csv(user_file_path)
        choosed_company_id=choosed_company.get_company_id()
        user_login_list=[]
        login=''
        user_connected = None
        

        while not Connected:
            for user_obj in user_list:
                user_company_id = user_obj.get_user_company_id()
                if user_company_id == choosed_company_id:
                    user_login_list.append(user_obj.get_user_login())
            while not login in user_login_list:
                login = input("Login : ")
                time.sleep(0.1)
                if login in user_login_list:
                    if User.check_user_state(login, choosed_company_id ,user_file_path):
                        WrongPassword = True
                        while WrongPassword:
                            password = getpass('Password:')
                            time.sleep(0.1)
                            if User.verify_psswd(user_obj.get_user_password(),password):
                                user_connected = user_obj
                                Team_IT_functions.clearConsole()
                                print('you are now connected')
                                print('')
                                time.sleep(0.1)
                                WrongPassword=False
                            else:
                                print('wrong password')
                                print('1 : retry')
                                print('2 : change login')
                                #mettre la possibilité de changer de login
                        Connected = True 
                    else:
                        print("this login is deactivated in this company, choose an other one or change company")
                        time.sleep(0.1)
                        Team_IT_functions.start_connexion_process(company_file_path,user_file_path)

                else:
                    print('This login doesn\'t exist in this company')
                    time.sleep(0.1)
                    print('1 : retry')
                    print('2 : change company')
                    #mettre la possibilité de changer de compagnie
        User.connected(user_connected, company_file_path, user_file_path)
#fin connect()

    def connected(user_connected, company_file_path, user_file_path):
        print('1 : profil')
        time.sleep(0.1)
        print('2 : user-list')
        time.sleep(0.1)
        print('3 : disconnect')
        time.sleep(0.1)
        if user_connected.get_user_level() == "director":
            print('4 : manage users')
            time.sleep(0.1)
            print('5 : manage company')
            time.sleep(0.1)
        
        while True:
            try:
                number=int(input("Make your choice: "))
                Team_IT_functions.clearConsole()
                time.sleep(0.1)
            except:
                print("invalid or empty value, you should choose 1, 2 or 3")

            if number == 1:              
                User.show_profile(user_connected, company_file_path, user_file_path)
            elif number == 2:              
                User.show_user_list(user_file_path,user_connected)
            elif number == 3:
                Team_IT_functions.start_connexion_process(company_file_path,user_file_path) 
            elif number == 4 and user_connected.get_user_level() == "director":
                User.manage_users()
            elif number == 5 and user_connected.get_user_level() == "director":
                User.manage_company()
            else:
                time.sleep(0.1)
                print("Invalid Choise! You should choose 1, 2 or 3.")
                time.sleep(0.1)


    def show_profile(user_connected, company_file_path, user_file_path):
        print("")
        print("PROFILE")
        print("")
        print("UserName : ", user_connected.get_user_name())
        print("UserFirstname : ", user_connected.get_user_firstname())
        print("Age : ", user_connected.get_user_age())
        print("Phone : ", user_connected.get_user_phone())
        print("Email : ", user_connected.get_user_email())
        print("Company : ", company.Company.get_company_from_id(user_connected.get_user_company_id(), company_file_path))
        print("Job : ", user_connected.get_user_job())
        print("Level : ", user_connected.get_user_level())
        print("")
        print("")
        time.sleep(0.1)
        print('1 : edit')
        time.sleep(0.1)
        print('2 : back')
        

        while True:
            try:
                number=int(input("Make your choice: "))
                Team_IT_functions.clearConsole()
                time.sleep(0.1)
            except:
                print("invalid or empty value, you should choose 1 or 2")

            if number == 1:              
                User.edit_profile(user_connected)
            elif number == 2:  
                User.connected(user_connected, company_file_path, user_file_path)
            else:
                time.sleep(0.1)
                print("Invalid Choise! You should choose 1 or 2")
                time.sleep(0.1)


#Todo
    def edit_profile(user_connected):
        print("Which information would you change ?")
        print("")
        print("1 : UserName")
        print("2 : UserFirstname")
        print("3 : Age")
        print("4 : Phone")
        print("5 : Email")



    def show_user_list(user_file_path, user_connected):
        user_dic = {}
        user_list = Team_IT_functions.load_user_from_csv(user_file_path)
        for user_obj in user_list:
            if user_connected.get_user_company_id() == user_obj.get_user_company_id():
                user_name = user_obj.get_user_name()
                user_firstname = user_obj.get_user_firstname()
                user_age = user_obj.get_user_age()
                user_phone = user_obj.get_user_phone()
                user_email = user_obj.get_user_email()
                user_level = user_obj.get_user_level()
                user_dic[user_obj.get_user_login()]=[user_name,user_firstname,user_age,user_phone,user_email,user_level]
        print ("{:<8} {:<8} {:<15} {:<5} {:<11} {:<20} {:<9}".format('Login','UserName','UserFirstname','Age','Phone','Email','Level'))
        for key, value in user_dic.items():
            userName, userFirstname, age, phone, email, level = value
        print ("{:<8} {:<8} {:<15} {:<5} {:<11} {:<20} {:<9}".format(key, userName, userFirstname, age, phone, email, level))

#Todo    
    def manage_users():
        print("manage users")
        time.sleep(0.1)
        print('1 : create')
        time.sleep(0.1)
        print('2 : activate')
        time.sleep(0.1)
        print('3 : deactivate')
        time.sleep(0.1)


#Todo
    def manage_company():
        print("manage company")

    def check_user_state(login, companyID,user_file_path):
        State = False
        user_list = Team_IT_functions.load_user_from_csv(user_file_path)
        

        for user_obj in user_list:
            check = int(user_obj.get_user_state())
            if login == user_obj.get_user_login() and user_obj.get_user_company_id() == companyID:
                if check != 0 :
                    State = True
        return State