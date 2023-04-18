import pygame
from camera import CameraGroup
from carte import Carte
from save import SaveData



all_sprites = pygame.sprite.Group()

collision_sprites = pygame.sprite.Group()

projectile_sprites = pygame.sprite.Group()

ennemi_projectiles = pygame.sprite.Group()

ennemi_group = pygame.sprite.Group()

collision_sprites = pygame.sprite.Group()

player_sprite = pygame.sprite.GroupSingle()

all_sprites.add(projectile_sprites)


camera_groups = {
    "Dungeon": CameraGroup(Carte('Dungeon'), [('ExitDungeon', 'Overworld', 'DungeonExit')]),
    "Overworld": CameraGroup(Carte('Overworld'), [('EnterDungeon', 'Dungeon', 'DungeonEntrance')]),
}

save_data = SaveData('save.json')
map_name = save_data.load_player_map()
if map_name is None:
    camera_group = camera_groups["Overworld"]
else:
    camera_group = camera_groups[map_name]