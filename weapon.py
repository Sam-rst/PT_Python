class Weapon: 
    type = "weapon"

    def __init__(self, name, bonus_attack, bonus_defense, range):
        self.name = name 
        self.bonus_attack = bonus_attack
        self.bonus_defense = bonus_defense 
        self.range = range 

    def __str__(self):
        return f"You found {self.name}, with {self.bonus_attack} atk, and {self.bonus_defense} def"     
    
   