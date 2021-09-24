import os, hashlib, pathlib, binascii, time, csv
from corp import Corp
from user import User
from employee import Employee
from director import Director

def start_connexion_process(file_path):
    print("Please choose an option")
    print("1: Create a new corp")
    print("2: Connect to an existing corp")
    try:
        number=int(input("Make your choice: "))
    except:
        print("invalid or empty value, you should choose 1 or 2")
    check_value=True
    while check_value:
        if number == 1:
            Corp.create_corp(file_path)
            check_value=False
        elif number == 2:
            Corp.load_corp_from_csv(file_path)
            check_value=False
        else:
            print("Invalid Choise! You should choose 1 or 2.")
    