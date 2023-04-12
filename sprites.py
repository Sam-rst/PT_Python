import pygame
from projectiles import Projectile

all_sprites = pygame.sprite.Group()
collision_sprites = pygame.sprite.Group()
projectile_sprites = pygame.sprite.Group()
collision_sprites = pygame.sprite.Group()
player_sprite = pygame.sprite.GroupSingle()
all_sprites.add(projectile_sprites)
