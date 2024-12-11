class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.amies = []  # liste pour stocker les amies
    def se_presenter(self):
        print(f"Bonjour, je m'appelle {self.prenom} {self.nom}, j'ai {self.age} ans.")
    def ajouter_amie(self, amie):
        if amie not in self.amies:
            self.amies.append(amie)#ajouter amie
            print(f"{amie.prenom} est ajoutee a la liste d'amies de {self.prenom}.")
        else:
            print(f"{amie.prenom} est deja une amie de {self.prenom}.")
    def afficher_amies(self):
        if not self.amies:
            print(f"{self.prenom} n'a pas encore d'amies.")
        else:
            print(f"les amies de {self.prenom} sont :")
            for amie in self.amies:
                print(f" - {amie.prenom} {amie.nom}")
#Test
personne1 = Personne("jabrane", "aya", 21)
personne2 = Personne("nmer", "houda", 21)
personne3 = Personne("lahsuni", "nora", 21)
# Présentation des personnes
personne1.se_presenter()
personne2.se_presenter()
personne3.se_presenter()
# Ajout d'amies
personne1.ajouter_amie(personne2)
personne1.ajouter_amie(personne3)
personne1.afficher_amies()
personne1.ajouter_amie(personne2)
personne2.afficher_amies()
