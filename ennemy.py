from caracter import *

class Ennemy(Caracter):
    type = 'Ennemy'
    
    def __init__(self, name, pos, groups):
        super().__init__(name, pos, groups)
        self.transform_to_ennemy()
        self.range_can_attack = 5
        
    def transform_to_ennemy(self):
        self.frames["Bottom Walk"] = demon_bottom_walks
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
    
    def shoot(self):
        EnnemiProjectile(self.rect.center, [sprites.ennemi_projectiles])
    
    def update(self, dt):
        self.old_rect = self.rect.copy()

        # Collisions and moving setup
        self.apply_collisions(dt)
        if (self.get_ticks() - self.last_move) > self.cooldown_move:
            print('Moving !!')
            self.change_direction()
            self.last_move = self.get_ticks()
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()


        # Attack setup
        # if (self.get_ticks() - self.last_shot) > self.cooldown_attack:
        #     self.shoot()
        #     self.last_shot = self.get_ticks()
        
        if self.get_ticks() - self.last_shot > self.cooldown_attack:
            # self.shoot()
            print('Shooting !!')
            self.last_shot = self.get_ticks()
        
        self.animation_state()