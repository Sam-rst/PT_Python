from caracter import *

class Ennemy(Caracter):
    type = 'Ennemy'
    
    def __init__(self, name, max_HP, attack, range_attack, defense, pos, groups):
        super().__init__(name, max_HP, attack, range_attack, defense, pos, groups)
        self.transform_to_ennemy()
        self.range_can_attack = 5
        
    def transform_to_ennemy(self):
        self.frames["Bottom Walk"] = demon_bottom_walks
        self.image = self.frames[self.animation_direction][self.animation_index]
        self.image = self.transform_scale()
        self.rect = self.image.get_rect(center = self.get_pos())
        self.set_speed(100)
        
        
        # Si le temps de recharge est écoulé et que l'ennemi peut tirer, on tire un projectile

    
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
        projectile = EnnemiProjectile(self.rect.center)
        ennemi_projectiles.add(projectile)
        all_sprites.add(projectile)
    
    def update(self, dt):
        self.old_rect = self.rect.copy()

        # Collisions and moving setup
        self.apply_collisions(dt)
        if (self.get_ticks() - self.cooldown_move) > 1500:
            self.change_direction()
            self.cooldown_move = self.get_ticks()
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.animation_state()

        # Attack setup
        if (self.get_ticks() - self.last_shot) > self.cooldown_attack:
            self.shoot()
            self.last_shot = self.get_ticks()