import pygame
import random
import math , sys

# Initialisation de Pygame
pygame.init()

# Définition de la taille de la fenêtre
WINDOW_SIZE = (800, 600)

# Création de la fenêtre
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Jeu de tir")

# Définition des couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


class Joueur(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2)
        self.cooldown = 150  # temps de recharge en millisecondes
        self.last_shot = 0   # temps en millisecondes depuis le début de l'exécution de la boucle de jeu lors du dernier tir
        self.speed = 5
        self.max_hp = 20
        self.hp = self.max_hp
    def afficher_game_over(self):
        font = pygame.font.Font(None, 64)
        text = font.render("Game Over", True, WHITE)
        text_rect = text.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2))
        screen.blit(text, text_rect)
        pygame.display.flip()
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            self.rect.move_ip(-self.speed, 0)
        if keys[pygame.K_d]:
            self.rect.move_ip(self.speed, 0)
        if keys[pygame.K_z]:
            self.rect.move_ip(0, -self.speed)
        if keys[pygame.K_s]:
            self.rect.move_ip(0, self.speed)

        # Contraindre le joueur à rester dans l'écran
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > WINDOW_SIZE[0]:
            self.rect.right = WINDOW_SIZE[0]
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > WINDOW_SIZE[1]:
            self.rect.bottom = WINDOW_SIZE[1]
        
        if pygame.sprite.spritecollide(self, ennemi_projectiles, True):
            print(self.hp)
            self.hp -= 10

        while self.hp <= 0:
            for event in pygame.event.get():
                self.afficher_game_over()
                print("vous êtes nul, vous êtes mort")
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
            keys = pygame.key.get_pressed()
            if keys[pygame.K_e]:
                self.hp = self.max_hp   
                
                
                break

                
        

        # Si la touche d'espace est pressée et que le temps de recharge est écoulé
        if pygame.mouse.get_pressed()[0] and pygame.time.get_ticks() - self.last_shot > self.cooldown:
            projectile = Projectile(self.rect.center)
            projectiles.add(projectile)
            all_sprites.add(projectile)
            self.last_shot = pygame.time.get_ticks()  # on enregistre le temps du dernier tir
    
    



class BarreDeVie(pygame.sprite.Sprite):
    def __init__(self, joueur):
        super().__init__()
        self.joueur = joueur
        self.image = pygame.Surface([self.joueur.rect.width, 5])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = self.joueur.rect.center

    def update(self):
        pourcentage_vie = self.joueur.points_de_vie / self.joueur.points_de_vie_max * 100
        if pourcentage_vie >= 50:
            self.image.fill(GREEN)
        elif pourcentage_vie >= 20:
            self.image.fill(RED)
        else:
            self.image.fill(RED)

        self.rect.center = self.joueur.rect.center

class Projectile(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.speed = 10
        self.direction = self.get_direction()
        self.damage = 5
        self.max_distance = 250
        self.distance_traveled = 0

    def update(self):
        self.rect.move_ip(self.direction[0] * self.speed, self.direction[1] * self.speed)
        self.distance_traveled += self.speed
        if self.distance_traveled >= self.max_distance:
            self.kill()
        if self.rect.bottom < 0:
            self.kill()

        # Si le projectile touche le carré ennemi, le faire perdre des points de vie
        ennemi_touche = pygame.sprite.spritecollide(self, ennemi_group, False)
        if ennemi_touche:
            ennemi_touche[0].perdre_hp(self.damage)
            self.kill()


    def get_direction(self):
        # On calcule la direction du projectile en fonction de la position de la souris
        mouse_pos = pygame.mouse.get_pos()
        dx = mouse_pos[0] - self.rect.centerx
        dy = mouse_pos[1] - self.rect.centery
        distance = math.sqrt(dx ** 2 + dy ** 2)
        if distance == 0:
            return (0, -1)
        else:
            return (dx / distance, dy / distance)

class EnnemiProjectile(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.speed = 5
        self.damage = 10
        self.max_distance = 300
        self.distance_traveled = 0

    def update(self):
        self.distance_traveled += self.speed
        if self.distance_traveled >= self.max_distance:
            self.kill()

        # Calculer la direction du projectile pour qu'elle vise le joueur
        direction = self.get_direction()
        self.rect.move_ip(direction[0] * self.speed, direction[1] * self.speed)

        # # Si le projectile touche le joueur, lui faire perdre des points de vie
        # joueur_touche = pygame.sprite.spritecollide(self, joueur_group, False)
        # if joueur_touche:
        #     print("touche")
        #     joueur_touche[0].perdre_hp(self.damage)

        #     self.kill()

    def get_direction(self):
        # On calcule la direction du projectile en fonction de la position du joueur
        joueur_pos = joueur.rect.center
        dx = joueur_pos[0] - self.rect.centerx
        dy = joueur_pos[1] - self.rect.centery
        distance = math.sqrt(dx ** 2 + dy ** 2)
        if distance == 0:
            return (0, -1)
        else:
            return (dx / distance, dy / distance)



class Ennemi(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WINDOW_SIZE[0] //2, WINDOW_SIZE[1] // 4)

        self.max_hp = 20
        self.hp = self.max_hp
        self.cooldown = 2000  # temps de recharge en millisecondes
        self.last_shot = 0   # temps en millisecondes depuis le début de l'exécution de la boucle de jeu lors du dernier tir

    def update(self):
        # On met à jour la position de l'ennemi
        self.rect.move_ip(0, 2)
        if self.rect.top > WINDOW_SIZE[1]:
            self.kill()

        # Si le temps de recharge est écoulé, on tire un projectile
        if pygame.time.get_ticks() - self.last_shot > self.cooldown:
            projectile = EnnemiProjectile(self.rect.center)
            ennemi_projectiles.add(projectile)
            all_sprites.add(projectile)
            self.last_shot = pygame.time.get_ticks()  # on enregistre le temps du dernier tir


    def perdre_hp(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.kill()

all_sprites = pygame.sprite.Group()
projectiles = pygame.sprite.Group()
ennemi_group = pygame.sprite.Group()
ennemi_projectiles = pygame.sprite.Group()
joueur_group = pygame.sprite.Group()

joueur = Joueur()
all_sprites.add(joueur)


running = True
clock = pygame.time.Clock()

while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Mise à jour des sprites
    all_sprites.update()

    # Création d'un nouvel ennemi toutes les 60 frames
    if random.randint(0, 59) == 0:
        ennemi = Ennemi()
        ennemi_group.add(ennemi)
        all_sprites.add(ennemi)

    # Affichage des sprites
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

    # Limite de 60 images par seconde
    clock.tick(60)

pygame.quit()




