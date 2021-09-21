import os, hashlib, pathlib, binascii
from corp import Corp
from member import Member
from employee import Employee
from director import Director

actual_path= pathlib.Path(__file__ )
parent_path = actual_path.parent.__str__()
file_path= parent_path+"\data\corp.csv"
file_exists = os.path.exists(file_path)

#beginning of the main
print ("hello user, and welcome to your best personal assistant, yoru")

if file_exists:
    if os.stat(file_path).st_size == 0:
        print("there seem to be problems with your created company. You need to create valid one before")
        #fonction creation entreprise (et suite qu'il advient)

    else:
        newCorp = Corp("000","hola","pme","info","france","bât Beta Parc Technopolis, 3 AV du Canada, 91940 les Ulis")
        newUser = Employee("Fabien","PIRES","20","0672626957","fabien.pires20@gmail.com","fpires","azertyuiop","000","Ingénieur réseau")
        print(newUser.get_member_level())
        print(newUser.get_member_password())
        stored_psswd = newUser.get_member_password()
        print(Employee.verify_psswd(stored_psswd,"azertyuiop"))
        #créer un dico de donnée pour sauvegarder l'utilisateur créé 


else:
    print("No corporation was create before so you should do it first")
    #fonction pour créer une entreprise
    #un utilisateur root sera créé par défaut auquel on demande la modification du mot de passe par defaut







