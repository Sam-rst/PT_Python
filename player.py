from caracter import *
from sprites import *

class Player(Caracter):
    type = 'Player'
    
    def __init__(self, name, pos, groups):
        super().__init__(name, pos, groups)
        self.transform_to_player()
    
    def transform_to_player(self):
        self.frames["Bottom Walk"] = player_bottom_walks
        self.frames["Left Walk"] = player_left_walks
        self.frames["Top Walk"] = player_top_walks
        self.frames["Right Walk"] = player_right_walks
        self.image = self.frames[self.animation_direction][self.animation_index]
        self.image = self.transform_scale()
        # self.rect = self.image.get_rect(center = self.get_pos())
        
    
    def input(self):
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()
        
        if mouse[0] and pygame.time.get_ticks() - self.last_shot > self.cooldown_attack:
            self.shoot()
        
        if keys[pygame.K_z] or keys[pygame.K_s] or keys[pygame.K_d] or keys[pygame.K_q]:
            if keys[pygame.K_z]:
                self.direction.y = -1
                self.animation_direction = 'Top Walk'
                self.is_moving = True
            elif keys[pygame.K_s]:
                self.direction.y = 1
                self.animation_direction = 'Bottom Walk'
                self.is_moving = True
            else:
                self.direction.y = 0
                
            if keys[pygame.K_d]:
                self.direction.x = 1
                self.animation_direction = 'Right Walk'
                self.is_moving = True
            elif keys[pygame.K_q]:
                self.direction.x = -1
                self.animation_direction = 'Left Walk'
                self.is_moving = True
            else:
                self.direction.x = 0
        else:
            self.direction.x = 0
            self.direction.y = 0
            self.is_moving = False
            self.animation_index = 0

    def shoot(self):
        Projectile(self, [sprites.projectile_sprites] + list(sprites.camera_groups.values()))
        self.last_shot = pygame.time.get_ticks()  # on enregistre le temps du dernier tir
        self.is_attack = True
        
    def update(self, dt):
        self.old_rect = self.rect.copy()
        self.input()
        self.apply_collisions(dt)
        self.animation_state()
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

class Warrior(Player):
    type = "Warrior"
    
    def __init__(self, name, pos, groups):
        super().__init__(name, pos, groups)
        self.transform_to_warrior()
    
    def transform_to_warrior(self):
        """Transformer le player en warrior"""
        self.frames['Bottom Walk'] = warrior_bottom_walks
        self.frames['Left Walk'] = warrior_left_walks
        self.frames['Top Walk'] = warrior_top_walks
        self.frames['Right Walk'] = warrior_right_walks
        self.frames['Bottom Attack'] = warrior_bottom_attack
        self.frames['Left Attack'] = warrior_left_attack
        self.frames['Top Attack'] = warrior_top_attack
        self.frames['Right Attack'] = warrior_right_attack
        self.image = self.frames[self.animation_direction][self.animation_index]
        self.image = self.transform_scale()
        self.set_range(10)
        
    def update(self, dt):
        self.old_rect = self.rect.copy()
        self.input()
        self.apply_collisions(dt)
        self.animation_state()
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()


class Mage(Player):
    type = "Mage"

    # def compute_defense(self, roll, damages):
    #     print("Bonus : Magic armor ! (-3 wournds)")
    #     return super().compute_defense(roll, damages) - 3


class Thief(Player):
    type = "Thief"
    
    # def compute_damages(self, roll, target):
    #     print(f"Bonus : Backstab (+{target.get_defense()} damages) !")
    #     return super().compute_damages(roll, target) + target.get_defense()