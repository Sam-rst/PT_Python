from dice import Dice, RiggedDice
from rich import print
from math import sqrt 
from weapon import Weapon


    
class Caracter:
    type = "caracter"

    def __init__(self, name, max_health, attack, defense, weapon, dice):
        self.name = name
        self.max_health = max_health
        self.health = self.max_health
        self.attack_value = attack
        self.defense_value = defense
        self.weapon = weapon
        self.dice = dice

    def __str__(self):
        return f"I'm {self.name}, a {type(self).type} with {self.max_health}hp ({self.attack_value} atk / {self.defense_value} def)"

    def regenerate(self):
        self.health = self.max_health
    
    def decrease_health(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0

    def show_health(self):
        missing_health = self.max_health - self.health
        health_bar = f"{self.name} healthbar : [{'●'*self.health}{'○'*missing_health}] {self.health}/{self.max_health}hp"
        print(health_bar)

    def get_type(self):
        return type(self).type

    def get_defense(self):
        return self.defense_value
    
    def get_name(self):
        return self.name

    def compute_damages(self, roll, target):
        damages = roll + self.attack_value
        return damages

    def attack(self, target):
        if self.is_alive():
            if self.distance(target) > self.weapon.weapon_range():
                    print("La cible est hors de portée²")
            roll = self.dice.roll()
            distance  = self.distance_to(target)
            damages = self.compute_damages(roll, target)
            print(
                f"⚔️ {self.get_type()} [red]{self.name}[/red] attack with {damages} damages (attack: {self.attack_value} + roll: {roll})")
            target.defend(damages)

    def compute_defense(self, roll, damages):
        return damages - roll - self.defense_value

    def defend(self, damages):

        roll = self.dice.roll()
        wounds = self.compute_defense(roll, damages)
        print(f"🛡️ {self.get_type()} [blue]{self.name}[/blue] defend against {damages} damages and take {wounds} wounds ({damages} damages - defense {self.defense_value} - roll {roll})")
        self.decrease_health(wounds)
        self.show_health()

    def distance(self, target):
        x_distance = abs(self.x - target.x)
        y_distance = abs(self.y - target.y)
        return sqrt(x_distance**2 + y_distance**2)

    def switch_weapon(self, new_weapon):
        print(f"Tu a trouvés {new_weapon.name} !")
        print(f"Veux tu remplacer ta/ton {self.weapon.name} par celle-ci ? ")

        reponse = input("Remplacer ? o/n ")

        while reponse != "o" and reponse != "n":
            print("Erreur, écrivez o/n")
            reponse = input("Remplacer ? o/n ")

        if reponse == "o":
            self.weapon = new_weapon
            print(f"Tu possèdes désormais {self.weapon.name}")
        elif reponse == "n":
            print(f"Tu choisis de garder {self.weapon.name}")

class Player(Caracter):
    pass
    
    
class Warrior(Player):
    type = "Warrior"
    
    def compute_damages(self, roll, target):
        print("Bonus : Axe in your face ! (+3 damages)")
        return super().compute_damages(roll, target) + 3


class Mage(Player):
    type = "Mage"

    def compute_defense(self, roll, damages):
        print("Bonus : Magic armor ! (-3 wournds)")
        return super().compute_defense(roll, damages) - 3


class Thief(Player):
    type = "Thief"
    
    def compute_damages(self, roll, target):
        print(f"Bonus : Backstab (+{target.get_defense()} damages) !")
        return super().compute_damages(roll, target) + target.get_defense()


if __name__ == "__main__":
    a_dice = Dice(6)
    
    sword0 = Weapon("Epée en bois", 1, 0, 1)
    sword1 = Weapon("Epée commune", 2, 0, 1)
    sword2 = Weapon("Epée rare", 4, 0, 1)
    sword3 = Weapon("Epée épique", 6, 0, 1)
    sword4 = Weapon("Epée légendaire", 8, 0, 1)
    warrior1 = Warrior("Mike", 20, 8, 3, sword0, a_dice)
    mage1 = Mage("Helen", 20, 8, 3,"Baton de soUrcier", a_dice)
    thief1 = Thief("Robin", 20, 8, 3,"Dague en plastique", a_dice)
    print(warrior1)
    print(thief1)

    while (warrior1.is_alive() and thief1.is_alive()):
        warrior1.attack(thief1)
        thief1.attack(warrior1)

#faire une def pour changer d'armes