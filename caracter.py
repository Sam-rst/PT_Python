import pygame, settings
from dice import Dice, RiggedDice
from math import sqrt 
from weapon import Weapon
from debug import debug
from projectiles import Projectile, EnnemiProjectile
from sprites import *
from settings import *
from random import randint

    
class Caracter(pygame.sprite.Sprite):
    type = "Caracter"

    def __init__(self, name, max_HP, attack, defense, pos, obstacles, groups):
        super().__init__(groups)
        
        # Aspects of the caracter
        self.name = name
        self.max_HP = max_HP
        self.HP = self.max_HP
        self.attack_value = attack
        self.defense_value = defense
        self.range = 5 # rayon d'attaque du caractère
        self.cooldown = 2000 #temps de recharge en millisecondes
        self.last_shot = 0 # temps en millisecondes depuis le début de l'exécution de la boucle de jeu lors du dernier tir
        
        # Surface and rectangle
        self.image = pygame.Surface((16, 16))
        self.rect = self.image.get_rect(center = pos)
        self.old_rect = self.rect.copy()
        
        self.screen = pygame.display.get_surface()
        
        self.obstacles = obstacles
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2()
        self.animation_speed = 0.1
        self.speed = 500


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
        self.max_HP = new_value

    def get_HP(self):
        """Permet de récupérer la vie du caractère"""
        return self.max_HP
    
    def set_range(self, new_value):
        """Changer la range avec la nouvelle valeur new_value"""
        self.range = new_value
    
    def get_range(self):
        """Permet de récupérer la range du caractère"""
        return self.max_HP
    
    def set_cooldown(self, new_value):
        """Changer le cooldown avec la nouvelle valeur new_value"""
        self.cooldown = new_value
    
    def get_cooldown(self):
        """Permet de récupérer le cooldown du caractère"""
        return self.cooldown
    
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
        self.rect= new_pos
        self.pos = self.rect
    
    def get_pos(self):
        """Permet de récupérer la position du caractère"""
        return self.pos
    
    def set_speed(self, new_value):
        """Changer la valeur de la vitesse du caractère"""
        self.speed = new_value
        
    def get_speed(self):
        """Permet de récupérer la vitesse du caractère"""
        return self.speed
    
    def get_width(self):
        return self.image.get_width() * scale // 2.5
    
    def get_height(self):
        return self.image.get_height() * scale // 2.5
    
    def transform_scale(self):
        return pygame.transform.scale(self.image, (self.get_width(), self.get_height()))
    
    def __str__(self):
        return f"Le {self.get_type()} {self.get_name()} possède : vie = {self.get_HP()}/{self.get_max_HP()}, attaque = {self.get_attack_value()}, defense = {self.get_defense_value}, cooldown = {self.get_cooldown()}, attack range = {self.get_range()}, position = {self.get_pos()}"
    
    def regenerate(self):
        """Permet de regénérer la vie du caractère"""
        self.health = self.max_health
        
    def level_up(self):
        self.set_attack_value(self.get_attack_value + 5)
        self.set_defense_value(self.get_defense_value + 2)
        self.set_max_HP += 5
        self.regenerate
    
    def decrease_health(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0

    def collision(self, direction):
        collision_sprites = pygame.sprite.spritecollide(self, self.obstacles, False)
        if collision_sprites:
            for sprite in collision_sprites:
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

    def window_collision(self, direction, resolution):
        if direction == 'horizontal':
            if self.rect.left < 0: #With the left side of the window
                self.rect.left = 0
                self.pos.x = self.rect.x
                self.direction.x *= -1
            if self.rect.right > resolution[0]: #With the right side of the window
                self.rect.right = resolution[0]
                self.pos.x = self.rect.x
                self.direction.x *= -1
                
        if direction == 'vertical': #With the top side of the window
            if self.rect.top < 0:
                self.rect.top = 0
                self.pos.y = self.rect.y
                self.direction.y *= -1
            if self.rect.bottom > resolution[1]:
                self.rect.bottom = resolution[1]
                self.pos.y = self.rect.y
                self.direction.y *= -1
                
    def apply_collisions(self, dt):
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.x = round(self.pos.x)
        self.collision('horizontal')
        # self.window_collision('horizontal', resolution)
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.y = round(self.pos.y)
        self.collision('vertical')
        # self.window_collision('vertical', resolution)
        
    def update(self, dt):
        self.apply_collisions(dt)