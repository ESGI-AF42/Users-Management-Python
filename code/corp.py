##classe pour contextualisé le projet

class Corp():

    def __init__(self, Name, Type, Sector, Country, Address):
        self.name = Name
        self.type = Type
        self.sector = Sector
        self.country = Country
        self.address = Address

##getters and setters de l'entreprise inutiles car ils n'y a qu'une seule entreprise dans le projet
    def get_entreprise_name(self):
        return self.name
    
    def get_entreprise_type(self):
        return self.type

    def get_entreprise_sector(self):
        return self.sector

    def get_entreprise_country(self):
        return self.country

    def get_entreprise_address(self):
        return self.address


    def set_entreprise_name(self,Name):
        self.name = Name

    def set_entreprise_type(self,Type):
        self.type = Type

    def set_entreprise_sector(self,Sector):
        self.sector = Sector

    def set_entreprise_country(self,Country):
        self.country = Country

    def set_entreprise_address(self,Address):
        self.address = Address

##fin des getters and setters