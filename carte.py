import pygame
import pytmx
from pytmx.util_pygame import load_pygame
from obstacle import Obstacle

class Carte:
    def __init__(self, screen, map_name):
        # screen and camera
        self.screen = screen
        self.camera = pygame.Rect(0, 0, screen.get_width(), screen.get_height())

        # tmxdata
        self.image = pygame.image.load('graphics/Tiled/data/export/map_Overworld.png')
        # self.image = pygame.transform.rotozoom(self.image, 0, 2)
        # self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect(topleft = (0,0))
        self.tmxdata = load_pygame(f'graphics/Tiled/data/tmx/{map_name}.tmx')
        self.layers = self.tmxdata.visible_layers
    
    def get_group_object(self, name_group):
        """Méthode permettant d'obtenir la couche d'objets désirée selon son nom"""
        for object_layer in self.tmxdata.objectgroups:
            if object_layer.name == name_group:
                return object_layer

    def create_obstacles(self, name_group, groups):
        """Méthode permettant de créer les obstacles selon le nom de la couche d'objet 
        et dans quel groupe se situent les obstacles (ex : collision_sprites, all_sprites)"""
        for obj in self.get_group_object(name_group):
            Obstacle(self.screen, obj, groups)

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
        return int(obj.x), int(obj.y)
    
    def get_waypoint(self, name_waypoint):
        obj_layer = self.get_group_object('Waypoints')
        for obj in obj_layer:
            if obj.name == name_waypoint:
                return self.get_pos_obj(obj)

    def get_pickup_distance(self, name_group):
        obj_layer = self.get_group_object(name_group)
        obj_pos = []
        for obj in obj_layer:
            obj_pos.append((obj.name, self.get_pos_obj(obj)))
        
        pickup_distance = 50
        return obj_pos, pickup_distance

    def calculate_cam(self, player_pos):
        cam_x = player_pos[0] - (self.camera.width / 2)
        cam_y = player_pos[1] - (self.camera.height / 2)
        cam_x = max(0, min(cam_x, self.tmxdata.width * self.tmxdata.tilewidth - self.camera.width))
        cam_y = max(0, min(cam_y, self.tmxdata.height * self.tmxdata.tileheight - self.camera.height))
        self.camera = pygame.Rect(cam_x, cam_y, self.camera.width, self.camera.height)

    # def draw(self):
    #     for layer in self.layers:
    #         if isinstance(layer, pytmx.TiledTileLayer):
    #             for x, y, image in layer.tiles():
    #                 self.screen.blit(image, (x * self.tmxdata.tilewidth - self.camera.x, y * self.tmxdata.tileheight - self.camera.y))
    
    def draw(self):
        self.screen.blit(self.image, (self.rect.x * self.tmxdata.tilewidth - self.camera.x, self.rect.y * self.tmxdata.tileheight - self.camera.y))
    
    def update(self, player_pos):
        self.calculate_cam(player_pos)
        self.draw()
