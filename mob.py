from caracter import Caracter

class Mob(Caracter):
    
    def __init__(self, name, max_health, attack, defense, weapon, dice):
        super().__init__(name, max_health, attack, defense, weapon, dice)
        