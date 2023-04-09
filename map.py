import pygame, pytmx
from pytmx.util_pygame import load_pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
class Carte:
    def __init__(self):
        self.tmxdata = load_pygame('graphics/Tiled/data/tmx/map_Overworld.tmx')
        self.layers = self.tmxdata.visible_layers
        self.collision_objects = [object_layer for object_layer in self.tmxdata.objectgroups if object_layer.name =='Obstacles']
        self.collision_tiles = []

        # for x, y, tile in self.collision_layer.tiles():
        #     if tile:
        #         self.collision_tiles.append(pygame.Rect(x * self.tmxdata.tilewidth, y * self.tmxdata.tileheight, self.tmxdata.tilewidth, self.tmxdata.tileheight))

    def str(self):
        pass

    def draw(self, screen, camera_x, camera_y):
        screen.fill((0, 0, 0))
        for layer in self.layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, image in self.layer.tiles():
                    screen.blit(image, (x * self.tmxdata.tilewidth - camera_x, y * self.tmxdata.tileheight - camera_y))

    def get_collision_tiles(self):
        return self.collision_tiles

    def get_width(self):
        return self.tmxdata.width * self.tmxdata.tilewidth

    def get_height(self):
        return self.tmxdata.height * self.tmxdata.tileheight
    
    