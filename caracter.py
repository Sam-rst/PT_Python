import pygame, settings
from dice import Dice, RiggedDice
from rich import print
from math import sqrt 
from weapon import Weapon
from debug import debug
from projectiles import Projectile
from sprites import all_sprites, projectile_sprites
from settings import *

    
class Caracter(pygame.sprite.Sprite):
    type = "caracter"

    def __init__(self, name, max_HP, attack, defense, obstacles):
        super().__init__()
        self.name = name
        self.max_HP = max_HP
        self.HP = self.max_HP
        self.attack_value = attack
        self.defense_value = defense
        self.range = 5 # rayon d'attaque du caractère
        self.cooldown = 2000 #temps de recharge en millisecondes
        self.last_shot = 0 # temps en millisecondes depuis le début de l'exécution de la boucle de jeu lors du dernier tir
        self.image = pygame.Surface((16, 16))
        self.rect = self.image.get_rect(midbottom = (200, 200))
        
        self.obstacles = obstacles
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2()
        self.speed = 200
        
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
        self.window_collision('horizontal', resolution)
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.y = round(self.pos.y)
        self.collision('vertical')
        self.window_collision('vertical', resolution)
        
    def update(self, dt):
        self.apply_collisions(dt)
        

class Player(Caracter):
    
    def __init__(self, name, max_HP, attack, defense, obstacles):
        super().__init__(name, max_HP, attack, defense, obstacles)
        player_standing = [pygame.image.load('graphics/player/walking/bottom/anim_1.png').convert_alpha()]
        
        player_bottom_walks = [pygame.image.load('graphics/player/walking/bottom/anim_1.png').convert_alpha(),
                        pygame.image.load('graphics/player/walking/bottom/anim_2.png').convert_alpha(),
                        pygame.image.load('graphics/player/walking/bottom/anim_3.png').convert_alpha(),
                        pygame.image.load('graphics/player/walking/bottom/anim_4.png').convert_alpha()]
        
        player_left_walks = [pygame.image.load('graphics/player/walking/left/anim_1.png').convert_alpha(),
                           pygame.image.load('graphics/player/walking/left/anim_2.png').convert_alpha(),
                           pygame.image.load('graphics/player/walking/left/anim_3.png').convert_alpha(),
                           pygame.image.load('graphics/player/walking/left/anim_4.png').convert_alpha()]
    
        player_top_walks = [pygame.image.load('graphics/player/walking/top/anim_1.png').convert_alpha(),
                          pygame.image.load('graphics/player/walking/top/anim_2.png').convert_alpha(),
                          pygame.image.load('graphics/player/walking/top/anim_3.png').convert_alpha(),
                          pygame.image.load('graphics/player/walking/top/anim_4.png').convert_alpha()]
        
        player_right_walks = [pygame.image.load('graphics/player/walking/right/anim_1.png').convert_alpha(),
                            pygame.image.load('graphics/player/walking/right/anim_2.png').convert_alpha(),
                            pygame.image.load('graphics/player/walking/right/anim_3.png').convert_alpha(),
                            pygame.image.load('graphics/player/walking/right/anim_4.png').convert_alpha()]
        self.frames = {
            "Standing" : player_standing,
            "Bottom" : player_bottom_walks,
            "Top" : player_top_walks,
            "Left" : player_left_walks,
            "Right" : player_right_walks
        }
        
        #Image and animations
        self.animation_index = 0
        self.animation_direction = "Standing"
        self.image = self.frames[self.animation_direction][self.animation_index]
        self.animation_speed = 0.1
        
        #Position
        self.rect = self.image.get_rect(midbottom = (400, 300))
        self.old_rect = self.rect.copy()
        self.is_moving = False
        
    def input(self):
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()
        
        if mouse[0] and pygame.time.get_ticks() - self.last_shot > self.cooldown:
            self.create_projectile()
            
        if keys[pygame.K_z]:
            self.direction.y = -1
            self.animation_direction = 'Top'
            self.is_moving = True
        elif keys[pygame.K_s]:
            self.direction.y = 1
            self.animation_direction = 'Bottom'
            self.is_moving = True
        else:
            self.direction.y = 0
            # self.is_moving = False
            # self.animation_direction = 'Standing'
        
        if keys[pygame.K_d]:
            self.direction.x = 1
            self.animation_direction = 'Right'
            self.is_moving = True
            
        elif keys[pygame.K_q]:
            self.direction.x = -1
            self.animation_direction = 'Left'
            self.is_moving = True
        else:
            self.direction.x = 0
            # self.is_moving = False
            # self.animation_direction = 'Standing'
        #Movement
    
    def create_projectile(self):
        projectile = Projectile(self.rect.center)
        projectile_sprites.add(projectile)
        all_sprites.add(projectile)
        self.last_shot = pygame.time.get_ticks()  # on enregistre le temps du dernier tir
        print("Tire")
    
    
    def animation_state(self):
        if self.is_moving:
            self.animation_index += self.animation_speed
            if self.animation_index >= len(self.frames[self.animation_direction]):
                self.animation_index = 0
            self.image = self.frames[self.animation_direction][int(self.animation_index)]
            # debug(self.animation_index)
        
    
        
    # def draw(self, screen):
    #     screen.blit(self.image, self.rect)
        

        
    def update(self, dt):
        self.old_rect = self.rect.copy()
        self.apply_collisions(dt)
        self.input()
        self.animation_state()
        # self.draw(screen)
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        




        
class Warrior(Caracter):
    type = "Warrior"
    
    # def compute_damages(self, roll, target):
    #     print("Bonus : Axe in your face ! (+3 damages)")
    #     return super().compute_damages(roll, target) + 3
    
    def transform(self):
        """Transformer le player en warrior"""
        pass


class Mage(Caracter):
    type = "Mage"

    # def compute_defense(self, roll, damages):
    #     print("Bonus : Magic armor ! (-3 wournds)")
    #     return super().compute_defense(roll, damages) - 3


class Thief(Player):
    type = "Thief"
    
    def compute_damages(self, roll, target):
        print(f"Bonus : Backstab (+{target.get_defense()} damages) !")
        return super().compute_damages(roll, target) + target.get_defense()


if __name__ == "__main__":
    a_dice = Dice(6)
    
    sword0 = Weapon("Epée en bois", 1, 0, 1)
    sword1 = Weapon("Epée commune", 2, 0, 1)
    sword2 = Weapon("Epée rare", 4, 0, 1)
    sword3 = Weapon("Epée épique", 6, 0, 1)
    sword4 = Weapon("Epée légendaire", 8, 0, 1)
    warrior1 = Warrior("Mike", 20, 8, 3, sword0, a_dice)
    mage1 = Mage("Helen", 20, 8, 3,"Baton de soUrcier", a_dice)
    thief1 = Thief("Robin", 20, 8, 3,"Dague en plastique", a_dice)
    print(warrior1)
    print(thief1)

    while (warrior1.is_alive() and thief1.is_alive()):
        warrior1.attack(thief1)
        thief1.attack(warrior1)

#faire une def pour changer d'armes