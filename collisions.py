import pygame
from settings import *

class CollisionTile(pygame.sprite.Sprite):
    type = 'CollisionTile'
    
    def __init__(self, image, pos, group):
        super().__init__(group)
        self.image = image
        self.image.fill('#0045a1')
        self.rect = self.image.get_rect(center = pos)
        self.old_rect = self.rect.copy()
        self.pos = pygame.math.Vector2(self.rect.center)
        
    def get_pos(self):
        return self.pos
        
    def get_type(self):
        return type(self).type