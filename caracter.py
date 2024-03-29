import pygame, time
from dice import Dice, RiggedDice
from math import sqrt 
from weapon import Weapon
from debug import debug
from projectiles import Projectile, EnnemiProjectile
from settings import *
from random import randint, choice
from images import *
import sprites
    
class Caracter(pygame.sprite.Sprite):
    type = "Caracter"

    def __init__(self, name, pos, groups):
        super().__init__(groups)
        self.save_data = sprites.save_data
        # Aspects of the caracter
        self.name = name
        self.max_HP = 1
        self.HP = self.max_HP
        self.attack_value = 1
        self.defense_value = 1
        self.range = 10 * scale  # rayon d'attaque du caractère
        self.cooldown_attack = 200 #temps de recharge en millisecondes
        self.last_shot = 0 # temps en millisecondes depuis le début de l'exécution de la boucle de jeu lors du dernier tir

        # Image and animations
        self.frames = {
            "Bottom Walk" : caracter_bottom_walks,
            "Left Walk" : caracter_left_walks,
            "Top Walk" : caracter_top_walks,
            "Right Walk" : caracter_right_walks
        }
        self.animation_index = 0
        self.animation_direction = "Bottom Walk"
        self.image = self.frames[self.animation_direction][self.animation_index]
        self.image = self.transform_scale()
        self.animation_speed = 0.5
        self.is_moving = False
        self.is_attack = False

        # Rectangle
        self.rect = self.image.get_rect(midbottom = pos)
        self.old_rect = self.rect.copy()

        # Screen
        self.screen = pygame.display.get_surface()

        # Moving
        self.pos = pygame.math.Vector2(self.rect.midbottom)
        self.direction = pygame.math.Vector2()
        self.speed = 500
        self.cooldown_move = 1500
        self.last_move = 0
        
        self.is_teleporting = False
        self.is_animating = False


    def set_name(self, new_name):
        """Changer le nom avec la nouvelle valeur new_name"""
        self.name = new_name

    def get_name(self):
        """Permet de récupérer le nom du caractère"""
        return self.name
    
    def set_max_HP(self, new_value):
        """Changer la valeur du nombre maximum d'HP"""
        self.max_HP = new_value

    def get_max_HP(self):
        """Permet de récupérer la vie maximale caractère"""
        return self.max_HP
    
    def set_HP(self, new_value):
        """Changer la valeur du nombre d'HP du carcatère"""
        self.HP = new_value

    def get_HP(self):
        """Permet de récupérer la vie du caractère"""
        return self.HP
    
    def set_range(self, new_value):
        """Changer la range avec la nouvelle valeur new_value"""
        self.range = new_value
    
    def get_range(self):
        """Permet de récupérer la range du caractère"""
        return self.range
    
    def set_cooldown_attack(self, new_value):
        """Changer le cooldown avec la nouvelle valeur new_value"""
        self.cooldown_attack = new_value
    
    def get_cooldown_attack(self):
        """Permet de récupérer le cooldown du caractère"""
        return self.cooldown_attack
    
    def set_attack_value(self, new_value):
        """Changer la valeur d'attaque avec la nouvelle valeur new_value"""
        self.attack_value = new_value
    
    def get_attack_value(self):
        """Permet de récupérer la valeur de l'attaque du caractère"""
        return self.attack_value
    
    def set_defense_value(self, new_value):
        """Changer la valeur d'attaque avec la nouvelle valeur new_value"""
        self.defense_value = new_value

    def get_defense_value(self):
        """Permet de récupérer la valeur de défense du caractère"""
        return self.defense_value
    
    def get_type(self):
        """Permet de récupérer le type du caractère"""
        return type(self).type
    
    def set_pos(self, new_pos):
        """Changer la position du caractère selon la nouvelle position new_pos"""
        # self.pos = new_pos
        self.pos.x = new_pos[0]
        self.pos.y = new_pos[1]
    
    def get_pos(self):
        """Permet de récupérer la position du caractère"""
        return self.pos
    
    def set_speed(self, new_value):
        """Changer la valeur de la vitesse du caractère"""
        self.speed = new_value
        
    def get_speed(self):
        """Permet de récupérer la vitesse du caractère"""
        return self.speed
    
    def set_cooldown_move(self, new_value):
        """Changer la valeur du cooldown de déplacement"""
    
    def get_ticks(self):
        """Permet de récupérer le temps en seconde"""
        return pygame.time.get_ticks()
    
    def get_width(self):
        return self.image.get_width() * scale // 2.5
    
    def get_height(self):
        return self.image.get_height() * scale // 2.5
    
    def transform_scale(self):
        return pygame.transform.scale(self.image, (self.get_width(), self.get_height()))
    
    def __str__(self):
        return f"Le {self.get_type()} {self.get_name()} possède : vie = {self.get_HP()}/{self.get_max_HP()}, attaque = {self.get_attack_value()}, defense = {self.get_defense_value()}, cooldown = {self.get_cooldown_attack()}, attack range = {self.get_range()}, position = {self.get_pos()}"

    def regenerate(self):
        """Permet de regénérer la vie du caractère"""
        self.HP = self.max_HP

    def level_up(self):
        self.set_attack_value(self.attack_value + 5)
        self.set_defense_value(self.defense_value + 2)
        self.set_max_HP(self.max_HP + 5)
        self.regenerate()
    
    def decrease_health(self, amount):
        self.set_HP(self.get_HP() - amount)
        if self.get_HP() < 0:
            self.set_HP(0)
            
    def display_life(self, screen, offset):
        life_ratio = self.get_HP() / self.get_max_HP()
        x = self.pos.x - 10 - offset.x
        y = self.pos.y - 10 - offset.y
        pygame.draw.rect(screen, '#ff0000', pygame.rect.Rect(x, y, 100, 10), 5)
        pygame.draw.rect(screen, '#00ff00', pygame.rect.Rect(x, y, 100 * life_ratio, 10), 5)

    def collision(self, direction):
        if self.is_teleporting: return
        
        collisions = pygame.sprite.spritecollide(self, sprites.camera_group.collision_group, False)
        if collisions:
            for sprite in sprites.camera_group.collision_group:
                if  direction == 'horizontal':
                    #Collision on the right
                    if self.rect.right >= sprite.rect.left and self.old_rect.right <= sprite.old_rect.left:
                        self.rect.right = sprite.rect.left
                        self.pos.x = self.rect.x

                    #Collision on the left
                    if self.rect.left <= sprite.rect.right and self.old_rect.left >= sprite.old_rect.right:
                        self.rect.left = sprite.rect.right
                        self.pos.x = self.rect.x

                if direction == 'vertical':
                    #Collisions on the top
                    if self.rect.top <= sprite.rect.bottom and self.old_rect.top >= sprite.old_rect.bottom:
                        self.rect.top = sprite.rect.bottom
                        self.pos.y = self.rect.y
                    #Collisions on the bottom
                    if self.rect.bottom >= sprite.rect.top and self.old_rect.bottom <= sprite.old_rect.top:
                        self.rect.bottom = sprite.rect.top
                        self.pos.y = self.rect.y

    def map_collision(self, direction):
        if direction == 'horizontal':
            if self.rect.left < 0: #With the left side of the map
                self.rect.left = 0
                self.pos.x = self.rect.x
            if self.rect.right > sprites.camera_group.carte.get_size_map_width():
                self.rect.right = sprites.camera_group.carte.get_size_map_width()
                self.pos.x = self.rect.x

        if direction == 'vertical': #With the top side of the window
            if self.rect.top < 0:
                self.rect.top = 0
                self.pos.y = self.rect.y
            if self.rect.bottom > sprites.camera_group.carte.get_size_map_height() - sprites.camera_group.carte.get_tileheight():
                self.rect.bottom = sprites.camera_group.carte.get_size_map_height() - sprites.camera_group.carte.get_tileheight()
                self.pos.y = self.rect.y

    def apply_collisions(self, dt):
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.x = round(self.pos.x)
        self.collision('horizontal')
        self.map_collision('horizontal')
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.y = round(self.pos.y)
        self.collision('vertical')
        self.map_collision('vertical')

    def animation_state(self):
        if self.is_attack:
            if not self.is_animating:
                self.is_animating = True
                self.animation_index = 0

            while self.animation_index < len(self.frames[self.animation_direction]):
                self.image = self.frames[self.animation_direction][int(self.animation_index)]
                self.image = self.transform_scale()
                self.animation_index += self.animation_speed

            self.animation_index = 0
            self.is_attack = False
            self.is_animating = False

        elif self.is_moving:
            if not self.is_animating:
                self.is_animating = True
                self.animation_index = 0

            self.animation_index += self.animation_speed
            if self.animation_index >= len(self.frames[self.animation_direction]):
                self.animation_index = 0
            else:
                self.image = self.frames[self.animation_direction][int(self.animation_index)]
                self.image = self.transform_scale()
        else:
            self.is_animating = False


            
    def debug(self):
        pygame.draw.rect(self.screen, '#ff0000', self.rect, 5)
        pygame.draw.rect(self.screen, '#00ff00', self.old_rect, 5)
        pygame.draw.circle(self.screen, '#fd5a61', self.get_pos(), 5)
        self.image.fill('#0000ff')