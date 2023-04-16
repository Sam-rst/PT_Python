import pygame
from settings import *

class Obstacle(pygame.sprite.Group):
    
    def __init__(self, collision_object, group):
        super().__init__(group)
        self.screen = pygame.display.get_surface()
        self.image = pygame.Surface((collision_object.width * scale, collision_object.height * scale))
        self.rect = self.image.get_rect(topleft = (collision_object.x * scale, collision_object.y * scale))
        self.old_rect = self.rect.copy()
        
    def draw(self):
        self.image.fill((255, 0, 0))
        self.screen.blit(self.image, self.rect)
