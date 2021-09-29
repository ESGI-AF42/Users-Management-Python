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
    
    check_value=True
    while check_value:
        try:
            number=int(input("Make your choice: "))
            time.sleep(0.1)
        except:
            print("invalid or empty value, you should choose 1 or 2")

        if number == 1:
            time.sleep(0.5)
            Company.create_company(company_file_path,user_file_path)
            check_value=False
        elif number == 2:
            time.sleep(0.5)
            company_list = Company.load_company_from_csv(company_file_path)
            company_choosed = Company.choose_company(company_list)
            connect(company_file_path, user_file_path, company_choosed)
            check_value=False  
        else:
            time.sleep(0.5)
            print("Invalid Choise! You should choose 1 or 2.")
            time.sleep(0.5)

    
        


#debut connect()
def connect(company_file_path,user_file_path,company):
    print(company_file_path)
    print(user_file_path)
    print(company.get_company_id())
#fin connect()
    