# definition de la classe "Rectangle"
class Rectangle:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
    def calculer_surface(self):
        return self.largeur * self.hauteur
    def calculer_perimetre(self):
        return (self.largeur + self.hauteur)*2
# creation d'une instance de la classe "Rectangle"
rectangle1 = Rectangle(5, 3)
# calcul et affichage de la surface
surface = rectangle1.calculer_surface()
print(f"La surface du rectangle est : {surface}")
# calcul et affichage du perimetre
perimetre = rectangle1.calculer_perimetre()
print(f"Le perimetre du rectangle est : {perimetre}")
