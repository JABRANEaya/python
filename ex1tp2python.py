class Chien:
    def __init__(self, nom, race, age):
        self.nom = nom
        self.race = race
        self.age = age  
    def aboyer(self):
        print("Woof!")
# Création d'une instance de la classe "Chien"
mon_chien = Chien("max", "bergi", 5)
print("le nom est : ",mon_chien.nom)
print("le race est :",mon_chien.race) 
print("lage est :",mon_chien.age)  
# Appel de la méthode "aboyer"
mon_chien.aboyer()  