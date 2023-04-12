import pygame, sys, pytmx, time
from carte import Carte
from obstacle import Obstacle
from caracter import Player
from debug import debug
from save import SaveData
from inventaire import Inventaire
from menu import Menu
from dice import Dice
from sprites import *
from settings import *

# Initialisation de pygame
pygame.init()
screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()

# Création de la map
carte = Carte(screen, 'map_Overworld')

player = Player("Etienne", 20, 8, 3, collision_sprites)
all_sprites.add(player)
player_sprite.add(player)

print(player)
player.level_up()
print(player)
# Création des sprites
carte.create_obstacles('Obstacles', collision_sprites)

# save_data = SaveData('save.json')
# removed_objects = save_data.load_removed_objects()
# items = save_data.load_inventory()
# inventaire = Inventaire()
# # menu = Menu()
# # menu_ouvert = False
# player_data = save_data.load_player_data()
# if player_data is not None:
#     position_data = player_data.get("player_position")
#     if position_data is not None:
#         new_pos = (position_data['x'], position_data['y'])
#         player.change_pos(new_pos)
# else:
#     # player.change_pos(pos_spawn)
#     pass
back_buffer = pygame.Surface(resolution)

last_time = time.time()
while True:
    dt = time.time() - last_time
    last_time = time.time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                # menu.run()
                print("Menu ouvert")
                
            if event.key == pygame.K_e:
                obj_pos, pickup_distance = carte.get_pickup_distance('Items')
                player_x, player_y = player.get_position()
                print("Objet pris")

    screen.blit(carte.image, (0, 0))
    # all_sprites.update(dt)
    # all_sprites.draw(screen)
    player_sprite.update(dt)
    player_sprite.draw(screen)
    projectile_sprites.update()
    projectile_sprites.draw(screen)
    # collision_sprites.draw(screen)
    
    pygame.display.flip()
    clock.tick(144)

pygame.quit()