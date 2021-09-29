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
from company import Company
from user import User
from employee import Employee
from director import Director


actual_path= pathlib.Path(__file__ )
parent_path = actual_path.parent.__str__()
company_file_path = parent_path+'\data\company.csv'
user_file_path = parent_path+'\data\\user.csv'
company_file_exist = os.path.exists(company_file_path)
user_file_exist = os.path.exists(user_file_path)


#beginning of the main
print ("hello user, and welcome to your best personal assistant, yoru")
time.sleep(2)

if not user_file_exist:
        User.create_userCSV(user_file_path)

if company_file_exist:

    #demander quelle entreprise est la notre, sinon il faut en créer
    #si on choisit de créer entreprise alors meme procesus que pour la creation normal
    #sinon on choisit une des entreprises pour se connecter 
    Team_IT_functions.start_connexion_process(company_file_path,user_file_path)
        #on se connecte avec un user de l'entreprise correspondante
        #prochaine fonction: sauvegarder user dans le fichier
            
    #print(newUser.get_user_level())
    #print(newUser.get_user_password())
    #stored_psswd = newUser.get_user_password()
    #print(User.verify_psswd(stored_psswd,"azertyuiop"))
        
else:
    print("No Companyoration was create before so you should do it first. Please complete empty fields")
    time.sleep(0.1)
    Company.create_companyCSV(company_file_path)
    Company.create_company(company_file_path,user_file_path)
    #un utilisateur root sera créé par défaut auquel on demande la modification du mot de passe par defaut
