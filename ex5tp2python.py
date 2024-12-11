# definition de la classe parent "Animal"
class Animal:
    def faire_du_bruit(self):
        print("le chien max ou la chat mimi fait un bruit")
# sous-classe "Chien" qui herite de "Animal"
class Chien(Animal):
    def faire_du_bruit(self):#implementation specifique pour le chien
        print("le chien max dit :haw haw haw")
# sous-classe "Chat" qui herite de "Animal"
class Chat(Animal):
    def faire_du_bruit(self):
       print("la chat mimi dit :myaw myaw myaw ")
# test
# instance de la classe "Chien"
max = Chien()
max.faire_du_bruit() 
# instance de la classe "Chat"
mimi = Chat()
mimi.faire_du_bruit()  
# instance de la classe "Animal" 
animal = Animal()
animal.faire_du_bruit()
