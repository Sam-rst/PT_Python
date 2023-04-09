import pygame

class Obstacle(pygame.sprite.Sprite):
    
    def __init__(self, collision_object):
        super().__init__()
        self.image = pygame.Surface((collision_object.width, collision_object.height))
        # self.rect = pygame.Rect(collision_object.x, collision_object.y, collision_object.width, collision_object.height)
        self.rect = self.image.get_rect(center = (collision_object.x, collision_object.y))
        self.old_rect = self.rect.copy()