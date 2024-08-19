import Data
import Medecin
import Infirmier
import Patient


class Hopital:
    def __init__(self):
        pass

    # ------------------------------------------------------------
    # Méthodes

    def Nouveau_med(self, nom, prenom, num_medecin):
        new_med =  Medecin.Medecin(nom, prenom, num_medecin)
        Data.medecins.append(new_med)
    def Conger_med(self, num_medecin):
        for index, medecin in enumerate(Data.medecins):
            if medecin.num_medecin == num_medecin:
                Data.medecins_en_conger.append(Data.medecins.pop(index))

    def Lookup_med(self, num_medecin):
        for medecin in Data.medecins:
            if medecin.num_medecin == num_medecin:
                print(medecin)

    def Nouveau_inf(self, nom, prenom, num_infirmier):
        new_inf = Infirmier.Infirmier(nom, prenom, num_infirmier)
        Data.infirmiers.append(new_inf)

    def Conger_inf(self, num_infirmier):
        for index, infirmier in enumerate(Data.infirmiers):
            if infirmier.num_infirmier == num_infirmier:
                Data.infirmiers_en_conger.append(Data.infirmiers.pop(index))

    def Lookup_inf(self, num_infirmier):
        for infirmier in Data.infirmiers:
            if infirmier.num_infirmier == num_infirmier:
                print(infirmier)

    def Afficher_staff(self):
        print(f"Liste de médecins : {Data.medecins}\nListe d'infirmiers / ères : {Data.infirmiers}")

    def Nouveau_patient(self,nom, prenom, num_patient):
        new_patient =  Patient.Patient(nom, prenom, num_patient)
        Data.patients.append(new_patient)

    def Conger_patient(self, num_patient):
        for index, patient in enumerate(Data.patients):
            if patient.num_patient == num_patient:
                Data.patients.pop(index)
                interim_dict = {}  # Adding an intermidiary dictionnary in order to avoid RuntimeError: dictionary changed size during iteration
                for key, value in Data.dict_patients_locaux.items():
                    interim_dict[key] = value
                for key in interim_dict.keys():
                    if patient.num_patient == key:
                        Data.dict_patients_locaux.pop(key)

    def Lookup_patient(self, num_patient):
        for patient in Data.patients:
            if patient.num_patient == num_patient:
                print(patient)

    def Garder_patient(self, num_patient, local):
        for patient in Data.patients:
            if patient.num_patient == num_patient:
                Data.dict_patients_locaux[num_patient] = local

    def Afficher_Locaux(self):
        print(Data.dict_patients_locaux)

