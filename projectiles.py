import pygame
import random
import math , sys
from sprites import *
from settings import *

# Définition des couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

class Projectile(pygame.sprite.Sprite):
    type = 'Projectile'
    
    def __init__(self, player_sprite, groups):
        super().__init__(groups)
        
        # Screen
        self.screen = pygame.display.get_surface()
        
        # Player sprite 
        self.caracter = player_sprite
        
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

    def update(self, dt):
        self.old_rect = self.rect.copy()
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.x = round(self.pos.x)
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.y = round(self.pos.y)
        
        self.distance_traveled += 1
        if  self.distance_traveled >= self.range:
            self.kill()
            
        ennemy_touched = pygame.sprite.spritecollide(self, ennemi_group, False)
        if ennemy_touched:
            for ennemy in ennemy_touched:
                ennemy.decrease_health(self.caracter.get_attack_value())
                ennemy.is_alive()
                self.kill()

    def get_direction(self):
        # On calcule la direction du projectile en fonction de la position de la souris
        mouse_pos = pygame.mouse.get_pos()
        self.direction = pygame.Vector2(([mouse_pos[0] - (resolution[0] // 2), mouse_pos[1] - (resolution[1] // 2)])).normalize()
        
    def get_type(self):
        return type(self).type
        
        
class EnnemiProjectile(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.speed = 5
        self.damage = 10
        self.max_distance = 300
        self.distance_traveled = 0

    def get_direction(self):
        # On calcule la direction du projectile en fonction de la position du joueur
        joueur_pos = player_sprite.sprite.rect.center
        dx = joueur_pos[0] - self.rect.centerx
        dy = joueur_pos[1] - self.rect.centery
        distance = math.sqrt(dx ** 2 + dy ** 2)
        if distance == 0:
            return (0, -1)
        else:
            return (dx / distance, dy / distance)
        
    def update(self):
        self.distance_traveled += self.speed
        if self.distance_traveled >= self.max_distance:
            self.kill()

        # Calculer la direction du projectile pour qu'elle vise le joueur
        direction = self.get_direction()
        self.rect.move_ip(direction[0] * self.speed, direction[1] * self.speed)

        # # Si le projectile touche le joueur, lui faire perdre des points de vie
        # joueur_touche = pygame.sprite.spritecollide(self, joueur_group, False)
        # if joueur_touche:
        #     print("touche")
        #     joueur_touche[0].perdre_hp(self.damage)

        #     self.kill()