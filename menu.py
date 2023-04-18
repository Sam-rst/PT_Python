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
                            
                            return
                
                self.fenetre.fill((0, 0, 0))
                
                pygame.draw.rect(self.fenetre, (255, 255, 255), bouton_guerrier)
                pygame.draw.rect(self.fenetre, (255, 255, 255), bouton_mage)
                pygame.draw.rect(self.fenetre, (255, 0, 0), bouton_guerrier, 3)
                pygame.draw.rect(self.fenetre, (255, 0, 0), bouton_mage, 3)
                
                font = pygame.font.Font(None, 30)
                texte_guerrier = font.render("Guerrier", True, (0, 0, 0))
                texte_mage = font.render("Mage", True, (0, 0, 0))
                self.fenetre.blit(texte_guerrier, (bouton_guerrier.x + 10, bouton_guerrier.y + 10))
                self.fenetre.blit(texte_mage, (bouton_mage.x + 10, bouton_mage.y + 10))
                
                pygame.display.flip()

        else:            
            if self.class_joueur['Class'] == 'Warrior':
                    player = Warrior("Test", camera_group.carte.get_waypoint('Spawn'), [player_sprite] + list(camera_groups.values()))
            if self.class_joueur['Class'] == 'Mage':
                # player = Mage("Test", [player_sprite] + list(camera_groups.values()))
                pass
            if self.class_joueur['Class'] == 'Thief':
                # player = Thief("Test", [player_sprite] + list(camera_groups.values()))
                pass

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
            pos = (player_pos['x'], player_pos['y'])
            player.set_pos(pos)

            return player