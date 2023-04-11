import json
from caracter import *

class Encoder(json.JSONEncoder):
    
    def default(self, obj):
        if isinstance(obj, Warrior):
            return {
                "__class__": "Warrior",
                "name": obj.name,
                "max_health": obj.max_health,
                "attack": obj.attack,
                "defend": obj.defense,
            }

        if isinstance(obj, Mage):
                return {
                    "class": "Mage",
                    "name": obj.name,
                    "max_health": obj.max_health,
                    "attack": obj.attack,
                    "defend": obj.defense,
                }
        return None