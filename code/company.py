##classe pour contextualisé le projet
import os, hashlib, pathlib, binascii, time, csv,Team_IT_functions 
from user import User
from director import Director


class Company():

    def __init__(self, CompanyID,CompanyName, CompanyType, CompanySector, CompanyCountry, CompanyAddress):
        self.company_id = int(CompanyID)
        self.company_name = CompanyName
        self.company_type = CompanyType
        self.company_sector = CompanySector
        self.company_country = CompanyCountry
        self.company_address = CompanyAddress


##début des des getters and setters
    def get_company_id(self):
        return self.company_id

    def get_company_name(self):
        return self.company_name
    
    def get_company_type(self):
        return self.company_type

    def get_company_sector(self):
        return self.company_sector

    def get_company_country(self):
        return self.company_country

    def get_company_address(self):
        return self.company_address


    def set_company_name(self,CompanyName):
        self.company_name = CompanyName

    def set_company_type(self,CompanyType):
        self.company_type = CompanyType

    def set_company_sector(self,CompanySector):
        self.company_sector = CompanySector

    def set_company_country(self,CompanyCountry):
        self.company_country = CompanyCountry

    def set_company_address(self,CompanyAddress):
        self.company_address = CompanyAddress
##fin des getters and setters


#debut get_company_from_id()
    def get_company_from_id(CompanyID,company_file_path):
        company_list=Company.load_company_from_csv(company_file_path)
        for company_obj in company_list:
            if company_obj.get_company_id() == CompanyID:
                return company_obj.get_company_name()
#fin get_company_from_id()


#debut create_companyCSV()
    def create_companyCSV(company_file_path):
        with open(company_file_path, 'w') as csvfile:
            filewriter = csv.writer(csvfile, lineterminator = '\n', delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(['CompanyID', 'CompanyName', 'CompanyType', 'CompanySector', 'CompanyCountry', 'CompanyAddress'])
            csvfile.close()
#fin create_companyCSV()


#debut create_company()
    def create_company(company_file_path,user_file_path):
        CompanyID=Company.next_company_id(company_file_path)
        CompanyName =""
        CompanyType =""
        CompanySector ="" 
        CompanyCountry =""
        CompanyAddress =""          
        while not CompanyName:
            try:
                CompanyName=input("Company Name (must be a string):")
                time.sleep(0.1)
            except:
                print("invalid or empty value, you should choose a string")

        while not CompanyType:
            try:
                CompanyType=input("Company Type (must be a string):")
                time.sleep(0.1)
            except:
                print("invalid or empty value, you should choose a string")

        while not CompanySector:
            try:
                CompanySector=input("Company Sector (must be a string):")
                time.sleep(0.1)
            except:
                print("invalid or empty value, you should choose a string")

        while not CompanyCountry:
            try:
                CompanyCountry=input("Company Country (must be a string):")
                time.sleep(0.1)
            except:
                print("invalid or empty value, you should choose a string")

        while not CompanyAddress:
            try:
                CompanyAddress=input("Company Address (must be a string):")
                time.sleep(0.1)
            except:
                print("invalid or empty value, you should choose a string")
        user_company = Company(CompanyID, CompanyName, CompanyType, CompanySector, CompanyCountry, CompanyAddress)
        Company.save_company(user_company, company_file_path)
        print("Company created")
        Team_IT_functions.clearConsole()
        Director.create_root_user(CompanyID,user_file_path)
        User.connect(company_file_path,user_file_path,user_company)
#fin create_company()


#debut save_company()
    def save_company(self, company_file_path):
       with open(company_file_path, 'a') as csvfile:
            filewriter = csv.writer(csvfile, lineterminator = '\n', delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow([self.get_company_id(), self.get_company_name(), self.get_company_type(), self.get_company_sector(), self.get_company_country(), self.get_company_address()])
            csvfile.close()
#fin save_company()


#debut load_company_from_csv()
    def load_company_from_csv(company_file_path):
        company_list = []
        with open(company_file_path, 'r') as csvfile:
            filereader = csv.reader(csvfile, lineterminator = '\n', delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            CompanyID_cpt = 0
            CompanyName_cpt = 0
            CompanyType_cpt = 0
            CompanySector_cpt = 0
            CompanyCountry_cpt = 0
            CompanyAddress_cpt = 0
            tmp_cpt = 0
            for line in filereader:
                for column in line:
                    if column == "CompanyID":
                        CompanyID_cpt = tmp_cpt
                        tmp_cpt=tmp_cpt+1

                    elif column == "CompanyName":
                        CompanyName_cpt = tmp_cpt
                        tmp_cpt=tmp_cpt+1

                    elif column == "CompanyType":
                        CompanyType_cpt = tmp_cpt
                        tmp_cpt=tmp_cpt+1

                    elif column == "CompanySector":
                        CompanySector_cpt = tmp_cpt
                        tmp_cpt=tmp_cpt+1

                    elif column == "CompanyCountry":
                        CompanyCountry_cpt = tmp_cpt
                        tmp_cpt=tmp_cpt+1

                    elif column == "CompanyAddress":
                        CompanyAddress_cpt = tmp_cpt
                        tmp_cpt=tmp_cpt+1
                        
                    else:
                        break   
                if line[CompanyID_cpt] != "CompanyID":
                    company_list.append(Company(line[CompanyID_cpt],line[CompanyName_cpt],line[CompanyType_cpt],line[CompanySector_cpt],line[CompanyCountry_cpt],line[CompanyAddress_cpt]))
            csvfile.close()
            return company_list
#fin load_company_from_csv()


    def choose_company(company_list, company_file_path, user_file_path):
        if len(company_list)==0:
            print("No existing company")
            time.sleep(0.1)
            print("Please create one")
            time.sleep(0.1)
            Company.create_company(company_file_path, user_file_path)
        else:
            print("which company is yours ? ")
            time.sleep(0.1)
            list_company_id = []
            choosed_company = None
            
            for company_obj in company_list:
                print (company_obj.get_company_id()," : ",company_obj.get_company_name())
                company_id = company_obj.get_company_id()
                list_company_id.append(company_id)
                time.sleep(0.1)

            while not choosed_company or not choosed_company in list_company_id :
                try:
                    choosed_company=int(input("Make your choice : "))
                    time.sleep(0.1)
                except: 
                    print("error")

                if not choosed_company in list_company_id:
                    print('This number is not in the list')
            for company_obj in company_list:
                if company_obj.get_company_id() == choosed_company:
                    return company_obj

    def next_company_id(company_file_path):
        company_id=[]
        company_list=Company.load_company_from_csv(company_file_path)

        for company_obj in company_list:
            company_id.append(company_obj.get_company_id())
        return len(company_id)+1


