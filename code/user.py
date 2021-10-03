import os, hashlib, pathlib, binascii, time, csv, Team_IT_functions, shutil
from tempfile import NamedTemporaryFile
from getpass import getpass
from random import randint
import company

        

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


#debut create_login() polymorphie
    def create_login(username, userfirstname, user_company_id, user_file_path):
        usernameLow = str.lower(username)
        UserFirstnameLow = str.lower(userfirstname)
        login = UserFirstnameLow[0]+usernameLow
        user_list=Team_IT_functions.load_user_from_csv(user_file_path)
        cpt = 0
        for user_obj in user_list:
            if user_obj.get_user_login() == login and user_company_id == user_obj.get_user_company_id():
                cpt=cpt+1
                login = login + str(cpt)
        return login
#fin create_login()

#debut generate_psswd() 
    def generate_psswd():
        psswd = ''
        for i in range(8):
            if i <= 1:
                rng = randint(65, 90)
            elif i <= 4:
                rng = randint(97, 122)
            elif i <= 6:
                rng = randint(48, 57)
            else:
                rng = randint(33, 47)
            psswd = psswd + chr(rng)
        return psswd
#fin generate_psswd()


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
        user_name = self.get_user_name()
        user_first_name = self.get_user_firstname()
        user_company_id = self.get_user_company_id()
        new_login = User.create_login(user_name, user_first_name, user_company_id, user_file_path)
        print ('login : ', new_login) 
        print ('password : ', self.get_user_password())

        with open(user_file_path, 'a') as csvfile:
            filewriter = csv.writer(csvfile, lineterminator = '\n', delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow([user_name, user_first_name, self.get_user_age(), self.get_user_phone(), self.get_user_email(), new_login, User.hash_psswd(self.get_user_password()), user_company_id, self.get_user_state(), self.get_user_job(), self.get_user_level()])
            csvfile.close()
#fin save_user()

#debut connect()
    def connect(company_file_path,user_file_path,choosed_company):
        Connected = False
        user_list = Team_IT_functions.load_user_from_csv(user_file_path)
        choosed_company_id=choosed_company.get_company_id()
        user_company_list=[]
        user_company_login_list=[]
        login=''
        user_connected = None
        

        while not Connected:
            for user_obj in user_list:
                if user_obj.get_user_company_id() == choosed_company_id:
                    user_company_list.append(user_obj)

            for user_company_obj in user_company_list:
                user_company_login_list.append(user_company_obj.get_user_login())

            while not login in user_company_login_list:
                login = input("Login : ")
                time.sleep(0.1)
                if login in user_company_login_list:
                    for user_from_login in user_company_list:
                        if user_from_login.get_user_login() == login:
                            break

                    if User.check_user_state(login, choosed_company_id ,user_file_path):
                        WrongPassword = True
                        while WrongPassword:
                            password = getpass('Password:')
                            time.sleep(0.1)
                            if User.verify_psswd(user_from_login.get_user_password(),password):
                                user_connected = user_from_login
                                Team_IT_functions.clearConsole()
                                print('you are now connected')
                                print('')
                                time.sleep(0.1)
                                WrongPassword=False
                            else:
                                choice_list = [1,2]
                                number = None
                                print('wrong password')
                                print('1 : retry')
                                print('2 : change login')
                                while True:
                                    while not number or not number in choice_list:
                                        try:
                                            number=int(input("Make your choice: "))
                                            Team_IT_functions.clearConsole()
                                            time.sleep(0.1)
                                        except:
                                            print("error")
                                        
                                        if number == 1:              
                                            break
                                        elif number == 2:              
                                            User.connect(company_file_path,user_file_path,choosed_company)
                                        else:
                                            time.sleep(0.1)
                                            print("Invalid Choice! You should choose 1 or 2.")
                                            time.sleep(0.1)
                                    break
                        Connected = True 
                    else:
                        print("this login is deactivated in this company, choose an other one or change company")
                        time.sleep(0.1)
                        Team_IT_functions.start_connexion_process(company_file_path,user_file_path)

                else:
                    choice_list = [1,2]
                    number = None
                    print('This login doesn\'t exist in this company')
                    time.sleep(0.1)
                    print('1 : retry')
                    print('2 : change company')
                    while True:
                        while not number or not number in choice_list:
                            try:
                                number=int(input("Make your choice: "))
                                Team_IT_functions.clearConsole()
                                time.sleep(0.1)
                            except:
                                print("error")

                            if number == 1:              
                                break
                            elif number == 2:              
                                company_list = company.Company.load_company_from_csv(company_file_path)
                                new_choosed_company = company.Company.choose_company(company_list, company_file_path, user_file_path)
                                Team_IT_functions.clearConsole()
                                User.connect(company_file_path, user_file_path, new_choosed_company)
                            else:
                                time.sleep(0.1)
                                print("Invalid Choice! You should choose 1 or 2.")
                                time.sleep(0.1)
                        break

        User.connected(user_connected, company_file_path, user_file_path)
#fin connect()

    def connected(user_connected, company_file_path, user_file_path):
        choice_list = [1,2,3]
        choice_list2 = [4,5]
        number = None
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
            while not number or not number in choice_list or not number in choice_list2:
                try:
                    number=int(input("Make your choice: "))
                    Team_IT_functions.clearConsole()
                    time.sleep(0.1)
                except:
                    print("error")

                if number in choice_list:
                    if number == 1:              
                        User.show_profile(user_connected, company_file_path, user_file_path)
                    elif number == 2:              
                        User.show_user_list(user_file_path, company_file_path, user_connected)
                    else:
                        Team_IT_functions.start_connexion_process(company_file_path,user_file_path) 

                elif number in choice_list2 and user_connected.get_user_level() == "director":    
                    if number == 4:
                        User.manage_users(user_connected,company_file_path,user_file_path)
                    else :
                        User.manage_company()

                else:
                    time.sleep(0.1)
                    print("Invalid Choice!")
                    time.sleep(0.1)

    def show_profile(user_connected, company_file_path, user_file_path):
        choice_list = [1,2]
        number = None
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
            while not number or not number in choice_list:
                try:
                    number=int(input("Make your choice: "))
                    Team_IT_functions.clearConsole()
                    time.sleep(0.1)
                except:
                    print("error")

                if number == 1:              
                    User.edit_profile(user_connected, user_file_path , company_file_path)
                elif number == 2: 
                    User.connected(user_connected, company_file_path, user_file_path)
                else:
                    time.sleep(0.1)
                    print("Invalid Choice! You should choose 1 or 2")
                    time.sleep(0.1)



    def edit_profile(user_connected, user_file_path, company_file_path):
        choice_list = [1,2,3,4,5,6]
        number = None
        print("Which information would you change ?")
        print("")
        print("1 : UserName")
        print("2 : UserFirstname")
        print("3 : Age")
        print("4 : Phone")
        print("5 : Email")
        print("6 : Password")

        while True:
            while not number or not number in choice_list:
                try:
                    number=int(input("Make your choice: "))
                    Team_IT_functions.clearConsole()
                    time.sleep(0.1)
                except:
                    print("error")

                if number == 1:              
                    User.update_value(user_connected, user_file_path, "UserName")
                elif number == 2: 
                    User.update_value(user_connected, user_file_path, "UserFirstname")
                elif number == 3: 
                    User.update_value(user_connected, user_file_path, "Age")
                elif number == 4: 
                    User.update_value(user_connected, user_file_path, "Phone")
                elif number == 5:   
                    User.update_value(user_connected, user_file_path, "Email")           
                elif number == 6:  
                    User.update_value(user_connected, user_file_path, "Password")
                else:
                    time.sleep(0.1)
                    print("Invalid Choice! You should choose 1,2,3,4 or 5")
                    time.sleep(0.1)           
            User.show_profile(user_connected, company_file_path, user_file_path)
            

    def update_value(user_connected, user_file_path, fields):
        if fields == "UserName":
            value = input("UserName : ")
            user_connected.set_user_name(value)

        elif fields == "UserFirstname":
            value = input("UserFirstname : ")
            user_connected.set_user_firstname(value)

        elif fields == "Age":
            value = input("Age : ")
            user_connected.set_user_age(value)

        elif fields =="Phone":
            value = input("Phone : ")
            user_connected.set_user_phone(value)

        elif fields =="Email":
            value = input("Email : ")
            user_connected.set_user_email(value)

        else:
            value = getpass("Password : ")
            user_connected.set_user_password(value)

        User.replace_inCSV(user_file_path,user_connected)



    def show_user_list(user_file_path, company_file_path, user_connected):
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

        check=getpass("get back ? (press enter)")
        Team_IT_functions.clearConsole()
        User.connected(user_connected, company_file_path, user_file_path)
        

 
    def manage_users(user_connected,company_file_path,user_file_path):
        choice_list = [1,2,3,4]
        number = None

        print("manage users")
        time.sleep(0.1)
        print('1 : create')
        time.sleep(0.1)
        print('2 : activate')
        time.sleep(0.1)
        print('3 : deactivate')
        time.sleep(0.1)
        print('4 : back')
        time.sleep(0.1)

        while True:
            while not number or not number in choice_list:
                try:
                    number=int(input("Make your choice: "))
                    Team_IT_functions.clearConsole()
                    time.sleep(0.1)
                except:
                    print("error")
            
                if number == 1:              
                    Team_IT_functions.create_user(user_connected,company_file_path, user_file_path)
                elif number == 2:  
                    User.activate_user(user_connected, user_file_path, company_file_path)
                elif number == 3:  
                    User.deactivate_user(user_connected, user_file_path, company_file_path)
                elif number == 4:  
                    User.connected(user_connected, company_file_path, user_file_path)
                else:
                    time.sleep(0.1)
                    print("Invalid Choice! You should choose 1,2,3 or 4")
                    time.sleep(0.1)




#Todo
    def manage_company(user_connected, company_file_path, user_file_path):
        check=getpass(" Function not implemented yet (press enter)")
        Team_IT_functions.clearConsole()
        User.connected(user_connected, company_file_path, user_file_path)





    def check_user_state(login, companyID,user_file_path):
        State = False
        user_list = Team_IT_functions.load_user_from_csv(user_file_path)
        

        for user_obj in user_list:
            check = int(user_obj.get_user_state())
            if login == user_obj.get_user_login() and user_obj.get_user_company_id() == companyID:
                if check != 0 :
                    State = True
                    break
        return State




    def replace_inCSV(user_file_path,user_to_change):
        tempfile = NamedTemporaryFile(mode='w', delete=False)
        cpt_column = Team_IT_functions.search_in_file(user_file_path)

        with open(user_file_path, 'r') as csvfile, tempfile:
            filereader = csv.reader(csvfile, lineterminator = '\n', delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter = csv.writer(tempfile, lineterminator = '\n', delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for line in filereader:
                if str(user_to_change.get_user_company_id()) == line[cpt_column['CompanyID']] and user_to_change.get_user_login() == line[cpt_column['Login']]:
                    filewriter.writerow([user_to_change.get_user_name(), user_to_change.get_user_firstname(), user_to_change.get_user_age(), user_to_change.get_user_phone(), user_to_change.get_user_email(), user_to_change.get_user_login(), user_to_change.get_user_password(), user_to_change.get_user_company_id(), user_to_change.get_user_state(), user_to_change.get_user_job(), user_to_change.get_user_level()]) 
                else:
                    filewriter.writerow([line[cpt_column['UserName']], line[cpt_column['UserFirstname']], line[cpt_column['Age']], line[cpt_column['Phone']], line[cpt_column['Email']], line[cpt_column['Login']], line[cpt_column['Password']], line[cpt_column['CompanyID']], line[cpt_column['State']], line[cpt_column['Job']], line[cpt_column['Level']]]) 
        shutil.move(tempfile.name, user_file_path) 
            


    def activate_user(user_connected, user_file_path, company_file_path):
        print("which user you want activate ?")
        user_off_company_list = []
        user_off_company_dic = {}
        number = None
        cpt = 0
        user_list=Team_IT_functions.load_user_from_csv(user_file_path)
        for user_obj in user_list:
            if user_connected.get_user_company_id() == user_obj.get_user_company_id():
                if user_obj.get_user_state() == "0":
                    user_off_company_list.append(user_obj)
        for user_off_company_obj in user_off_company_list:
            cpt = cpt + 1
            user_off_company_dic[cpt]= user_off_company_obj
            print(cpt ," : ", user_off_company_obj.get_user_login())
        print (cpt+1 ," : Back")

        while True:
            while not number:
                try:
                        number=int(input("Make your choice: "))
                        time.sleep(0.1)
                except:
                    print("error")    
                if number <= cpt:
                    Team_IT_functions.clearConsole()
                    user_off_company_dic[number].set_user_state(1)
                    User.replace_inCSV(user_file_path,user_off_company_dic[number])
                    User.manage_users(user_connected,company_file_path,user_file_path)

                elif number == cpt+1:
                    Team_IT_functions.clearConsole()
                    User.manage_users(user_connected,company_file_path,user_file_path)
          
                else:
                    print("Invalid Choice!")




    def deactivate_user(user_connected, user_file_path, company_file_path):
        print("which user you want activate ?")
        user_up_company_list = []
        user_up_company_dic = {}
        number = None
        cpt = 0
        user_list=Team_IT_functions.load_user_from_csv(user_file_path)
        for user_obj in user_list:
            if user_connected.get_user_company_id() == user_obj.get_user_company_id():
                if user_obj.get_user_state()=="1" and user_obj.get_user_login() != "root" :
                    user_up_company_list.append(user_obj)
        for user_up_company_obj in user_up_company_list:
            cpt = cpt + 1
            user_up_company_dic[cpt]= user_up_company_obj
            print(cpt ," : ", user_up_company_obj.get_user_login())
        print (cpt+1 ," : Back")
        while True:
            while not number:
                try:
                        number=int(input("Make your choice: "))
                        time.sleep(0.1)
                except:
                    print("error")    
                if number <= cpt:
                    Team_IT_functions.clearConsole()
                    user_up_company_dic[number].set_user_state(0)
                    User.replace_inCSV(user_file_path,user_up_company_dic[number])
                    User.manage_users(user_connected,company_file_path,user_file_path)

                elif number == cpt+1:
                    Team_IT_functions.clearConsole()
                    User.manage_users(user_connected,company_file_path,user_file_path)

                else:
                    print("Invalid Choice!")

                   
        