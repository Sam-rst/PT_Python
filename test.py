import pygame, sys, pytmx
from pytmx.util_pygame import load_pygame

pygame.init()

# Chargez les images pour chaque animation
animation_droite = [pygame.image.load("graphics/player/droite.png")]
animation_gauche = [pygame.image.load("graphics/player/gauche.png")]
animation_haut = [pygame.image.load("graphics/player/haut.png")]
animation_bas = [pygame.image.load("graphics/player/bas.png"), pygame.image.load("graphics/player/bas2.png"), pygame.image.load("graphics/player/bas3.png"), pygame.image.load("graphics/player/bas4.png")]


screen = pygame.display.set_mode((800, 600))

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
    if object_layer.name == 'Obstacles':
        print("That's good !")
        for obj in object_layer:
            print(obj)
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

while True:
    dt = clock.tick(60) / 1000.0
    
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
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_UP]:
        player_pos[1] -= player_speed * dt
        direction = 'haut'
        is_moving = True
    elif keys[pygame.K_DOWN]:
        player_pos[1] += player_speed * dt
        direction = 'bas'
        is_moving = True
    if keys[pygame.K_LEFT]:
        player_pos[0] -= player_speed * dt
        direction = 'gauche'
        is_moving = True
    elif keys[pygame.K_RIGHT]:
        player_pos[0] += player_speed * dt
        direction = 'droite'
        is_moving = True
    
    if is_moving == False:
        compteur_animation = 0   # Réinitialisez le compteur d'animation à zéro si le joueur ne bouge pas
        
    # Déterminez quelle animation du personnage doit être affichée en fonction de la direction de déplacement
    if direction == "droite":
        animation = animation_droite
    elif direction == "gauche":
        animation = animation_gauche
    elif direction == "haut":
        animation = animation_haut
    elif direction == "bas":
        animation = animation_bas
    
    # Incrémentez le compteur d'animation pour passer à l'image suivante
    compteur_animation += dt / temps_animation

    if compteur_animation >= len(animation):
        compteur_animation = 0
    
    # Mettez à jour l'écran de jeu
    pygame.display.update()
    
    # calculer les coordonnées de la caméra pour centrer sur le joueur
    cam_x = player_pos[0] - (screen.get_width() / 2)
    cam_y = player_pos[1] - (screen.get_height() / 2)
    # limiter les coordonnées de la caméra pour ne pas sortir de la carte
    cam_x = max(0, min(cam_x, tmxdata.width * tmxdata.tilewidth - screen.get_width()))
    cam_y = max(0, min(cam_y, tmxdata.height * tmxdata.tileheight - screen.get_height()))
    
    # dessiner les tuiles de la carte à partir des coordonnées de la caméra
    screen.fill((0, 0, 0))
    for layer in layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            # Dessiner la couche de tuiles
            for x, y, image in layer.tiles():
                screen.blit(image, (x * tmxdata.tilewidth - cam_x, y * tmxdata.tileheight - cam_y))
        # elif isinstance(layer, pytmx.TiledObjectGroup):
        #     # Dessiner les objets de la couche
        #     for obj in layer.objects():
        #         print(obj.name, obj.x, obj.y, obj.width, obj.height)

    
    # dessiner le joueur par rapport aux coordonnées de la caméra
    screen.blit(animation[int(compteur_animation)], (player_pos[0] - cam_x, player_pos[1] - cam_y))
# ..
