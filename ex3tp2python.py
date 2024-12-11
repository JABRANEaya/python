# Définition de la classe "CompteBancaire"
class CompteBancaire:
    def __init__(self, titulaire, solde=0):
        self.titulaire = titulaire
        self.solde = solde
#la methode deposer montant qui ajouter l'argent au solde
    def deposer(self, montant):
        self.solde += montant
        print(f"{montant}dh déposés. Nouveau solde: {self.solde}dh")
#la methode retirer montant qui Retire le montant du solde si c'est possible
    def retirer(self, montant):
        if montant > self.solde:
            print("Fonds insuffisants pour effectuer ce retrait.")
        else:
            self.solde -= montant
            print(f"{montant}dh retirés. Nouveau solde: {self.solde}dh")
#la methode Affiche le solde actuel 
    def afficher_solde(self):
        print(f"Solde actuel: {self.solde}dh")


# Création d'un compte bancaire
compte = CompteBancaire("aya", 1000)

# Test des méthodes
compte.afficher_solde()      # Affiche le solde initial
compte.deposer(500)          # Dépose 500dh
compte.afficher_solde()      # Affiche le nouveau solde
compte.retirer(300)          # Retire 300dh
compte.afficher_solde()      # Affiche le solde après retrait
compte.retirer(1500)         # Tente de retirer plus que le solde
