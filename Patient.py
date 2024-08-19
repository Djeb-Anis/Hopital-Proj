
class Patient:
    def __init__(self, nom, prenom, num_patient):
        self.nom = nom
        self.prenom = prenom
        self.num_patient = num_patient

    def __str__(self):
        return f"Patient: {self.prenom} {self.nom}, Numéro de patient: {self.num_patient}"

