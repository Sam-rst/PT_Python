import pygame
from camera import CameraGroup
from save import SaveData



all_sprites = pygame.sprite.Group()

projectile_sprites = pygame.sprite.Group()

ennemi_projectiles = pygame.sprite.Group()

items_drop = pygame.sprite.Group()

ennemi_group = pygame.sprite.Group()
demons_group = pygame.sprite.Group()
goblins_group = pygame.sprite.Group()
skeletons_group = pygame.sprite.Group()
zombies_group = pygame.sprite.Group()

player_sprite = pygame.sprite.GroupSingle()
player = None

items_sprites = pygame.sprite.Group()

dungeon_collisions = pygame.sprite.Group()
overworld_collisions = pygame.sprite.Group()
waterfalls_collisions = pygame.sprite.Group()
swamp_collisions = pygame.sprite.Group()
watertemple_collisions = pygame.sprite.Group()
castle_collisions = pygame.sprite.Group()
camera_groups = {
    "Dungeon": CameraGroup(name_map='Dungeon', list_teleporters=[('ExitDungeon', 'Overworld', 'DungeonExit')], layers_obstacles=(['Collisions'], dungeon_collisions)),
    "Overworld": CameraGroup(name_map='Overworld', list_teleporters=[('DungeonEntrance', 'Dungeon', 'DungeonEntrance'), ('SwampEntrance', 'Swamp', 'OverworldExit')], layers_obstacles=(['Collisions'], overworld_collisions)),
    "Waterfall" : CameraGroup(name_map='Waterfall', list_teleporters=[('SwampEntrance', 'Swamp', 'WaterfallExit'), ('WatertempleEntrance', 'Watertemple', 'WatertempleEntrance'), ('CastleEntrance', 'Castle', 'CastleEntrance')], layers_obstacles=(['Collisions'], waterfalls_collisions)),
    "Swamp": CameraGroup(name_map='Swamp', list_teleporters=[('OverworldEntrance', 'Overworld', 'SwampExit'), ('EntranceWaterfall', 'Waterfall', 'WaterfallEntrance')], layers_obstacles=(['Collisions'], swamp_collisions)),
    "Watertemple" : CameraGroup(name_map='Watertemple', list_teleporters=[('WatertempleExit', 'Waterfall', 'WatertempleExit')], layers_obstacles=(['Collisions'], watertemple_collisions)),
    "Castle" : CameraGroup(name_map='Castle', list_teleporters=[('CastleEntrance', 'Castle', 'CastleEntrance'), ('WaterfallEntrance', 'Waterfall', 'CastleExit')], layers_obstacles=(['Collisions'], castle_collisions))
}
# Water Fall ;)

save_data = SaveData('save.json')
map_name = save_data.load_player_map()
mob_dead = save_data.load_mob_dead()

if map_name is None:
    camera_group = camera_groups["Overworld"]
else:
    camera_group = camera_groups[map_name]