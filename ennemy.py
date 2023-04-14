from caracter import *

class Ennemy(Caracter):
    type = 'Ennemy'
    
    def __init__(self, name, max_HP, attack, defense, pos, obstacles, groups):
        super().__init__(name, max_HP, attack, defense, pos, obstacles, groups)
        self.image = pygame.image.load("graphics/caracters/ennemy/demon/walking/anim_1.png").convert_alpha()
        self.image = self.transform_scale()
        self.time_move = 0

        
        # Si le temps de recharge est écoulé et que l'ennemi peut tirer, on tire un projectile
        if pygame.time.get_ticks() - self.last_shot > self.cooldown:
            self.shoot()
            self.last_shot = pygame.time.get_ticks()

    def shoot(self):
        projectile = EnnemiProjectile(self.rect.center)
        ennemi_projectiles.add(projectile)
        all_sprites.add(projectile)

    def perdre_hp(self, damage):
        self.HP -= damage
        if self.HP <= 0:
            self.kill()
    
    def update(self, dt):
        # On met à jour la position de l'ennemi de manière aléatoire toutes les 500 ms
        if pygame.time.get_ticks() - self.time_move > 500:
            self.rect.move_ip(randint(-5, 5), randint(-5, 5))
            self.time_move = pygame.time.get_ticks()