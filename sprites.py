import pygame
from camera import CameraGroup
from save import SaveData



all_sprites = pygame.sprite.Group()

projectile_sprites = pygame.sprite.Group()

ennemi_projectiles = pygame.sprite.Group()

ennemi_group = pygame.sprite.Group()

collision_sprites = pygame.sprite.Group()

player_sprite = pygame.sprite.GroupSingle()

items_sprites = pygame.sprite.Group()

camera_groups = {
    "Dungeon": CameraGroup(name_map='Dungeon', list_teleporters=[('DungeonExit', 'Overworld', 'DungeonExit')], list_layers_obstacles=['Buildings', 'Mountains']),
    "Overworld": CameraGroup(name_map='Overworld', list_teleporters=[('DungeonEntrance', 'Dungeon', 'DungeonEntrance')], list_layers_obstacles=['Buildings', 'Rivers', 'Moutains', 'DecorationObstacles'])
    # "Swamp": CameraGroup(name_map='Swamp', list_teleporters=[('OverworldEntrance', 'Overworld', '')])
}

save_data = SaveData('save.json')
map_name = save_data.load_player_map()
if map_name is None:
    camera_group = camera_groups["Overworld"]
else:
    camera_group = camera_groups[map_name]