import pygame, sys, pytmx, time
from carte import Carte
from caracter import Player
from obstacle import Obstacle

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


for object_layer in carte.tmxdata.objectgroups:
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

    carte.update(player.pos)
    player.update(dt, resolution)
    collision_sprites.update()

    pygame.display.update()
    clock.tick(60)