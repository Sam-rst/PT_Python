import pygame, sys, pytmx, time
from pytmx.util_pygame import load_pygame
from carte import Carte
from caracter import Player
from obstacle import Obstacle

pygame.init()

resolution = (800, 600)
screen = pygame.display.set_mode(resolution)

tmxdata = load_pygame('graphics/Tiled/data/tmx/map_Overworld.tmx')

x = 400
y = 300

player_pos = [400, 300]
player_speed = 100

direction = 'droite'

layers = tmxdata.layers
# print(layers)
# for layer in tmxdata.visible_layers:
#     print(layer)

# layernames = tmxdata.layernames
# print(layernames['Waypoints'])
# print(tmxdata.get_layer_by_name('Waypoints'))



for object_layer in tmxdata.objectgroups:
    if object_layer.name == 'Waypoints':
        print("c bon")
        for obj in object_layer:
            if obj.name == 'Spawn':
                obj_coord = (int(obj.x), int(obj.y))
                print(obj_coord)

                

            
# for obj in tmxdata.objects:
#     if obj.name == 'BorderMoutain1':
#         moutain_surf = obj.image
#         print(moutain_surf)
        # moutain_rect = moutain_surf.get_rect()

clock = pygame.time.Clock()

compteur_animation = 0  

temps_animation = 1/15

is_moving = False

zoom_level = 1 # variable de zoom, initialisé à 1 (pas de zoom)

carte = Carte(screen, 'map_Overworld')
carte.remove_object('Piece')

all_sprites = pygame.sprite.Group()
collision_sprites = pygame.sprite.Group()

for object_layer in tmxdata.objectgroups:
    if object_layer.name == 'Obstacles':
        for obj in object_layer:
            obstacle = Obstacle(screen, collision_object = obj, groups = [all_sprites, collision_sprites])

player = Player(screen, all_sprites, collision_sprites)

last_time = time.time()
while True:
    dt = time.time() - last_time
    last_time = time.time()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                is_moving = False
            elif event.key == pygame.K_PLUS: # Touche "+" pour augmenter le zoom
                zoom_level += 1
            elif event.key == pygame.K_MINUS: # Touche "-" pour diminuer le zoom
                zoom_level = max(1, zoom_level-1) # zoom minimum est 1 (pas de zoom)
    
    # keys = pygame.key.get_pressed()
    
    # if keys[pygame.K_UP]:
    #     player_pos[1] -= player_speed * dt
    #     direction = 'haut'
    #     is_moving = True
    # elif keys[pygame.K_DOWN]:
    #     player_pos[1] += player_speed * dt
    #     direction = 'bas'
    #     is_moving = True
    # if keys[pygame.K_LEFT]:
    #     player_pos[0] -= player_speed * dt
    #     direction = 'gauche'
    #     is_moving = True
    # elif keys[pygame.K_RIGHT]:
    #     player_pos[0] += player_speed * dt
    #     direction = 'droite'
    #     is_moving = True
    
    # if is_moving == False:
    #     compteur_animation = 0   # Réinitialisez le compteur d'animation à zéro si le joueur ne bouge pas
        
    # Déterminez quelle animation du personnage doit être affichée en fonction de la direction de déplacement
    # if direction == "droite":
    #     animation = animation_droite
    # elif direction == "gauche":
    #     animation = animation_gauche
    # elif direction == "haut":
    #     animation = animation_haut
    # elif direction == "bas":
    #     animation = animation_bas
    
    # Incrémentez le compteur d'animation pour passer à l'image suivante
    # compteur_animation += dt / temps_animation

    # if compteur_animation >= len(animation):
    #     compteur_animation = 0
    
    # Mettez à jour l'écran de jeu
    
    # calculer les coordonnées de la caméra pour centrer sur le joueur
    # cam_x = player_pos[0] - (screen.get_width() / 2)
    # cam_y = player_pos[1] - (screen.get_height() / 2)
    # cam_coord = carte.calculate_cam(player_pos)
    # limiter les coordonnées de la caméra pour ne pas sortir de la carte
    # cam_x = max(0, min(cam_x, tmxdata.width * tmxdata.tilewidth - screen.get_width()))
    # cam_y = max(0, min(cam_y, tmxdata.height * tmxdata.tileheight - screen.get_height()))
    
    # dessiner les tuiles de la carte à partir des coordonnées de la caméra
    # carte.draw(cam_coord)
    # screen.fill((0, 0, 0))
    # for layer in layers:
    #     if isinstance(layer, pytmx.TiledTileLayer):
    #         # Dessiner la couche de tuiles
    #         for x, y, image in layer.tiles():
    #             screen.blit(image, (x * tmxdata.tilewidth - cam_x, y * tmxdata.tileheight - cam_y))
        # elif isinstance(layer, pytmx.TiledObjectGroup):
        #     # Dessiner les objets de la couche
        #     for obj in layer.objects():
        #         print(obj.name, obj.x, obj.y, obj.width, obj.height)

    # dessiner le joueur par rapport aux coordonnées de la caméra
    # screen.blit(animation[int(compteur_animation)], (player_pos[0] - cam_coord[0], player_pos[1] - cam_coord[1]))
    # screen.blit(animation[int(compteur_animation)], (player_pos[0] - cam_x, player_pos[1] - cam_y))
    
    # all_sprites.update(dt, resolution)
    carte.update(player.pos)
    player.update(dt, resolution)
    # collision_sprites.draw()
    
    pygame.display.update()
    clock.tick(60)