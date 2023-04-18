import pygame, sys, time, math
from settings import *
import sprites
from debug import debug
from carte import Carte
from player import *
from ennemy import *
from save import *
from inventaire import *
from menu import Menu
from items import Item

pygame.init()

clock = pygame.time.Clock()

# Création des sprites
e1 = Ennemy("Gargantua", (400, 500), [sprites.camera_groups["Dungeon"], sprites.ennemi_group])
e2 = Ennemy("Gargantua", (400, 500), [sprites.camera_groups["Dungeon"], sprites.ennemi_group])
e3 = Ennemy("Gargantua", (400, 500), [sprites.camera_groups["Dungeon"], sprites.ennemi_group])
e4 = Ennemy("Gargantua", (400, 500), [sprites.camera_groups["Dungeon"], sprites.ennemi_group])
e5 = Ennemy("Gargantua", (400, 500), [sprites.camera_groups["Dungeon"], sprites.ennemi_group])

# Saves
menu = Menu()
player = menu.run()
save_data = SaveData("save.json")
last_save_time = pygame.time.get_ticks()
inventaire = Inventaire()

# TODO: Charge la liste des items depuis un fichier tileds avec des Waypoints
piece1 = Item('Piece', sprites.camera_group.carte.get_waypoint('Spawn'), [sprites.camera_group, sprites.items_sprites])
items = [piece1]



# Type camera
sprites.camera_group.set_type_camera("box")

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

            for tp in sprites.camera_group.teleporters:
                if event.key == pygame.K_e and player.rect.colliderect(tp.rect):
                    sprites.camera_group = sprites.camera_groups[tp.name_destination]
                    # print(f"Nom de la map : {camera_group.carte.map_name}")
                    # print(f"Nom de la destination : {tp.name_destination}, nom du waypoint de destination : {tp.name_tp_back}")
                    player.set_pos(sprites.camera_group.carte.get_waypoint(tp.name_tp_back))
            if event.key == pygame.K_a and player.rect.colliderect(piece1.rect):
                piece1.remove_object(piece1)

    screen.fill('#71ddee') #Map overworld
    # screen.fill('#1f1f1f') #Map Dungeon
    # carte.get_door('ExitDungeon')
    sprites.camera_group.update(dt)
    sprites.camera_group.custom_draw(player)

    # Permettre de debuger les sprites
    # sprites.camera_group.debug()

    # Sauvegarde la position du joueur toutes les 5 secondes
    current_time = pygame.time.get_ticks()
    if current_time - last_save_time > 5000:
        player_position = {"x": player.pos.x, "y": player.pos.y}
        player_map = sprites.camera_group.carte.map_name
        save_data.save_player_map(player_map)
        save_data.save_player_position(player_position)
        last_save_time = current_time

    pygame.display.update()
    clock.tick(60)

pygame.quit()
