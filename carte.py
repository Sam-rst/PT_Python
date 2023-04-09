import pygame, pytmx
from pytmx.util_pygame import load_pygame

# pygame.init()
# screen = pygame.display.set_mode((800, 600))
class Carte:
    def __init__(self, screen):
        
        # tmxdata
        self.tmxdata = load_pygame('graphics/Tiled/data/tmx/map_Overworld.tmx')
        self.layers = self.tmxdata.visible_layers
        self.collision_objects = [object_layer for object_layer in self.tmxdata.objectgroups if object_layer.name =='Obstacles']
        
        # screen and camera
        self.screen = screen
        
    def calculate_cam(self, player_pos):
        cam_x = player_pos[0] - (self.screen.get_width() / 2)
        cam_y = player_pos[1] - (self.screen.get_height() / 2)
        cam_x = max(0, min(cam_x, self.tmxdata.width * self.tmxdata.tilewidth - self.screen.get_width()))
        cam_y = max(0, min(cam_y, self.tmxdata.height * self.tmxdata.tileheight - self.screen.get_height()))
        return [cam_x, cam_y]
    
    def draw(self, cam_coord):
        # self.screen.fill((0, 0, 0))
        for layer in self.layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, image in layer.tiles():
                    self.screen.blit(image, (x * self.tmxdata.tilewidth - cam_coord[0], y * self.tmxdata.tileheight - cam_coord[1]))
