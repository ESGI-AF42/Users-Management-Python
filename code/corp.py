##classe pour contextualisé le projet
import os, hashlib, pathlib, binascii, time, csv

class Corp():

    def __init__(self, CorpID,CorpName, CorpType, CorpSector, CorpCountry, CorpAddress):
        self.corp_id = CorpID
        self.corp_name = CorpName
        self.corp_type = CorpType
        self.corp_sector = CorpSector
        self.corp_country = CorpCountry
        self.corp_address = CorpAddress


##getters and setters de l'entreprise inutiles car ils n'y a qu'une seule entreprise dans le projet
    def get_corp_name(self):
        return self.corp_name
    
    def get_corp_type(self):
        return self.corp_type

    def get_corp_sector(self):
        return self.corp_sector

    def get_corp_country(self):
        return self.corp_country

    def get_corp_address(self):
        return self.corp_address


    def set_corp_name(self,CorpName):
        self.corp_name = CorpName

    def set_corp_type(self,CorpType):
        self.corp_type = CorpType

    def set_corp_sector(self,CorpSector):
        self.corp_sector = CorpSector

    def set_corp_country(self,CorpCountry):
        self.corp_country = CorpCountry

    def set_corp_address(self,CorpAddress):
        self.corp_address = CorpAddress

##fin des getters and setters
    

    def create_corpCSV(file_path):
        with open(file_path, 'w') as csvfile:
            filewriter = csv.writer(csvfile, lineterminator = '\n', delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(['CorpID', 'CorpName', 'CorpType', 'CorpSector', 'CorpCountry', 'CorpAddress'])
            csvfile.close()
  
    def create_corp(file_path):
        CorpID =""
        CorpName =""
        CorpType =""
        CorpSector ="" 
        CorpCountry =""
        CorpAddress =""
        print("No corporation was create before so you should do it first. Please complete empty fields")
        time.sleep(1)
        while not CorpID:
            try:
                CorpID=int(input("Corp ID (must be a number):"))
            except:
                print("invalid or empty value, you should choose an integer")
        
        while not CorpName:
            try:
                CorpName=input("Corp Name (must be a string):")
            except:
                print("invalid or empty value, you should choose a string")

        while not CorpType:
            try:
                CorpType=input("Corp Type (must be a string):")
            except:
                print("invalid or empty value, you should choose a string")

        while not CorpSector:
            try:
                CorpSector=input("Corp Sector (must be a string):")
            except:
                print("invalid or empty value, you should choose a string")

        while not CorpCountry:
            try:
                CorpCountry=input("Corp Country (must be a string):")
            except:
                print("invalid or empty value, you should choose a string")

        while not CorpAddress:
            try:
                CorpAddress=input("Corp Address (must be a string):")
            except:
                print("invalid or empty value, you should choose a string")

        with open(file_path, 'a') as csvfile:
            filewriter = csv.writer(csvfile, lineterminator = '\n', delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow([CorpID, CorpName, CorpType, CorpSector, CorpCountry, CorpAddress])
            csvfile.close()