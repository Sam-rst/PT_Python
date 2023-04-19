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
                "Class": "Mage",
                "Name": obj.get_name(),
                "Max HP": obj.get_max_HP(),
                "Attack value": obj.get_attack_value(),
                "Attack range": obj.get_range(),
                "Defend value": obj.get_defense_value(),
                # "Position": obj.get_pos(),
                
                
            }
        if isinstance(obj, Archer):
                return {
                "Class": "Archer",
                "Name": obj.get_name(),
                "Max HP": obj.get_max_HP(),
                "Attack value": obj.get_attack_value(),
                "Attack range": obj.get_range(),
                "Defend value": obj.get_defense_value(),
                # "Position": obj.get_pos(),
                
                
            }
        if isinstance(obj, Assassin):
                return {
                "Class": "Assassin",
                "Name": obj.get_name(),
                "Max HP": obj.get_max_HP(),
                "Attack value": obj.get_attack_value(),
                "Attack range": obj.get_range(),
                "Defend value": obj.get_defense_value(),
                # "Position": obj.get_pos(),
                
                
            }
        if isinstance(obj, Guard):
                return {
                "Class": "Guard",
                "Name": obj.get_name(),
                "Max HP": obj.get_max_HP(),
                "Attack value": obj.get_attack_value(),
                "Attack range": obj.get_range(),
                "Defend value": obj.get_defense_value(),
                # "Position": obj.get_pos(),
                
                
            }
        if isinstance(obj, Tank):
                return {
                "Class": "Tank",
                "Name": obj.get_name(),
                "Max HP": obj.get_max_HP(),
                "Attack value": obj.get_attack_value(),
                "Attack range": obj.get_range(),
                "Defend value": obj.get_defense_value(),
                # "Position": obj.get_pos(),
                
                
            }
        
        return None