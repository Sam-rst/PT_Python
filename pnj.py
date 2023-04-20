from caracter import *


class Pnj(Caracter):
    type = 'Pnj'
    
    def __init__(self, name, pos, groups):
        super().__init__(name, pos, groups)
        self.transform_to_pnj()
        # self.items = []
        
    def transform_to_pnj(self):
        # self.frames["Bottom Walk"] = demon_bottom_walks
        self.image = self.frames[self.animation_direction][self.animation_index]
        self.image = self.transform_scale()
        self.rect = self.image.get_rect(center = self.get_pos())
        self.set_speed(100)

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
            # self.piecemob = Item('Piece', self.get_pos(), [sprites.camera_group, sprites.items_sprites, sprites.items_drop])
            self.items.append(self.piecemob)
            
    def random_spawn(self):
        width, height = sprites.camera_group.carte.get_size_map()
        self.set_pos((randint(100, width-100), randint(100, height-100)))


    def display_life(self, screen, offset):
        life_ratio = self.get_HP() / self.get_max_HP()
        x = self.pos.x - 10 - offset.x
        y = self.pos.y - 10 - offset.y
        pygame.draw.rect(screen, '#ff0000', pygame.rect.Rect(x, y, 100, 10), 5)
        pygame.draw.rect(screen, '#00ff00', pygame.rect.Rect(x, y, 100 * life_ratio, 10), 5)
    
    def update(self, dt):
        self.old_rect = self.rect.copy()
        # Collisions and moving setup
        self.apply_collisions(dt)
        if (self.get_ticks() - self.last_move) > self.cooldown_move:
            # print('Moving !!')
            self.change_direction()
            self.last_move = self.get_ticks()
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.animation_state()
        self.rect = self.image.get_rect(topleft = self.get_pos())

    
        
class Marchand(Pnj):
    type = 'Marchand'
    
    def __init__(self, name, pos, groups):
        super().__init__(name, pos, groups)
        self.transform_to_marchand()
        
    def transform_to_marchand(self):
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

class Pretre(Pnj):
    type = 'Pretre'
    
    def __init__(self, name, pos, groups):
        super().__init__(name, pos, groups)
        self.transform_to_marchand()
        
    def transform_to_marchand(self):
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
