import os, hashlib, pathlib, binascii, time, csv
from company import Company
from user import User
from employee import Employee
from director import Director

def start_connexion_process(company_file_path,user_file_path):
    choice_list = [1,2,3]
    number = None
    print("Please choose an option")
    time.sleep(0.1)
    print("1: Create a new Company")
    time.sleep(0.1)
    print("2: Connect to an existing Company")
    time.sleep(0.1)
    print("3: Shutdown")
    time.sleep(0.1)
    while True:
        while not number or not number in choice_list:
            try:
                number=int(input("Make your choice: "))
                clearConsole()
                time.sleep(0.1)
            except:
                print("error")

            if number == 1:
                    time.sleep(0.1)
                    Company.create_company(company_file_path,user_file_path)
            elif number == 2:
                    time.sleep(0.1)
                    company_list = Company.load_company_from_csv(company_file_path)
                    choosed_company = Company.choose_company(company_list, company_file_path, user_file_path)
                    clearConsole()
                    User.connect(company_file_path, user_file_path, choosed_company)
            elif number == 3:
                    quit()  
            else:
                time.sleep(0.1)
                print("Invalid Choice! You should choose 1, 2 or 3.")
                time.sleep(0.1)
            

#debut load_user_from_csv()
def load_user_from_csv(user_file_path):
        user_list = []
        cpt_column = search_in_file(user_file_path)
        with open(user_file_path, 'r') as csvfile:
            filereader = csv.reader(csvfile, lineterminator = '\n', delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for line in filereader:
                if line[cpt_column["UserName"]] != "UserName":
                    if line[cpt_column["Level"]] == "director":
                        user_list.append(Director(line[cpt_column["UserName"]], line[cpt_column["UserFirstname"]], line[cpt_column["Age"]], line[cpt_column["Phone"]], line[cpt_column["Email"]], line[cpt_column["Login"]], line[cpt_column["Password"]], line[cpt_column["CompanyID"]], line[cpt_column["State"]], line[cpt_column["Job"]]))
                    elif line[cpt_column["Level"]] == "employee":
                        user_list.append(Employee(line[cpt_column["UserName"]], line[cpt_column["UserFirstname"]], line[cpt_column["Age"]], line[cpt_column["Phone"]], line[cpt_column["Email"]], line[cpt_column["Login"]], line[cpt_column["Password"]], line[cpt_column["CompanyID"]], line[cpt_column["State"]], line[cpt_column["Job"]]))
            csvfile.close()
        return user_list    
#fin load_user_from_csv()




#debut create_user()

def create_user(user_connected, company_file_path, user_file_path):

    company_id=user_connected.get_user_company_id()
    user_name =""
    user_first_name =""
    email ="" 
    age =""
    phone =""
    job =""
    state = None
    check_director = None 

    while not user_name:
        try:
            user_name=input("User Name (must be a string):")
            time.sleep(0.1)
        except:
            print("invalid or empty value, you should choose a string")

    while not user_first_name:
        try:
            user_first_name=input("User FirstName (must be a string):")
            time.sleep(0.1)
        except:
            print("invalid or empty value, you should choose a string")

    while not email:
        try:
            email=input("User Email (must be a string):")
            time.sleep(0.1)
        except:
            print("invalid or empty value, you should choose a string")

    while not age:
        try:
            age=input("User Age (must be a string):")
            time.sleep(0.1)
        except:
            print("invalid or empty value, you should choose a string")

    while not phone:
        try:
            phone=input("User Phone (must be a string):")
            time.sleep(0.1)
        except:
            print("invalid or empty value, you should choose a string")

    while not job:
        try:
            job=input("User job (must be a string):")
            time.sleep(0.1)
        except:
            print("invalid or empty value, you should choose a string")

    while state == None:
        try:
            check=str.lower(input("would you activate this new user ? (y/n):"))
            time.sleep(0.1)
            if check == "y":
                state = 1
            elif check == "n":
                state = 0
            else:
                print("wrong value, you should choose y or n")
        except:
            print("invalid or empty value, you should choose y or n")

    while check_director == None:
        try:
            check=str.lower(input("is this user is a director ? (y/n):"))
            time.sleep(0.1)
            if check == "y":
                check_director = 1
            elif check == "n":
                check_director = 0
            else:
                print("wrong value, you should choose y or n")
        except:
            print("invalid or empty value, you should choose y or n")

    login = User.create_login(user_name, user_first_name, company_id, user_file_path)
    password = User.generate_psswd()
    if check_director:
        new_user = Director(user_name, user_first_name, age, phone, email, login, password, company_id, state,job)
    else:
        new_user = Employee(user_name, user_first_name, age, phone, email, login, password, company_id, state,job)
    User.save_user(new_user,user_file_path)
    print("new user created")
    User.connected(user_connected, company_file_path, user_file_path)

#fin create_user()
        

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)


def search_in_file(user_file_path):
    columnInfile = {}

    with open(user_file_path, 'r') as csvfile:
        filereader = csv.reader(csvfile, lineterminator = '\n', delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        UserName_cpt = 0
        UserFirstname_cpt = 0
        Age_cpt = 0
        Phone_cpt = 0
        Email_cpt = 0
        Login_cpt = 0
        Password_cpt = 0
        CompanyID_cpt = 0
        Job_cpt = 0
        State_cpt = 0
        Level_cpt = 0
        tmp_cpt = 0
        for line in filereader:
            for column in line:
                if column == "UserName":
                    columnInfile["UserName"] = tmp_cpt
                    tmp_cpt=tmp_cpt+1

                elif column == "UserFirstname":
                    columnInfile["UserFirstname"] = tmp_cpt
                    tmp_cpt=tmp_cpt+1

                elif column == "Age":
                    columnInfile["Age"] = tmp_cpt
                    tmp_cpt=tmp_cpt+1

                elif column == "Phone":
                    columnInfile["Phone"] = tmp_cpt
                    tmp_cpt=tmp_cpt+1

                elif column == "Email":
                    columnInfile["Email"] = tmp_cpt
                    tmp_cpt=tmp_cpt+1

                elif column == "Login":
                    columnInfile["Login"] = tmp_cpt
                    tmp_cpt=tmp_cpt+1

                elif column == "Password":
                    columnInfile["Password"] = tmp_cpt
                    tmp_cpt=tmp_cpt+1

                elif column == "CompanyID":
                    columnInfile["CompanyID"] = tmp_cpt
                    tmp_cpt=tmp_cpt+1

                elif column == "Job":
                    columnInfile["Job"] = tmp_cpt
                    tmp_cpt=tmp_cpt+1

                elif column == "State":
                    columnInfile["State"] = tmp_cpt
                    tmp_cpt=tmp_cpt+1

                elif column == "Level":
                    columnInfile["Level"] = tmp_cpt
                    tmp_cpt=tmp_cpt+1
                        
                else:
                    break   
        csvfile.close()
    return columnInfile
        



    