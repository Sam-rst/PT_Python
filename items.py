import pygame
from settings import *
from images import *
from inventaire import Inventaire
from save import SaveData

class Item(pygame.sprite.Sprite):
    type = "Item"
    
    def __init__(self, name_item, pos, groups):
        super().__init__(groups)
        self.name = name_item
        self.animation_index = 0
        if self.name == 'Piece':
            self.frames = piece_anim
        self.animation_speed = 0.2
        self.image = self.frames[self.animation_index]
        self.image = self.transform_scale()
        self.rect = self.image.get_rect(topleft = pos)
        self.old_rect = self.rect.copy()
        self.pos = pygame.math.Vector2(self.rect.topleft)
        # Charger les données sauvegardées pour les objets supprimés
        self.save_data = SaveData('save.json')
        self.removed_objects = self.save_data.load_removed_objects()
        self.items = self.save_data.load_inventory()
        self.inventaire = Inventaire()

    def get_pos(self):
        return self.pos

    def get_type(self):
        return type(self).type
    
    def get_width(self):
        return self.image.get_width() * scale
    
    def get_height(self):
        return self.image.get_height() * scale
    
    def get_rect(self):
        return self.rect
    
    def transform_scale(self):
        return pygame.transform.scale(self.image, (self.get_width(), self.get_height()))
    
    def animation_state(self):
        self.animation_index += self.animation_speed
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        else:
            self.image = self.frames[int(self.animation_index)]
            self.image = self.transform_scale()
            self.rect = self.image.get_rect(topleft = self.get_pos())
     
    def remove_object(self, name_item):
        
        self.kill()

        self.inventaire.ajouter_objet(self.name)
        self.items.append(self.name)
        self.save_data.save_inventory(self.items)

        
    def update(self, dt):
        self.animation_state()


# def remove_object(self, obj_name):
#         # Supprimer l'objet de la couche d'objets
#         for obj in self.obj_layer:
#             if obj.name == obj_name:
#                 self.obj_layer.remove(obj)
#                 break
#         # Ajouter l'objet à l'inventaire
#         self.inventaire.ajouter_objet(obj_name)
#         self.items.append(obj_name)
#         self.save_data.save_inventory(self.items)
#         # Ajouter l'objet à la liste des objets supprimés dans les données sauvegardées
#         self.removed_objects.append(obj_name)
#         self.save_data.save_removed_objects(self.removed_objects)