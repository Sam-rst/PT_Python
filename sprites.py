import pygame
from camera import CameraGroup
from carte import Carte

all_sprites = pygame.sprite.Group()

collision_sprites = pygame.sprite.Group()

projectile_sprites = pygame.sprite.Group()

ennemi_projectiles = pygame.sprite.Group()

ennemi_group = pygame.sprite.Group()

collision_sprites = pygame.sprite.Group()

player_sprite = pygame.sprite.GroupSingle()

all_sprites.add(projectile_sprites)

# camera_group = CameraGroup()
