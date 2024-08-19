import Hopital

Hopital_de_Montreal = Hopital.Hopital()

Hopital_de_Montreal.Nouveau_med("Doe", "John", 123 )
Hopital_de_Montreal.Lookup_med(123)
print("# --------------------")
Hopital_de_Montreal.Nouveau_inf("Dae", "Jane", 1234)
Hopital_de_Montreal.Lookup_inf(1234)
print("# --------------------")
Hopital_de_Montreal.Nouveau_patient("Smith", "Jaden", 123456)
Hopital_de_Montreal.Lookup_patient(123456)
print("# --------------------")
Hopital_de_Montreal.Garder_patient(123456, "C203")
Hopital_de_Montreal.Afficher_Locaux()
print("# --------------------")
Hopital_de_Montreal.Conger_med(123)
Hopital_de_Montreal.Conger_inf(1234)
Hopital_de_Montreal.Conger_patient(123456)

Hopital_de_Montreal.Afficher_staff()
Hopital_de_Montreal.Afficher_Locaux()


