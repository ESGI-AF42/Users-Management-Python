##objectifs, application de création et gestion d'entreprise et d'employés
#lors de la création dune entreprise un user root est créé avec par mot de passe root 
#(ce mot de passe devra etre changé)
#
#un user fait forcément partie d'une enreprise
#un user est soit "director" soit "employee"
#tout user peut modifier ses paramètres sauf son appartenance à une entreprise et son log3
#
#seul un director peut ajouter un employee ou un autre director
#seul un director peut supprimer un employee
#seul un director peut modifier les informations de l'entreprise

import os, hashlib, pathlib, binascii, time, csv, Team_IT_functions
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
        #demander quelle entreprise est la notre, sinon il faut en créer
        Team_IT_functions.start_connexion_process(file_path)
            #si on choisit de créer entreprise alors meme procesus que pour la creation normal
            #sinon on se connecte avec un user de l'entreprise correspondante
        newUser = Employee("Fabien","PIRES","20","0672626957","fabien.pires20@gmail.com","fpires","azertyuiop","1","Ingénieur réseau")
        print(newUser.get_user_level())
        print(newUser.get_user_password())
        stored_psswd = newUser.get_user_password()
        print(User.verify_psswd(stored_psswd,"azertyuiop"))
        


else:
    print("No corporation was create before so you should do it first. Please complete empty fields")
    time.sleep(1)
    #fonction pour créer le fichier entreprise
    Corp.create_corpCSV(file_path)
    #fonction pour créer une entreprise
    Corp.create_corp(file_path)

    #un utilisateur root sera créé par défaut auquel on demande la modification du mot de passe par defaut







