##classe pour contextualisé le projet

class Corp():

    def __init__(self, CorpName, CorpType, CorpSector, CorpCountry, CorpAddress):
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