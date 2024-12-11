class Livre:
    def __init__(self, titre, auteur, annee_publication):
        self.titre = titre
        self.auteur = auteur
        self.annee_publication = annee_publication       
    def __str__(self):
       return f"'{self.titre}' de {self.auteur} (publié en {self.annee_publication})"
class Bibliotheque:
    def __init__(self):
        self.livres = []  # Liste pour stocker les livres
    def ajouter_livre(self, livre):
        self.livres.append(livre)#ajouter un livre a la biblio
        print(f"le livre est ajouter : {livre}")
    def afficher_livres(self):# affiche tous les livres de la bibliotheque
        if not self.livres:
            print("la bibliotheque est vide.")
        else:
            print("livres dans la bibliotheque :")
            for livre in self.livres:
                print(f" - {livre}")
# test
# creation de quelques livres
livre1 = Livre("le chien vert", "ayajabrane", 2020)
livre2 = Livre("le chien rose", "ana", 2021)
livre3 = Livre("le chien move", "moi", 2024)
# creation de la bibliotheque
ma_bibliotheque = Bibliotheque()
# ajout des livres a la bibliotheque
ma_bibliotheque.ajouter_livre(livre1)
ma_bibliotheque.ajouter_livre(livre2)
ma_bibliotheque.ajouter_livre(livre3)
# affichage des livres de la bibliotheque
ma_bibliotheque.afficher_livres()
