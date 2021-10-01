import os, hashlib, pathlib, binascii, time, csv
from company import Company
from user import User
from employee import Employee
from director import Director

def start_connexion_process(company_file_path,user_file_path):
    print("Please choose an option")
    time.sleep(0.1)
    print("1: Create a new Company")
    time.sleep(0.1)
    print("2: Connect to an existing Company")
    time.sleep(0.1)
    print("3: Shutdown")
    time.sleep(0.1)

    check_value=True
    while check_value:
        try:
            number=int(input("Make your choice: "))
            clearConsole()
            time.sleep(0.1)
        except:
            print("invalid or empty value, you should choose 1, 2 or 3")

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
            print("Invalid Choise! You should choose 1, 2 or 3.")
            time.sleep(0.1)
            

#debut load_user_from_csv()
def load_user_from_csv(user_file_path):
        user_list = []
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
                        UserName_cpt = tmp_cpt
                        tmp_cpt=tmp_cpt+1

                    elif column == "UserFirstname":
                        UserFirstname_cpt = tmp_cpt
                        tmp_cpt=tmp_cpt+1

                    elif column == "Age":
                        Age_cpt = tmp_cpt
                        tmp_cpt=tmp_cpt+1

                    elif column == "Phone":
                        Phone_cpt = tmp_cpt
                        tmp_cpt=tmp_cpt+1

                    elif column == "Email":
                        Email_cpt = tmp_cpt
                        tmp_cpt=tmp_cpt+1

                    elif column == "Login":
                        Login_cpt = tmp_cpt
                        tmp_cpt=tmp_cpt+1

                    elif column == "Password":
                        Password_cpt = tmp_cpt
                        tmp_cpt=tmp_cpt+1

                    elif column == "CompanyID":
                        CompanyID_cpt = tmp_cpt
                        tmp_cpt=tmp_cpt+1

                    elif column == "Job":
                        Job_cpt = tmp_cpt
                        tmp_cpt=tmp_cpt+1

                    elif column == "State":
                        State_cpt = tmp_cpt
                        tmp_cpt=tmp_cpt+1

                    elif column == "Level":
                        Level_cpt = tmp_cpt
                        tmp_cpt=tmp_cpt+1
                        
                    else:
                        break   
                if line[UserName_cpt] != "UserName":
                    if line[Level_cpt] == "director":
                        user_list.append(Director(line[UserName_cpt], line[UserFirstname_cpt], line[Age_cpt], line[Phone_cpt], line[Email_cpt], line[Login_cpt], line[Password_cpt], line[CompanyID_cpt], line[State_cpt], line[Job_cpt]))
                    elif line[Level_cpt] == "employee":
                        user_list.append(Employee(line[UserName_cpt], line[UserFirstname_cpt], line[Age_cpt], line[Phone_cpt], line[Email_cpt], line[Login_cpt], line[Password_cpt], line[CompanyID_cpt], line[State_cpt], line[Job_cpt]))
            return user_list    
#fin load_user_from_csv()


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)
    
        



    