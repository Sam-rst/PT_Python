import pygame
import random
import math , sys
from sprites import *

# Définition des couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

class Projectile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        
        # Surface and rectangle
        self.image = pygame.Surface([10, 10])
        self.image.fill('#00ff00')
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = 5
        self.direction = self.get_direction()
        self.distance_traveled = 0
        self.damage = 100

    def update(self):
        self.rect.move_ip(self.direction[0] * self.speed, self.direction[1] * self.speed)
        self.distance_traveled += self.speed
        if self.distance_traveled >= 500:
            self.kill()
        if self.rect.bottom < 0:
            self.kill()
        
                # Si le projectile touche le carré ennemi, le faire perdre des points de vie
        ennemi_touche = pygame.sprite.spritecollide(self, ennemi_group, False)
        if ennemi_touche:
            ennemi_touche[0].perdre_hp(self.damage)
            self.kill()
            print("tué")

        # # Si le projectile touche le carré ennemi, le faire perdre des points de vie
        # ennemi_touche = pygame.sprite.spritecollide(self, ennemi_group, False)
        # if ennemi_touche:
        #     ennemi_touche[0].perdre_hp(self.damage)
        #     self.kill()

    def get_direction(self):
        # On calcule la direction du projectile en fonction de la position de la souris
        mouse_pos = pygame.mouse.get_pos()
        dx = mouse_pos[0] - self.rect.centerx
        dy = mouse_pos[1] - self.rect.centery
        distance = math.sqrt(dx ** 2 + dy ** 2)
        if distance == 0:
            return (0, -1)
        else:
            return (dx / distance, dy / distance)
        
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

