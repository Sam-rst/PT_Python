import pygame, sys, time
from settings import *
from sprites import *
from debug import debug
from carte import Carte
from player import *
from ennemy import *
from save import *
from inventaire import *


# Initialisation de pygame
pygame.init()

clock = pygame.time.Clock()

# Création de la map
# change_map('Dungeon')



# # player = Player("Etienne", 20, 8, 3, spawn_pos, collision_sprites, camera_group)
# player = Player("Etienne", 20, 8, 10, 3, (500, 500), [player_sprite, camera_group])
# player.set_pos(carte.get_waypoint('Spawn'))
# print(player.get_pos())
# Création des sprites
e1 = Ennemy("Gargantua", 100, 10, 200, 10, (400, 500), [camera_group, ennemi_group])
e2 = Ennemy("Gargantua", 100, 10, 200, 10, (400, 500), [camera_group, ennemi_group])
e3 = Ennemy("Gargantua", 100, 10, 200, 10, (400, 500), [camera_group, ennemi_group])
e4 = Ennemy("Gargantua", 100, 10, 200, 10, (400, 500), [camera_group, ennemi_group])
e5 = Ennemy("Gargantua", 100, 10, 200, 10, (400, 500), [camera_group, ennemi_group])
# ennemi1 = Ennemy("Etienne", 100, 10, 10, (800, 400), collision_sprites, [camera_group, ennemi_group])
save_data = SaveData("save.json")
frame_counter = 0
last_save_time = pygame.time.get_ticks()
        # Charger les données sauvegardées pour initialiser la position du joueur
player_data = save_data.load_player_data()
if player_data is not None:
    position_data = player_data.get("player_position") # accéder au dictionnaire de position du joueur
    if position_data is not None:
        player = Player("Etienne", 20, 8, 10, 3, (position_data["x"], position_data["y"]), [player_sprite, camera_group])
 # récupérer les coordonnées x et y du joueur
else:
    player = Player("Etienne", 20, 8, 10, 3, carte.get_waypoint('Spawn'), [player_sprite, camera_group])

 # self.reset_menu = ResetMenu(self.screen.get_width(), self.screen.get_height())
inventaire = Inventaire()
# menu = Menu()
menu_ouvert = False
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


    # screen.fill('#71ddee') #Map overworld
    screen.fill('#1f1f1f') #Map Dungeon
    # carte.get_door('ExitDungeon')
    camera_group.update(dt)
    camera_group.custom_draw(player, 'box')

    # Permettre de debuger les sprites
    camera_group.debug()

    # Sauvegarde la position du joueur toutes les 5 secondes
    current_time = pygame.time.get_ticks()
    if current_time - last_save_time > 5000:
        player_position = {"x": player.pos.x, "y": player.pos.y}
        save_data.save_player_position(player_position)
        last_save_time = current_time

    pygame.display.update()
    clock.tick(60)

pygame.quit()
