import os
import json
from encoder import Encoder

class SaveData:
    def __init__(self, filename):
        self.filename = filename

    def save_player_position(self, player_position):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}

        data["player_position"] = player_position

        try:
            with open(self.filename, "w") as file:
                json.dump(data, file)
        except IOError:
            print("Erreur lors de l'écriture du fichier de sauvegarde.")

    def load_player_data(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            return None
        
    def save_player_map(self, player_map):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}

        data["map_name"] = player_map
        try:
            with open(self.filename, "w") as file:
                json.dump(data, file)
        except IOError:
            print("Erreur lors de l'écriture du fichier de sauvegarde.")

    def load_player_map(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                if "map_name" in data:
                    return data["map_name"]
                else:
                    return None
        except FileNotFoundError:
            return None

    def save_removed_objects(self, removed_objects):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}

        # Si des données existent déjà dans le fichier, on ajoute les objets supprimés à ces données
        if "removed_objects" in data:
            for object_name in removed_objects:
                # if object_name not in data["removed_objects"]:
                data["removed_objects"].append(object_name)
        else:
            data["removed_objects"] = removed_objects

        try:
            with open(self.filename, "w") as file:
                json.dump(data, file)
        except IOError:
            print("Erreur lors de l'écriture du fichier de sauvegarde.")

    def load_removed_objects(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                if "removed_objects" in data:
                    return data["removed_objects"]
                else:
                    return []
        except FileNotFoundError:
            return []

    def reset(self):
        try:
            os.remove(self.filename)
        except FileNotFoundError:
            pass

    def save_inventory(self, inventory):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}

        data["inventory"] = inventory

        try:
            with open(self.filename, "w") as file:
                json.dump(data, file)
        except IOError:
            print("Erreur lors de l'écriture du fichier de sauvegarde.")

    def load_inventory(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                if "inventory" in data:
                    return data["inventory"]
                else:
                    return  []
        except FileNotFoundError:
            return []
    
    def remove_item_from_inventory(self, item_name):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}

        # Vérifier si l'inventaire existe déjà
        if "inventory" in data:
            # Supprimer l'élément souhaité de la liste d'inventaire
            if item_name in data["inventory"]:
                data["inventory"].remove(item_name)
        else:
            print("L'inventaire n'existe pas.")

        try:
            with open(self.filename, "w") as file:
                json.dump(data, file)
        except IOError:
            print("Erreur lors de l'écriture du fichier de sauvegarde.")
        
    def save_player_life(self, player_life):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}

        data["player_life"] = player_life

        try:
            with open(self.filename, "w") as file:
                json.dump(data, file)
        except IOError:
            print("Erreur lors de l'écriture du fichier de sauvegarde.")

    def load_player_life(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                if "player_life" in data:
                    return data["player_life"]
                else:
                    return  []
        except FileNotFoundError:
            return []
        
    def save_mob_dead(self, mob_name):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}

        if "mob_name" in data:
                # if object_name not in data["removed_objects"]:
                data["mob_name"].append(mob_name)
        else:
            data["mob_name"] = [mob_name]

        try:
            with open(self.filename, "w") as file:
                json.dump(data, file)
        except IOError:
            print("Erreur lors de l'écriture du fichier de sauvegarde.")

    def load_mob_dead(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                if "mob_name" in data:
                    return data["mob_name"]
                else:
                    return  []
        except FileNotFoundError:
            return []
        
    def save_player_class(self, player_class):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}

        data["player_class"] = player_class

        try:
            with open(self.filename, "w") as file:
                json.dump(data, file, cls=Encoder)
        except IOError:
            print("Erreur lors de l'écriture du fichier de sauvegarde.")

    def load_player_class(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                if "player_class" in data:
                    return data["player_class"]
                else:
                    return None
        except FileNotFoundError:
            return None
        
    def player_class_exists(self):
        return self.load_player_class() is not None
    