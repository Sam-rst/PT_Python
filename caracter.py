import pygame, settings
from dice import Dice, RiggedDice
from rich import print
from math import sqrt 
from weapon import Weapon
from debug import debug



    
class Caracter(pygame.sprite.Sprite):
    type = "caracter"

    def __init__(self, name, max_health, attack, defense, weapon, dice):
        self.name = name
        self.max_health = max_health
        self.health = self.max_health
        self.attack_value = attack
        self.defense_value = defense
        self.weapon = weapon
        self.dice = dice

    def __str__(self):
        return f"I'm {self.name}, a {type(self).type} with {self.max_health}hp ({self.attack_value} atk / {self.defense_value} def)"

    def regenerate(self):
        self.health = self.max_health
    
    def decrease_health(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0

    def show_health(self):
        missing_health = self.max_health - self.health
        health_bar = f"{self.name} healthbar : [{'●'*self.health}{'○'*missing_health}] {self.health}/{self.max_health}hp"
        print(health_bar)

    def get_type(self):
        return type(self).type

    def get_defense(self):
        return self.defense_value
    
    def get_name(self):
        return self.name

    def compute_damages(self, roll, target):
        damages = roll + self.attack_value
        return damages

    def attack(self, target):
        if self.is_alive():
            if self.distance(target) > self.weapon.weapon_range():
                    print("La cible est hors de portée²")
            roll = self.dice.roll()
            distance  = self.distance_to(target)
            damages = self.compute_damages(roll, target)
            print(
                f"⚔️ {self.get_type()} [red]{self.name}[/red] attack with {damages} damages (attack: {self.attack_value} + roll: {roll})")
            target.defend(damages)

    def compute_defense(self, roll, damages):
        return damages - roll - self.defense_value

    def defend(self, damages):

        roll = self.dice.roll()
        wounds = self.compute_defense(roll, damages)
        print(f"🛡️ {self.get_type()} [blue]{self.name}[/blue] defend against {damages} damages and take {wounds} wounds ({damages} damages - defense {self.defense_value} - roll {roll})")
        self.decrease_health(wounds)
        self.show_health()

    def distance(self, target):
        x_distance = abs(self.x - target.x)
        y_distance = abs(self.y - target.y)
        return sqrt(x_distance**2 + y_distance**2)

    def switch_weapon(self, new_weapon):
        print(f"Tu a trouvés {new_weapon.name} !")
        print(f"Veux tu remplacer ta/ton {self.weapon.name} par celle-ci ? ")

        reponse = input("Remplacer ? o/n ")

        while reponse != "o" and reponse != "n":
            print("Erreur, écrivez o/n")
            reponse = input("Remplacer ? o/n ")

        if reponse == "o":
            self.weapon = new_weapon
            print(f"Tu possèdes désormais {self.weapon.name}")
        elif reponse == "n":
            print(f"Tu choisis de garder {self.weapon.name}")

class Player(pygame.sprite.Sprite):
    
    def __init__(self, screen, groups, obstacles):
        super().__init__(groups)
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
        self.screen = screen
        
        #Position
        self.rect = self.image.get_rect(midbottom = (400, 300))
        self.old_rect = self.rect.copy()
        
        #Movement
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2()
        self.speed = 200
        self.is_moving = False
        self.obstacles = obstacles
        
    def input(self):
        keys = pygame.key.get_pressed()
        
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
    
    def animation_state(self):
        if self.is_moving:
            self.animation_index += self.animation_speed
            if self.animation_index >= len(self.frames[self.animation_direction]):
                self.animation_index = 0
            self.image = self.frames[self.animation_direction][int(self.animation_index)]
            debug(self.animation_index)
        
    def apply_collisions(self, dt, resolution):
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.x = round(self.pos.x)
        self.collision('horizontal')
        self.window_collision('horizontal', resolution)
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.y = round(self.pos.y)
        self.collision('vertical')
        self.window_collision('vertical', resolution)
        
    def draw(self):
        self.screen.blit(self.image, self.rect)
        
    def update(self, dt, resolution):
        self.old_rect = self.rect.copy()
        self.apply_collisions(dt, resolution)
        self.input()
        self.animation_state()
        # print(self.pos)
        self.draw()
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        




        
class Warrior(Player):
    type = "Warrior"
    
    def compute_damages(self, roll, target):
        print("Bonus : Axe in your face ! (+3 damages)")
        return super().compute_damages(roll, target) + 3


class Mage(Player):
    type = "Mage"

    def compute_defense(self, roll, damages):
        print("Bonus : Magic armor ! (-3 wournds)")
        return super().compute_defense(roll, damages) - 3


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