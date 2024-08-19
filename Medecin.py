
class Medecin:
    def __init__(self, nom, prenom, num_medecin):
        self.nom = nom
        self.prenom = prenom
        self.num_medecin = num_medecin

    def __str__(self):
        return f"Médecin: {self.prenom} {self.nom}, Numéro de médecin: {self.num_medecin}"