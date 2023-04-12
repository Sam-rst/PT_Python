import pygame, sys, pytmx, time
from carte import Carte
from caracter import Player
from obstacle import Obstacle
from debug import debug
from save import SaveData
from inventaire import Inventaire
from menu import Menu
from dice import Dice

# Initialisation de pygame
pygame.init()
resolution = (800, 600)
screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()

# Création de la map
carte = Carte(screen, 'map_Overworld')
# Création des sprites
all_sprites = pygame.sprite.Group()
collision_sprites = pygame.sprite.Group()

carte.create_obstacles('Obstacles', [all_sprites, collision_sprites])
pos_spawn = carte.get_waypoint('Spawn')

# Récupération des données sauvegardées dans le fichier JSON
player = Player(screen, all_sprites, collision_sprites)
all_sprites.add(player)

save_data = SaveData('save.json')
removed_objects = save_data.load_removed_objects()
items = save_data.load_inventory()
inventaire = Inventaire()
# menu = Menu()
# menu_ouvert = False
player_data = save_data.load_player_data()
if player_data is not None:
    position_data = player_data.get("player_position")
    if position_data is not None:
        new_pos = (position_data['x'], position_data['y'])
        player.change_pos(new_pos)
else:
    # player.change_pos(pos_spawn)
    pass

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

    carte.update(player.pos)
    player.update(dt, resolution)
    collision_sprites.update()

    pygame.display.update()
    clock.tick(60)