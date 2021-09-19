class Membres():

    def __init__(self, Nom, Prénom, Age, Poste, Numéro, email, login, mot_de_passe):
        self.nom = Nom
        self.prenom = Prénom
        self.age = Age
        self.poste = Poste
        self.numero = Numéro
        self.email = Email
        self.login = Login
        self.mot_de_passe = Mot_De_Passe

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

    def get_entreprise_email(self):
        return self.email
    
    def get_entreprise_login(self):
        return self.login

    def get_entreprise_password(self):
        return self.mot_de_passe
