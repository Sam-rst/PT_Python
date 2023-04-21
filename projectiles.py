import pygame
import random
import math , sys
import sprites
from settings import *

class Projectile(pygame.sprite.Sprite):
    type = 'Projectile'
    
    def __init__(self, caracter_sprite, groups):
        super().__init__(groups)
        
        # Screen
        self.screen = pygame.display.get_surface()
        
        # Player sprite 
        self.caracter = caracter_sprite
        
        # Surface and rectangle
        self.image = pygame.image.load('graphics/weapons/orbs/orb_red.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = self.caracter.get_pos())
        self.old_rect = self.rect.copy()
        
        self.pos = pygame.math.Vector2(self.rect.center)
        self.direction = pygame.math.Vector2()
        self.get_direction()
        
        self.speed = 1000
        self.range = self.caracter.get_range()
        self.distance_traveled = 0

    def get_pos(self):
        return self.pos
    
    def get_ticks(self):
        return pygame.time.get_ticks()

    def get_type(self):
        return type(self).type
    
    def get_direction(self):
        # On calcule la direction du projectile en fonction de la position de la souris
        mouse_pos = pygame.mouse.get_pos()
        if sprites.camera_group.type_camera == "center":
            self.direction = pygame.Vector2((mouse_pos[0] - self.screen.get_size()[0] // 2, mouse_pos[1] - self.screen.get_size()[1] // 2)).normalize()
        elif sprites.camera_group.type_camera == "box":
            player_pos = self.caracter.pos - sprites.camera_group.offset
            self.direction = pygame.Vector2(mouse_pos - player_pos).normalize()

        if not self.caracter.is_animating:
            self.caracter.is_attack = True
            if (-1 < self.direction.x < 1) and (0 < self.direction.y < 1):
                self.caracter.animation_direction = "Bottom Attack"

            elif (-1 < self.direction.x < 0) and (-1 < self.direction.y < 1):
                self.caracter.animation_direction = "Left Attack"

            elif (-1 < self.direction.x < 1) and (-1 < self.direction.y < 0):
                self.caracter.animation_direction = 'Top Attack'

            elif (0 < self.direction.x < 1) and (-1 < self.direction.y < 1):
                self.caracter.animation_direction = "Right Attack"

        self.caracter.is_animating = True

    
    def update(self, dt):
        self.old_rect = self.rect.copy()
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.x = round(self.pos.x)
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.y = round(self.pos.y)
        
        #Changement de la direction de l'animation
        self.distance_traveled += 1
        if  self.distance_traveled >= self.range:
            self.kill()

        ennemy_touched = pygame.sprite.spritecollide(self, sprites.ennemi_group, False)
        if ennemy_touched:
            for ennemy in ennemy_touched:
                ennemy.decrease_health(self.caracter.get_attack_value())
                ennemy.is_alive()
                self.kill()

        
class EnnemiProjectile(Projectile):
    type = 'EnnemiProjectile'
    def __init__(self, caracter_sprite, groups):
        super().__init__(caracter_sprite, groups)
        self.image = pygame.image.load('graphics/weapons/orbs/orb_yellow.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = self.caracter.get_pos())
        self.player = sprites.player

    def get_direction(self):
        # On calcule la direction du projectile en fonction de la position du joueur
        player_pos = sprites.player.get_pos()

        dx = player_pos[0] - self.pos.x
        dy = player_pos[1] - self.pos.y
        distance = math.sqrt(dx ** 2 + dy ** 2)

        if distance == 0:
            self.direction.x = 0
            self.direction.y = -1
        else:
            self.direction.x = dx / distance
            self.direction.y = dy / distance

        self.caracter.is_attack = True
        if (-1 < self.direction.x < 1) and (0 < self.direction.y < 1):
            self.caracter.animation_direction = "Bottom Attack"

        elif (-1 < self.direction.x < 0) and (-1 < self.direction.y < 1):
            self.caracter.animation_direction = "Left Attack"

        elif (-1 < self.direction.x < 1) and (-1 < self.direction.y < 0):
            self.caracter.animation_direction = 'Top Attack'

        elif (0 < self.direction.x < 1) and (-1 < self.direction.y < 1):
            self.caracter.animation_direction = "Right Attack"

    def update(self, dt):
        self.old_rect = self.rect.copy()
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.x = round(self.pos.x)
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.y = round(self.pos.y)
        
        #Changement de la direction de l'animation
        self.distance_traveled += 1
        if  self.distance_traveled >= self.range:
            self.kill()

        player_touched = pygame.sprite.spritecollide(self, [sprites.player], False)
        if player_touched:
            self.player.decrease_health(self.caracter.get_attack_value())
            self.player.is_alive()
            self.kill()
            
    def get_type(self):
        return type(self).type