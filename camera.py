import pygame
from settings import *

class CameraGroup(pygame.sprite.Group):
    def __init__(self, carte):
        super().__init__()
        self.screen = pygame.display.get_surface()
        
        # Camera Offset
        self.offset = pygame.math.Vector2()
        self.half_w = self.screen.get_size()[0] // 2
        self.half_h = self.screen.get_size()[1] // 2
        
        # Ground
        self.carte = carte
        
        # Box setup
        self.camera_borders = {'left' : 300, 'right' : 300, 'top' : 200, 'bottom' : 200}
        l = self.camera_borders['left']
        t = self.camera_borders['top']
        w = self.screen.get_size()[0] - (self.camera_borders['left'] + self.camera_borders['right'])
        h = self.screen.get_size()[1] - (self.camera_borders['top'] + self.camera_borders['bottom'])
        self.camera_rect = pygame.Rect(l, t, w, h)
        
    def center_target_camera(self, target):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h
    
    def box_target_camera(self, target):
        if target.rect.left < self.camera_rect.left: #move camera on the left
            self.camera_rect.left = target.rect.left
            
        if target.rect.right > self.camera_rect.right: #move camera on the right
            self.camera_rect.right = target.rect.right
        
        if target.rect.top < self.camera_rect.top: #move camera on the top
            self.camera_rect.top = target.rect.top
        
        if target.rect.bottom > self.camera_rect.bottom: #move camera on the bottom
            self.camera_rect.bottom = target.rect.bottom
        
        self.offset.x = self.camera_rect.left - self.camera_borders['left']
        self.offset.y = self.camera_rect.top - self.camera_borders['top']

    def custom_draw(self, player, type_camera):
        """Choix du type de la caméra selon 5 types avec la liste en paramètre :
            - 'center'
            - 'box'"""

        if type_camera == 'center': self.center_target_camera(player)
        elif type_camera == 'box': self.box_target_camera(player)
        else:
            raise ValueError("Ce type de camera n'existe pas")
        
        # Ground
        for layer in self.carte.layers:
            for x, y, image in layer.tiles():
                # image = pygame.transform.scale2x(image)
                image = pygame.transform.scale(image, (self.carte.tilewidth, self.carte.tileheight))
                ground_offset = (x*self.carte.tilewidth, y*self.carte.tileheight) - self.offset
                self.screen.blit(image, ground_offset)
        
        # Active elements
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.screen.blit(sprite.image, offset_pos)
        
        # pygame.draw.rect(self.screen, 'yellow', self.camera_rect, 5)