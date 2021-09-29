import os, hashlib, pathlib, binascii, time, csv
from company import Company
from user import User
from employee import Employee
from director import Director

def start_connexion_process(company_file_path,user_file_path):
    print("Please choose an option")
    print("1: Create a new Company")
    print("2: Connect to an existing Company")
    try:
        number=int(input("Make your choice: "))
    except:
        print("invalid or empty value, you should choose 1 or 2")
    check_value=True
    while check_value:
        if number == 1:
            Company.create_company(company_file_path,user_file_path)
            check_value=False
        elif number == 2:
            Company.load_company_from_csv(company_file_path)
            check_value=False
        else:
            print("Invalid Choise! You should choose 1 or 2.")


#debut connect()
def connect(company_file_path,user_file_path,company):
    print(company_file_path)
    print(user_file_path)
    print(company.get_company_id())
#fin connect()
    