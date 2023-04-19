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
Demon("Gargantua", (400, 500), [sprites.camera_groups["Dungeon"], sprites.ennemi_group])
Demon("Gargantua", (400, 500), [sprites.camera_groups["Dungeon"], sprites.ennemi_group])
Demon("Gargantua", (400, 500), [sprites.camera_groups["Dungeon"], sprites.ennemi_group])
Demon("Gargantua", (400, 500), [sprites.camera_groups["Dungeon"], sprites.ennemi_group])
Demon("Gargantua", (400, 500), [sprites.camera_groups["Dungeon"], sprites.ennemi_group])

# Saves
menu = Menu()
sprites.player = menu.run()
player = sprites.player
save_data = SaveData("save.json")
last_save_time = pygame.time.get_ticks()
inventaire = Inventaire()

dead_ennemies = sprites.mob_dead
print(dead_ennemies)
for name_ennemy in dead_ennemies:
    print(name_ennemy)

# TODO: Charge la liste des items depuis un fichier tileds avec des Waypoints
piece1 = Item('Piece', sprites.camera_group.carte.get_waypoint('SpawnItems'), [sprites.camera_group, sprites.items_sprites])
items = [piece1]
# Type camera
sprites.camera_group.set_type_camera("center")

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
                    name_dest = tp.name_destination
                    sprites.camera_group = sprites.camera_groups[name_dest]
                    # print(f"Nom de la map : {camera_group.carte.map_name}")
                    # print(f"Nom de la destination : {tp.name_destination}, nom du waypoint de destination : {tp.name_tp_back}")
                    # print(f'La position de la teleportation : {tp.pos} et du joueur : {player.get_pos()}')
                    player.set_pos(sprites.camera_groups[name_dest].carte.get_waypoint(tp.name_tp_back))
            if event.key == pygame.K_a and player.rect.colliderect(piece1.rect):
                piece1.remove_object(piece1)

    #Test
            # if player.HP < 0:
            #     sprites.camera_group.carte.game_over()
            #     if event.key == pygame.K_e:
            #         player.set_HP == player.max_HP
            #         player.set_pos(sprites.camera_group.carte.get_waypoint('Spawn'))

    dungeon_bg = ['Dungeon']
    overworld_bg = ['Overworld', 'Swamp', 'Waterfall']
    if sprites.camera_group.carte.map_name in dungeon_bg:
        screen.fill('#1f1f1f') #Map Dungeon
    elif sprites.camera_group.carte.map_name in overworld_bg:
        screen.fill('#71ddee') #Map overworld

    sprites.camera_group.update(dt)
    sprites.camera_group.custom_draw(player)

    # Permettre de debuger les sprites
    sprites.camera_group.debug()

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
