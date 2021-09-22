import os, hashlib, pathlib, binascii, time, csv
from corp import Corp
from user import User
from employee import Employee
from director import Director

actual_path= pathlib.Path(__file__ )
parent_path = actual_path.parent.__str__()
file_path= parent_path+"\data\corp.csv"
file_exists = os.path.exists(file_path)



#beginning of the main
print ("hello user, and welcome to your best personal assistant, yoru")
time.sleep(3)

if file_exists:
    if os.stat(file_path).st_size == 0:
        print("there seem to be problems with your created company. You need to create valid one before")
        Corp.create_corp(file_path)

    else:
        newCorp = Corp("000","hola","pme","info","france","bât Beta Parc Technopolis, 3 AV du Canada, 91940 les Ulis")
        newUser = Employee("Fabien","PIRES","20","0672626957","fabien.pires20@gmail.com","fpires","azertyuiop","000","Ingénieur réseau")
        print(newUser.get_user_level())
        print(newUser.get_user_password())
        stored_psswd = newUser.get_user_password()
        print(Employee.verify_psswd(stored_psswd,"azertyuiop"))
        #créer un dico de donnée pour sauvegarder l'utilisateur créé 


else:
    #fonction pour créer le fichier entreprise
    Corp.create_corpCSV(file_path)

    #fonction pour créer une entreprise
    Corp.create_corp(file_path)

    #un utilisateur root sera créé par défaut auquel on demande la modification du mot de passe par defaut







