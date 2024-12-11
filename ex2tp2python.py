class Voiture:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee
    def afficher_info(self):
        print(f"Marque: {self.marque}, Modèle: {self.modele}, Année: {self.annee}")

# Création des instances de la classe "Voiture"
voiture_1 = Voiture("toyota", "petite", 2003)
voiture_2 = Voiture("nessan", "grande", 2005)
voiture_3 = Voiture("taxi", "rose", 2004)
# Appel de la méthode "afficher_info"
voiture_1.afficher_info()  
voiture_2.afficher_info()
voiture_3.afficher_info()


#methode 2 (sans l'utilisation de f dans print)
class Voiture:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee
    def afficher_info(self):
        print("Marque:"+ self.marque +", Modèle:" + self.modele +", Année:" + str(self.annee))

# Création des instances de la classe "Voiture"
voiture_1 = Voiture("toyota", "petite", 2003)
voiture_2 = Voiture("nessan", "grande", 2005)
voiture_3 = Voiture("taxi", "rose", 2004)
# Appel de la méthode "afficher_info"
voiture_1.afficher_info()  
voiture_2.afficher_info()
voiture_3.afficher_info()