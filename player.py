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
    
    def is_alive(self):
        if self.HP == 0:
            self.kill()
            return False
        return True
    
    def input(self):
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()
        
        if mouse[0] and (self.get_ticks() - self.last_shot > self.cooldown_attack):
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
        self.set_range(3)
        self.set_max_HP(100)
        self.set_HP(self.get_max_HP())
        self.set_attack_value(20)
        self.set_defense_value(10)
        self.set_cooldown_attack(800)
        self.set_speed(250)

class Mage(Player):
    type = "Mage"
    
    def __init__(self, name, pos, groups):
        super().__init__(name, pos, groups)
        self.transform_to_mage()
    
    def transform_to_mage(self):
        """Transformer le player en warrior"""
        self.frames['Bottom Walk'] = mage_bottom_walks
        self.frames['Left Walk'] = mage_left_walks
        self.frames['Top Walk'] = mage_top_walks
        self.frames['Right Walk'] = mage_right_walks
        self.frames['Bottom Attack'] = mage_bottom_attack
        self.frames['Left Attack'] = mage_left_attack
        self.frames['Top Attack'] = mage_top_attack
        self.frames['Right Attack'] = mage_right_attack
        self.image = self.frames[self.animation_direction][self.animation_index]
        self.image = self.transform_scale()
        self.set_range(20)
        self.set_max_HP(80)
        self.set_HP(self.get_max_HP())
        self.set_attack_value(15)
        self.set_defense_value(5)
        self.set_cooldown_attack(800)
        self.set_speed(275)

class Assassin(Player):
    type = "Assassin"
    
    def __init__(self, name, pos, groups):
        super().__init__(name, pos, groups)
        self.transform_to_assassin()
    
    def transform_to_assassin(self):
        """Transformer le player en warrior"""
        self.frames['Bottom Walk'] = assassin_bottom_walks
        self.frames['Left Walk'] = assassin_left_walks
        self.frames['Top Walk'] = assassin_top_walks
        self.frames['Right Walk'] = assassin_right_walks
        self.frames['Bottom Attack'] = assassin_bottom_attack
        self.frames['Left Attack'] = assassin_left_attack
        self.frames['Top Attack'] = assassin_top_attack
        self.frames['Right Attack'] = assassin_right_attack
        self.image = self.frames[self.animation_direction][self.animation_index]
        self.image = self.transform_scale()
        self.set_range(3)
        self.set_max_HP(75)
        self.set_HP(self.get_max_HP())
        self.set_attack_value(12)
        self.set_defense_value(2)
        self.set_cooldown_attack(400)
        self.set_speed(600)

class Guard(Player):
    type = "Guard"
    
    def __init__(self, name, pos, groups):
        super().__init__(name, pos, groups)
        self.transform_to_guard()
    
    def transform_to_guard(self):
        """Transformer le player en warrior"""
        self.frames['Bottom Walk'] = guard_bottom_walks
        self.frames['Left Walk'] = guard_left_walks
        self.frames['Top Walk'] = guard_top_walks
        self.frames['Right Walk'] = guard_right_walks
        self.frames['Bottom Attack'] = guard_bottom_attack
        self.frames['Left Attack'] = guard_left_attack
        self.frames['Top Attack'] = guard_top_attack
        self.frames['Right Attack'] = guard_right_attack
        self.image = self.frames[self.animation_direction][self.animation_index]
        self.image = self.transform_scale()
        self.set_range(2)
        self.set_max_HP(150)
        self.set_HP(self.get_max_HP())
        self.set_attack_value(10)
        self.set_defense_value(15)
        self.set_cooldown_attack(1200)
        self.set_speed(250)

class Archer(Player):
    type = "Archer"
    
    def __init__(self, name, pos, groups):
        super().__init__(name, pos, groups)
        self.transform_to_archer()
    
    def transform_to_archer(self):
        """Transformer le player en warrior"""
        self.frames['Bottom Walk'] = archer_bottom_walks
        self.frames['Left Walk'] = archer_left_walks
        self.frames['Top Walk'] = archer_top_walks
        self.frames['Right Walk'] = archer_right_walks
        self.frames['Bottom Attack'] = archer_bottom_walks
        self.frames['Left Attack'] = archer_left_attack
        self.frames['Top Attack'] = archer_top_attack
        self.frames['Right Attack'] = archer_right_attack
        self.image = self.frames[self.animation_direction][self.animation_index]
        self.image = self.transform_scale()
        self.set_range(75)
        self.set_max_HP(95)
        self.set_HP(self.get_max_HP())
        self.set_attack_value(18)
        self.set_defense_value(2)
        self.set_cooldown_attack(850)
        self.set_speed(450)

class Tank(Player):
    type = "Tank"
    
    def __init__(self, name, pos, groups):
        super().__init__(name, pos, groups)
        self.transform_to_tank()
    
    def transform_to_tank(self):
        """Transformer le player en warrior"""
        self.frames['Bottom Walk'] = tank_bottom_walks
        self.frames['Left Walk'] = tank_left_walks
        self.frames['Top Walk'] = tank_top_walks
        self.frames['Right Walk'] = tank_right_walks
        self.frames['Bottom Attack'] = tank_bottom_attack
        self.frames['Left Attack'] = tank_left_attack
        self.frames['Top Attack'] = tank_top_attack
        self.frames['Right Attack'] = tank_right_attack
        self.image = self.frames[self.animation_direction][self.animation_index]
        self.image = self.transform_scale()
        self.set_range(2)
        self.set_max_HP(300)
        self.set_HP(self.get_max_HP())
        self.set_attack_value(10)
        self.set_defense_value(20)
        self.set_cooldown_attack(1000)
        self.set_speed(150)