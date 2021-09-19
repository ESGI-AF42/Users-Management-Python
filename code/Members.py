class Membres():

    def __init__(self, Nom, Prénom, Age, Poste, Numéro):
        self.nom = Nom
        self.prenom = Prénom
        self.age = Age
        self.poste = Poste
        self.numero = Numéro

    def get_entreprise_name(self):
        return self.nom

    def get_entreprise_first_name(self):
        return self.prenom
    
    def get_entreprise_age(self):
        return self.age

    def get_entreprise_post(self):
        return self.poste

    def get_entreprise_number(self):
        return self.numero
