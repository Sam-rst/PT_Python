from dice import Dice, RiggedDice
from rich import print

class Caracter:
    type = "caracter"

    def __init__(self, name, max_health, attack, defense, dice):
        self.name = name
        self.max_health = max_health
        self.health = self.max_health
        self.attack_value = attack
        self.defense_value = defense
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
            roll = self.dice.roll()
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


class Warrior(Caracter):
    type = "Warrior"
    
    def compute_damages(self, roll, target):
        print("Bonus : Axe in your face ! (+3 damages)")
        return super().compute_damages(roll, target) + 3


class Mage(Caracter):
    type = "Mage"

    def compute_defense(self, roll, damages):
        print("Bonus : Magic armor ! (-3 wournds)")
        return super().compute_defense(roll, damages) - 3


class Thief(Caracter):
    type = "Thief"
    
    def compute_damages(self, roll, target):
        print(f"Bonus : Backstab (+{target.get_defense()} damages) !")
        return super().compute_damages(roll, target) + target.get_defense()


if __name__ == "__main__":
    a_dice = Dice(6)

    car1 = Warrior("Mike", 20, 8, 3, a_dice)
    car2 = Mage("Helen", 20, 8, 3, a_dice)
    car3 = Thief("Robin", 20, 8, 3, a_dice)
    print(car1)
    print(car3)
    
    while (car1.is_alive() and car3.is_alive()):
        car1.attack(car3)
        car3.attack(car1)