# definition de la classe "Personne"
class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
    def se_presenter(self):
        print(f"Bonjour, je m'appelle {self.prenom} {self.nom} et j'ai {self.age} ans.")
# definition de la sous-classe "Etudiant" qui hérite de "Personne"
class Etudiant(Personne):
    def __init__(self, nom, prenom, age, matricule):
        # apel au constructeur de la classe Perspnne
        super().__init__(nom, prenom, age)
        self.matricule = matricule
# affiche les informations de la personne
    def etudier(self):
        print(f"Je suis etudiante en master avec le matricule(CNE) {self.matricule} et je suis en train d'etudier.")


# création d'instances pour tester
# instance de la classe Personne
personne = Personne("jabrane", "aya", 20)
personne.se_presenter()  

# instance de la sous-classe Etudiant
etudiant = Etudiant("aya", "jabrane", 20, "A139010455")
etudiant.se_presenter() 
etudiant.etudier() 
