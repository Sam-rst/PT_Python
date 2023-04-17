import pygame, sys, time
from settings import *
from sprites import *
from debug import debug
from carte import Carte
from player import *
from ennemy import *
from save import *
from inventaire import *
from menu import Menu

# def retreive_data(caracter):

# Initialisation de pygame
pygame.init()

clock = pygame.time.Clock()


# Création des sprites
e1 = Ennemy("Gargantua", 100, 10, 200, 10, (400, 500), [camera_groups["Dungeon"], ennemi_group])
e2 = Ennemy("Gargantua", 100, 10, 200, 10, (400, 500), [camera_groups["Dungeon"], ennemi_group])
e3 = Ennemy("Gargantua", 100, 10, 200, 10, (400, 500), [camera_groups["Dungeon"], ennemi_group])
e4 = Ennemy("Gargantua", 100, 10, 200, 10, (400, 500), [camera_groups["Dungeon"], ennemi_group])
e5 = Ennemy("Gargantua", 100, 10, 200, 10, (400, 500), [camera_groups["Dungeon"], ennemi_group])

# Saves
menu = Menu()
player = menu.run()
print('test1')
save_data = SaveData("save.json")
frame_counter = 0
last_save_time = pygame.time.get_ticks()

player_class = save_data.load_player_class()
        # Charger les données sauvegardées pour initialiser la position du joueur
player_data = save_data.load_player_data()
if player_data is not None:
    position_data = player_data.get("player_position") # accéder au dictionnaire de position du joueur
    if position_data is not None:
        player.set_pos((position_data["x"], position_data["y"]))
else:
    player.set_pos(camera_group.carte.get_waypoint('Spawn'))

#  self.reset_menu = ResetMenu(self.screen.get_width(), self.screen.get_height())
 
inventaire = Inventaire()


print('test2')
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

            for tp in camera_group.tps:
                if event.key == pygame.K_e and player.rect.colliderect(tp):
                    camera_group = camera_groups[tp.name_destination]
                    player.set_pos(camera_group.carte.get_waypoint("Spawn"))
                # print('Test en cours')
                # change_map(teleportation.name_destination)
                # print('Test réussi')

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
