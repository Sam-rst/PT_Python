import pygame, sys
from dice import Dice
from save import SaveData
from caracter import Warrior, Mage


class Menu:
    def __init__(self):
        self.fenetre = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.save_data = SaveData('save.json')
        self.class_joueur = self.save_data.load_player_class()
        
    def run(self):
        if self.class_joueur:
            # sert a passer si le joueur a deja une classe
            return
        else:
            # Sinon, on affiche le menu de sélection de classe
            largeur_bouton = 200
            bouton_guerrier = pygame.Rect((self.fenetre.get_width() - largeur_bouton) / 2, 100, largeur_bouton, 50)
            bouton_mage = pygame.Rect((self.fenetre.get_width() - largeur_bouton) / 2, 200, largeur_bouton, 50)
            classe = None
            
            while True:
                for evenement in pygame.event.get():
                    if evenement.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif evenement.type == pygame.MOUSEBUTTONDOWN:
                        if bouton_guerrier.collidepoint(pygame.mouse.get_pos()):
                            classe = Warrior("mechant", 20, 8, 3)
                            self.save_data.save_player_class(classe)
                            
                            return
                        elif bouton_mage.collidepoint(pygame.mouse.get_pos()):
                            classe = Mage("fdp", 20, 8, 3)
                            self.save_data.save_player_class(classe)
                            
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
