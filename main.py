import pygame, sys, time
from settings import *
from sprites import *
from debug import debug
from carte import Carte
from player import *
from ennemy import *

# Initialisation de pygame
pygame.init()

clock = pygame.time.Clock()

# Création de la map
OVERWORLD = Carte('map_Overworld')
TEST_MAP = Carte('Test')
camera_group = CameraGroup(OVERWORLD)
# spawn_pos = carte.get_waypoint('Spawn')

# player = Player("Etienne", 20, 8, 3, spawn_pos, collision_sprites, camera_group)
player = Player("Etienne", 20, 8, 3, (500, 500), collision_sprites, [player_sprite, camera_group])
# Création des sprites
# carte.create_obstacles('Obstacles', [collision_sprites, camera_group])
# carte.create_obstacles('Obstacles', collision_sprites)
ennemi = Ennemy("Gargantua", 100, 10, 10, (400, 500), collision_sprites, [camera_group, ennemi_group])
ennemi1 = Ennemy("Etienne", 100, 10, 10, (800, 400), collision_sprites, [camera_group, ennemi_group])

last_time = time.time()
while True:
    dt = time.time() - last_time
    last_time = time.time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                # menu.run()
                print("Menu ouvert")
                
            if event.key == pygame.K_e:
                # obj_pos, pickup_distance = carte.get_pickup_distance('Items')
                # player_x, player_y = player.get_position()
                print("Objet pris")
    
    screen.fill('#71ddee')

    camera_group.update(dt)
    camera_group.custom_draw(player, 'box')
    # player.debug()

    # ennemi.update()
    

    # ennemi_group.draw(screen)
    # ennemi_group.update()
    # ennemi_projectiles.update()
    # ennemi_projectiles.draw(screen)
    
    # projectile_sprites.update()
    # projectile_sprites.draw(screen)

    pygame.display.update()
    clock.tick(60)

pygame.quit()