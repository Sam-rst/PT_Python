import pygame
from save import SaveData
from caracter import *
from items import Item

class Ennemy(Caracter):
    type = 'Ennemy'
    
    def __init__(self, name, pos, groups):
        super().__init__(name, pos, groups)
        self.transform_to_ennemy()
        self.range_can_attack = 5
        self.items = []
    def transform_to_ennemy(self):
        # self.frames["Bottom Walk"] = demon_bottom_walks
        self.image = self.frames[self.animation_direction][self.animation_index]
        self.image = self.transform_scale()
        self.rect = self.image.get_rect(center = self.get_pos())
        self.set_speed(100)
        self.set_attack_value(5)
        self.set_cooldown_attack(2500)
        self.set_HP(50)

    def change_direction(self):
        if randint(0,1):
            self.direction.x = randint(-1, 1)
            self.direction.y = randint(-1, 1)
            self.is_moving = True
        else:
            self.is_moving = False
            self.direction.x = 0
            self.direction.y = 0
        
        if self.direction.x == -1:
            self.animation_direction = 'Left Walk'
        elif self.direction.x == 1:
            self.animation_direction = 'Right Walk'
        
        if self.direction.y == -1:
            self.animation_direction = 'Top Walk'
        elif self.direction.y == 1:
            self.animation_direction = 'Bottom Walk'
    
    def is_alive(self):
        if self.get_HP() <= 0:
            self.kill()
            self.save_data.save_mob_dead(self.name)
            self.piecemob = Item('Piece', self.get_pos(), [sprites.camera_group, sprites.items_sprites, sprites.items_drop])
            self.items.append(self.piecemob)
    
    def random_spawn(self):
        width, height = sprites.camera_group.carte.get_size_map()
        self.set_pos((randint(100, width-100), randint(100, height-100)))

    def shoot(self):
        EnnemiProjectile(self, [sprites.ennemi_projectiles] + list(sprites.camera_groups.values()))

    def update(self, dt):
        self.is_alive()
        self.old_rect = self.rect.copy()
        # Collisions and moving setup
        self.apply_collisions(dt)
        if (self.get_ticks() - self.last_move) > self.cooldown_move:
            # print('Moving !!')
            self.change_direction()
            self.last_move = self.get_ticks()
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        if self.get_ticks() - self.last_shot > self.cooldown_attack:
            self.shoot()
            self.is_attack = True
            # print('Shooting !!')
            self.last_shot = self.get_ticks()
        else:
            self.is_attack = False
        
        self.animation_state()
        self.rect = self.image.get_rect(topleft = self.get_pos())
        
class Demon(Ennemy):
    type = 'Demon'
    
    def __init__(self, name, pos, groups):
        super().__init__(name, pos, groups)
        self.transform_to_demon()
        
    def transform_to_demon(self):
        """Transformer le player en demon"""
        self.frames['Bottom Walk'] = demon_bottom_walks
        self.frames['Left Walk'] = demon_left_walks
        self.frames['Top Walk'] = demon_top_walks
        self.frames['Right Walk'] = demon_right_walks
        self.frames['Bottom Attack'] = demon_bottom_attack
        self.frames['Left Attack'] = demon_left_attack
        self.frames['Top Attack'] = demon_top_attack
        self.frames['Right Attack'] = demon_right_attack
        self.image = self.frames[self.animation_direction][self.animation_index]
        self.image = self.transform_scale()
        self.cooldown_attack = 2000
        self.set_max_HP(8000)
        
        self.random_spawn()

class Goblin(Ennemy):
    type = 'Goblin'
    
    def __init__(self, name, pos, groups):
        super().__init__(name, pos, groups)
        self.transform_to_goblin()
        
    def transform_to_goblin(self):
        """Transformer le player en goblin"""
        self.frames['Bottom Walk'] = goblin_bottom_walks
        self.frames['Left Walk'] = goblin_left_walks
        self.frames['Top Walk'] = goblin_top_walks
        self.frames['Right Walk'] = goblin_right_walks
        self.frames['Bottom Attack'] = goblin_bottom_attack
        self.frames['Left Attack'] = goblin_left_attack
        self.frames['Top Attack'] = goblin_top_attack
        self.frames['Right Attack'] = goblin_right_attack
        self.image = self.frames[self.animation_direction][self.animation_index]
        self.image = self.transform_scale()
        
        self.random_spawn()

class Zombie(Ennemy):
    type = 'Zombie'
    
    def __init__(self, name, pos, groups):
        super().__init__(name, pos, groups)
        self.transform_to_zombie()
        
    def transform_to_zombie(self):
        """Transformer le player en zombie"""
        self.frames['Bottom Walk'] = zombie_bottom_walks
        self.frames['Left Walk'] = zombie_left_walks
        self.frames['Top Walk'] = zombie_top_walks
        self.frames['Right Walk'] = zombie_right_walks
        self.frames['Bottom Attack'] = zombie_bottom_attack
        self.frames['Left Attack'] = zombie_left_attack
        self.frames['Top Attack'] = zombie_top_attack
        self.frames['Right Attack'] = zombie_right_attack
        self.image = self.frames[self.animation_direction][self.animation_index]
        self.image = self.transform_scale()

        self.random_spawn()
        
class Skeleton(Ennemy):
    type = 'Skeleton'
    
    def __init__(self, name, pos, groups):
        super().__init__(name, pos, groups)
        self.transform_to_skeleton()
        
    def transform_to_skeleton(self):
        """Transformer le player en skeleton"""
        self.frames['Bottom Walk'] = skeleton_bottom_walks
        self.frames['Left Walk'] = skeleton_left_walks
        self.frames['Top Walk'] = skeleton_top_walks
        self.frames['Right Walk'] = skeleton_right_walks
        self.frames['Bottom Attack'] = skeleton_bottom_attack
        self.frames['Left Attack'] = skeleton_left_attack
        self.frames['Top Attack'] = skeleton_top_attack
        self.frames['Right Attack'] = skeleton_right_attack
        self.image = self.frames[self.animation_direction][self.animation_index]
        self.image = self.transform_scale()
        
        self.random_spawn()