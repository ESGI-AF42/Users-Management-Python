import os
import pathlib

actual_path= pathlib.Path(__file__ )
parent_path = actual_path.parent.__str__()
file_path= parent_path+"\data\corp.csv"


file_exists = os.path.exists(file_path)

print ("hello user, and welcome to your best personal assistant, yoru")

if file_exists:
    if os.stat(file_path).st_size == 0:
        print("there seem to be problems with your created company. You need to create valid one before")
        #fonction creation entreprise (et suite qu'il advient)

    else:
        print("which corporation is yours")

else:
    print("No corporation was create before so you should do it first")
    #fonction pour créer une entreprise
    #un utilisateur root sera créé par défaut auquel on demande la modification du mot de passe par defaut





