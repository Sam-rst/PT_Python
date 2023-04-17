import json
from player import *

class Encoder(json.JSONEncoder):
    
    def default(self, obj):
        if isinstance(obj, Warrior):
            return {
                "Class": "Warrior",
                "Name": obj.get_name(),
                "Max HP": obj.get_max_HP(),
                "Attack value": obj.get_attack_value(),
                "Attack range": obj.get_range(),
                "Defend value": obj.get_defense_value(),
                # "Position": obj.get_pos(),
                
                
            }

        if isinstance(obj, Mage):
                return {
                    "class": "Mage",
                    "max_health": obj.get_max_health(),
                    "attack": obj.get_attack_value(),
                    "defend": obj.get_defense_value()
                }
        return None