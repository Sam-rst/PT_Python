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
# spawn_pos = carte.get_waypoint('Spawn')

# player = Player("Etienne", 20, 8, 3, spawn_pos, collision_sprites, camera_group)
player = Player("Etienne", 20, 8, 10, 3, (500, 500), [player_sprite, camera_group])
print(player)
# Création des sprites
# carte.create_obstacles('Obstacles', [collision_sprites, camera_group])
# carte.create_obstacles('Obstacles', collision_sprites)
ennemi = Ennemy("Gargantua", 100, 10, 200, 10, (400, 500), [camera_group, ennemi_group])
# ennemi1 = Ennemy("Etienne", 100, 10, 10, (800, 400), collision_sprites, [camera_group, ennemi_group])

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

    pygame.display.update()
    clock.tick(60)

pygame.quit()