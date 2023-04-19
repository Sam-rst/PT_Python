import pygame, pytmx, sprites, sys
from pytmx.util_pygame import load_pygame
from collisions import CollisionTile
from settings import *
from inventaire import Inventaire

class Carte:
    
    def __init__(self, map_name):
        # screen
        self.screen = pygame.display.get_surface()
        # tmxdata
        self.map_name = map_name
        self.tmxdata = load_pygame(f'graphics/Tiled/data/tmx/{self.map_name}.tmx')
        self.width = self.tmxdata.width
        self.height = self.tmxdata.height
        
        # Layers and Tiles
        self.tilewidth = self.tmxdata.tilewidth * scale
        self.tileheight = self.tmxdata.tileheight * scale
        
        self.size_map_width = self.width * self.tilewidth
        self.size_map_height = self.height * self.tileheight
        
        self.layers = self.get_layers()

        self.collision_layers = []
        self.collision_tiles = []

    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
    
    def get_tilewidth(self):
        return self.tilewidth
    
    def get_tileheight(self):
        return self.tileheight
    
    def get_size_map_width(self):
        return self.size_map_width
    
    def get_collision_tiles(self):
        return self.collision_tiles
    
    def get_size_map_height(self):
        return self.size_map_height

    def create_collisions(self, groups):
        for layer in self.layers:
            if layer.name in self.collision_layers:
                for x, y, image in layer.tiles():
                    # print(f'Le layer : {layer.name} va créer les sprites de collision')
                    image = pygame.transform.scale(image, (self.tilewidth, self.tileheight))
                    self.collision_tiles.append(CollisionTile(image, (x*self.tilewidth, y * self.tileheight), groups))

    def get_layers(self):
        layer_list = []
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                layer_list.append(layer)
        return layer_list
        
    def get_group_object(self, name_group):
        """Méthode permettant d'obtenir la couche d'objets désirée selon son nom"""
        for object_layer in self.tmxdata.objectgroups:
            if object_layer.name == name_group:
                return object_layer

    def create_teleportation(self, name_teleportation, name_destination, name_tp_back, groups):
        obj = self.get_obj('Waypoints', name_teleportation)
        return Teleportation(obj, name_destination, name_tp_back, groups)

    def get_pos_obj(self, obj):
        return int(obj.x * scale), int(obj.y * scale)

    def get_obj(self, name_group, obj_name):
        obj_layer = self.get_group_object(name_group)
        for obj in obj_layer:
            if obj.name == obj_name:
                return obj
    
    def get_waypoint(self, name_waypoint):
        try : 
            obj = self.get_obj('Waypoints', name_waypoint)
            return self.get_pos_obj(obj)
        except:
            raise ValueError("Je n'arrive pas à retrouver ton waypoint")
    
    def get_pickup_distance(self, tmx_data):
        # Extraire la position de l'objet à collecter
        obj_pos = []
        for obj in tmx_data.objects:
            obj_pos.append((obj.name, (obj.x, obj.y)))
        # Définir la distance à laquelle le joueur peut ramasser l'objet
        pickup_distance = 50

        return obj_pos, pickup_distance
    
    def game_over(self):
        # Afficher un message de fin de partie et quitter la boucle principale
        font = pygame.font.SysFont(None, 64)
        text = font.render("Game Over appuyez sur E pour respawn", True, (255, 0, 0))
        text_rect = text.get_rect(center=(self.width * scale, self.height * scale))
        self.screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.delay(10000)

        # # Supprimer le fichier save.json
        # if os.path.exists(self.save_file):
        #     os.remove(self.save_file)
            
        pygame.quit()
        sys.exit()

    
class Teleportation(pygame.sprite.Sprite):
    type = 'Teleportation'
    def __init__(self, obj, name_destination, name_tp_back, groups):
        super().__init__(groups)
        self.obj = obj
        self.name_destination = name_destination
        self.name_tp_back = name_tp_back
        self.image = pygame.Surface((self.obj.width * scale, self.obj.height * scale))
        self.rect = self.image.get_rect(topleft = (self.obj.x * scale, self.obj.y * scale))
        self.old_rect = self.rect.copy()
        self.pos = pygame.math.Vector2(self.rect.topleft)

    def get_pos(self):
        return self.pos

    def get_type(self):
        return type(self).type