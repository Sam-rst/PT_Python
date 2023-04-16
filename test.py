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
change_map('Dungeon')



# player = Player("Etienne", 20, 8, 3, spawn_pos, collision_sprites, camera_group)
player = Player("Etienne", 20, 8, 10, 3, (500, 500), [player_sprite, camera_group])
player.set_pos(carte.get_waypoint('Spawn'))
print(player.get_pos())
# Création des sprites
e1 = Ennemy("Gargantua", 100, 10, 200, 10, (400, 500), [camera_group, ennemi_group])
e2 = Ennemy("Gargantua", 100, 10, 200, 10, (400, 500), [camera_group, ennemi_group])
e3 = Ennemy("Gargantua", 100, 10, 200, 10, (400, 500), [camera_group, ennemi_group])
e4 = Ennemy("Gargantua", 100, 10, 200, 10, (400, 500), [camera_group, ennemi_group])
e5 = Ennemy("Gargantua", 100, 10, 200, 10, (400, 500), [camera_group, ennemi_group])
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
                pass
                
    
    screen.fill('#71ddee')
    carte.get_door('ExitDungeon')
    camera_group.update(dt)
    camera_group.custom_draw(player, 'box')
    camera_group.debug()
    # player.debug()
    # e1.debug()
    # e2.debug()
    # e3.debug()
    # e4.debug()
    # e5.debug()

    pygame.display.update()
    clock.tick(60)

pygame.quit()