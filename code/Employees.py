class Employés():

        def __init__(self, Age, Numéro, Salaire, Fonction):
        self.age = Age
        self.numero = Numéro
        self.salaire = Salaire
        self.fonction = Fonction

    def get_entreprise_age(self):
        return self.age

    def get_entreprise_number(self):
        return self.numero
    
    def get_entreprise_salaire(self):
        return self.salaire
    
    def get_entreprise_fonction(self):
        return self.fonction
