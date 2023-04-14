from caracter import *

class Player(Caracter):
    type = 'Player'
    
    def __init__(self, name, max_HP, attack, defense, pos, obstacles, groups):
        super().__init__(name, max_HP, attack, defense, pos, obstacles, groups)
        player_standing = [pygame.image.load('graphics/caracters/player/villager/walking/bottom/anim_1.png').convert_alpha()]
        
        player_bottom_walks =  [pygame.image.load('graphics/caracters/player/villager/walking/bottom/anim_1.png').convert_alpha(),
                                pygame.image.load('graphics/caracters/player/villager/walking/bottom/anim_2.png').convert_alpha(),
                                pygame.image.load('graphics/caracters/player/villager/walking/bottom/anim_3.png').convert_alpha(),
                                pygame.image.load('graphics/caracters/player/villager/walking/bottom/anim_4.png').convert_alpha(),
                                pygame.image.load('graphics/caracters/player/villager/walking/bottom/anim_5.png').convert_alpha(),
                                pygame.image.load('graphics/caracters/player/villager/walking/bottom/anim_6.png').convert_alpha(),
                                pygame.image.load('graphics/caracters/player/villager/walking/bottom/anim_7.png').convert_alpha(),
                                pygame.image.load('graphics/caracters/player/villager/walking/bottom/anim_8.png').convert_alpha(),
                                pygame.image.load('graphics/caracters/player/villager/walking/bottom/anim_9.png').convert_alpha()]
        
        player_left_walks = [pygame.image.load('graphics/caracters/player/villager/walking/left/anim_1.png').convert_alpha(),
                             pygame.image.load('graphics/caracters/player/villager/walking/left/anim_2.png').convert_alpha(),
                             pygame.image.load('graphics/caracters/player/villager/walking/left/anim_3.png').convert_alpha(),
                             pygame.image.load('graphics/caracters/player/villager/walking/left/anim_4.png').convert_alpha()]
    
        player_top_walks = [pygame.image.load('graphics/caracters/player/villager/walking/top/anim_1.png').convert_alpha(),
                            pygame.image.load('graphics/caracters/player/villager/walking/top/anim_2.png').convert_alpha(),
                            pygame.image.load('graphics/caracters/player/villager/walking/top/anim_3.png').convert_alpha(),
                            pygame.image.load('graphics/caracters/player/villager/walking/top/anim_4.png').convert_alpha()]
        
        player_right_walks = [pygame.image.load('graphics/caracters/player/villager/walking/right/anim_1.png').convert_alpha(),
                              pygame.image.load('graphics/caracters/player/villager/walking/right/anim_2.png').convert_alpha(),
                              pygame.image.load('graphics/caracters/player/villager/walking/right/anim_3.png').convert_alpha(),
                              pygame.image.load('graphics/caracters/player/villager/walking/right/anim_4.png').convert_alpha()]
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
        self.image = self.transform_scale()
        
        #Position
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
            self.image = self.transform_scale()
    
    def debug(self):
        self.image.fill('#00ff00')
        
    def update(self, dt):
        self.old_rect = self.rect.copy()
        self.apply_collisions(dt)
        self.input()
        self.animation_state()
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()



class Warrior(Player):
    type = "Warrior"
    
    # def compute_damages(self, roll, target):
    #     print("Bonus : Axe in your face ! (+3 damages)")
    #     return super().compute_damages(roll, target) + 3
    
    def transform(self):
        """Transformer le player en warrior"""
        pass


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