import pygame, sys
from dice import Dice
from save import SaveData
from player import *
from camera import *
from sprites import *

class Menu:
    def __init__(self):
        self.fenetre = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.save_data = SaveData('save.json')
        self.class_joueur = self.save_data.load_player_class()
        self.player_data = self.save_data.load_player_data()
        self.map_name = self.save_data.load_player_map()
        
    def run(self):
        if self.class_joueur is None:
            largeur_bouton = 200
            bouton_guerrier = pygame.Rect((self.fenetre.get_width() - largeur_bouton) / 2, 100, largeur_bouton, 50)
            bouton_mage = pygame.Rect((self.fenetre.get_width() - largeur_bouton) / 2, 200, largeur_bouton, 50)
            bouton_assassin = pygame.Rect((self.fenetre.get_width() - largeur_bouton) / 2, 300, largeur_bouton, 50)
            bouton_guard = pygame.Rect((self.fenetre.get_width() - largeur_bouton) / 2, 400, largeur_bouton, 50)
            bouton_archer = pygame.Rect((self.fenetre.get_width() - largeur_bouton) / 2, 500, largeur_bouton, 50)
            bouton_tank = pygame.Rect((self.fenetre.get_width() - largeur_bouton) / 2, 600, largeur_bouton, 50)
            
            while True:
                for evenement in pygame.event.get():
                    if evenement.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif evenement.type == pygame.MOUSEBUTTONDOWN:
                        if bouton_guerrier.collidepoint(pygame.mouse.get_pos()):
                            player = Warrior("mechant", camera_group.carte.get_waypoint('Spawn'), [player_sprite] + list(camera_groups.values()))
                            self.save_data.save_player_class(player)
                            
                            return player
                        elif bouton_mage.collidepoint(pygame.mouse.get_pos()):
                            player = Mage("fdp", camera_group.carte.get_waypoint('Spawn'), [player_sprite] + list(camera_groups.values()))
                            self.save_data.save_player_class(player)
                            
                            return player
                        
                        elif bouton_assassin.collidepoint(pygame.mouse.get_pos()):
                            player = Assassin("arabe", camera_group.carte.get_waypoint('Spawn'), [player_sprite] + list(camera_groups.values()))
                            self.save_data.save_player_class(player)

                            return player
                        
                        elif bouton_guard.collidepoint(pygame.mouse.get_pos()):
                            player = Guard("Renoi", camera_group.carte.get_waypoint('Spawn'), [player_sprite] + list(camera_groups.values()))
                            self.save_data.save_player_class(player)

                            return player

                        elif bouton_archer.collidepoint(pygame.mouse.get_pos()):
                            player = Archer("FDP2", camera_group.carte.get_waypoint('Spawn'), [player_sprite] + list(camera_groups.values()))
                            self.save_data.save_player_class(player)

                            return player
                        
                        elif bouton_tank.collidepoint(pygame.mouse.get_pos()):
                            player = Tank("Aissa", camera_group.carte.get_waypoint('Spawn'), [player_sprite] + list(camera_groups.values()))
                            self.save_data.save_player_class(player)

                            return player
                
                self.fenetre.fill((0, 0, 0))
                
                pygame.draw.rect(self.fenetre, (255, 255, 255), bouton_guerrier)
                pygame.draw.rect(self.fenetre, (255, 255, 255), bouton_mage)
                pygame.draw.rect(self.fenetre, (255, 255, 255), bouton_assassin)
                pygame.draw.rect(self.fenetre, (255, 255, 255), bouton_guard)
                pygame.draw.rect(self.fenetre, (255, 255, 255), bouton_archer)
                pygame.draw.rect(self.fenetre, (255, 255, 255), bouton_tank)
                pygame.draw.rect(self.fenetre, (255, 0, 0), bouton_guerrier, 3)
                pygame.draw.rect(self.fenetre, (255, 0, 0), bouton_mage, 3)
                pygame.draw.rect(self.fenetre, (255, 0, 0), bouton_assassin, 3)
                pygame.draw.rect(self.fenetre, (255, 0, 0), bouton_guard, 3)
                pygame.draw.rect(self.fenetre, (255, 0, 0), bouton_archer, 3)
                pygame.draw.rect(self.fenetre, (255, 0, 0), bouton_tank, 3)
                
                font = pygame.font.Font(None, 30)
                texte_guerrier = font.render("Guerrier", True, (0, 0, 0))
                texte_mage = font.render("Mage", True, (0, 0, 0))
                texte_assassin = font.render("Assassin", True, (0, 0, 0))
                texte_guard = font.render("Guard", True, (0, 0, 0))
                texte_archer = font.render("Archer", True, (0, 0, 0))
                texte_tank = font.render("Tank", True, (0, 0, 0))
                self.fenetre.blit(texte_guerrier, (bouton_guerrier.x + 10, bouton_guerrier.y + 10))
                self.fenetre.blit(texte_mage, (bouton_mage.x + 10, bouton_mage.y + 10))
                self.fenetre.blit(texte_assassin, (bouton_assassin.x + 10, bouton_assassin.y + 10))
                self.fenetre.blit(texte_guard, (bouton_guard.x + 10, bouton_guard.y + 10))
                self.fenetre.blit(texte_archer, (bouton_archer.x + 10, bouton_archer.y + 10))
                self.fenetre.blit(texte_tank, (bouton_tank.x + 10, bouton_tank.y + 10))
                
                pygame.display.flip()

        else:            
            if self.class_joueur['Class'] == 'Warrior':
                player = Warrior("Test", camera_group.carte.get_waypoint('Spawn'), [player_sprite] + list(camera_groups.values()))
                    
            if self.class_joueur['Class'] == 'Mage':
                # player = Mage("Test", [player_sprite] + list(camera_groups.values()))
                player = Mage("Test", camera_group.carte.get_waypoint('Spawn'), [player_sprite] + list(camera_groups.values()))
                    
            if self.class_joueur['Class'] == 'Assassin':
                player = Assassin("Test", camera_group.carte.get_waypoint('Spawn'), [player_sprite] + list(camera_groups.values()))
            
            if self.class_joueur['Class'] == 'Guard':
                player = Guard("Test", camera_group.carte.get_waypoint('Spawn'), [player_sprite] + list(camera_groups.values()))

            if self.class_joueur['Class'] == 'Archer':
                player = Archer("Test", camera_group.carte.get_waypoint('Spawn'), [player_sprite] + list(camera_groups.values()))

            if self.class_joueur['Class'] == 'Tank':
                player = Tank("Test", camera_group.carte.get_waypoint('Spawn'), [player_sprite] + list(camera_groups.values()))

            name = self.class_joueur['Name']
            player.set_name(name)
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