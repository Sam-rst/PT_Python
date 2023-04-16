import pygame, pytmx
from pytmx.util_pygame import load_pygame
from obstacle import Obstacle
from settings import *

class Carte:
    
    def __init__(self, map_name):
        # screen
        self.screen = pygame.display.get_surface()
        
        # tmxdata
        self.tmxdata = load_pygame(f'graphics/Tiled/data/tmx/{map_name}.tmx')
        self.width = self.tmxdata.width
        self.height = self.tmxdata.height
        
        # Layers and Tiles
        self.tilewidth = self.tmxdata.tilewidth * scale
        self.tileheight = self.tmxdata.tileheight * scale
        
        self.size_map_width = self.width * self.tilewidth
        self.size_map_height = self.height * self.tileheight
        
        self.layers = self.get_layers()

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
    
    def get_size_map_height(self):
        return self.size_map_height

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

    def create_obstacles(self, name_group, groups):
        """Méthode permettant de créer les obstacles selon le nom de la couche d'objet 
        et dans quel groupe se situent les obstacles (ex : collision_sprites, all_sprites)"""
        for obj in self.get_group_object(name_group):
            Obstacle(obj, groups)

    def remove_object(self, name_group, obj_name):
        """Méthode permettant de supprimer un objet obj_name d'une couche layer_name"""
        obj_layer = self.get_group_object(name_group)
        list_obj = []
        for obj in obj_layer:
            if obj.name == obj_name:
                obj_layer.remove(obj)
                list_obj.append(obj)
        return obj

    def get_pos_obj(self, obj):
        return int(obj.x * scale), int(obj.y * scale)
    
    def get_obj(self, name_group, obj_name):
        obj_layer = self.get_group_object(name_group)
        for obj in obj_layer:
            if obj.name == obj_name:
                return obj
    
    def get_rect_obj(self, obj):
        obj_image = obj.image
        obj_rect = obj_image.get_rect(topleft = (obj.x, obj.y))
        return obj_image, obj_rect
    
    def get_waypoint(self, name_waypoint):
        obj = self.get_obj('Waypoints', name_waypoint)
        return self.get_pos_obj(obj)
    
    def get_door(self, name_door):
        obj = self.get_obj('Waypoints', name_door)
        obj_image, obj_rect = self.get_rect_obj(obj)
        self.screen.blit(obj_image, obj_rect)
        
        
    def get_pickup_distance(self, name_group):
        obj_layer = self.get_group_object(name_group)
        obj_pos = []
        for obj in obj_layer:
            obj_pos.append((obj.name, self.get_pos_obj(obj)))
        
        pickup_distance = 50
        return obj_pos, pickup_distance