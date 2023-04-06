import random 

#Création de la classe Dice
class Dice:
    """Classe Dice qui permet de créer un objet dé, qui possède un seul attribut le nombre de faces du dé"""
    
    type = "dice" #Nom de l'objet de la classe
    def __init__(self, faces:int = 6) -> None:
        """Initialisation de la classe avec un seul attribut en paramètre : faces"""
        self.faces = faces
    
    def __str__(self) -> str:
        """Méthode permettant d'obtenir un affichage de la classe Dice"""
        return f"I'm a {self.__faces} faces {type(self).type}"
    
    def roll(self) -> int:
        """Méthode permettant de lancer un dé selon le nombre de faces"""
        return random.randint(1, self.faces)
    
class RiggedDice(Dice):
    """Classe RiggedDice qui est une sous-classe de la classe Dice et qui permet de lancer un dé truqué ou non"""

    type = "rigged dice"
    def roll(self, rigged:bool = False):
        """Si lors de l'appel de la fonction, en paramètre de la fonction il y a True alors le dé devient un dé truqué.
        C'est-à-dire que le la méthode renverra toujours la face qui possède le plus grand nombre. Sinon, renvoie un lancement normal"""
        return self.faces if rigged else super().roll() #Appel de la fonction parente roll() et lance un dé normal
    
if __name__ == '__main__':
    dice1 = Dice()
    dice2 = RiggedDice()
    for i in range(1000):
        print(f"Lauch {i+1}: {dice2.roll(True)}")