import pygame

class Obstacle(pygame.sprite.Sprite):
    
    def __init__(self, screen, collision_object, groups):
        super().__init__(groups)
        self.image = pygame.Surface((collision_object.width, collision_object.height))
        # self.rect = pygame.Rect(collision_object.x, collision_object.y, collision_object.width, collision_object.height)
        self.rect = self.image.get_rect(topleft = (collision_object.x, collision_object.y))
        self.old_rect = self.rect.copy()
        self.screen = screen
        
    def draw(self):
        self.image.fill((255, 0, 0))
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        self.draw()