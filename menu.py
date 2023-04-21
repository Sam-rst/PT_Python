import pygame, sys
from dice import Dice
from save import SaveData
from player import *
from camera import *
from sprites import *

class Menu:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.save_data = SaveData('save.json')
        self.class_joueur = self.save_data.load_player_class()
        self.player_data = self.save_data.load_player_data()
        self.player_HP = self.save_data.load_player_life()
        self.map_name = self.save_data.load_player_map()
        
    def run(self):
        if self.class_joueur is None:
            largeur_bouton = 200
            bouton_guerrier = pygame.Rect((self.screen.get_width() - largeur_bouton) / 2, 300, largeur_bouton, 50)
            bouton_mage = pygame.Rect((self.screen.get_width() - largeur_bouton) / 2, 400, largeur_bouton, 50)
            bouton_assassin = pygame.Rect((self.screen.get_width() - largeur_bouton) / 2, 500, largeur_bouton, 50)
            bouton_guard = pygame.Rect((self.screen.get_width() - largeur_bouton) / 2, 600, largeur_bouton, 50)
            bouton_archer = pygame.Rect((self.screen.get_width() - largeur_bouton) / 2, 700, largeur_bouton, 50)
            bouton_tank = pygame.Rect((self.screen.get_width() - largeur_bouton) / 2, 800, largeur_bouton, 50)
            
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if bouton_guerrier.collidepoint(pygame.mouse.get_pos()):
                            player = Warrior("Ray Sist", camera_group.carte.get_waypoint('Spawn'), [player_sprite] + list(camera_groups.values()))
                            player_position = {"x": player.pos.x, "y": player.pos.y}
                            self.save_data.save_player_position(player_position)
                            self.save_data.save_player_map(camera_group.carte.map_name)
                            self.save_data.save_player_life(player.get_HP())
                            return player
                        
                        elif bouton_mage.collidepoint(pygame.mouse.get_pos()):
                            player = Mage("Ray Sist", camera_group.carte.get_waypoint('Spawn'), [player_sprite] + list(camera_groups.values()))
                            player_position = {"x": player.pos.x, "y": player.pos.y}
                            self.save_data.save_player_position(player_position)
                            self.save_data.save_player_map(camera_group.carte.map_name)
                            self.save_data.save_player_life(player.get_HP())
                            return player
                        
                        elif bouton_assassin.collidepoint(pygame.mouse.get_pos()):
                            player = Assassin("Ray Sist", camera_group.carte.get_waypoint('Spawn'), [player_sprite] + list(camera_groups.values()))
                            self.save_data.save_player_class(player)
                            player_position = {"x": player.pos.x, "y": player.pos.y}
                            self.save_data.save_player_position(player_position)
                            self.save_data.save_player_map(camera_group.carte.map_name)
                            self.save_data.save_player_life(player.get_HP())
                            return player
                        
                        elif bouton_guard.collidepoint(pygame.mouse.get_pos()):
                            player = Guard("Ray Sist", camera_group.carte.get_waypoint('Spawn'), [player_sprite] + list(camera_groups.values()))
                            player_position = {"x": player.pos.x, "y": player.pos.y}
                            self.save_data.save_player_position(player_position)
                            self.save_data.save_player_map(camera_group.carte.map_name)
                            self.save_data.save_player_life(player.get_HP())
                            return player

                        elif bouton_archer.collidepoint(pygame.mouse.get_pos()):
                            player = Archer("Ray Sist", camera_group.carte.get_waypoint('Spawn'), [player_sprite] + list(camera_groups.values()))
                            player_position = {"x": player.pos.x, "y": player.pos.y}
                            self.save_data.save_player_position(player_position)
                            self.save_data.save_player_map(camera_group.carte.map_name)
                            self.save_data.save_player_life(player.get_HP())
                            return player
                        
                        elif bouton_tank.collidepoint(pygame.mouse.get_pos()):
                            player = Tank("Ray Sist", camera_group.carte.get_waypoint('Spawn'), [player_sprite] + list(camera_groups.values()))
                            player_position = {"x": player.pos.x, "y": player.pos.y}
                            self.save_data.save_player_position(player_position)
                            self.save_data.save_player_map(camera_group.carte.map_name)
                            self.save_data.save_player_life(player.get_HP())
                            return player
                
                self.screen.fill((0, 0, 0))

                font_grand = pygame.font.Font('graphics/font/Enchanted_Land.otf', 50)
                texte_bienvenue = font_grand.render("Bienvenue dans The Quest-ionable Heroe", True, (255, 255, 255))
                texte_bienvenue2 = font_grand.render("Choisissez votre classe", True, (255, 255, 255))
                self.screen.blit(texte_bienvenue, ((self.screen.get_width() - texte_bienvenue.get_width()) / 2, 50))
                self.screen.blit(texte_bienvenue2, ((self.screen.get_width() - texte_bienvenue2.get_width()) / 2, 100))
                pygame.draw.rect(self.screen, (255, 255, 255), bouton_guerrier)
                pygame.draw.rect(self.screen, (255, 255, 255), bouton_mage)
                pygame.draw.rect(self.screen, (255, 255, 255), bouton_assassin)
                pygame.draw.rect(self.screen, (255, 255, 255), bouton_guard)
                pygame.draw.rect(self.screen, (255, 255, 255), bouton_archer)
                pygame.draw.rect(self.screen, (255, 255, 255), bouton_tank)
                pygame.draw.rect(self.screen, (0, 0, 0), bouton_guerrier, 3)
                pygame.draw.rect(self.screen, (0, 0, 0), bouton_mage, 3)
                pygame.draw.rect(self.screen, (0, 0, 0), bouton_assassin, 3)
                pygame.draw.rect(self.screen, (0, 0, 0), bouton_guard, 3)
                pygame.draw.rect(self.screen, (0, 0, 0), bouton_archer, 3)
                pygame.draw.rect(self.screen, (0, 0, 0), bouton_tank, 3)
                
                font = pygame.font.Font('graphics/font/Enchanted_Land.otf', 30)
                texte_guerrier = font.render("Guerrier", True, (0, 0, 0))
                texte_mage = font.render("Mage", True, (0, 0, 0))
                texte_assassin = font.render("Assassin", True, (0, 0, 0))
                texte_guard = font.render("Garde", True, (0, 0, 0))
                texte_archer = font.render("Archer", True, (0, 0, 0))
                texte_tank = font.render("Tank", True, (0, 0, 0))
                self.screen.blit(texte_guerrier, (bouton_guerrier.x + 10, bouton_guerrier.y + 10))
                self.screen.blit(texte_mage, (bouton_mage.x + 10, bouton_mage.y + 10))
                self.screen.blit(texte_assassin, (bouton_assassin.x + 10, bouton_assassin.y + 10))
                self.screen.blit(texte_guard, (bouton_guard.x + 10, bouton_guard.y + 10))
                self.screen.blit(texte_archer, (bouton_archer.x + 10, bouton_archer.y + 10))
                self.screen.blit(texte_tank, (bouton_tank.x + 10, bouton_tank.y + 10))
                
                pygame.display.flip()

        else:            
            if self.class_joueur['Class'] == 'Warrior':
                player = Warrior("Ray Sist", camera_group.carte.get_waypoint('Spawn'), [player_sprite] + list(camera_groups.values()))
                    
            if self.class_joueur['Class'] == 'Mage':
                # player = Mage("Test", [player_sprite] + list(camera_groups.values()))
                player = Mage("Ray Sist", camera_group.carte.get_waypoint('Spawn'), [player_sprite] + list(camera_groups.values()))
                    
            if self.class_joueur['Class'] == 'Assassin':
                player = Assassin("Ray Sist", camera_group.carte.get_waypoint('Spawn'), [player_sprite] + list(camera_groups.values()))
            
            if self.class_joueur['Class'] == 'Guard':
                player = Guard("Ray Sist", camera_group.carte.get_waypoint('Spawn'), [player_sprite] + list(camera_groups.values()))

            if self.class_joueur['Class'] == 'Archer':
                player = Archer("Ray Sist", camera_group.carte.get_waypoint('Spawn'), [player_sprite] + list(camera_groups.values()))

            if self.class_joueur['Class'] == 'Tank':
                player = Tank("Ray Sist", camera_group.carte.get_waypoint('Spawn'), [player_sprite] + list(camera_groups.values()))

            name = self.class_joueur['Name']
            player.set_name(name)
            player.set_HP(self.player_HP)
            max_HP = self.class_joueur['Max HP']
            player.set_max_HP(max_HP)
            attack_value = self.class_joueur['Attack value']
            player.set_attack_value(attack_value)
            defend_value = self.class_joueur['Defend value']
            player.set_defense_value(defend_value)
            attack_range = self.class_joueur['Attack range']
            player.set_range(attack_range)
            player_pos = self.player_data.get('player_position')
            player.set_pos((player_pos['x'], player_pos['y']))

            return player