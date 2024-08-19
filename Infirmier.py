
class Infirmier:
    def __init__(self, nom, prenom, num_infirmier):
        self.nom = nom
        self.prenom = prenom
        self.num_infirmier = num_infirmier

    def __str__(self):
        return f"Infirmier: {self.prenom} {self.nom}, Numéro d'infirmier: {self.num_infirmier}"
